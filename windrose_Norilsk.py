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

r_track=[13.157894736842104, 21.052631578947366, 13.157894736842104, 7.894736842105263, 10.526315789473683, 15.789473684210526, 13.157894736842104, 5.263157894736842, 7.894736842105263, 31.57894736842105, 63.1578947368421, 100.0, 92.10526315789474, 63.1578947368421, 81.57894736842105, 63.1578947368421, 18.421052631578945]


r_cloud=[6.557377049180328, 13.114754098360656, 6.557377049180328, 4.918032786885246, 8.19672131147541, 6.557377049180328, 14.754098360655737, 27.86885245901639, 45.90163934426229, 85.24590163934425, 73.77049180327869, 93.44262295081968, 100.0, 80.32786885245902, 36.0655737704918, 39.34426229508197, 8.19672131147541]

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
fig.write_image("Norilsk_reanalysis.png")
