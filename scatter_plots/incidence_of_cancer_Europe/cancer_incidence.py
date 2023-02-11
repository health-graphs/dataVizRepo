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
                    skiprows=25, skipfooter=43, header=0)


# group by year and average
EURO_mean=round(data.groupby(['YEAR']).mean(),1)

# scatter plot using customized color_continuous_scale
fig=px.scatter(EURO_mean, size='value', color='value', color_continuous_scale=[[0, 'green'], [0.5, 'yellow'], [1, 'red']],
               title="Average ...")



fig.show()
