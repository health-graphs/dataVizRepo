# By B. Javanmardi (https://github.com/behjava)
# Visualising Total Fertility Rate in Europe
# data file HFA_25_EN.csv obtained from European Health Information Gateway.
# Years data is available in this file: 1950—2019
# read file skip metadata rows

import os
import pandas as pd
import plotly.express as px


def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)

data=pd.read_csv('data/HFA_25_EN.csv', sep=',',
                    skiprows=25, skipfooter=83, header=0)

# group by year and average
EURO_mean=round(data.groupby(['YEAR']).mean(),1)

# EURO_mean_after_1979 = EURO_mean[EURO_mean.index>1979]

# scatter plot using customized color_continuous_scale
fig=px.scatter(EURO_mean, size='value', size_max=30, color='value', color_continuous_scale=[[0, 'red'], [0.5, 'yellow'], [1, 'green']])
fig.update_yaxes(title_text='Births per women')
fig.update(layout_coloraxis_showscale=False)
fig.add_annotation(dict(font=dict(color='black',size=10)), x=2012, y=1.3,
            text="©DataDeed.de",
            showarrow=False,
            yshift=1)

# fig.add_annotation(dict(font=dict(color='grey',size=15)), x=2000, y=43,
#             text="Data Source: European Health Information Gateway (WHO)",
#             showarrow=False,
#             yshift=1)

fig.update_layout(modebar_remove=['lasso2d','select2d'])

assure_path_exists('output/')
fig.write_html("output/total_fertility_rate_Europe.html")
fig.write_image("output/total_fertility_rate_Europe.jpg", scale=5.0)

fig.show()
