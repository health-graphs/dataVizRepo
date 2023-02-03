# By B. Javanmardi (behnamjavanmardi.com)
# data file HFA_73_EN.csv obtained from European Health Information Gateway.
# Years data is available in this file: 1950—2019
# read file skip metadata rows

import numpy as np
import pandas as pd
import plotly.express as px

data=pd.read_csv('/Users/javanmardi/Work/DataViz/dataViz_data/infant_mortality/HFA_73_EN.csv', sep=',', skiprows=25, skipfooter=56, header=0)

# group by year and average
mean_EUR_infant_mortality=data.groupby(['YEAR']).mean()

# scatter plot
fig = px.scatter(mean_EUR_infant_mortality)
fig.show()
