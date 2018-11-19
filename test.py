#!/usr/bin/env/python3

import sys
dic =
open("taxa_to_species_map.txt",
        "r")
g = open("gene_tree.nwk", "r")
f = open("species_tree.nwk", "r")
spec_tree = f.read()
gene_tree = g.read()

for i in spec_tree:
    if (i == "'"):
        #appel de substring typical jusqu'au prochain '
    #comparaison de la substring
