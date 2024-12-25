# By B. Javanmardi (https://github.com/behjava)
# Visualising Estimated infant mortality per 1000 live births in Europe
# data file HFA_73_EN.csv obtained from European Health Information Gateway.
# Years data is available in this file: 1950—2019
# read file skip metadata rows

import os
import pandas as pd
import plotly.express as px


def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)

data=pd.read_csv('data/HFA_73_EN.csv', sep=',',
                    skiprows=25, skipfooter=56, header=0)

# group by year and average
EURO_mean=round(data.groupby(['YEAR']).mean(),1)

# scatter plot using customized color_continuous_scale
fig=px.scatter(EURO_mean, size='value', size_max=15, color='value', color_continuous_scale=[[0, 'green'], [0.5, 'yellow'], [1, 'red']])
fig.update_yaxes(title_text='Infant deaths per 1000 live births')
fig.update(layout_coloraxis_showscale=False)
fig.add_annotation(dict(font=dict(color='black',size=9)), x=1953, y=10,
            text="©2024 Health-Graphs.com",
            showarrow=False,
            yshift=10)



fig.update_layout(
    autosize=True,
    modebar_remove=['lasso2d', 'select2d']
)

assure_path_exists('output/')
fig.write_html("output/infant_mortality_Europe.html")
fig.write_image("output/infant_mortality_Europe.jpg", scale=5.0)

fig.show()
