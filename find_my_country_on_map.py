import plotly.express as px

import plotly.io as pio

pio.renderers.default = "browser"

country = input("Enter your country name: ")

data = {
    'Country': [country], 
    'Values': [100]
}

fig = px.choropleth(
    data, 
    locations='Country', 
    locationmode="country names", 
    color="Values", 
    color_continuous_scale="Inferno", 
    title=f"Country MaP Highlighting {country}"
)

fig.write_html("map.html")
