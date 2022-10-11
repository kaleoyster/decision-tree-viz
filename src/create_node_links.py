"""
Description:
    Creates nodes and links
"""
import csv
import json
import random
import argparse
import pandas as pd
from maps import *
from tqdm import tqdm
from collections import defaultdict

def read_file(path):
    """
    Description:
        Returns file path given filename
    """
    all_paths = list()
    with open(path, 'r') as csv_file:
        paths = csv.reader(csv_file, delimiter = ',')
        header = next(paths)
        for row in paths:
            all_paths.append(row)
    return all_paths, header

def create_node_dictionary(paths, dataframe):
    """
    Description:
        Return nodes, new_nodes, and dictionary
    """
    new_nodes = []
    node_labels = defaultdict()
    header = dataframe.columns
    attribute_dict = defaultdict()

    # Store rules 
    dictionary = defaultdict(list)
    for row in paths[:]:
        label = row[-1]
        rule = row[3:-1]
        rule = ' '.join(rule)
        node = row[2].strip(" ")
        record_val = dataframe[dataframe['structureNumber'] == node]
        list_of_dicts = record_val.to_dict('records')[0]
        attribute_dict[node] = list_of_dicts
        dictionary[node].append(rule)
        node_labels[node] = label

    nodes = list(dictionary.keys())
    for node in nodes:
        group_val = node_labels[node]
        rule = dictionary[node]
        attr_dict = attribute_dict[node]
        temp = {
                  'id': node,
                  'group': group_val,
                  'rule': rule
                }

        for col, val in attr_dict.items():
            if col == 'material':
                mat_map = mapDict['CatMaterial']
                val = int(val)
                val = mat_map[val]

            temp[col] = val

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
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--inputfile', help='input filename')
    parser.add_argument('-s', '--sample', help='input filename')

    args = parser.parse_args()
    path = args.inputfile
    sample_file = args.sample

    all_paths, path_header = read_file(path)

    filter_paths = []
    samples, sample_header = read_file(sample_file)

    # Get structure numbers
    new_sample = []
    for index in samples:
        temp = index[0]
        new_sample.append(temp)
    structure_numbers = new_sample

    # Matching the structure number from path.csv 
    # with sample.csv
    for sample in all_paths:
        sam_id = sample[2]
        if sam_id in structure_numbers:
            filter_paths.append(sample)

    samples_df = pd.DataFrame(samples, columns = sample_header)
    nodes, new_nodes, dictionary = create_node_dictionary(filter_paths, samples_df)
    links = create_links(nodes, dictionary)
    network =  create_json(new_nodes, links)

    output_path = 'network.json'
    with open(output_path, 'w+') as json_file:
        json.dump(network, json_file, indent=4)

if __name__ == '__main__':
    main()
