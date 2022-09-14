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
        returns file path given filename
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
        return nodes, new_nodes, and dictionary
    """
    dictionary = defaultdict(list)
    new_nodes = []
    node_labels = defaultdict()
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
        temp = {'id': node,
                'group': int(group_val)
               }
        new_nodes.append(temp)
    return nodes, new_nodes, dictionary

def compare_rules(rule1, rule2):
    """
    Description:
        return common_rules
    """
    rule1 = set(rule1)
    rule2 = set(rule2)
    common_rules = rule1.intersection(rule2)
    return len(common_rules)

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
                common_rules = compare_rules(rule1, rule2)
                if common_rules > 0:
                    link = {
                        'source':bridge1,
                        'target':bridge2,
                        'value':common_rules,
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
    nodes, new_nodes, dictionary = create_node_dictionary(all_paths)
    links = create_links(nodes, dictionary)
    network =  create_json(new_nodes, links)
    path = '../docs/data' + '/' + 'network.json'
    with open(path, 'w+') as json_file:
        json.dump(network, json_file, indent=4)

if __name__ == '__main__':
    main()
