import plotly.graph_objects as go
import numpy as np

directions=[0, 22.5, 45.0, 67.5, 90.0, 112.5, 135.0, 157.5, 180.0, 202.5, 225.0, 247.5, 270.0, 292.5, 315.0, 337.5,360]
mock_dir=[]
for i in range(len(directions)):
    new_dir=np.abs(directions[i]-360)
    mock_dir.append(new_dir)
    
directions=mock_dir

#r_track=[62.96, 18.51851851851852, 5.555555555555555, 11.11111111111111, 11.11111111111111, 1.8518518518518516, 1.8518518518518516, 5.555555555555555, 5.555555555555555, 1.8518518518518516, 5.555555555555555, 1.8518518518518516, 16.666666666666664, 48.148148148148145, 100.0, 70.37037037037037,62.96]
h_track=[52.95437452323148, 62.18468088513015, 61.400201730603854, 53.208631054795624, 78.2617893355204, 72.38184505624817, 85.72286885402409, 72.2331847061043, 74.75956550005536, 63.89020151701284, 63.49325832461049, 55.65667404494942, 62.34917547789892, 62.67341823732986, 56.434612763800196, 56.37907096404038,52.95437452323148]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=h_track,
    theta=mock_dir,
    mode='lines',
)
             )

fig.add_trace(go.Scatterpolar(
    r=r_track,
    theta=mock_dir,
    mode='lines',
)
             )

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
