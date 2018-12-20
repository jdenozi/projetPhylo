#!/usr/bin/env python3
# -*- coding: utf-8 -*

import node
import re
def lectureArbre(fichier):
    global index
    with open(fichier) as f:
        arbre = f.read()
    #corps = arbre.replace(re.findall("\w;", arbre)[0], "")
    index = len(arbre) - 2 
    return arbre

#if arbre.endswith()
#arbre.strip()


def parser(parent, courant, niveau, arbre):
    global index
    strtmp = ""
    while index >= 0 :
        if arbre[index] == ")" :
            courant.name=strtmp
            nouvelenfant = node.node(parent = courant, enfants = [], gen = niveau+1)
            courant.enfants.append(nouvelenfant)
            strtmp = ""
            index -= 1
            parser(courant, nouvelenfant, niveau+1, arbre)
        elif arbre[index] == ",":
            if strtmp != "" : parent.enfants[-1].name = strtmp
            nouveaufrere = node.node(parent = parent, enfants = [], gen = niveau)
            parent.enfants.append(nouveaufrere)
            strtmp = ""
            index -= 1
        elif arbre[index] == "(":
            index -= 1
            parent.enfants[-1].name=strtmp
            return
        elif arbre[index] == ":":
            parent.enfants[-1].dist=float(strtmp[::-1])
            strtmp = ""
            index -= 1
        elif arbre[index] == ";":
            index -= 1
            pass
        else : 
            strtmp = strtmp+arbre[index]
            index -= 1
