import plotly.graph_objects as go
  
fig = go.Figure(data=go.Scatterpolar(
    r=[1, 2, 3, 4, 5, 6, 7, 8, 9],
    theta=[69, 141, 213, 285, 357,
           429, 501, 573, 645],
    mode='lines',
))
  
fig.show()
