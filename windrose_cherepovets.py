import plotly.express as px
import plotly.graph_objects as go
import numpy as np
fig = go.Figure()
mock_dir=[]
#directions=[10,30,50,70,90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350]
directions=[0, 22.5, 45.0, 67.5, 90.0, 112.5, 135.0, 157.5, 180.0, 202.5, 225.0, 247.5, 270.0, 292.5, 315.0, 337.5]
for i in range(len(directions)):
    new_dir=np.abs(directions[i]-360)
    mock_dir.append(new_dir)
    
directions=mock_dir
#r_cloud=[30.612244897959183,18.367346938775512,4.081632653061225,12.244897959183673,8.16326530612245,4.081632653061225,2.0408163265306123,0.0,6.122448979591836,6.122448979591836,6.122448979591836,2.0408163265306123,2.0408163265306123,16.3265306122449,38.775510204081634,100.0,73.46938775510205,75.51020408163265]
#r_track=[21.951219512195124,17.073170731707318,7.317073170731707,11.38211382113821,4.0650406504065035,8.94308943089431,6.504065040650407,9.75609756097561,15.447154471544716,22.76422764227642,28.455284552845526,40.65040650406504,47.96747967479675,82.92682926829268,90.2439024390244,100.0,71.54471544715447,47.15447154471545]

r_track=[39.130434782608695, 60.86956521739131, 45.65217391304348, 15.217391304347828, 13.043478260869565, 2.1739130434782608, 6.521739130434782, 0.0, 4.3478260869565215, 8.695652173913043, 15.217391304347828, 34.78260869565217, 32.608695652173914, 47.82608695652174, 86.95652173913044, 100.0, 41.30434782608695]



r_cloud=[14.545454545454545, 26.36363636363636, 13.636363636363635, 7.2727272727272725, 5.454545454545454, 4.545454545454546, 7.2727272727272725, 13.636363636363635, 26.36363636363636, 59.09090909090909, 60.909090909090914, 100.0, 97.27272727272728, 78.18181818181819, 50.0, 52.72727272727272, 18.181818181818183]


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
    marker_color='rgba(255,0,255,0.5)'
))

fig.add_trace(go.Barpolar(
    
    theta = directions,
    r=r_cloud_over,
    name='Cloud',
    marker_color='rgba(0,0,255,0.5)'
))

fig.add_trace(go.Barpolar(
    
    theta = directions,
    r=r_track_over,

    name='Track',
    marker_color='rgba(255,0,0,0.5)'
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
fig.write_image("Cherepovets_reanalysis.png")
