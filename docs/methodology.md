<h1 align='center'>
     Methodology 
</h1>

<p center='align'> <b>Figure 1: Research methodology of the study</b></p>

## Data 
* **Source:** IRIS dataset
* 👉 [**Data acqusition and transformation**](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)

## Data transformation

To generate a network of rules and samples, following are the steps:

1. Conversion of the decision tree rules and samples to a network
2. Network analysis

### Conversion of the decision tree to network

The following steps are implemented for transformation of the dataset. 

1. Conversion of decision tree rules from for each sample
    - Serialization: Converting decision tree rules to csv files for each sample.

## 🧪 Formulation of the rule and sample network 

The following is the formulation of the idea (rule and sample network) using definition / notation from graph theory.


### Mathematical definition and formulation

The following is the mathematical formualtion of the rules and sample network Formally, a graph is sets $(V, E)$, where [1]:

- $V$ is a non-empty set whose elements are called $vertices$, each element in $V$ is a sample, or a point of data in the given dataset.
- $E$ is a collection of two-element subsets of $v \in V$ called $Edges$. Each edge $e \in E$ denotes a rule association of two-element subset.

The network of the $E$ and $V$ is defined as:
$$ N = (V, E) $$

We use $A--B$ to denote an edge between vertices $A$ and $B$ rather than the set notation ${A, B}$. Note that $A--B$ and $B--A$ are the same edge, just as ${A, B}$ and ${B, A}$ are the same set.

### TODO
- **How to define a cluster?**
- **How to define graphical properties of rules and samples?**
    - What is true for a specific link and node?
- **How to describe that there is a value to the link as well?**
- **How to describe that there is a value to the size of node as well?**

### Edge cases
1. Every node should be connected to at least with a link node. Because, every node comes from root node.
2. If there is a commonality between the nodes then there is a link.
3. There can not be duplicate links in a system.

## Similar techniques

###  Conceptual graph analysis
- Conceptual graph analysis was developed by Grasser and Murachver in 1985 to get detailed knowledge from computer science experts and found away of representing it in a coherent fashion. There was a transformation of nodes an questions of the original method and have extended its application from information design to instructional design.

- Conceptual graph analysis are fundamentally different from rule and graph objects.

#### Assumptions
1. Expert knowledge can be gained through structured and unstructured interview.
2. Expert knowledge can be graphed and labeled in a graph 

#### Steps
1. Clarify the uses of the graph information
2. Choose a set of situations for the expert to analyze
3. Construct a rough graph
4. Prepare a list of follow-up questions
5. Expand the graph
6. Review the final graph


## References
1. [Conceptual Graph Analysis - a brief introduction](https://slideplayer.com/slide/3741719/)
