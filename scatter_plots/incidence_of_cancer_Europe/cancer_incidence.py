# By B. Javanmardi (https://github.com/behjava)
# Visualising Incidence of cancer per 100 000 in Europe
# data file HFA_357_EN.csv obtained from European Health Information Gateway.
# some outliers were rejected before ploting. The data source should be consulted for details.

import os
import pandas as pd
import plotly.express as px


def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)

data=pd.read_csv('data/HFA_357_EN.csv', sep=',',
                    skiprows=25, skipfooter=43, header=0)


# group by year and average
EURO_mean=round(data.groupby(['YEAR']).mean(),1)


# filtered due to incomplete or outlier behaviour of the data points. The data tabel and the source should be consulted for more details.
filtered=EURO_mean.loc[1980:2018]

# scatter plot using customized color_continuous_scale
fig=px.scatter(filtered, size='value', color='value', color_continuous_scale=[[0, 'green'], [0.5, 'yellow'], [1, 'red']],
               title="Average ...")




fig.show()
