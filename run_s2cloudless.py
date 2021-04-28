from s2cloudless import S2PixelCloudDetector
import numpy as np
import rasterio
from rasterio.warp import reproject, Resampling
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
import sys
import os
import argparse
        
def plot_cloud_mask(mask, input_folder,figsize=(15, 15), fig=None):
    new_mask = [[255 if b==1 else b for b in i] for i in mask]
    im_result = Image.fromarray(np.uint8(new_mask))
    im_result=im_result.resize((10980,10980),Image.NEAREST)
    im_result.save(input_folder+"/s2cloudless_prediction.png")

#Resampling to achieve 10 m resolution:

for folder in os.listdir("/home/heido/scl_data/"):
    print(folder)
    
    if("S2A_MSIL1C" in folder):
        identifier=folder.split("_")[5]+"_"+folder.split("_")[2]+"_"
        for folder2 in os.listdir("/home/heido/scl_data/"+folder+"/GRANULE/"):
            input_folder="/home/heido/scl_data/"+folder+"/GRANULE/"+folder2+"/IMG_DATA"

            with rasterio.open(os.path.join(input_folder,identifier+"B01.jp2")) as dataset:
                B01 = dataset.read(out_shape=(dataset.count,int(dataset.height * 6),int(dataset.width * 6)),resampling=Resampling.bilinear)                  
		

            with rasterio.open(os.path.join(input_folder,identifier+"B02.jp2")) as dataset:
                B02 = dataset.read(out_shape=(dataset.count,int(dataset.height * 1),int(dataset.width * 1)),resampling=Resampling.bilinear)


            with rasterio.open(os.path.join(input_folder,identifier+"B04.jp2")) as dataset:
                B04 = dataset.read(out_shape=(dataset.count,int(dataset.height * 1),int(dataset.width * 1)),resampling=Resampling.bilinear)


            with rasterio.open(os.path.join(input_folder,identifier+"B05.jp2")) as dataset:
                B05 = dataset.read(out_shape=(dataset.count,int(dataset.height * 2),int(dataset.width * 2)),resampling=Resampling.bilinear)


            with rasterio.open(os.path.join(input_folder,identifier+"B08.jp2")) as dataset:
                B08 = dataset.read(out_shape=(dataset.count,int(dataset.height * 1),int(dataset.width * 1)),resampling=Resampling.bilinear)


            with rasterio.open(os.path.join(input_folder,identifier+"B8A.jp2")) as dataset:
                B8A = dataset.read(out_shape=(dataset.count,int(dataset.height * 2),int(dataset.width * 2)),resampling=Resampling.bilinear)


            with rasterio.open(os.path.join(input_folder,identifier+"B09.jp2")) as dataset:
                B09 = dataset.read(out_shape=(dataset.count,int(dataset.height * 6),int(dataset.width * 6)),resampling=Resampling.bilinear)


            with rasterio.open(os.path.join(input_folder,identifier+"B10.jp2")) as dataset:
                B10 = dataset.read(out_shape=(dataset.count,int(dataset.height * 6),int(dataset.width * 6)),resampling=Resampling.bilinear)


            with rasterio.open(os.path.join(input_folder,identifier+"B11.jp2")) as dataset:
                B11 = dataset.read(out_shape=(dataset.count,int(dataset.height * 2),int(dataset.width * 2)),resampling=Resampling.bilinear)


            with rasterio.open(os.path.join(input_folder,identifier+"B12.jp2")) as dataset:
                B12 = dataset.read(out_shape=(dataset.count,int(dataset.height * 2),int(dataset.width * 2)),resampling=Resampling.bilinear)


            bands = np.array([np.dstack((B01[0]/10000.0,B02[0]/10000.0,B04[0]/10000.0,B05[0]/10000.0,B08[0]/10000.0,B8A[0]/10000.0,B09[0]/10000.0,B10[0]/10000.0,B11[0]/10000.0,B12[0]/10000.0))])


            cloud_detector = S2PixelCloudDetector(threshold=0.4, average_over=22, dilation_size=11)  
            cloud_probs = cloud_detector.get_cloud_probability_maps(bands)
            mask = cloud_detector.get_cloud_masks(bands).astype(rasterio.uint8)

            plot_cloud_mask(mask[0],folder)

