# By B. Javanmardi (https://github.com/behjava)
# Visualising cumulative death caused by COVID19
# data file WHO-COVID-19-global-data.csv obtained from WHO.

import os
import numpy as np
import pandas as pd
import plotly.express as px
import pycountry


def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)

data=pd.read_csv('/Users/javanmardi/Work/DataViz/dataViz_data/COVID19/WHO/WHO-COVID-19-global-data.csv', sep=',', header=0)


# Enhanced function to convert two-letter country codes to three-letter codes
# with error handling
def alpha2_to_alpha3(alpha_2):
    try:
        return pycountry.countries.get(alpha_2=alpha_2).alpha_3
    except Exception:
        # Print the problematic code for review
        # print(f"Error converting country code: {alpha_2}")
        return None

# Apply the conversion to the data
data['country_code_alpha3'] = data['Country_code'].apply(alpha2_to_alpha3)



# Convert 'Cumulative_deaths' to log for a better color diffrentiation, but control the tick values.

data['log_Cumulative_deaths'] = np.log10(data['Cumulative_deaths'] + 1)
tick_positions = [1,2,3,4,5,6,7,8,9,10]
tick_texts = [str(int(10**(tick))) for tick in tick_positions]

# Create the interactive world map
fig = px.choropleth(data, locations='country_code_alpha3',
                    color='log_Cumulative_deaths',
                    hover_name='Country',
                    hover_data={'Cumulative_deaths': True, 'log_Cumulative_deaths': False, 'country_code_alpha3': False},
                    animation_frame= "Date_reported",color_continuous_scale='Portland')


# Customize the colorbar to reflect the original data values
fig.update_coloraxes(colorbar_tickmode='array', colorbar_tickvals=tick_positions, colorbar_ticktext=tick_texts)

fig.update_coloraxes(colorbar_orientation='h')
fig.update_coloraxes(colorbar_title_text='Cumulative COVID-19 Deaths')

fig.update_layout(modebar_remove=['lasso2d','select2d'])

assure_path_exists('output/')
fig.write_html("output/cumulative_COVID19_death_WHO.html")
# fig.write_image("output/infant_mortality_Europe.jpg", scale=5.0)

fig.show()
