#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:26:41 2017

@author: sophie

fatal: 
[('head', 1096), ('foot', 539), ('hand', 340), ('body', 288), ('arm', 209), ('chest', 207), ('leg', 180), ('back', 173), ('neck', 155), ('face', 136), ('heart', 104), ('shoulder', 71), ('abdomen', 62), ('torso', 50), ('brain', 40), ('knee', 36), ('ankle', 24), ('bone', 22), ('eye', 22), ('elbow', 20), ('hip', 19), ('jaw', 19), ('waist', 18), ('liver', 18), ('spine', 17), ('artery', 15), ('pelvis', 14), ('wrist', 14), ('nose', 12), ('stomach', 12), ('thigh', 10), ('nail', 9), ('groin', 9), ('mouth', 9), ('skin', 8), ('throat', 8), ('lip', 7), ('ear', 7), ('tooth', 7), ('tissue', 7), ('vein', 6), ('vertebra', 5), ('radius', 4), ('calf', 4), ('chin', 4), ('cheek', 4), ('hair', 4), ('muscle', 4), ('tongue', 4), ('tibia', 3), ('bladder', 3), ('arch', 3), ('clavicle', 3), ('femur', 3), ('sole', 3), ('pancreas', 3), ('spleen', 3), ('kidney', 3), ('fibula', 2), ('pinky', 2), ('lobe', 2), ('ligament', 2), ('scapula', 2), ('breast', 1), ('belly', 1), ('pupil', 1), ('eyebrow', 1), ('eyelid', 1), ('trachea', 1), ('navel', 1), ('metatarsal', 1)]
time taken: 102.99986505508423 seconds
empty: 4409 / 6930

amputation catastrophic
[('hand', 3561), ('foot', 1299), ('leg', 722), ('arm', 698), ('head', 596), ('face', 371), ('back', 306), ('body', 224), ('wrist', 200), ('ankle', 181), ('bone', 175), ('knee', 172), ('neck', 161), ('shoulder', 159), ('hip', 122), ('eye', 121), ('chest', 117), ('elbow', 104), ('pelvis', 99), ('skin', 87), ('vertebra', 72), ('abdomen', 72), ('femur', 68), ('tibia', 64), ('pinky', 63), ('nail', 62), ('thigh', 49), ('jaw', 48), ('torso', 48), ('tendon', 45), ('fibula', 45), ('ear', 43), ('spine', 34), ('nose', 33), ('muscle', 31), ('tissue', 29), ('stomach', 27), ('ligament', 25), ('tooth', 24), ('throat', 21), ('brain', 20), ('clavicle', 18), ('chin', 17), ('mouth', 17), ('lip', 16), ('spleen', 16), ('calf', 16), ('groin', 15), ('artery', 15), ('hair', 15), ('waist', 14), ('cheek', 14), ('liver', 14), ('shin', 10), ('bladder', 10), ('radius', 9), ('kidney', 9), ('scapula', 9), ('patella', 8), ('tongue', 7), ('ulna', 7), ('sole', 6), ('metacarpal', 6), ('metatarsal', 6), ('cartilage', 5), ('pancreas', 5), ('heart', 5), ('vein', 4), ('eyelid', 4), ('sternum', 4), ('sacrum', 4), ('esophagus', 4), ('rectum', 3), ('eyebrow', 3), ('coccyx', 3), ('humerus', 3), ('skeleton', 2), ('urethra', 2), ('diaphragm', 2), ('lobe', 1), ('instep', 1), ('thyroid', 1), ('thorax', 1), ('trachea', 1), ('iris', 1), ('breast', 1), ('nipple', 1), ('nostril', 1), ('larynx', 1), ('mandible', 1), ('arch', 1), ('tarsal', 1), ('ureter', 1)]
time taken: 119.7072389125824 seconds
empty: 1518 / 6536

catastrophic
[('hand', 62), ('foot', 38), ('arm', 29), ('leg', 28), ('head', 23), ('face', 20), ('back', 19), ('body', 12), ('neck', 11), ('eye', 10), ('shoulder', 8), ('wrist', 6), ('chest', 5), ('skin', 5), ('ankle', 5), ('bone', 4), ('ear', 4), ('elbow', 4), ('throat', 2), ('abdomen', 2), ('sole', 2), ('hip', 2), ('tibia', 1), ('fibula', 1), ('shin', 1), ('lip', 1), ('nose', 1), ('spine', 1), ('rectum', 1), ('jaw', 1), ('hair', 1), ('chin', 1), ('mouth', 1), ('humerus', 1), ('ligament', 1), ('femur', 1), ('knee', 1), ('torso', 1), ('waist', 1)]
time taken: 5.460524082183838 seconds
empty: 165 / 290

number catastrophic
[('hand', 80), ('foot', 54), ('arm', 45), ('leg', 40), ('head', 38), ('face', 32), ('back', 26), ('body', 21), ('neck', 19), ('eye', 18), ('ankle', 11), ('shoulder', 11), ('skin', 10), ('chest', 10), ('throat', 10), ('wrist', 8), ('nose', 6), ('elbow', 6), ('ear', 5), ('bone', 5), ('hair', 4), ('abdomen', 3), ('hip', 3), ('waist', 3), ('jaw', 2), ('eyelid', 2), ('sole', 2), ('stomach', 1), ('nail', 1), ('vertebra', 1), ('pelvis', 1), ('tibia', 1), ('fibula', 1), ('shin', 1), ('kidney', 1), ('lip', 1), ('spine', 1), ('rectum', 1), ('tendon', 1), ('chin', 1), ('mouth', 1), ('muscle', 1), ('spleen', 1), ('pancreas', 1), ('nipple', 1), ('humerus', 1), ('ligament', 1), ('femur', 1), ('knee', 1), ('heart', 1), ('torso', 1)]
time taken: 9.85194706916809 seconds
empty: 313 / 525

"""
import extract_body_parts as bp

if __name__ == '__main__':
    print("fatal: ")
    bp.extract_body_parts("data/fatal.csv", "output/fatal_output.csv")
    print("amputation catastrophic")
    bp.extract_body_parts("data/amp_catastrophic.csv", "output/amp_catastrophic_output.csv")
    print("catastrophic")
    bp.extract_body_parts("data/catastrophic.csv", "output/catastrophic_output.csv")
    print("number catastrophic")
    bp.extract_body_parts("data/number_catastrophic.csv", "output/number_catastrophic_output.csv")
    
    
