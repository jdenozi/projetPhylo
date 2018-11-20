#!/usr/bin/env python3
#-*- coding Utf-8 -*-

import sys,os,re
from node import*

index =0
def lectureArbre(fichier):
    global index
    with open(fichier) as f:
        arbre=f.read()
    index = len(arbre)-2
    return arbre


def creationArbre(parent, niveau, arbre):
    global index
    listeEnfants = []
    strtmp = ""
    print("debut creation")
    print (index)
    while index >= 0:
        #if arbre[index] == ';':
            #index -= 1
            #return (node(gen=0, name="root", enfants=creationArbre(self, 1)))
        if arbre[index] == ')':  # création enfant
            index -= 1
            listeEnfants.append(node(gen=niveau, parent=parent, enfants=
            creationArbre(parent, niveau + 1, arbre)))
        elif arbre[index] == ',':  # création frère(s)
            #parent.enfants[-1].name = strtmp
            strtmp = ""
            index -= 1
            listeEnfants.append(node(gen=niveau, parent=parent, enfants=
            creationArbre(parent, niveau + 1, arbre)))
        elif arbre[index] == '(':  # sortie de la fratrie
            #parent.enfants[-1].name = strtmp
            strtmp = ""
            index -= 1
            niveau -= 1
            return(listeEnfants)
        elif arbre[index] == ':':
            #parent.distance = strtmp
            strtmp = ""
            index -= 1
        else:
            strtmp = strtmp + (arbre[index])
            index -= 1


def parcoursArbre(root):
    print(root)
    if (not root.isLeaf()): 
        for i in root.enfants:
            parcoursArbre(i)
