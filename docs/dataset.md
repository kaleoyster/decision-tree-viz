<h1 align='center'>
   📀 Dataset
</h1>

The following table provides description regarding data generated for this repository.

### Data processing:

In understanding the 
1. Data collection
2. Data processing
3. Data transformation
4. Modeling

### Attributes:


The following are the attributes required to model the decision tree for future maintenance and repair.

| Attribute  | Data Type | Sample size | Data Source |
|----------- |-----------|-------------|-------------|
| Year built | numerical | 10,000      | NBI         |
| Average Daily Traffic | numerical -> categorical | X | NBI |
| Average Daily Truck Traffic  | numerical -> categorical | X | NBI |
| Snowfall | numerical | X | NBI |
| Longitude | numerical | X | NBI |
| Latitude | numerical | X | NBI |
| Freeze thaw | numerical | X | NBI |
| Skew | categorical | X | NBI |
| Material | categorical | X | NBI |
| Number of spans in Main unit | numerical | X | NBI |
| Length of maximum span | numerical | X | NBI |
| Structure Length | numerical | X | NBI | 
| Bridge roadway width curb to curb | X | NBI |
| Operating rating | numerical | X | NBI |
| Scour critical bridges | ordinal | X | NBI |
| Lanes on structure | numerical | X | NBI |
| Designated Inspection Frequency | numerical | X | NBI |
| Toll | numerical | X | NBI | 
| Designed Load | numerical | X | NBI |
| Type of design | Categorical | X | NBI |
| Deck CR | ordinal -> numerical | X | NBI |  
| Substructure CR | ordinal -> numerical | NBI | 
| Superstructure CR | ordinal -> numerical | NBI | 

The class label is computed using condition rating for each of the components, with the use of bridge intervention matrix:
1. Superstructure
2. Substructure
3. Deck

### 👉  Dataset

| Document      | Documentation type | Description |
| ------------- | ------------------ | ----------- |
| [Path.txt](dataset.md) | Data | Contains raw rules from the decision tree|
| [Path.csv](quickstart.md) | Data | Contains serialized rules of the decision tree |

