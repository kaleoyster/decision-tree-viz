"""
Description:
    Creates nodes and links
"""
import csv
import json
import random
import pandas as pd
from tqdm import tqdm
from collections import defaultdict

def read_file(path = 'path.csv'):
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
                  'group': group_val, 
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
    filter_sample = ['129',
                     '128',
                     '95',
                     '75',
                     '25',
                     '11',
                     '7',
                     '3',
                     '2',
                     '1',
                     '123',
                     '111',
                     '85',
                     '77',
                     '65',
                     '53'
                    ]

    # class 0: gravel bridges
    filter_sample_0 = ['50',
                     '51',
                     '52',
                     '53',
                     '54',
                     '55',
                     '56',
                     '58',
                     '59',
                     '61',
                     '63',
                     '64',
                     '65',
                     '66',
                     '68',
                     '70',
                     '71',
                     '72',
                     '73',
                     '74',
                     '75',
                     '76',
                     '77',
                     '78',
                     '82',
                     '83',
                     '84',
                     '85',
                     '86',
                     '87',
                     '88',
                     '89',
                     '90',
                     '91',
                     '92',
                     '94',
                     '95',
                     '96',
                     '97',
                     '99',
                     '100',
                     '101',
                     '102',
                     '103',
                     '104',
                     '105',
                     '106',
                     '107',
                     '108',
                     '109',
                     '110',
                     '111',
                     '112',
                     '113',
                     '114',
                     '115',
                     '116',
                     '117',
                     '118',
                     '119',
                     '120',
                     '121',
                     '122',
                     '123',
                     '124',
                     '125',
                     '126',
                     '127',
                     '128',
                     '129',
                     '130',
                     '131',
                     '132',
                     '133',
                     '134',
                     '135',
                     '136',
                     '137',
                     '138',
                     '139',
                     '140',
                     '141',
                     '142',
                     '143',
                     '144',
                     '145',
                     '146',
                     '147',
                     '148',
                     '149']

    # Class 1: paved bridges
    filter_sample_1 = ['0',
                        '1',
                        '2',
                        '3',
                        '4',
                        '5',
                        '6',
                        '7',
                        '8',
                        '9',
                        '10',
                        '11',
                        '12',
                        '13',
                        '14',
                        '15',
                        '16',
                        '17',
                        '18',
                        '19',
                        '20',
                        '21',
                        '22',
                        '23',
                        '24',
                        '25',
                        '26',
                        '27',
                        '28',
                        '29',
                        '30',
                        '31',
                        '32',
                        '33',
                        '34',
                        '35',
                        '36',
                        '37',
                        '38',
                        '39',
                        '40',
                        '41',
                        '42',
                        '43',
                        '44',
                        '45',
                        '46',
                        '47',
                        '48',
                        '49',
                        '57',
                        '60',
                        '62',
                        '67',
                        '69',
                        '79',
                        '80',
                        '81',
                        '93',
                        '98']

    filter_paths = []
    samples = read_file('samples.csv')
    samples = samples[:30]
    #samples = filter_sample_1
    new_sample = []
    for index in samples:
        temp = index[0]
        new_sample.append(temp)
    samples = new_sample

    for sample in all_paths:
        sam_id = sample[2]
        if sam_id in samples:
            filter_paths.append(sample)

    nodes, new_nodes, dictionary = create_node_dictionary(filter_paths)
    links = create_links(nodes, dictionary)
    network =  create_json(new_nodes, links)
    #path = '../docs/data' + '/' + 'network.json'
    # For source testing
    path = 'network.json'
    with open(path, 'w+') as json_file:
        json.dump(network, json_file, indent=4)

if __name__ == '__main__':
    main()
