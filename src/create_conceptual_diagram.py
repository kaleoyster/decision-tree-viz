"""
Description:
    Create conceptual diagram with respect to IRIS dataset
"""
import sys
import csv
import random
import argparse
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

def read_sample(sample):
    """
    Returns a list of decision paths
    """
    all_paths = []
    with open(sample, 'r') as csv_file:
        paths = csv.reader(csv_file, delimiter=',')
        header = next(paths)
        for row in paths:
            row = row[0]
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
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--inputfile', help='input filename')
    parser.add_argument('-s', '--sample', help='sample filename')

    args = parser.parse_args()
    path = args.inputfile
    sample_file = args.sample

    paths = read_file(path)
    samples = read_sample(sample_file)
    samples = random.sample(samples, 50)
    create_conceptual_table(paths, samples)

if __name__ == '__main__':
    main()
