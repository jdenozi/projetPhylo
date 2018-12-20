#!/usr/bin/env python3
#-*- coding Utf-8 -*-

import sys, os, re
import node
import newickparser

os.system("clear")
root = node.node(name ="root", gen = 0, enfants = [])
newickparser.parser(None, root, 0, newickparser.lectureArbre("arbre.nwk").strip())
#print(newickparser.lectureArbre("arbre.nwk").strip())
print(root)



