#!/usr/bin/env python3
#-*- coding Utf-8 -*-

import sys,os,re
from node import*

index = 0


def lectureArbre(fichier):
    global index
    with open(fichier) as f:
        arbre = f.read()
    index = len(arbre) - 2
    return arbre


def creationArbre(parent, niveau, arbre):
    global index
    listeEnfants = []
    strtmp = ""
    print("appel fonction")
    while index >= 0:
        print ("indice {} niveau {}".format(index, niveau))
        print (arbre[index])
        #if arbre[index] == ';':
            #index -= 1
            #return (node(gen=0, name="root", enfants=creationArbre(self, 1)))
        if arbre[index] == ')':  # création enfant
            index -= 1
            listeEnfants.append(node(name="parenttest", gen=niveau, parent=parent,))
            listeEnfants[-1].enfants=creationArbre(listeEnfants[-1], niveau+1, arbre)
            #listeEnfants.append(node(name=parent, gen=niveau, parent=parent, enfants=
            #creationArbre(parent, niveau+1, arbre)))
        elif arbre[index] == ',':  # création frère(s)
            #parent.enfants[-1].name = strtmp
            strtmp = ""
            index -= 1
            print("deuxième enfant")
            print(parent)
            #parent.enfants.append(node(gen=niveau, parent=parent, enfants=
            #creationArbre(parent, niveau + 1, arbre)))
        elif arbre[index] == '(':  # sortie de la fratrie
            #parent.enfants[-1].name = strtmp
            strtmp = ""
            index -= 1
            niveau -= 1
            print(listeEnfants)
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
