import plotly.express as px

import pandas as pd 

data = pd.DataFrame(dict(keys = [50, 60, 30, 20], values = ["Raw Material Cost", "Factory Cost", "Adminstration Cost", "Selling Cost"]))

figure = px.line_polar(data, r='keys', theta='values', line_close=True)

figure.update_traces(fill="toself")

figure.write_html("radar.html")