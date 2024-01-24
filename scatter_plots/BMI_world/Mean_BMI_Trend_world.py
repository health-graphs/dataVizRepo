# By B. Javanmardi (https://github.com/behjava)
# Visualising Mean BMI Trend in the world
# data files NCD_BMI_MEANC_females.csv and NCD_BMI_MEANC_males.csv obtained from Global Health Observatory data repository.



import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)

data_males=pd.read_csv('data/NCD_BMI_MEANC_males.csv', sep=',', header=0)
data_females=pd.read_csv('data/NCD_BMI_MEANC_females.csv', sep=',', header=0)

#removing the first three rows
data_males=data_males.drop([0, 1, 2])
data_females=data_females.drop([0, 1, 2])

#renaming the first column
data_males=data_males.rename(columns={'Unnamed: 0': 'Countries'}, errors="raise")
data_females=data_females.rename(columns={'Unnamed: 0': 'Countries'}, errors="raise")


# Define a regular expression to extract the measurement part
pattern = r'(\d+\.\d+)'

# Apply the regular expression to each cell in the DataFrame (excluding the first column)
data_males.iloc[:, 1:] = data_males.iloc[:, 1:].apply(lambda col: col.str.extract(pattern, expand=False))
data_females.iloc[:, 1:] = data_females.iloc[:, 1:].apply(lambda col: col.str.extract(pattern, expand=False))

# Convert the measurement values to numeric (float) for averaging
data_males.iloc[:, 1:] = data_males.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
data_females.iloc[:, 1:] = data_females.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Calculate the mean along each column (year)
average_per_year_males = data_males.iloc[:, 1:].mean()
average_per_year_females = data_females.iloc[:, 1:].mean()

# Sort the result in ascending order based on the number of years
average_per_year_males_sorted = average_per_year_males.sort_values()
average_per_year_females_sorted = average_per_year_females.sort_values()

# Convert the Series to a DataFrame
average_per_year_df_males = average_per_year_males_sorted.to_frame(name='Mean_BMI')
average_per_year_df_females = average_per_year_females_sorted.to_frame(name='Mean_BMI')

# Rename the index to 'YEAR'
average_per_year_df_males = average_per_year_df_males.rename_axis('YEAR')
average_per_year_df_females = average_per_year_df_females.rename_axis('YEAR')


main_opacity=1.0
custom_color_scale = [
    [0.0, 'green'],
    [0.5, 'yellow'],
    [1.0, 'red']
]

fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=average_per_year_df_males.index, y=average_per_year_df_males.Mean_BMI,
                    mode='markers', name='Males',
                    opacity=main_opacity,
                    marker=dict(
                            size=average_per_year_df_males.Mean_BMI,
                            symbol=9,
                            color=average_per_year_df_males.Mean_BMI,
                            colorscale='Plasma')))

fig.add_trace(go.Scatter(x=average_per_year_df_females.index, y=average_per_year_df_females.Mean_BMI,
                    mode='markers', name='Females',
                    opacity=main_opacity,
                    marker=dict(
                            size=average_per_year_df_females.Mean_BMI,
                            symbol=3,
                            color=average_per_year_df_females.Mean_BMI,
                            colorscale='Viridis')))




fig.update_yaxes(title_text='Average Worldwide BMI Trend')
fig.update_xaxes(title_text='YEAR')
fig.update(layout_coloraxis_showscale=False)
fig.add_annotation(dict(font=dict(color='black',size=10)), x=30, y=22.5,
            text="©DataDeed.de",
            showarrow=False,
            yshift=1)

fig.update_layout(modebar_remove=['lasso2d','select2d'])

assure_path_exists('output/')
fig.write_html("output/Mean_BMI_Trend_world.html")
fig.write_image("output/Mean_BMI_Trend_world.jpg", scale=5.0)

fig.show()
