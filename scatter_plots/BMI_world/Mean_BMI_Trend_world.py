# By B. Javanmardi (https://github.com/behjava)
# Visualising Mean BMI Trend in the world
# data files NCD_BMI_MEANC_females.csv and NCD_BMI_MEANC_males.csv obtained from Global Health Observatory data repository.



import os
import pandas as pd
import plotly.express as px


def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)

data_males=pd.read_csv('data/NCD_BMI_MEANC_males.csv', sep=',', header=0)

#removing the first three rows
data_males=data_males.drop([0, 1, 2])

#renaming the first column
data_males=data_males.rename(columns={'Unnamed: 0': 'Countries'}, errors="raise")


# Define a regular expression to extract the measurement part
pattern = r'(\d+\.\d+)'

# Apply the regular expression to each cell in the DataFrame (excluding the first column)
data_males.iloc[:, 1:] = data_males.iloc[:, 1:].apply(lambda col: col.str.extract(pattern, expand=False))

# Convert the measurement values to numeric (float) for averaging
data_males.iloc[:, 1:] = data_males.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Calculate the mean along each column (year)
average_per_year_males = data_males.iloc[:, 1:].mean()

# Sort the result in ascending order based on the number of years
average_per_year_males_sorted = average_per_year_males.sort_values()

# Convert the Series to a DataFrame
average_per_year_df_males = average_per_year_males_sorted.to_frame(name='Mean BMI')

# Rename the index to 'YEAR'
average_per_year_df_males = average_per_year_df_males.rename_axis('YEAR')




# # scatter plot using customized color_continuous_scale
# fig=px.scatter(EURO_mean, size='value', size_max=30, color='value', color_continuous_scale=[[0, 'green'], [0.5, 'yellow'], [1, 'red']])
# fig.update_yaxes(title_text='Infant deaths per 1000 live births')
# fig.update(layout_coloraxis_showscale=False)
# fig.add_annotation(dict(font=dict(color='black',size=10)), x=1955, y=15,
#             text="©DataDeed.de",
#             showarrow=False,
#             yshift=1)
#
# # fig.add_annotation(dict(font=dict(color='grey',size=15)), x=2000, y=43,
# #             text="Data Source: European Health Information Gateway (WHO)",
# #             showarrow=False,
# #             yshift=1)
#
# fig.update_layout(modebar_remove=['lasso2d','select2d'])
#
# assure_path_exists('output/')
# fig.write_html("output/infant_mortality_Europe.html")
# fig.write_image("output/infant_mortality_Europe.jpg", scale=5.0)
#
# fig.show()
