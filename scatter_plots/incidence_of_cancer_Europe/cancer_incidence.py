# By B. Javanmardi (https://github.com/behjava)
# Visualising

import os
import pandas as pd
import plotly.express as px


def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)

data=pd.read_csv('data/HFA_357_EN.csv', sep=',',
                    skiprows=25, skipfooter=56, header=0)
