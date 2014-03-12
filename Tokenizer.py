#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

class Tokenizer:
    
    def tokenize(self,text):
        text = text.decode('utf-8')
        text = re.sub(ur'(?u)([^մթառՄ0-9]|[^0-9\s\.][մթա]|[^ք][^ա]ռ)(\.)',ur'\1 \2 ',text)
        text = re.sub(ur'(?u)(հզ)\s(\.)\s(-ից|-ի|-ին)',ur'\1\2\3 ',text)
        text = re.sub(ur'(?u)([\(«<\[%\$&/\*@!\?,:`~\)>»\]])',ur' \1 ',text)
        text = re.sub(ur'(?u)([0-9]+)\s(,)\s([0-9]+)',ur'\1\2\3',text)
        text = re.sub(ur'(?u)([^՞´\s]+)([՞´])(\S+)',ur'\1\3 \2' ,text)
        text = re.sub(ur'(?u)([^՞´\s]+)([՞´])\s',ur'\1 \2' ,text)
        text = re.sub(ur'(?u)(\.\.+)',ur' \1 ',text)
        text = text.encode('utf-8')
        tokens = text.split()
        for i in range(0,len(tokens)):
            if(i<len(tokens)-1):
                if((tokens[i]=="մի" and tokens[i+1]=="քան") or (tokens[i]=="մի" and tokens[i+1]=="քանի") or
                   (tokens[i]=="Ինչ-որ" and tokens[i+1]=="բան")):
                    tokens[i]= tokens[i]+" "+tokens[i+1]
                    tokens.pop(i+1)
        return tokens
    
    def evaluate(self,tagged_sents,sents):
        gold_tokens = []
        for sent in tagged_sents:
            for tup in sent:
                gold_tokens.append(tup[0])        
        test_sent_tokens = []
        for sent in sents:
            test_sent_tokens.append(self.tokenize(sent))
        test_tokens = sum(test_sent_tokens,[])
        
        if(len(gold_tokens)>len(test_tokens)):
            test_tokens.extend(["NumberBalancer"]*abs(len(gold_tokens)-len(test_tokens)))
        if(len(gold_tokens)<len(test_tokens)):
            gold_tokens.extend(["NumberBalancer"]*abs(len(gold_tokens)-len(test_tokens)))

        difference = set(test_tokens)-set(gold_tokens)
        difference2 = set(gold_tokens)-set(test_tokens)
        difference_size = 0
        difference2_size = 0
        for token in difference:
            difference_size += test_tokens.count(token)
        for token in difference2:
            difference2_size += gold_tokens.count(token)
        print 1-float(difference_size+difference2_size)/len(test_tokens+gold_tokens)
              
