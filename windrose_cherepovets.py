import plotly.express as px
import plotly.graph_objects as go
fig = go.Figure()

r_cloud=[30.927835051546392, 19.587628865979383, 12.371134020618557, 8.24742268041237, 4.123711340206185, 6.185567010309279, 4.123711340206185, 11.34020618556701, 24.742268041237114, 38.144329896907216, 51.546391752577314, 77.31958762886599, 100.0, 98.96907216494846, 79.38144329896907, 63.91752577319587, 52.57731958762887, 37.11340206185567]
r_track=[75.60975609756098, 56.09756097560976, 36.58536585365854, 12.195121951219512, 14.634146341463413, 0.0, 9.75609756097561, 0.0, 4.878048780487805, 2.4390243902439024, 12.195121951219512, 24.390243902439025, 34.146341463414636, 29.268292682926827, 48.78048780487805, 73.17073170731707, 87.8048780487805, 100.0]

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
    r=r_common,
    name='Common',
    marker_color='rgba(106,81,163,0.5)'
))

fig.add_trace(go.Barpolar(
    r=r_cloud_over,
    name='Cloud',
    marker_color='rgba(100,150,201,0.5)'
))

fig.add_trace(go.Barpolar(
    r=r_track_over,
    name='Track',
    marker_color='rgba(10,120,245,0.5)'
))

fig.update_layout(
    title='Wind Speed Distribution in Laurel, NE',
    font_size=16,
    legend_font_size=16,
    polar_radialaxis_ticksuffix='%',
    polar_angularaxis_rotation=90,

)
fig.write_image("Cherepovets_reanalysis.png")
