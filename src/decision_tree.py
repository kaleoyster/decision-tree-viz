"""
Description:
    A decision tree model to predict iris dataset.
Author:
    Akshay Kale
Date:
    July 2, 2022
"""
import sys
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
import graphviz
#import matplotlib as plt

def load_dataset():
    """
    Description:
        Loads a dataset from sklearn.dataset
    Args:
        None
    Returns:
        dataset object
    """
    iris = load_iris()
    return iris

def print_decision_paths(clf, X_test, features):
    """
    Description:
        print decision path

    Args:
        X_test
        all_data
    """
    #TODO: Replace the X_test with all_data

    n_nodes = clf.tree_.node_count
    children_left = clf.tree_.children_left
    children_right = clf.tree_.children_right
    feature = clf.tree_.feature
    threshold = clf.tree_.threshold

    #oStdout = sys.stdout
    fileName = 'paths.txt'
    nodeList = []
    sampleIdList = []
    featureIdList = []
    valueList = []
    inequalityList = []
    thresholdList = []

    node_indicator = clf.decision_path(X_test)
    leaf_id = clf.apply(X_test)

    sample_ids = [i for i in range(10)]
    with open(fileName, 'w') as f:
        for sample_id in sample_ids:
            # Obtain ids of the nodes `sample_id` goes through, i.e., row `sample_id`
            node_index = node_indicator.indices[
                node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
            ]

            print("Rules used to predict sample {id}:\n".format(id=sample_id))
            for node_id in node_index:
                # Continue to the next node if it is a leaf node
                if leaf_id[sample_id] == node_id:
                    continue

                # Check if value of the split feature for sample 0 is below threshold
                if X_test[sample_id, feature[node_id]] <= threshold[node_id]:
                    threshold_sign = "<="
                    nodeList.append(node_id)
                    sampleIdList.append(sample_id)
                    featureIdList.append(features[feature[node_id]])
                    valueList.append(X_test[sample_id, feature[node_id]])
                    inequalityList.append(threshold_sign)
                    thresholdList.append(threshold[node_id])

                else:
                    threshold_sign = ">"
                    print(
                    "decision node {node} : (X_test[{sample}, {feature}] = {value}) "
                    "{inequality} {threshold})".format(
                        node=node_id,
                        sample=sample_id,
                        feature=feature[node_id],
                        value=X_test[sample_id, feature[node_id]],
                        inequality=threshold_sign,
                        threshold=threshold[node_id],
                    )
                )
                nodeList.append(node_id)
                sampleIdList.append(sample_id)
                featureIdList.append(features[feature[node_id]])
                valueList.append(X_test[sample_id, feature[node_id]])
                inequalityList.append(threshold_sign)
                thresholdList.append(threshold[node_id])
    #sys.stdout = oStdout
    data = pd.DataFrame({
                     'node': nodeList,
                     'sampleId': sampleIdList,
                     'featureId': featureIdList,
                     'valueId': valueList,
                     'inequality': inequalityList,
                     'threshold': thresholdList
                    })

    data.to_csv("path.csv")


def main():
    """
    Driver function
    """

    iris = load_dataset()

    # Splitting the dataset
    removed =[0, 10, 20, 30, 50, 60, 70, 80, 90, 100]
    new_target = np.delete(iris.target, removed)
    new_data = np.delete(iris.data, removed, axis=0)
    features = iris['feature_names']
    X_test = iris.data[removed]

    # Train classifier
    clf = tree.DecisionTreeClassifier()

    # Defining decision tree classifier
    clf = clf.fit(new_data, new_target)

    # Train data on new data and new target
    tree.plot_tree(clf)

    # Make predictions
    prediction = clf.predict(iris.data[removed])
    dot_data = tree.export_graphviz(clf, out_file=None)
    iris = load_iris()

    # Export
    r = tree.export_text(clf, feature_names=iris['feature_names'])
    tree.export_graphviz(clf, out_file='tree.dot')
    dot_data = tree.export_graphviz(clf, out_file=None,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     special_characters=True)
    graph = graphviz.Source(dot_data)

    # Assign removed data as input
    #print("Original Labels", iris.target[removed])
    #print("Labels Predicted", prediction)

    print_decision_paths(clf, X_test, features)


if __name__=="__main__":
    main()
