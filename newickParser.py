#!/usr/bin/python3
#-*- coding Utf-8 -*-

import sys,os,re
from node import*
os.system('clear')

with open("gene_tree.nwk") as f:
    arbre = f.read()
f.close()
i = len(arbre)-2
root = node()
#root = node(gen=0, name = "root")
def creationArbre(arbre, parent, niveau, index):
    if index >=0 :
        listeEnfants =[]
        if arbre[index]==')': #création enfant 
            #listeEnfants.append(node(gen=generation, parent = parent, enfants = creationArbre(arbre, generation+1, i-1)))
            print(')')
        elif arbre[index] == '(' :#sortie de la fratrie
            #generation = generation-1
            print('(')
        elif arbre[index] == ',' :# nouveau frère
            print(',')
            #parent.enfants.append(node(gen=generation, parent = parent))
        index-=1
        creationArbre(arbre, parent, niveau, index)
        return (listeEnfants) 
    return None
root.enfants = creationArbre(arbre, root, 1, i)
print (arbre)
