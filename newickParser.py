#!/usr/bin/python3
#-*- coding Utf-8 -*-

import sys,os,re
from node import*
os.system('clear')
os.system('rm arbre.nwk')


#root = node(gen=0, name = "root")


def creationArbre(arbre, parent, niveau, index):
    if index >= 0:
        listeEnfants = []
        if arbre[index] == ')':  # création enfant
            listeEnfants.append(node(
                gen=niveau, parent=parent, enfants=
                creationArbre(arbre, parent, niveau + 1, index - 1)))
            print(listeEnfants)
        elif arbre[index] == '(':  # sortie de la fratrie
            niveau -= niveau
        elif arbre[index] == ',':  # nouveau frère
            parent.enfants.append(node(gen=niveau, parent=parent))
        # os.system("echo -n \"%s\" >> arbre.nwk" % i)
        index -= 1
        creationArbre(arbre, parent, niveau, index)
        return (listeEnfants)
    return None


def parcoursArbre(root):
    print (parcours)

