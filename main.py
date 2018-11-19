# -*- coding: utf-8 -*-

from node import *
from newickParser import *
print("bob")
with open("gene_tree.nwk") as f:
    arbre = f.read()
f.close()
i = len(arbre) - 1
root = node()
root.enfants = creationArbre(arbre, root, 1, i)
print("fin")