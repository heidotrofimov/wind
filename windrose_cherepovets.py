import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import sys
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

tracks= [37, 28, 21,  7,  6,  1,  3,  0,  2,  4,  7, 16, 15, 22, 40, 46]
clouds= [36,  29,  15,   8,   6,   5,   8,  15,  29,  65,  67, 110, 107,  86, 55,  58]
zeros= [181, 121,  72,  51, 46,  61,  92, 119, 238, 366, 560, 600, 600, 449, 342, 296]



abs_nr=[]
cloud_pr=[]
track_pr=[]

for i in range(len(tracks)):
    abs_nr.append(tracks[i]+clouds[i]+zeros[i])
    cloud_pr.append((tracks[i]+clouds[i])/(tracks[i]+clouds[i]+zeros[i]))
    track_pr.append((tracks[i])/(tracks[i]+clouds[i]))

if(sys.argv[1]=='all'):
    choice=abs_nr
    color='rgba(0,128,0,1.0)'
    
if(sys.argv[1]=='cloud'):
    choice=cloud_pr
    color='rgba(0,0,255,1.0)'
    
if(sys.argv[1]=='track'):
    choice=track_pr
    color='rgba(255,0,0,1.0)'


fig.add_trace(go.Barpolar(
   
    theta = directions,
    r=choice,
    marker_color=color
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
fig.write_image("Cherepovets_reanalysis.png")
