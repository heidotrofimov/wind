
import plotly.express as px
import plotly.graph_objects as go
fig = go.Figure()

r_cloud=[9.615384615384617, 15.384615384615385, 5.769230769230769, 5.769230769230769, 9.615384615384617, 7.6923076923076925, 9.615384615384617, 21.153846153846153, 46.15384615384615, 63.46153846153846, 82.6923076923077, 80.76923076923077, 100.0, 100.0, 94.23076923076923, 51.92307692307693, 34.61538461538461, 25.0]

r_track=[21.21212121212121, 21.21212121212121, 15.151515151515152, 6.0606060606060606, 12.121212121212121, 12.121212121212121, 21.21212121212121, 3.0303030303030303, 6.0606060606060606, 21.21212121212121, 24.242424242424242, 87.87878787878788, 100.0, 87.87878787878788, 69.6969696969697, 81.81818181818183, 72.72727272727273, 51.515151515151516]

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
fig.write_image("Norilsk_reanalysis.png")
