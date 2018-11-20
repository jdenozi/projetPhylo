#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import node
import newickParser

arbregene = newickParser.lectureArbre("test.nwk")
print(arbregene)
#index = len(arbregene) - 1
root = node.node(name="root", enfants=[], gen=0)
print(root)
root.enfants=newickParser.creationArbre(root, 0, arbregene)
newickParser.parcoursArbre(root)
print("fin")
