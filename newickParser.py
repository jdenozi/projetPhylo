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
    strtmp = ""
    while index >= 0:
        print ("indice {} niveau {}".format(index, niveau))
        #print (arbre[index])
        #if arbre[index] == ';':
            #index -= 1
            #return (node(gen=0, name="root", enfants=creationArbre(self, 1)))
        if arbre[index] == ')':  # création enfant
            index -= 1
            parent.enfants.append(
                node(name="test", gen=niveau + 1, parent=parent, enfants=[]))
            print(parent.enfants[-1].name)
            creationArbre(parent.enfants[-1], niveau + 1, arbre)
            print(parent.parent)
            print(niveau)
        elif arbre[index] == ',':  # création frère(s)
            strtmp = ""
            index -= 1
            parent.parent.enfants.append(
                node(name="frere", gen=niveau, parent=parent, enfants=[]))
        elif arbre[index] == '(':  # sortie de la fratrie
            strtmp = ""
            index -= 1
            return
        elif arbre[index] == ':':
            #parent.distance = strtmp
            strtmp = ""
            index -= 1
        else:
            strtmp = strtmp + (arbre[index])
            index -= 1


def parcoursArbre(root):
    if (not root.isLeaf()):
        for i in root.enfants:
            parcoursArbre(i)
            print(i)
