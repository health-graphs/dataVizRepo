# By B. Javanmardi (behnamjavanmardi.com)
# Visualising Estimated infant mortality per 1000 live births in Europe 
# data file HFA_73_EN.csv obtained from European Health Information Gateway.
# Years data is available in this file: 1950—2019
# read file skip metadata rows

import pandas as pd
import plotly.express as px

data=pd.read_csv('/Users/javanmardi/Work/DataViz/dataViz_data/infant_mortality/HFA_73_EN.csv', sep=',',
                    skiprows=25, skipfooter=56, header=0)

# group by year and average
EURO_mean=data.groupby(['YEAR']).mean()

# scatter plot using customized color_continuous_scale
fig=px.scatter(EURO_mean, size='value', color='value', color_continuous_scale=[[0, 'green'], [0.5, 'yellow'], [1, 'red']],
               title="Estimated infant mortality per 1000 live births")
fig.update_yaxes(title_text='Deaths per 1000 live births')
fig.show()
