#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.metrics import accuracy


class Tagger:
 
    def __init__(self,tagged_train_sents):
        self.tagged_train_sents = tagged_train_sents
    
    def tag(self,tokens):
        regex_tagger = nltk.RegexpTagger(
        [(r'^[!\?%&\$]+$','OP'),
         (r'^[\.,:`´՞~]+$','P'),
         (r'^\p{Lu}\S+$','NP'),
         (r'^\S+[ըն]$','NN'),
         (r'^\S+ական$|^\S+ային$|^\S+ավետ$|^\S+ավոր$|^\S+ավուն$|^\S+ե$|^\S+յա$|^\S+ոտ$|^\S+ուն$','JJ'),
         (r'^\S+ելի$|^\S+ալի$|^\S+գույն$|^ան\S+$|^ապ\S+$|^դժ\S+$|^տ\S+$|^չ\S+$|^ամենա\S+$','JJ'),
         (r'^\S+րոր$|^\S+դ$|^\S+երորդ$|^\S+րդ$|^առաջին$','CD'),
         (r'^(\S+)-\1$','CD'),
         (r'^\S+բար$|^\S+պես$|^\S+որեն$|^\S+ովին$|^\S+ակի$|^\S+գին$|^\S+պատիկ$|^\S+վարի$','RB'),
         (r'^\S+ուստ$|^\S+ուց$|^\S+անց$|^\S+իցս$|^\S+ակի$|^\S+ացի$|^\S+երեն$','RB'),
         (r'^\S+իս$|^\S+ած$|^\S+ող$|^\S+իք$|^\S+ում$|^\S+ու$','PRP'),
         (r'^\S+ել$|^\S+ալ$|^\S+մ$|^\S+ս$|^\S+ի$|^\S+նք$|^\S+ք$|^\S+ն$|^\S+ի$|^\S+իր$|^\S+ր$','VB'),
         (r'ինք$|իք$|^\S+ին$|^\S+իր$|^\S+ա$|^\S+ու$|^\S+եք$|^կ\S+$','VB')
        ])
        #unigram_tagger = nltk.UnigramTagger(self.tagged_train_sents)
        unigram_tagger = nltk.UnigramTagger(self.tagged_train_sents, backoff = regex_tagger)
        bigram_tagger = nltk.BigramTagger(self.tagged_train_sents, backoff = unigram_tagger)

        temp_tagged_sent = bigram_tagger.tag(tokens)
        tagged_sent = []
        for i in range(0,len(temp_tagged_sent)):
                tagged_word = list(temp_tagged_sent[i])
                if(temp_tagged_sent[i][1]==None and temp_tagged_sent[i-1][1]=='JJ'):
                    tagged_word[1]="NN"
                    tagged_sent.append(tuple(tagged_word))
                    continue
                if(temp_tagged_sent[i][1]==None and temp_tagged_sent[i-1][0]=='ավելի'):
                    tagged_word[1]="JJ"
                    tagged_sent.append(tuple(tagged_word))
                    continue
                if((temp_tagged_sent[i][1]==None)and
                   ((temp_tagged_sent[i-1][0]=='պիտի' or 'պետք')or(temp_tagged_sent[i+1][0]=='պիտի' or 'պետք'))
                   and (i != len(tagged_sent)-1)):
                    tagged_word[1]="VB"
                    tagged_sent.append(tuple(tagged_word))
                    continue
                else:
                    tagged_sent.append(tuple(tagged_word)) 
                #tagged_sent.append(tuple(tagged_word)) 
        return tagged_sent
           
    def evaluate(self,tagged_gold_sents):
        gold_tokens = []
        for sent in tagged_gold_sents:
            for tup in sent:
                gold_tokens.append(tup[0])
        test_tagged_tokens = self.tag(gold_tokens)
        gold_tagged_tokens = sum(tagged_gold_sents,[])
        print accuracy(gold_tagged_tokens, test_tagged_tokens) 
        



        
