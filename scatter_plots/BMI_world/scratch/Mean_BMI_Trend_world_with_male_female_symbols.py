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


color_continuous_scale=[[0, 'green'], [0.5, '#e6e600'], [1, 'red']]
fig = go.Figure()

# # Add traces
# fig.add_trace(go.Scatter(x=average_per_year_df_males.index, y=average_per_year_df_males.Mean_BMI,
#                     mode='markers', name='Males',
#                     opacity=main_opacity,
#                     marker=dict(
#                             size=average_per_year_df_males.Mean_BMI,
#                             symbol=9,
#                             color=average_per_year_df_males.Mean_BMI,
#                             colorscale=color_continuous_scale)))
#
# fig.add_trace(go.Scatter(x=average_per_year_df_females.index, y=average_per_year_df_females.Mean_BMI,
#                     mode='markers', name='Females',
#                     opacity=main_opacity,
#                     marker=dict(
#                             size=average_per_year_df_females.Mean_BMI,
#                             symbol=3,
#                             color=average_per_year_df_females.Mean_BMI,
#                             colorscale=color_continuous_scale)))


# Define the color scale
color_continuous_scale = px.colors.sequential.Viridis

# Get min and max BMI for color scaling and font sizing
bmi_min = min(average_per_year_df_males['Mean_BMI'].min(), average_per_year_df_females['Mean_BMI'].min())
bmi_max = max(average_per_year_df_males['Mean_BMI'].max(), average_per_year_df_females['Mean_BMI'].max())

# Function to map BMI values to colors
def map_color(value, vmin, vmax, colorscale):
    norm = (value - vmin) / (vmax - vmin)
    color_idx = int(norm * (len(colorscale) - 1))
    return colorscale[color_idx]

# Function to calculate font size based on BMI
def calc_font_size(value, vmin, vmax, min_size, max_size):
    norm = (value - vmin) / (vmax - vmin)
    return norm * (max_size - min_size) + min_size

# Map BMI values to colors and font sizes for males and females
male_colors = average_per_year_df_males['Mean_BMI'].apply(map_color, args=(bmi_min, bmi_max, color_continuous_scale))
female_colors = average_per_year_df_females['Mean_BMI'].apply(map_color, args=(bmi_min, bmi_max, color_continuous_scale))
male_font_sizes = average_per_year_df_males['Mean_BMI'].apply(calc_font_size, args=(bmi_min, bmi_max, 15, 35))
female_font_sizes = average_per_year_df_females['Mean_BMI'].apply(calc_font_size, args=(bmi_min, bmi_max, 15, 35))

# Initialize figure
fig = go.Figure()

# Add Male trace
fig.add_trace(go.Scatter(
    x=average_per_year_df_males.index,
    y=average_per_year_df_males.Mean_BMI,
    mode='text',
    name='Males',
    text=['\u2642']*len(average_per_year_df_males),
    textfont=dict(
        size=male_font_sizes,
        color=male_colors
    )
))

# Add Female trace
fig.add_trace(go.Scatter(
    x=average_per_year_df_females.index,
    y=average_per_year_df_females.Mean_BMI,
    mode='text',
    name='Females',
    text=['\u2640']*len(average_per_year_df_females),
    textfont=dict(
        size=female_font_sizes,
        color=female_colors
    )
))



fig.update_yaxes(title_text='Average Worldwide BMI Trend')
fig.update_xaxes(title_text='YEAR')
fig.update(layout_coloraxis_showscale=False)
fig.add_annotation(dict(font=dict(color='black',size=10)), x=35, y=22.5,
            text="©2024 Health-Graphs.org",
            showarrow=False,
            yshift=10)

fig.update_layout(
    autosize=True,
    modebar_remove=['lasso2d', 'select2d']
)

assure_path_exists('output/')
fig.write_html("output/Mean_BMI_Trend_world.html")
fig.write_image("output/Mean_BMI_Trend_world.jpg", scale=5.0)

fig.show()
