#!usr/bin/python3
# -*- coding Utf-8 -*-
class node:
    def _init_(self, **kwargs):
        self.name = kwargs.get('name')
        self.parent = kwargs.get('parent')
        self.enfants = kwargs.get('enfants')
        self.gen = kwargs.get('gen')
    
    def isRoot():
        if self.parent:
            return false
        else:
            return true
    def isLeaf():
        if self.enfants:
            return false
        else:
            return true

        
