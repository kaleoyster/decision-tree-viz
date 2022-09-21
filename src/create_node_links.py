"""
Description:
    Creates nodes and links
"""
import csv
import json
import random
from tqdm import tqdm
from collections import defaultdict

def read_file():
    """
    Description:
        Returns file path given filename
    """
    path = 'path.csv'
    all_paths = list()
    with open(path, 'r') as csv_file:
        paths = csv.reader(csv_file, delimiter = ',')
        header = next(paths)
        for row in paths:
            all_paths.append(row)
    return all_paths

def create_node_dictionary(paths):
    """
    Description:
        Return nodes, new_nodes, and dictionary
    """
    new_nodes = []
    node_labels = defaultdict()

    # Store rules 
    dictionary = defaultdict(list)
    for row in paths[:]:
        label = row[-1]
        rule = row[3:-1]
        rule = ' '.join(rule)
        node = row[2].strip(" ")
        dictionary[node].append(rule)
        node_labels[node] = label
    nodes = list(dictionary.keys())
    for node in nodes:
        group_val = node_labels[node]
        rule = dictionary[node]
        temp = {
                  'id': node,
                  'group': int(group_val), # Class label of the IRIS flower
                  'rule': rule
                }
        new_nodes.append(temp)
    return nodes, new_nodes, dictionary

def compare_rules(rule1, rule2):
    """
    Description:
        Return common_rules
    """
    rule1 = set(rule1)
    rule2 = set(rule2)
    common_rules = rule1.intersection(rule2)
    return len(common_rules), list(common_rules)

def create_links(nodes, dictionary):
    """
    Description:
        Given nodes and dictionary return links
    """
    links = list()
    for node1 in tqdm(range(0, len(nodes))):
        for node2 in range(0, len(nodes)):
            bridge1 = nodes[node1]
            bridge2 = nodes[node2]
            if node1 != node2:
                rule1 = dictionary.get(bridge1)
                rule2 = dictionary.get(bridge2)
                total_count, rules = compare_rules(rule1, rule2)
                if total_count > 0:
                    link = {
                        'source':bridge1,
                        'target':bridge2,
                        'value':total_count,
                        'common rules': rules
                        }
                    links.append(link)
    return links

def create_json(nodes, links):
    """
    Description:
        Given nodes and links return json
    """
    network = {
               'nodes':nodes,
               'links':links
              }
    return network

def main():
    all_paths = read_file()
    ## filter data-sets here to get either the 
        # TODO: Convert this into a function
    # Return the structure number by filtering through their attributes
    filter_sample = ['332',
                     '335',
                     '336',
                     '337'
                    ]

    filter_paths = []
    for sample in all_paths:
        sam_id = sample[0]
        if sam_id in filter_sample:
            filter_paths.append(sample)

    nodes, new_nodes, dictionary = create_node_dictionary(filter_paths)
    links = create_links(nodes, dictionary)
    network =  create_json(new_nodes, links)
    #path = '../docs/data' + '/' + 'network.json'
    print(network)
    # For source testing
    path = 'network.json'
    with open(path, 'w+') as json_file:
        json.dump(network, json_file, indent=4)

if __name__ == '__main__':
    main()
