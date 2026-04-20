# Visual Acuity Predictor

🚧 **Work in progress**

This project demonstrates an end-to-end machine learning workflow for predicting visual acuity from clinical parameters, including data preprocessing, model training, and FastAPI deployment.

The original dataset contains sensitive medical information and is not publicly available.  
A synthetic dataset with the same schema and similar statistical properties is provided for demonstration purposes.

To improve reliability on out-of-distribution inputs, the API applies prediction bounds and returns warnings when post-processing rules are triggered.


## Project structure

```
visual-acuity-predictor/  
├─ app/            # FastAPI application  
├─ artifacts/      # trained models and other generated files  
├─ data/           # synthetic dataset used for demonstration  
├─ notebooks/      # exploratory analysis and experiments  
├─ src/            # source code for data processing and model training  
├─ README.md  
└─ requirements.txt  
```


## Installation

1. Clone the repository:

```bash
git clone https://github.com/molgan/visual-acuity-predictor.git  
cd visual-acuity-predictor
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```

