#!/usr/bin/env/ python3
# -*- coding Utf-8 -*-


class node:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.parent = kwargs.get('parent')
        self.enfants = kwargs.get('enfants')
        self.gen = kwargs.get('gen')
        self.dist = kwargs.get('dist')

    def isRoot(self):
        if self.parent:
            return False
        else:
            return True

    def isLeaf(self):
        if self.enfants:
            return False
        else:
            return True

    def __repr__(self):
                return("nom({}) generation({}) enfants({}) parents({})".format
                (self.name, self.gen, self.enfants, self.parent))
