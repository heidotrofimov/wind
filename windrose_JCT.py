import plotly.express as px
import plotly.graph_objects as go
import numpy as np
fig = go.Figure()
mock_dir=[]
directions=[0,45,90,135,180,225,270,315]
for i in range(len(directions)):
    new_dir=np.abs(directions[i]-360)
    mock_dir.append(new_dir)   
directions=mock_dir
r_track=[19, 6, 6, 8, 8, 21,45, 22 ]
r_cloud=[53, 29, 16, 17, 50, 116,136, 92 ]

r_common=[]
r_track_over=[]
r_cloud_over=[]

for i in range(len(r_cloud)):
    cloud=r_cloud[i]
    track=r_track[i]
    if(cloud>track):
        common=track
        cloud_over=cloud
        track_over=0
        new_common=common/(1+(common/cloud_over))
        new_cloud_over=cloud_over/(1+(common/cloud_over))
        r_common.append(new_common)
        r_cloud_over.append(new_cloud_over)
        r_track_over.append(track_over)
    elif(track>cloud):
        common=cloud
        cloud_over=0
        track_over=track
        new_common=common/(1+(common/track_over))
        new_track_over=track_over/(1+(common/track_over))
        r_common.append(new_common)
        r_cloud_over.append(cloud_over)
        r_track_over.append(new_track_over)
    else:
        common=track
        track_over=0
        cloud_over=0
        r_common.append(common)
        r_cloud_over.append(cloud_over)
        r_track_over.append(track_over)
    

fig.add_trace(go.Barpolar(
   
    theta = directions,
    r=r_common,
 
    name='Common',
    marker_color='rgba(106,81,163,0.5)'
))

fig.add_trace(go.Barpolar(
    
    theta = directions,
    r=r_cloud_over,
    name='Cloud',
    marker_color='rgba(100,150,201,0.5)'
))

fig.add_trace(go.Barpolar(
    
    theta = directions,
    r=r_track_over,

    name='Track',
    marker_color='rgba(10,120,245,0.5)'
))

fig.update_layout(
    font_size=16,
    legend_font_size=16,
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
#fig.write_image("Thompson_reanalysis.png")

