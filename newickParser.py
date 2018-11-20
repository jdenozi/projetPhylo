#!/usr/bin/python3
#-*- coding Utf-8 -*-

import sys,os,re
from node import*
os.system('clear')
os.system('rm arbre.nwk')
#root = node(gen=0, name = "root")


def lectureArbre(fichier):
    with open(fichier) as f:
        arbre.read(f)
    print("f")
    return arbre


def creationArbre(parent, niveau):
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
            print(")")
            index -= 1
            listeEnfants.append(node(gen=niveau, parent=parent, enfants=
            creationArbre(parent, niveau + 1)))
        elif arbre[index] == ',':  # création frère(s)
            parent.enfants[-1].name = strtmp
            strtmp = ""
            listeEnfants.append(node(gen=niveau, parent=parent, enfants=
            creationArbre(parent, niveau + 1)))
        elif arbre[index] == '(':  # sortie de la fratrie
            parent.enfants[-1].name = strtmp
            strtmp = ""
            index -= 1
            niveau -= niveau
            retun(listeEnfants)
        elif arbre[index] == ':':
            parent.distance = strtmp
            strtmp = ""
            index -= 1
        else:
            strtmp = strtmp + (arbre[index])
            index -= 1


def parcoursArbre(root):
    print(root)
    for i in root.enfants:
        parcoursArbre(i)