#!/usr/bin/python
# -*- coding: utf-8 -*-


import nltk
import re

class FileCaller:
    
    def __init__(self,file):
        self.file = file

    def get_all(self):
        with open(self.file,"r") as file:
            text = file.read()
        return text

    def get_sents(self):
        with open(self.file,"r") as file:
            text = file.read()
            lines = []
            for line in text.split("\n"):
                if(line!=""):
                    lines.append(line)       
            sents = []
            for line in lines:
                for sent in re.split("(\S+[^:]+:)",line):
                    if(not re.match(r"^\s+$",sent) and sent!=""):
                        sents.append(sent)
            return sents
            
    def get_tagged_sents(self):
        with open("Tagged_"+self.file,"r") as file:
            text = file.read()
            sents = text.split("|||")
        tagged_sents = []
        for sent in sents:
            tagged_sent = [nltk.tag.str2tuple(t) for t in sent.split()]
            for i in range(0,len(tagged_sent)-1):
                if(i<len(tagged_sent)-1):
                    if(tagged_sent[i][1]==None):
                        tup = (tagged_sent[i][0]+" "+tagged_sent[i+1][0], tagged_sent[i+1][1])
                        tagged_sent[i+1] = tup
                        tagged_sent.pop(i)#for words with a space
            tagged_sents.append(tagged_sent)
        return tagged_sents

    def get_tokenized_sents(self):
        tagged_sents = self.get_tagged_sents()
        tokenized_sents = []
        tokenized_sent = []
        for tagged_sent in tagged_sents:
            for tup in tagged_sent:
                tokenized_sent.append(tup[0])
            tokenized_sents.append(tokenized_sent)
        return tokenized_sents


        


