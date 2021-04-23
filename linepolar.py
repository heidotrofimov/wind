import plotly.graph_objects as go
import numpy as np

directions=[0, 22.5, 45.0, 67.5, 90.0, 112.5, 135.0, 157.5, 180.0, 202.5, 225.0, 247.5, 270.0, 292.5, 315.0, 337.5]
mock_dir=[]
for i in range(len(directions)):
    new_dir=np.abs(directions[i]-360)
    mock_dir.append(new_dir)
    
directions=mock_dir

r_track=[62.96, 18.51851851851852, 5.555555555555555, 11.11111111111111, 11.11111111111111, 1.8518518518518516, 1.8518518518518516, 5.555555555555555, 5.555555555555555, 1.8518518518518516, 5.555555555555555, 1.8518518518518516, 16.666666666666664, 48.148148148148145, 100.0, 70.37037037037037]

  
fig = go.Figure(data=go.Scatterpolar(
    r=r_track,
    theta=mock_dir,
    mode='lines',
))
  
fig.show()
