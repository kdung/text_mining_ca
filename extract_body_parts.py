# -*- coding: utf-8 -*-
"""

@author: sophie
"""

import nltk
from nltk import pos_tag
from nltk import word_tokenize, sent_tokenize
import pandas as pd
import time

def find_body_parts(text, injury_verbs, cp, bp_dict, exclusions):
    body_parts = set()
    sents = find_main_sents(text, injury_verbs)
    for sent in sents:
        sen_pos = pos_tag(word_tokenize(sent))
        parsed_tree = cp.parse(sen_pos)
        #print(parsed_tree)
        bp = find_words_in_tree(parsed_tree, bp_dict, exclusions)
        #print(bp)
        body_parts.update(bp)
    #print(body_parts)
    return body_parts
    
def find_main_sents(text, injury_verbs):
    sents = sent_tokenize(text)
    #sents = [lem(sent) for sent in sents]
    sents = [sent for sent in sents if has_words(lem(sent), injury_verbs)]
    return sents
    
def has_words(sentence, words):
    tokens = word_tokenize(sentence.translate(sentence.maketrans('/',' ')))
    has = [a for a in words if a[0] in tokens]
    #print(str(has) + ": " + sentence)
    return has
    
def lem(sent):
    wnl = nltk.WordNetLemmatizer()
    tokens = word_tokenize(sent)
    tokens_lower=[t.lower() for t in tokens ]
    tokens_pos = pos_tag(tokens_lower, tagset = 'universal')
    pos_to_wnl_tags = {'ADJ':'a',
                       'ADJ_SAT':'s',
                       'ADV':'r',
                       'NOUN':'n',
                       'VERB':'v'}
    tokens_pos_lem = [wnl.lemmatize(t[0], pos = pos_to_wnl_tags[t[1]]) for t in tokens_pos if t[1] in pos_to_wnl_tags]
    #print(tokens_pos_lem)
    return ' '.join(tokens_pos_lem)
    
def find_words_in_tree(t, words, exclusions):
    bparts = []
    if hasattr(t, 'label') and t.label():
        if t.label() == 'NP':
            #print(t)
            bpart = ' '.join([child[0] for child in t if child[1] not in ['DT']])
            if is_body_part(bpart, words, exclusions):
                #print(bpart)
                bparts.append(bpart)
        else:
            for child in t:
               bparts.extend(find_words_in_tree(child, words, exclusions))
    return bparts

def is_body_part(text, bp_dict, exclusions):
    text_lem = lem(text)
    #print("is body part ",text_lem)
    has = has_words(text_lem, bp_dict) and not has_words(text_lem, exclusions)
    #print(str(has) + ": " + text)
    return has

def export_csv(words_list, output):
    import csv
    f = csv.writer(open(output, 'w'))
    f.writerow(['id','title','content'])
    for words_dict in words_list: 
        f.writerow([str(words_dict['id']), words_dict['title'], words_dict['content']])

    
def extract_body_parts(data_url, output):
    start_time = time.time()
    bodyparts = []
    cases = []
    bp_dict = pd.read_csv('body_parts.csv').values
    injury_verbs = pd.read_csv('injury_verbs.csv').values
    exclusions = pd.read_csv('exclusion_bp.csv').values
    data = pd.read_csv(data_url).values
    
    grammar = r"""
      NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
      PP: {<IN><NP>}               # Chunk prepositions followed by NP
      VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
      CLAUSE: {<NP><VP>}           # Chunk NP, VP
      """
    cp = nltk.RegexpParser(grammar)
    missing = 1
    for index, row in enumerate(data):
        try:
            summary = row[2].encode('ascii', 'ignore')
            # print(summary)
            parts = find_body_parts(str(summary), injury_verbs, cp, bp_dict, exclusions)
            #parts = find_main_sents(str(summary), injury_verbs)
            #print(parts)
            case = {}
            case['id'] = row[0]
            case['title'] = row[1]
            if parts:
                bodyparts.append(parts)
                case['content'] = ', '.join(parts)
            else:
                bodyparts.append([])
                case['content'] = ''
                missing += 1
                #print(row[0])
            cases.append(case)
            #if index > 10:
             #   break
        except Exception as ex:
            print(ex)
            continue
         
    #print('\n'.join([str(k) + ": " + str(parts) for k, parts in enumerate(bodyparts)]))
    export_csv(cases, output)
    
    from collections import Counter
    synonyms = {'feet':'foot',
                 'abdominal':'abdomen',
                 'temple':'head',
                 'forehead':'head',
                 'finger':'hand',
                 'thumb':'foot',
                 'palm':'hand',
                 'toe':'foot',
                 'scalp':'head',
                 'skull':'head',
                 'fingernail':'hand',
                 'heel':'foot',
                 'teeth':'tooth'}
    counter = Counter()
    for parts in bodyparts:
        for part in parts:
            for splitted in part.split(' '):
                splitted_lem = lem(splitted).lower()
                if splitted_lem in bp_dict:
                    key = synonyms[splitted_lem] if splitted_lem in synonyms else splitted_lem
                    counter[key] += 1

    print(counter.most_common(100))
    print("time taken:", str(time.time() - start_time), "seconds")
    print("empty:", missing, "/", str(len(cases)))
    