<h1 align='center'>
  Exploring the rules of the decision tree using Graph objects
</h1>

![Network of decision tree]()

- **Big idea** -- Machine learning models are explain and interpret.
- **Small idea** -- Specifically, in understanding the insights offered by the large decision tree models, such as, "How the rules affect the the entity" is challenging with complex models.
- **Birds eye view of the idea** -- We plan to undo the complexity of the large decision tree model and explain the relationship of between the insight within the model with respect to the data. 
- **Technical details** --  Train a dataset on a simple machine learning model such as decision tree. Using graphs / networks understand the rules of the decision tree.
- **What's next** -- Often, there a networks results in formation of various clusters. The future direction can explore the possibilities in identifying similarity between the structures.


### ๐ฏ Objective
- The objective of this research study is to develop a method for explaining large decision rules and how it affects data samples. 
* We specifically try apply this technique on the IRIS dataset.

### ๐ช Challenge
- In the real world dataset, it is a **challenge** to identify patterns and various factors that interact in explaining sample and decision made for each sample. 

### ๐งช Solution
- With large set of complicated rules, it is difficult to understand the interactions.
- We use explainable methods such as decision trees.
- Identify the commonality between the bridges by visualizing the rules between the trees.


### ๐ฌ Getting started

The following are the steps to setup this project:

####  Clone
```zsh
git clone https://github.com/kaleoyster/decision-tree-viz.git
```

#### Run requirements.txt

```zsh
pip install -r requirements.txt
```

#### Run the decision tree model

```zsh
python3 src/decision_tree.py
```

#### Run http server 

```zsh
python -m http.server
```

#### View visualization

```zsh
Serving HTTP on :: port 8000 (http://[localhost]:8000/) ...
```

### ๐ Additional references
| Document      | Documentation type | Description |
| ------------- | ------------------ | ----------- |
| [Quickstart](docs/quickstart.md) | Concept | An overview and guide to setup this project |
| [Methodology](docs/methodology.md) | Concept, Task | Simplest possible method of implementing your API |
| [Functions](docs/functions.md) | Reference | List of references for the functions used|
| [Related Projects](docs/related-projects.md) | Reference | List of projects related to this repository |

