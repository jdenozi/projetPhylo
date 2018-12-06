#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import node
import newickParser

arbregene = newickParser.lectureArbre("test.txt")
print(arbregene)
#index = len(arbregene) - 1
root = node.node(name="root", enfants=[], gen=0)
newickParser.creationArbre(root, 0, arbregene)
#newickParser.parcoursArbre(root)
print(root)
print("fin")
