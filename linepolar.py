import plotly.graph_objects as go
import numpy as np

directions=[0, 22.5, 45.0, 67.5, 90.0, 112.5, 135.0, 157.5, 180.0, 202.5, 225.0, 247.5, 270.0, 292.5, 315.0, 337.5,360]
mock_dir=[]
for i in range(len(directions)):
    new_dir=np.abs(directions[i]-360)
    mock_dir.append(new_dir)
    
directions=mock_dir

#r_track=[62.96, 18.51851851851852, 5.555555555555555, 11.11111111111111, 11.11111111111111, 1.8518518518518516, 1.8518518518518516, 5.555555555555555, 5.555555555555555, 1.8518518518518516, 5.555555555555555, 1.8518518518518516, 16.666666666666664, 48.148148148148145, 100.0, 70.37037037037037,62.96]
h_track=[54.18795514032085, 57.86920786607794, 62.249213056269355, 58.01055006083206, 61.39360623533046, 63.76329502746993, 61.831623346823044, 58.69859119081392, 57.124130803087645, 55.123535747927484, 55.369702528198964, 58.092380987220146, 58.564381130766826, 57.657385871465245, 58.40202860385087, 56.93434278676708,54.18795514032085]

  
fig = go.Figure(data=go.Scatterpolar(
    r=h_track,
    theta=mock_dir,
    mode='lines',
))

fig.update_layout(
    font_size=16,
    legend_font_size=18,
    polar_radialaxis_ticksuffix='',
    polar_angularaxis_rotation=90,
    direction='clockwise',
    polar_angularaxis=dict(
        tickmode = 'array',
        tickvals = [0, 45, 90, 135, 180, 225,270,315],
        ticktext = ['N', 'NW', 'W', 'SW', 'S', 'SE','E','NE']
    )
)
  
fig.show()
