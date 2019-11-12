from collections import Counter
from graphviz import Digraph
import numpy as np


class ID3DecisionTreeClassifier :

    def node_entropy(self, node):
        tot_nbr = node['samples']
        I = 0
        sample_cnt = node['classCounts']

        for type_class in sample_cnt:
            class_cnt = sample_cnt[type_class]
            sum_term = class_cnt/tot_nbr*np.log2(class_cnt/tot_nbr)
            I += sum_term
        
        return -I

    def __init__(self, minSamplesLeaf = 1, minSamplesSplit = 2) :

        self.__nodeCounter = 0

        # the graph to visualise the tree
        self.__dot = Digraph(comment='The Decision Tree')

        # suggested attributes of the classifier to handle training parameters
        self.__minSamplesLeaf = minSamplesLeaf
        self.__minSamplesSplit = minSamplesSplit


    # Create a new node in the tree with the suggested attributes for the visualisation.
    # It can later be added to the graph with the respective function
    def new_ID3_node(self, data, target, attributes, classes):
        sample_cnt = Counter()
        for i in target:
            sample_cnt[i] += 1
        nbr_samples = len(target)

        node = {'id': self.__nodeCounter, 'label': None, 'attribute': None, 'entropy': None, 'samples': None,
                         'classCounts': None, 'nodes': None}
        node['label'] = 'hej'
        node['attribute'] = attributes
        node['samples'] = nbr_samples
        node['classCounts'] = sample_cnt
        node['nodes'] = []
        node['entropy'] = self.node_entropy(node)


        self.__nodeCounter += 1
        return node

    # adds the node into the graph for visualisation (creates a dot-node)
    def add_node_to_graph(self, node, parentid=-1):
        nodeString = ''
        for k in node:
            if ((node[k] != None) and (k != 'nodes')):
                nodeString += "\n" + str(k) + ": " + str(node[k])

        self.__dot.node(str(node['id']), label=nodeString)
        if (parentid != -1):
            self.__dot.edge(str(parentid), str(node['id']))


    # make the visualisation available
    def make_dot_data(self) :
        return self.__dot


    # For you to fill in; Suggested function to find the best attribute to split with, given the set of
    # remaining attributes, the currently evaluated data and target.
    def find_split_attr(self, node):
        root_entropy = node_entropy(node)
        attributes = node['attributes']
        info_gain = []
        # Start with going through every attribute left.
        for att in attributes:
            # Now look at the subsets in the attribute ???HOW TO FIND DATA????
            for subset in attributes[att]:
                cnt_subset = 

        # Change this to make some more sense
        return None


    # the entry point for the recursive ID3-algorithm, you need to fill in the calls to your recursive implementation
    def fit(self, data, target, attributes, classes):

        # fill in something more sensible here... root should become the output of the recursive tree creation
        root = self.new_ID3_node(data,target,attributes,classes)
        #test_node = self.new_ID3_node()
        self.add_node_to_graph(root)
        #self.add_node_to_graph(test_node)

        return root



    def predict(self, data, tree) :
        predicted = list()

        # fill in something more sensible here... root should become the output of the recursive tree creation
        return predicted
    

