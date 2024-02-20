# MOSTLY AI - GenAI for Tabular Data

A Python wrapper for the MOSTLY AI platform.

| intent                                         | call              |
|------------------------------------------------|-------------------|
| Train a Generative AI on your tabular data     | `mostly.train`    |
| Generate unlimited synthetic data on demand    | `mostly.generate` |
| Empower your team with safe synthetic data     | `mostly.share`    |
| Connect to any data source within your org     | `mostly.connect`  |
| Probe the generator for the data that you need | `mostly.probe`    |
| Enrich the data with new LLM intelligence      | `mostly.enrich`   |


## Installation
```shell
pip install mostlyai
```

## Basic Usage
```python
from mostlyai import MostlyAI
mostly = MostlyAI(api_key='your_api_key') 
g = mostly.train(data)      # train a generator on your data
sd = mostly.generate(g)     # generate a synthetic dataset
syn = sd.data()             # consume synthetic as pd.DataFrame
```

## Advanced Usage
```python
from mostlyai import MostlyAI
mostly = MostlyAI(api_key='your_api_key') 
```
