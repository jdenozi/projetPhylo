#!/usr/bin/python3
#-*- coding Utf-8 -*-

import sys,os,re
import node.py

os.system('clear')

with open("gene_tree.nwk") as f:
    arbre = f.read()
f.close()
def creationArbre(arbre, niveau = 0, index = 0)
    listeEnfants =[]
    i = arbre.length()-1
    while i > 0 :
        if arbre[i] == ':':
        else if arbre[i] == ')' :
            generation = generation+1
            listeEnfants.append(node(gen=generation, enfants = creationArbre(arbre, index = i+1, niveau = generation)
        else if i == '('
            generation = generation-1
        else if i == ','
            listeNodes.append(node(gen=generation)

print (arbre)
