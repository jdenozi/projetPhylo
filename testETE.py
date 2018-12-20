#!/usr/bin/env python3
#-*- coding Utf-8 -*-
from ete3 import Tree

with open("test.txt") as f:
    arbre = f.read();


t = Tree(arbre)
t.show()
t.render("arbre.SVG")
