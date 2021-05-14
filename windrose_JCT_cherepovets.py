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

track_ref=[18, 66, 64, 26, 3, 1, 1, 9, 12, 55]
cloud_ref=[143, 106, 68, 24, 5, 19, 41, 115, 108, 70]

r_track=[64, 26, 3, 1, 1, 9, 18, 66]
r_cloud=[68, 24, 5, 19, 41, 115, 143, 106]

r_tr=[]
r_cl=[]

for i in range(len(r_track)):
    r_tr.append(r_track[i]/max(track_ref)*100)
    r_cl.append(r_cloud[i]/max(cloud_ref)*100)
r_track=r_tr
r_cloud=r_cl
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
        new_cloud_over=cloud_over-common
        r_common.append(common)
        r_cloud_over.append(new_cloud_over)
        r_track_over.append(track_over)
    elif(track>cloud):
        common=cloud
        cloud_over=0
        track_over=track
        new_track_over=track_over-common
        r_common.append(common)
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
 
    name='Clouds and tracks overlapping',
    marker_color='rgba(255,0,255,0.5)'
))

fig.add_trace(go.Barpolar(
    
    theta = directions,
    r=r_cloud_over,
    name='Only cloud',
    marker_color='rgba(0,0,255,0.5)'
))

fig.add_trace(go.Barpolar(
    
    theta = directions,
    r=r_track_over,

    name='Track',
    marker_color='rgba(255,0,0,0.5)'
))
fig.update_layout(
    font_size=36,
    legend_font_size=36,
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
fig.write_image("Cherepovets_JCT.png")
