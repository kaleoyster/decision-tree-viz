"""
Description:
    Create conceptual diagram with respect to IRIS dataset
"""
import csv
import pandas as pd
from concepts import Context
from collections import defaultdict

def read_file(path):
    """
    Returns a list of decision paths
    """
    all_paths = []
    with open(path, 'r') as csv_file:
        paths = csv.reader(csv_file, delimiter=',')
        header = next(paths)
        for row in paths:
            all_paths.append(row)
    return all_paths

def find_unique_rules(paths):
    """
    Description:
        Given a list of path
        return the unique set of rules

    Args:
        paths (list of list):
            Consist of the list of decision rules

    Return:
        unique_set
    """
    unique_set = []
    for row in paths:
        rule = row[3] + row[4] + row[5]
        unique_set.append(rule)
    unique_set = set(unique_set)
    return unique_set

def filter_samples(paths, filter_sample):
    """
    Description:
        Given filtered samples
    """
    filtered_sample = []
    for record in paths:
        sample_id = record[2]
        if sample_id in filter_sample:
            filtered_sample.append(record)
    return filtered_sample

def create_conceptual_table(paths, filter_sample):
    """
    Description:
        Given paths, return a conceptual table
        that includes objects and attributes

    Args:
        paths (list of list):
            Consist of decision rules and information of nodes

    Returns:
        paths
    """
    conceptual_paths = []
    sample_rule = defaultdict(list)
    unique_set = find_unique_rules(paths)
    rule_sample = defaultdict(list)

    # Utility function to select only a selected sample
    paths = filter_samples(paths, filter_sample)

    for record in paths:
        sample_id = record[2]
        rule = record[3] + record[4] + record[5]
        sample_rule[sample_id].append(rule)

    for sample, values in sample_rule.items():
        rule_sample['sample'].append(sample)
        for rule in unique_set:
            if rule in values:
                rule_sample[rule].append('X')
            else:
                rule_sample[rule].append('')

    # Create a dataframe to save relations
    df = pd.DataFrame(rule_sample)
    df.set_index('sample', inplace=True)
    df.to_csv('relations.csv', sep=',')

    # Load relations
    r = Context.fromfile('relations.csv', frmat='csv')

    # Visualize conceptual paths
    r.lattice.graphviz(view=True)
    return conceptual_paths

def main():
    """
    Driver function
    """
    path = 'path.csv'
    paths = read_file(path)

    # class 0
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
    # Class 1:
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

    create_conceptual_table(paths, filter_sample_0)

main()
