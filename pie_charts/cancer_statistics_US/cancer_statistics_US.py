# By B. Javanmardi (https://github.com/behjava)
# Visualising Cancer Statistics in US based on
# Cancer statistics, 2023
# Rebecca L. Siegel MPH, Kimberly D. Miller MPH, Nikita Sandeep Wagle MBBS, MHA, PhD, Ahmedin Jemal DVM, PhD
# https://doi.org/10.3322/caac.21763


import os
import pandas as pd
import plotly.express as px


def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)

data=pd.read_csv('data/US_Cancer_statistics_2023.csv', sep=';', header=0)



# for males
fig = px.pie(data, values='Estimated new cases Male', names='Cancer Type', title='Estimated 2023 cancer statistics for males in the United States')

fig.add_annotation(dict(font=dict(color='black',size=10)), x=0.01, y=0.01,
            text="©DataDeed.de",
            showarrow=False,
            yshift=1)
#
# fig.add_annotation(dict(font=dict(color='grey',size=15)), x=0.95, y=0.97,
#             text="Data from Siegel et al. (2023)",
#             showarrow=False,
#             yshift=1)

fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

# for females
fig2 = px.pie(data, values='Estimated new cases Female', names='Cancer Type', title='Estimated 2023 cancer statistics for females in the United States')

fig2.add_annotation(dict(font=dict(color='black',size=10)), x=0.01, y=0.01,
            text="©DataDeed.de",
            showarrow=False,
            yshift=1)
#
# fig2.add_annotation(dict(font=dict(color='grey',size=15)), x=0.95, y=0.97,
#             text="Data from Siegel et al. (2023)",
#             showarrow=False,
#             yshift=1)

fig2.update_traces(textposition='inside')
fig2.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')


assure_path_exists('output/')

fig.write_html("output/US_Cancer_statistics_2023_Males.html")
fig.write_image("output/US_Cancer_statistics_2023_Males.jpg", scale=2.0)

fig2.write_html("output/US_Cancer_statistics_2023_Females.html")
fig2.write_image("output/US_Cancer_statistics_2023_Females.jpg", scale=2.0)


fig.show()
# fig2.show()
