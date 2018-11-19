#!usr/bin/python3
# -*- coding Utf-8 -*-


class node:
    def _init_(self, **kwargs):
        self.name = kwargs.get('name')
        self.parent = kwargs.get('parent')
        self.enfants = kwargs.get('enfants')
        self.gen = kwargs.get('gen')

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