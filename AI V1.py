import cv2
import os
import numpy as np

# Folder containing images
image_folder = r"C:\Users\cyber\Desktop\AI Project\images"
video_name = "animated_caracter_video.avi"

# Set FPS (Frames per second)
fps = 5  # Adjust FPS for video speed

# Duration for each image in seconds
image_duration = 5  # Duration each image will stay on screen (in seconds)

# Get images from the folder
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
images.sort()  # Sort images in order

# Check if any images are found
if not images:
    print("Error: No images found in the folder!")
    exit()

print(f"Found images: {images}")  # Debugging line

# Your story (modify this part, make sure you have enough story parts)
story_texts = [
    "Nandimitra was a chief commander of the ten great giants. He was the nephew of Mitta, "
    "a general in the army of King Elara. He was a warrior of the Rakshasa Angam. "
    "Although he was small and tied to a rock to prevent him from crawling everywhere, "
    "his great strength and majesty enabled him to drag even the heavy rock and move from place to place, "
    "which led to him being given the name Nandimitra.",
    
    "He fought valiantly in many battles, his power and skill unmatched. "
    "But despite his strength, his greatest challenge was always his own heart. "
    "He longed for freedom and a life without chains, a life where he could be more than just a warrior."
]

# Ensure there are enough story texts to cover all images (repeat if necessary)
if len(story_texts) < len(images):
    story_texts *= (len(images) // len(story_texts)) + 1  # Repeat story texts if not enough

print(f"Story texts length: {len(story_texts)}")  # Debugging line

# Read the first image to get dimensions
first_image = cv2.imread(os.path.join(image_folder, images[0]))
if first_image is None:
    print("Error: Unable to read the first image.")
    exit()

height, width, layers = first_image.shape

# Define video writer
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

# Check if video writer is opened
if not video.isOpened():
    print("Error: Failed to open video writer.")
    exit()

# Add text to each image and write it to the video
for i, image in enumerate(images):
    frame = cv2.imread(os.path.join(image_folder, image))
    if frame is None:
        print(f"Error: Unable to read image {image}.")
        continue

    # Get text for this image (ensure dynamic text is assigned correctly)
    text = story_texts[i]
    
    # Debugging line to check text matching
    print(f"Adding text for image {image}: {text}")
    
    # Add a slight zoom-in and pan effect on the image (simulate animation)
    zoom_factor = 1.1  # Change this value for more/less zoom effect
    pan_factor = 10  # Move the image a little to simulate panning
    rows, cols, _ = frame.shape
    M_zoom = cv2.getRotationMatrix2D((cols / 2, rows / 2), 0, zoom_factor)
    frame_zoomed = cv2.warpAffine(frame, M_zoom, (cols, rows))
    frame_zoomed = frame_zoomed[pan_factor:rows-pan_factor, pan_factor:cols-pan_factor]  # Apply panning effect
    
    # Add text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_color = (255, 255, 255)  # White color
    position = (50, height - 50)  # Bottom-left corner
    
    # Add text with background shadow
    cv2.putText(frame_zoomed, text, (position[0] + 2, position[1] + 2), font, font_scale, (0, 0, 0), font_thickness + 2, cv2.LINE_AA)
    cv2.putText(frame_zoomed, text, position, font, font_scale, text_color, font_thickness, cv2.LINE_AA)

    # Write the frame for the duration of the image (fps * image_duration)
    for _ in range(int(fps * image_duration)):  # Write each frame for the correct duration
        video.write(frame_zoomed)

# Release the video writer
video.release()

# Check if the video is saved correctly
if not os.path.exists(video_name):
    print(f"Error: Video file {video_name} was not created.")
else:
    print(f"Video with story saved as {video_name}")
