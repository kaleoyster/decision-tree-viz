"""
Description:
    1. Creates nodes and links  [Done]
    2. Saves in json format [Done]
"""
import csv
import json
import random
from tqdm import tqdm
from collections import defaultdict

def read_file():
    all_paths = list()
    with open("path.csv", 'r') as csv_file:
        paths = csv.reader(csv_file, delimiter = ',')
        header = next(paths)
        for row in paths:
            all_paths.append(row)
    return all_paths

def create_node_dictionary(paths):
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
    print(new_nodes)
    return nodes, new_nodes, dictionary

def compare_rules(rule1, rule2):
    rule1 = set(rule1)
    rule2 = set(rule2)
    common_rules = rule1.intersection(rule2)
    return len(common_rules)

def create_links(nodes, dictionary):
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
                        'value':common_rules
                        }
                    links.append(link)
    return links

def create_json(nodes, links):
    network = {
               'nodes':nodes,
               'links':links
              }
    return json.dumps(network)

def main():
    all_paths = read_file()
    nodes, new_nodes, dictionary = create_node_dictionary(all_paths)
    links = create_links(nodes, dictionary)
    network =  create_json(new_nodes, links)

    with open('network.json', 'w') as json_file:
        json.dump(network, json_file)

    #fields = ['source', 'target', 'count']
    #with open('links.csv', 'w') as f:
    #    write = csv.writer(f)
    #    #write.writerow(fields)
    #    write.writerows(links)

if __name__ == '__main__':
    main()

