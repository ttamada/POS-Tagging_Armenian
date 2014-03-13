#!/usr/bin/python
# -*- coding: utf-8 -*-

from FileCaller import FileCaller
from Tokenizer import Tokenizer
from Tagger import Tagger


file = FileCaller("Corpus.txt")
tagged_sents = file.get_tagged_sents()
sents = file.get_sents()
text = file.get_all()
tagged_train_sents = tagged_sents[:80]+tagged_sents[83:]
tagged_gold_sents = tagged_sents[80:83]
gold_sents = sents[80:83]
tokenized_sents = file.get_tokenized_sents()
"""for sent in tokenized_sents:
    for token in sent:
        print token+"  ","""

print "--NUMBER OF SENTENCES--"
print(len(tagged_sents))
print "\n"

print "--TOKENIZER--" 
"""tokens = Tokenizer().tokenize(text)
for token in tokens:
    print "("+token+")",
print "\n" """
print "EVALUATE TOKENIZER"
print "RATE"
#Tokenizer().evaluate(tagged_gold_sents,gold_sents)
Tokenizer().evaluate(tagged_sents,sents)
print "ANSWER"
gold_tokens = []
for sent in tagged_sents:
    for tup in sent:
        gold_tokens.append(tup[0])
for token in gold_tokens:
    print "("+token+")",
print "\n\nTEST"
test_tokenized_sents = []
for sent in sents:
    test_tokenized_sents.append(Tokenizer().tokenize(sent))
test_tokens = sum(test_tokenized_sents,[])
for token in test_tokens:
    print "("+token+")",
print "\n\nNUMBER OF TOKENS ANSWER,TEST"
print len(gold_tokens),len(test_tokens)
print "\n\nDIFFERENCE\nONLY IN TEST"
difference = set(test_tokens)-set(gold_tokens)
for token in difference:
    print token+"  ",
print "\n\nONLY IN ANSWER"
difference2 = set(gold_tokens)-set(test_tokens)
for token in difference2:
    print token+"  ",
print "\n"


print "--TAGGER--"
tagger = Tagger(tagged_train_sents)
"""tagged_test_tokens = tagger.tag(Tokenizer().tokenize(text))
for tup in tagged_test_tokens:
    print str(tup[0])+"/"+str(tup[1]),"""
print "\n"
print "EVALUATE TAGGER"
print "RATE"
tagger.evaluate(tagged_gold_sents)
print "\n\nANSWER"
tagged_gold_tokens = sum(tagged_gold_sents,[])
for tup in tagged_gold_tokens:
        print str(tup[0])+"/"+str(tup[1]),
print "\n\nTEST"
gold_tokens = []
for sent in tagged_gold_sents:
    for tup in sent:
        gold_tokens.append(tup[0])
tagged_test_tokens = tagger.tag(gold_tokens)
for tup in tagged_test_tokens:
    print str(tup[0])+"/"+str(tup[1]),
print "\n\nDIFFERENCE\nONLY IN TEST"
difference = set(tagged_test_tokens)-set(tagged_gold_tokens)
for tup in difference:
    print str(tup[0])+"/"+str(tup[1]),
print "\n\nONLY IN ANSWER"
difference2 = set(tagged_gold_tokens)-set(tagged_test_tokens)
for tup in difference2:
    print str(tup[0])+"/"+str(tup[1]),

"""for sent in tagged_sents:
    for tup in sent:
        print str(tup[0])+"/"+str(tup[1]),
print "\n" """  


