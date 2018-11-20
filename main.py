# -*- coding: utf-8 -*-

import node
import newickParser

print("start")
arbregene = newickParser.lectureArbre("gene_tree.nwk")
print(arbregene)
index = len(arbregene) - 1
print(index)
root = node(name="root", enfants=[], gen=0)
print(root)
newickParser.creationArbre(root, 0)
print("fin")