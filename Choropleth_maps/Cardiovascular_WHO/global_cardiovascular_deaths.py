# By B. Javanmardi (https://github.com/behjava)
# Visualising Death rate from cardiovascular diseases
# data from WHO.

import os
import numpy as np
import pandas as pd
import plotly.express as px
import pycountry

# import plotly.offline as pyo




def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)

data=pd.read_csv('data/death_rate_cardiovascular_diseases_WHO.csv', sep=',', skiprows=1, header=0)

# Create the interactive world map
fig = px.choropleth(data, locations='Code',
                    color='Death',
                    hover_name='Entity', hover_data={'Death': True, 'Code': False}, animation_frame= "Year",color_continuous_scale='Burgyl')

fig.update_coloraxes(colorbar_orientation='h')
fig.update_coloraxes(colorbar_title_text='Death rate from cardiovascular diseases')

fig.update_layout(
    autosize=True,
    modebar_remove=['lasso2d', 'select2d']
)

fig.add_annotation(dict(font=dict(color='black',size=9)), x=0.95, y=-0.05,
            text="©2024 Health-Graphs.org",
            showarrow=False,
            yshift=10)



assure_path_exists('output/')

# pyo.plot(fig, filename='output/death_rate_cardiovascular_diseases_WHO.html', auto_open=False, config={'responsive': True})

fig.write_html("output/death_rate_cardiovascular_diseases_WHO.html")
fig.write_image("output/death_rate_cardiovascular_diseases_WHO.jpg", scale=5.0)



fig.show()
