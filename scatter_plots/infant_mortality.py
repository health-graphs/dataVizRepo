import numpy as np
import pandas as pd
import plotly.express as px

# read file skip metadata rows
data=pd.read_csv('/Users/javanmardi/Work/DataViz/dataViz_data/infant_mortality/HFA_73_EN.csv', sep=',', skiprows=25, header=0)
