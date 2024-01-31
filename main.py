import altair as alt
import pandas as pd

# Loading data
oecd_data = pd.read_excel('Dataset.xlsx')

# Data for the bar chart
bar_chart_data = oecd_data[['Unnamed: 0', '  Life satisfaction (Average Score)']].rename(
    columns={'Unnamed: 0': 'Country'})

# Creating a bar chart
bar_chart = alt.Chart(bar_chart_data).mark_bar().encode(
    x='Country',
    y=alt.Y('  Life satisfaction (Average Score):Q'),
    color='Country',
    tooltip=['Country', '  Life satisfaction (Average Score)']
).properties(
    width=800,
    height=400,
    title='Life Satisfaction by Country'
).interactive()

bar_chart.display()
html_snippet_bar_chart = bar_chart.to_html()

# Creating a scatter plot
scatter_plot_data = oecd_data[['Unnamed: 0', '  Personal earnings ($)', '  Life satisfaction (Average Score)']].rename(
    columns={'Unnamed: 0': 'Country'})

scatter_plot = alt.Chart(scatter_plot_data).mark_circle(size=60).encode(
    x='  Personal earnings ($)',
    y='  Life satisfaction (Average Score)',
    color='Country',
    tooltip=['Country', '  Personal earnings ($)', '  Life satisfaction (Average Score)']
).properties(
    width=800,
    height=400,
    title='Personal Earnings vs. Life Satisfaction by Country'
).interactive()

scatter_plot.display()
html_snippet_scatter_plot = scatter_plot.to_html()

# Creating a line chart
line_chart_data = oecd_data[['Unnamed: 0', '  Employment rate (%)', '  Self-reported health (%)']].rename(
    columns={'Unnamed: 0': 'Country'})

# Creating the actual line chart
line_chart = alt.Chart(line_chart_data).mark_line().encode(
    x='Country',
    y='  Employment rate (%)',
    color='Country',
    tooltip=['Country', '  Employment rate (%)', '  Self-reported health (%)']
)

# Adding a trend line using linear regression
trend_line = line_chart.transform_regression(
    'Country', 'Employment rate (%)', method="linear"
).mark_line(color='black', size=200)

# Combining the original chart with the trend line
line_chart_combine = line_chart + trend_line

# Setting properties
combined_chart_line = line_chart_combine.properties(
    width=800,
    height=400,
    title='Employment Rate and Self-reported Health by Country'
).interactive()

line_chart_combine.display()
html_snippet_line_chart = line_chart_combine.to_html()

# Histogram of Housing Expenditure
histogram_data = oecd_data[['Unnamed: 0', '  Housing expenditure (%)']].rename(columns={'Unnamed: 0': 'Country'})

histogram = alt.Chart(histogram_data).mark_bar().encode(
    alt.X('  Housing expenditure (%)', bin=True),
    y='count()',
    color='Country',
    tooltip=['Country', '  Housing expenditure (%)']
).properties(
    width=800,
    height=400,
    title='Distribution of Housing Expenditure'
).interactive()

histogram.display()
html_snippet_histogram = histogram.to_html()

# Area Chart for Rooms per Person and Water Quality
area_chart_data = oecd_data[['Unnamed: 0', '  Rooms per person (Ratio)']].rename(
    columns={'Unnamed: 0': 'Country'})

# Area Chart for Rooms per Person
area_chart = alt.Chart(area_chart_data).mark_area().encode(
    x='Country',
    y='  Rooms per person (Ratio)',
    color='Country',
    tooltip=['Country', '  Rooms per person (Ratio)']
).properties(
    width=800,
    height=400,
    title='Rooms per Person by Country'
).interactive()

area_chart.display()
html_snippet_area_chart = area_chart.to_html()

#Combining Charts
combined_chart_area = alt.vconcat(bar_chart, scatter_plot, line_chart, histogram, area_chart)

#Saving to HTML
combined_chart_area.save('visualizations.html')

html_snippet_combined = combined_chart_area.to_html()

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Quality of Life Visualizations</title>
</head>
<body>
    <h1>Quality of Life Data Visualizations</h1>
    {html_snippet_combined}
</body>
</html>
"""

with open('visualizations.html', 'w') as file:
    file.write(html_content)
