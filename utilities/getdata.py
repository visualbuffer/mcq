# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 17:20:13 2018

@author: shuva
"""
from utilities.document import Reader
import os

def get(directory = "./files"):
    files =  os.listdir(directory)
    valid = ['docx','doc','txt','pdf','rtf']
    paragraphs = []
    texts = []
    for document in files:
        extension = document.split('.')[-1]
        if extension in valid:
            print('PROCESSING : ',document)
            try : 
                reader = Reader(path=document)
                text =  reader.text
                para  =  text.split("\n\n")
                texts.append(text)
                paragraphs = paragraphs +para
            except:
                print('GOT ERROR FOR', document)
    return texts , paragraphs

