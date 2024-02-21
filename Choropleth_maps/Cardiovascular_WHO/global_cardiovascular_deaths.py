# By B. Javanmardi (https://github.com/behjava)
# Visualising Death rate from cardiovascular diseases
# data from WHO.

import os
import numpy as np
import pandas as pd
import plotly.express as px
import pycountry


def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)

data=pd.read_csv('data/death_rate_cardiovascular_diseases_WHO.csv', sep=',', skiprows=1, header=0)

# Create the interactive world map
fig = px.choropleth(data, locations='Code',
                    color='Death',
                    hover_name='Entity', hover_data={'Death': True, 'Code': False}, animation_frame= "Year",color_continuous_scale='Oryel')

fig.update_coloraxes(colorbar_orientation='h')
fig.update_coloraxes(colorbar_title_text='Death rate from cardiovascular diseases')


fig.update_layout(modebar_remove=['lasso2d','select2d'])

assure_path_exists('output/')
fig.write_html("output/death_rate_cardiovascular_diseases_WHO.html")


fig.show()
