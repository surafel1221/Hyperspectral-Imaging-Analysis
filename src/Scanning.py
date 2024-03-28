import os
import logging
import numpy as np
import cv2
import subprocess
from time import sleep

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

def start_scan(camera_fps, rail_speed, rail_length):
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)
    
    

    distance=rail_speed / camera_fps
    number_of_frames = int(rail_length / distance)
    
    
    
    print(f"Distance between captures: {distance:.2f} mm")
    print(f"Number of frames to capture: {number_of_frames}")
    
    libcamera_options = {'--width': 1280, '--height': 720, '--framerate': str(camera_fps)}
    breaktime = 1 / camera_fps 
    
    
   
    for i in range(number_of_frames):
        if not capture_image(i, output_dir, libcamera_options):
            logger.error("Failed to capture image, stopping.")
            break
        sleep(breaktime)  
    
    data_cube = construct_data_cube(output_dir, number_of_frames)
    logger.info(f"Data cube shape: {data_cube.shape}")


if __name__ == "__main__":
    start_scan()