#!/usr/bin/python
# -*- coding: utf-8 -*-


class trieNode:
    """ leaf to indicates end of string """  
    def __init__(self):
        self.next = {}
        self.leaf = False

    """function to add a string to trie"""

    def add_item(self, item):
        i = 0
        while i < len(item):
            k = item[i]
            if not k in self.next:
                node = trieNode()
                self.next[k] = node
            self = self.next[k]
            if i == len(item) - 1:  # if last character then mark it as a leaf node
                self.leaf = True
            else:
                self.leaf = False
            i += 1
    """ function to search a string in the created trie """
    def search(self, item):
        if self.leaf and len(item) == 0:
            return True
        first = item[:1]  # get start character of string to search in trie
        str = item[1:]  # get remaining char of string
        if first in self.next:
            return self.next[first].search(str)
        else:
            return False
    """ function to perform autocompletion.traverses till the last char of
      seached string inside trie and then performs a dfs traversal from the current node to get 
      all child nodes under the nodes and concatenate  to get final strings (for eg, ab is passed
      and trie contains abc and abd,then traverses till ab and do dfs to get abc and abd """

    def dfs(self, item):
        if self.leaf:
            print item
        for i in self.next:
            s = item + i
            self.next[i].dfs(s)

    def autocomplete(self, item):
        i = 0
        s = ''
        while i < len(item):
            k = item[i]
            s += k
            if k in self.next:
                self = self.next[k]
            else:
                return 'not found'
            i += 1
        self.dfs(s)
        return '###end###'


list = [
    'sin',
    'singh',
    'sign',
    'sinus',
    'sit',
    'silly',
    'side',
    'son',
    'soda',
    'sauce',
    'sand',
    'soap',
    'sar',
    'solo',
    'sour',
    'sun',
    'sure',
    'and',
    'ask',
    'animal',
    'an',
    'ant',
    'aunt',
    ]
x = trieNode()
for i in list:
    x.add_item(i)

print x.autocomplete('so')
