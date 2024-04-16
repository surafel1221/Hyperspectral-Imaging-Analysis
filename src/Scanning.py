import os
import subprocess
import time
import logging
import numpy as np
import cv2
from spectral.io.envi import save_image

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
"""
def capture_image(frame_index, output_dir, libcamera_options={}, preview_timeout=5000):
    filename = f"image_{frame_index:04d}.png"
    output_path = os.path.join(output_dir, filename)

    capture_command = [
        "libcamera-still", 
        "-o", output_path,
        "-t", "1000", 
        "--preview", 
        f"--preview-timeout={preview_timeout}"
    ]
    capture_command.append("--codec=png")
    capture_command.extend([f"{key}={value}" for key, value in libcamera_options.items()])

    try:
        subprocess.run(capture_command, check=True)
        logger.info(f"Image saved to: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"An error occurred: {e}")
        return False
"""


def construct_data_cube(images_directory, number_of_images):
    images = []
    for i in range(number_of_images):
        img_path = os.path.join(images_directory, f'image_{i:04d}.png')
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
        'datatype': 'uint16'  
    }
    save_image(outputfilename, data_cube, metadata=metadata, force=True)

def start_scan(camera_fps, rail_speed, rail_length):
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)

    frame_distance = rail_speed / camera_fps  # mm per frame
    number_of_frames = int(rail_length / frame_distance)

    libcamera_options = {'--width': 4600, '--height': 2590, '--framerate': str(camera_fps)}

    logger.info(f"Distance between captures: {frame_distance:.2f} mm")
    logger.info(f"Number of frames to capture: {number_of_frames}")

    for i in range(number_of_frames):
        if not capture_image(i, output_dir, libcamera_options):
            logger.error("Failed to capture image, stopping.")
            break
        time.sleep(1 / camera_fps)

    data_cube = construct_data_cube(output_dir, number_of_frames)
    logger.info(f"Data cube shape: {data_cube.shape}")

    output_filename = "output_data.lan"
    save_cube(data_cube, output_filename)

if __name__ == "__main__":
    start_scan()  