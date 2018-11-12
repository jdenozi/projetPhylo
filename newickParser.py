#!/usr/bin/python3
#-*- coding Utf-8 -*-

import sys,os,re

os.system('clear')

with open("gene_tree.nwk") as f:
    arbre = f.read()
f.close()
print (arbre)
