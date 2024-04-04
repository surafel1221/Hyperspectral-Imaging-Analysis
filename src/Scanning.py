import os
import serial
import time
import logging
import numpy as np
import cv2
import subprocess
from time import sleep
import spectral.io.envi as envi
from spectral.io.envi import save_image



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def capture_image(frame_index, output_dir, libcamera_options={}):
    filename = f"image_{frame_index:04d}.jpg"
    output_path = os.path.join(output_dir, filename)
    capture_command = ["libcamera-vid", "-o", output_path, "--nopreview", "-t", "1000"]
    capture_command.extend([f"{key}{value}" for key, value in libcamera_options.items()])
    try:
        subprocess.run(capture_command, check=True)
        logger.info(f"Image saved to: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"An error occurred: {e}")
        return False

   #as the camera moves across the object we capture each frame and save it and 
def construct_data_cube(images_directory, number_of_images):
    images = []
    for i in range(number_of_images):
        img_path = os.path.join(images_directory, f'image_{i:04d}.jpg')
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        if img is not None:
            images.append(img)
        else:
            logger.error(f"Failed to load image: {img_path}")
    data_cube = np.stack(images, axis=-1)  
    return data_cube
def save_cube(data_cube, outputfilename):
    metadata = {
        'description': 'Hyperspectral data cube',
        'bands': data_cube.shape[2],
        'lines': data_cube.shape[0],
        'samples': data_cube.shape[1],
        'interleave': 'bil',
        'datatype': 'uint16' # Change as per your data type
    }
    save_image(outputfilename, data_cube, metadata=metadata, force=True)
    
def start_scan(camera_fps, rail_speed, rail_length):
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)
    
    

    distance=rail_speed / camera_fps
    number_of_frames = int(rail_length / distance)
    
    ser = serial.Serial('/dev/ttyACM0', 115200)
    time.sleep(2)
    
    ser.write(b'$H\n')
    time.sleep(10)
    
    ser.write(b'G92 X0 Y0 Z0\n')

    
    print(f"Distance between captures: {distance:.2f} mm")
    print(f"Number of frames to capture: {number_of_frames}")
    
    #based on what the user inputed 
    ser.write(f'G01 F{rail_speed}\n'.encode())

    
    libcamera_options = {'--width': 1280, '--height': 720, '--framerate': str(camera_fps)}
    
    
    
   
    for i in range(number_of_frames):
        if not capture_image(i, output_dir, libcamera_options):
            logger.error("Failed to capture image, stopping.")
            ser.write(b'G01 F0\n')
            break
        sleep(1/camera_fps)  
        
    ser.write(b'G01 F0\n')
    ser.close()
    
    data_cube = construct_data_cube(output_dir, number_of_frames)
    logger.info(f"Data cube shape: {data_cube.shape}")
    
    output_filename = "output_data.lan"  
    save_cube(data_cube, output_filename)


if __name__ == "__main__":
    start_scan()