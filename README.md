<h1 align='center'>
 🌲 Exploring the rules of the decision tree 🌲
</h1>

![Network of decision tree](images/hexagon-actuarial.png)

- **Big idea** -- Machine learning models are difficult to understand. 
- **Small idea** -- Specifically, understanding, "How the rules affect the the entity" is not possible right now with complex models.
- **Birds eye view of the idea** --  We plan to undo the complexity of the machine learning model and explain what it means to make for the rest of the entities.
- **Technical details** --  Train a complex dataset (NBI) simple machine learning model such as decision tree. Using graphs / networks understand the rules of the decision tree.

### 🎯 Objective
- The objective of this research study is to develop a method for explaining large decision rules and how it affects bridges. 

### 💪 Challenge
- In the NBI dataset, it is a **challenge** to identify maintainance patterns and various factors that interact in explaining bridge performance and maintenance. Because, the use of `reconstruction_year` does not provide an valuable information about the type of repair or reconstruction done.

### 🧪 Solution
- To address this challenge we can use bridge intervention matrix, that utilizes the bridge intervention matrix for `deck` to identify various types of intervention depending on the probability of the transition.
- With large set of complicated rules, it is difficult to understand the interactions.
- We use explainable methods such as decision trees.
- Identify the commonality between the bridges by visualizing the rules between the trees.

![Deck Bridge Intervention Matrix](assets/intervention-matrix.png)

### 👉 Additional references
| Document      | Documentation type | Description |
| ------------- | ------------------ | ----------- |
| [Quickstart](docs/quickstart.md) | Concept | An overview and guide to setup this project |
| [Methodology](docs/methodology.md) | Concept, Task | Simplest possible method of implementing your API |
| [Functions](docs/functions.md) | Reference | List of references for the functions used|
| [Related Projects](docs/related-projects.md) | Reference | List of projects related to this repository |

