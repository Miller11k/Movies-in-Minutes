import cv2
import numpy as np

# Path to the video file
video_path = "/Users/miller/Python Movie Frame Project/James Bond Quantum of Solace.mp4"

# Initialize an empty array to store the dominant colors
dominant_colors = []

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was successfully opened
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Get the total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Display the total number of frames
print(f"Total frames: {total_frames}")

# Calculate the threshold to print progress
progress_threshold = total_frames / 10000  # Change by 0.01%

# Loop through each frame of the video
current_frame = 0
percentage_done = 0.0

while True:
    

    # Calculate the percentage completion
    
    
    
    # Read the current frame
    ret, frame = cap.read()
    
    # Increment the current frame count
    current_frame += 1
    percentage_done = (current_frame / total_frames) * 100
    print(f"Progress: {percentage_done:.2f}% (Frame: {current_frame}/{total_frames})")

    # Break the loop if the video has ended
    if not ret:
        break

    

    # # Check if the progress has changed by the threshold
    # if new_percentage - percentage_done >= progress_threshold:
    #     # Update the percentage_done variable
    #     percentage_done = new_percentage
        
    #     # Display the percentage completion
    #     print(f"Progress: {percentage_done:.2f}% (Frame: {current_frame}/{total_frames})")

    # Resize the frame for faster processing (optional)
    # frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    # Convert the frame from BGR to RGB color space
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Calculate the dominant color using K-means clustering
    pixels = frame_rgb.reshape(-1, 3)
    num_clusters = 1  # Number of clusters for K-means
    _, labels, centers = cv2.kmeans(
        pixels.astype(np.float32),
        num_clusters,
        None,
        criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
        attempts=10,
        flags=cv2.KMEANS_RANDOM_CENTERS,
    )

    # Get the dominant color (center) of the cluster
    dominant_color = centers[0].astype(int)

    # Add the dominant color to the array
    dominant_colors.append(dominant_color)

# Release the video file
cap.release()

# Create a new file called Dominant-Colors.txt and write the dominant colors for each frame in a new line
with open("Dominant-Colors.txt", "w") as file:
    for color in dominant_colors:
        file.write(str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + "\n")

# Print the dominant colors
for color in dominant_colors:
    print(color)