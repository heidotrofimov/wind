import plotly.express as px
import plotly.graph_objects as go
fig = go.Figure()

r_cloud=[30.612244897959183,18.367346938775512,4.081632653061225,12.244897959183673,8.16326530612245,4.081632653061225,2.0408163265306123,0.0,6.122448979591836,6.122448979591836,6.122448979591836,2.0408163265306123,2.0408163265306123,16.3265306122449,38.775510204081634,100.0,73.46938775510205,75.51020408163265]
r_track=[21.951219512195124,17.073170731707318,7.317073170731707,11.38211382113821,4.0650406504065035,8.94308943089431,6.504065040650407,9.75609756097561,15.447154471544716,22.76422764227642,28.455284552845526,40.65040650406504,47.96747967479675,82.92682926829268,90.2439024390244,100.0,71.54471544715447,47.15447154471545]

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
fig.write_image("Thompson_reanalysis.png")



