# -*- coding: utf-8 -*-

import nltk
from nltk import pos_tag
from nltk import word_tokenize, sent_tokenize
import pandas as pd

def find_body_parts(text, injury_verbs, cp, bp_dict):
    body_parts = set()
    sents = find_main_sents(text, injury_verbs)
    for sent in sents:
        sen_pos = pos_tag(word_tokenize(sent))
        parsed_tree = cp.parse(sen_pos)
        bp_tmp = find_words_in_tree(parsed_tree, bp_dict)
        body_parts.update([lem(bp) for bp in bp_tmp])
    #print(body_parts)
    return body_parts
    
def find_main_sents(text, injury_verbs):
    sents = sent_tokenize(text)
    #sents = [lem(sent) for sent in sents]
    sents = [sent for sent in sents if has_words(lem(sent), injury_verbs)]
    return sents
    
def has_words(sentence, words):
    has = [a for a in words if a[0] in word_tokenize(sentence)]
    #print(str(has) + ": " + sentence)
    return has
    
def lem(sent):
    wnl = nltk.WordNetLemmatizer()
    tokens = word_tokenize(sent)
    tokens_pos = pos_tag(tokens, tagset='universal')
    pos_to_wnl_tags = {'ADJ':'a',
                       'ADJ_SAT':'s',
                       'ADV':'r',
                       'NOUN':'n',
                       'VERB':'v'}
    tokens_pos_lem = [wnl.lemmatize(t[0], pos = pos_to_wnl_tags[t[1]]) for t in tokens_pos if t[1] in pos_to_wnl_tags]
    #print(tokens_pos_lem)
    return ' '.join(tokens_pos_lem)
    
def find_words_in_tree(t, words):
    bparts = []
    if hasattr(t, 'label') and t.label():
        if t.label() == 'NP':
            bpart = ' '.join([child[0] for child in t if child[1] not in ['DT']])
            if is_body_part(bpart, words):
                bparts.append(bpart)
        else:
            for child in t:
               bparts.extend(find_words_in_tree(child, words))
    return bparts

def is_body_part(text, bp_dict):
    has = has_words(lem(text), bp_dict)
    #print(str(has) + ": " + text)
    return has

def export_csv(words_list):
    import csv
    f = csv.writer(open('extracted_body_parts.csv', 'w'))
    f.writerow(['id','title','content'])
    for words_dict in words_list: 
        f.writerow([str(words_dict['id']), words_dict['title'], words_dict['content']])

    
if __name__ == '__main__':
    bodyparts = []
    cases = []
    bp_dict = pd.read_csv('body_parts.csv').values
    injury_verbs = pd.read_csv('injury_verbs.csv').values
    frame = pd.DataFrame(pd.read_excel('osha.xlsx',header=None))
    
    grammar = r"""
      NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
      PP: {<IN><NP>}               # Chunk prepositions followed by NP
      VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
      CLAUSE: {<NP><VP>}           # Chunk NP, VP
      """
    cp = nltk.RegexpParser(grammar)
    
    for index, row in frame.iterrows():
        try:
            summary = row[2].encode('ascii', 'ignore')
            # print(summary)
            parts = find_body_parts(str(summary), injury_verbs, cp, bp_dict)
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
                print(index)
            cases.append(case)
            if index > 30:
                break
        except Exception as ex:
            print(ex)
            continue
         
    #print('\n'.join([str(k) + ": " + str(parts) for k, parts in enumerate(bodyparts)]))
    """
    frame['5'] = [str(parts) for parts in bodyparts]
    frame['6'] = ''
    frame['7'] = ''
    """
    #frame.to_csv('osha_with_body_parts.csv', index = False)
    export_csv(cases)
    
    from collections import Counter
    
    counter = Counter()
    for parts in bodyparts:
        for part in parts:
            counter[part] += 1

    print(counter.most_common(10))
    