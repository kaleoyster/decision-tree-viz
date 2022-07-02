"""
Description:
    A decision tree model to predict iris dataset.

Author:
    Akshay Kale

Date:
    July 2, 2022
"""
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

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

def main():
    """
    Driver function
    """
    iris = load_dataset()
    print(iris.feature_names)

    # Spilitting the dataset
    removed =[0,50,100]
    new_target = np.delete(iris.target,removed)
    new_data = np.delete(iris.data,removed, axis=0)

    # Train classifier
    clf = tree.DecisionTreeClassifier()

    # Defining decision tree classifier
    clf = clf.fit(new_data,new_target)

    # Train data on new data and new target
    tree.plot_tree(clf)

    # Make predictions
    prediction = clf.predict(iris.data[removed])

    # Assign removed data as input
    print("Original Labels", iris.target[removed])
    print("Labels Predicted", prediction)

if __name__=="__main__":
    main()
