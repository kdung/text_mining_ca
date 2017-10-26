#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:26:41 2017

@author: sophie
"""
import extract_body_parts as bp

if __name__ == '__main__':
    print("fatal: ")
    bp.extract_body_parts("data/fatal.csv", "fatal_output.csv")
    print("amputation catastrophic")
    bp.extract_body_parts("data/amp_catastrophic.csv", "amp_catastrophic_output.csv")
    print("catastrophic")
    bp.extract_body_parts("data/catastrophic.csv", "catastrophic_output.csv")
    print("number catastrophic")
    bp.extract_body_parts("data/number_catastrophic.csv", "number_catastrophic_output.csv")