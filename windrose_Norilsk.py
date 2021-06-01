import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import sys
fig = go.Figure()
mock_dir=[]
#directions=[10,30,50,70,90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350]
directions=[0, 22.5, 45.0, 67.5, 90.0, 112.5, 135.0, 157.5, 180.0, 202.5, 225.0, 247.5, 270.0, 292.5, 315.0, 337.5]
directions=[0, 45.0, 90.0, 135.0, 180.0,225.0, 270.0, 315.0]
for i in range(len(directions)):
    new_dir=np.abs(directions[i]-360)
    mock_dir.append(new_dir)
    
directions=mock_dir
#r_cloud=[30.612244897959183,18.367346938775512,4.081632653061225,12.244897959183673,8.16326530612245,4.081632653061225,2.0408163265306123,0.0,6.122448979591836,6.122448979591836,6.122448979591836,2.0408163265306123,2.0408163265306123,16.3265306122449,38.775510204081634,100.0,73.46938775510205,75.51020408163265]
#r_track=[21.951219512195124,17.073170731707318,7.317073170731707,11.38211382113821,4.0650406504065035,8.94308943089431,6.504065040650407,9.75609756097561,15.447154471544716,22.76422764227642,28.455284552845526,40.65040650406504,47.96747967479675,82.92682926829268,90.2439024390244,100.0,71.54471544715447,47.15447154471545]

r_track=[13.157894736842104, 21.052631578947366, 13.157894736842104, 7.894736842105263, 10.526315789473683, 15.789473684210526, 13.157894736842104, 5.263157894736842, 7.894736842105263, 31.57894736842105, 63.1578947368421, 100.0, 92.10526315789474, 63.1578947368421, 81.57894736842105, 63.1578947368421, 18.421052631578945]


tracks=[ 12,  8,  5,  3,  4,  6,  5,  2,  3, 12, 24, 38, 35, 24, 31, 24]
clouds=[ 9,  8,  4,  3,  5,  4,  9, 17, 28, 52, 45, 57, 61, 49, 22, 24]
zeros=[123, 116,  87,  90,  89,  80, 126, 151, 222, 311, 367, 318, 283, 243, 212, 161]

tracks=[ 27, 12,  7, 10,10, 51, 63, 56]
clouds=[  22,  12,   9, 16,  61, 107, 113,  57]
zeros=[260, 189, 169, 227, 464, 701, 571, 398]




abs_nr=[]
cloud_pr=[]
track_pr=[]

tracks_normalized=[]
clouds_normalized=[]


abs_nr=[]
cloud_pr=[]
track_pr=[]

for i in range(len(tracks)):
    tracks_normalized.append(tracks[i]/np.sum(tracks))
    clouds_normalized.append(clouds[i]/np.sum(clouds))
    abs_nr.append(tracks[i]+clouds[i]+zeros[i])
    if(sys.argv[2]=='abs'):
        cloud_pr.append(clouds[i])
    else:
        cloud_pr.append((tracks[i]+clouds[i])/(tracks[i]+clouds[i]+zeros[i]))
    if(sys.argv[2]=='abs'):
        track_pr.append(tracks[i])
    else:
        track_pr.append((tracks[i])/(tracks[i]+clouds[i]))
        
r_common=[]
r_track_over=[]
r_cloud_over=[]



for i in range(len(clouds_normalized)):
    cloud=clouds_normalized[i]
    track=tracks_normalized[i]
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
    

if(sys.argv[1]=='all'):
    choice=abs_nr
    color='rgba(0,128,0,1.0)'
    
if(sys.argv[1]=='cloud'):
    choice=cloud_pr
    color='rgba(0,0,255,1.0)'
    
if(sys.argv[1]=='track'):
    choice=track_pr
    color='rgba(255,0,0,1.0)'

if(sys.argv[1]!='together'):
    
    fig.add_trace(go.Barpolar(

        theta = directions,
        r=choice,
        marker_color=color
    ))
else:
    
    for i in range(len(clouds_normalized)):
        cloud=[]
        track=[]
        if(clouds_normalized[i]>tracks_normalized[i]):
            for j in range(len(clouds_normalized)):
                if(j==i):
                    track.append(tracks_normalized[i])
                    cloud.append(clouds_normalized[i]-tracks_normalized[i])
                else:
                    cloud.append(0)
                    track.append(0)
            fig.add_trace(go.Barpolar(

                theta = directions,
                r=track,
                name='Tracks and clouds overlapping',
                marker_color='rgba(255,0,0,1.0)'
            ))
            fig.add_trace(go.Barpolar(

                theta = directions,
                r=cloud,
                name='Tracks and clouds overlapping',
                marker_color='rgba(0,0,255,1.0)'
            ))
        if(tracks_normalized[i]>clouds_normalized[i]):
            for j in range(len(clouds_normalized)):
                if(j==i):
                    track.append(tracks_normalized[i]-clouds_normalized[i])
                    cloud.append(clouds_normalized[i])
                else:
                    cloud.append(0)
                    track.append(0)
            fig.add_trace(go.Barpolar(

                theta = directions,
                r=cloud,
                name='Tracks and clouds overlapping',
                marker_color='rgba(0,0,255,1.0)'
            ))
            fig.add_trace(go.Barpolar(

                theta = directions,
                r=track,
                name='Tracks and clouds overlapping',
                marker_color='rgba(255,0,0,1.0)'
            ))
            


    '''
    fig.add_trace(go.Barpolar(
   
    theta = directions,
    r=r_common,
    name='Tracks and clouds overlapping',
    marker_color='rgba(255,0,255,1.0)'
    ))
    
    fig.add_trace(go.Barpolar(
        theta = directions,
        r=r_cloud_over,
        name='Only clouds',
        marker_color='rgba(0,0,255,1.0)'
    ))
    fig.add_trace(go.Barpolar(
        theta = directions,
        r=r_track_over,
        name='Tracks',
        marker_color='rgba(255,0,0,1.0)'
    ))
    '''



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
fig.write_image("Norilsk_reanalysis.png")
