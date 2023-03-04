# python3

import sys
import threading
import numpy


def compute_height(node):
    if not node.children:
        return 1
    else:
        children_depths = [compute_height(child) for child in node.children]
        return max(children_depths) + 1


class Node():
    def __init__(self,name): 
        self.children = []
        self.name = name 

    def addChild(self, child):
        self.children.append(child)

def generateTree(length, elements):

    nodes = []

    for i in range(length):
        nodes.append(Node(i))


    for i in range(length):
        if elements[i] == -1:
            root = nodes[i]

        else:
            nodes[elements[i]].addChild(nodes[i])
    return root

def main():
    length = 0
    filename = "/workspaces/tree-height-from-empty-renars9/test/"
    check = input()
    if( 'I' in check):
        length = int(input())
        inputs = input()

    elif('F' in check):
        filename = filename + input()

        if('a' in filename[-1]):
            print("invalid filename")
            return
        
        with open(filename) as f:
            length = int(f.readline())
            inputs = f.readline()

    else:
        inputs = ""

    arr = numpy.fromstring(inputs, dtype=int, sep=' ')
    tree = generateTree(length,arr)
    depth = compute_height(tree)
    print(depth)
    
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

