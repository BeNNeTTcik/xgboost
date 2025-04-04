# Data Project Template

<a target="_blank" href="https://datalumina.com/">
    <img src="https://img.shields.io/badge/Datalumina-Project%20Template-2856f7" alt="Datalumina Project" />
</a>

### Links to datasets
* Dataset [NID](https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection)<br />
* Dataset [Spambase](https://www.kaggle.com/datasets/colormap/spambase)<br />
* Dataset [SSH_Logs](https://www.kaggle.com/datasets/osamac/ssh-logs-with-attack-classification)<br />

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── external       <- Data from third party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- The final, canonical data sets for modeling
│   ├── raw            <- The original, immutable data dump
│   ├── generated      <- Examples of generated data 
│   ├── NID            <- Dataset [NID](https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection)
│   ├── spambase       <- Dataset [Spambase](https://www.kaggle.com/datasets/colormap/spambase)
│   └── ssh_logs       <- Dataset [SSH_Logs](https://www.kaggle.com/datasets/osamac/ssh-logs-with-attack-classification) 
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Workplace. Naming convention is a number (for ordering),
│   ├── nid.ipynb      <- Script for NID dataset (only oversampling)
│   ├── ssh2.ipynb     <- Script for SSH_logs dataset (only oversampling)
│   ├── spam.ipynb     <- Script for spam dataset (only oversampling)
│   └── undersampling.ipynb        <- Script for hybrid algorithm
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials
│
├── reports            <- Reports and params for machine learning models
│   ├── NID            <- Output reports: Metrix [Accuracy, Recall, F1-score, Precision] for NID dataset
│   │   └── conf matrix    <- Confussion matrix
│   ├── spambase       <- Output reports: Metrix [Accuracy, Recall, F1-score, Precision] for Spambase dataset
│   │   ├── conf matrix            <- Confussion matrix oversampling
|   │   └── conf matrix under      <- Confussion matrix hybrid
│   └── ssh            <- Decision Trees and Random Forest visualisation graphics
│       ├── conf matrix            <- Confussion matrix oversampling
|       └── conf matrix under      <- Confussion matrix hybrid
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── src                         <- Source code for this project
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    │    
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    ├── plots.py                <- Code to create visualizations 
    │
    └── services                <- Service classes to connect with external platforms, tools, or APIs
        └── __init__.py 
```

## Duplicating the .env File
To set up your environment variables, you need to duplicate the `.env.example` file and rename it to `.env`. You can do this manually or using the following terminal command:

```bash
cp .env.example .env # Linux, macOS, Git Bash, WSL
copy .env.example .env # Windows Command Prompt
```

This command creates a copy of `.env.example` and names it `.env`, allowing you to configure your environment variables specific to your setup.

--------
