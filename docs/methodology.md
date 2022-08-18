<h1 align='center'>
     Methodology 🧭
</h1>

![Methodology]()
<p center='align'> <b>Figure 1: Research methodology of the study</b></p>

## Data 

* **Source:** National Bridge Inventory
* **Timeline:** 1992 to 2021
* **State:** All U.S. states 🇺🇸
* 👉 [**Data acqusition and transformation**](https://github.com/kaleoyster/nbi/tree/b5fb41950ee0a44c1d8967a1a672c0e3ea47b07f)

## Data transformation

### Conversion of the decision tree to graph network
The following are the implemented steps used for transformation of the dataset. 

1. Conversion of decision tree rules from  for each sample
    - Serialization: Converting decision tree rules to csv files for each sample.

## 🧪 Formulaization / conversion of the decision - tree to nodes

### Definition of graphs
Formally, a graph is sets $(V, E)$, where [1]:
- $V$ is a non-empty set whose elements are called $vertices$
- $E$ is a collection of two-element subsets of $V$ called $Edges$.

We use $A--B$ to denote an edge between vertices $A$ and $B$ rather than the set notation $${A, B}$$. Note that $A--B$ and $B--A$ are the same edge, just as ${A, B}$ and ${B, A}$ are the same set.

### Mathematical formulation


### Edge cases
1. Every node should be connected to at least with a link node. Because, every node comes from root node.
2. If there is a commonality between the nodes then there is a link.
3. There can not be duplicate links in a system.
## Similar techniques

###  Conceptual graph analysis
Developed by Grasser and Murachver in 1985 to get detailed knwoledge from computer science experts and found  away of representing it in a coherent fashion. There was a transformation of nodes an questions of the original method and have extended its application from information design to instructional design.j

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

#### Differences from the Network

## References
1. [Conceptual Graph Analysis - a brief introduction](https://slideplayer.com/slide/3741719/)
