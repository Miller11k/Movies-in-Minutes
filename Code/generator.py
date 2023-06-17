import cv2
import numpy as np
import re
import sys




movie_name = input("\nEnter the name of the movie (for Dominant_Color.txt file): ") # Get User Input for Name of The Movie

movie_name = re.sub(r'[^\w\s]', '', movie_name) # Use RegEx to get rid of any punctuation in movie_name

movie_name = re.sub(' ', '_', movie_name).lower() # Use RegEx to replace spaces with underscores in movie_name

print(f"File created in Dominant_Color_Files will be named: \"{movie_name}_Dominant_Colors.txt\"")

file_name = "../Dominant_Color_Files/" + movie_name + "_Dominant_Colors.txt" # Create a new file Name which is the movie_name + "_Dominant_Colors.txt"

movie_file = input("\n\nEnter movie file name (Automatically adds \".mp4\"): ") # Get name of the movie file
print(f"Movie File Name: {movie_file}.mp4\n")

video_path = ("../Movie/" + movie_file + ".mp4") # Path to the video file in the Movie folder


dominant_colors = [] # Initialize an empty array to store the dominant colors

cap = cv2.VideoCapture(video_path) # Open the video file

# Check if the video file was successfully opened
if not cap.isOpened():
    print("Error opening video file")
    exit()

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # Get the total number of frames in the video

print(f"Total frames in video: {total_frames}\n") # Display the total number of frames


current_frame = 0 # Initialize Current Frame to 0
percentage_done = 0.0 # Initialize Percentage to 0%

while True: # Loop through each frame of the video
    
    ret, frame = cap.read() # Read the current frame
    
    current_frame += 1 # Increment the current frame count
    percentage_done = (current_frame / total_frames) * 100

    # Break the loop if the video has ended
    if not ret:
        break

    # # FOR TROUBLESHOOTING PURPOSES
    # # Display every 10000th frame as an image
    # if current_frame % 10000 == 0:
    #     cv2.imshow("Frame", frame)
    #     cv2.waitKey(0)



    # Print updating percentage completion
    sys.stdout.write(f"\r{percentage_done:.2f}% Complete")
    sys.stdout.flush()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert the frame from BGR to RGB color space

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
    ) # Run K-means to find dominant color

    dominant_color = centers[0].astype(int) # Get the dominant color (center) of the cluster
    
    dominant_colors.append(dominant_color) # Add the dominant color to the array

cap.release() # Release the video file



# Create a new file called Dominant-Colors.txt and write the dominant colors for each frame in a new line
with open(file_name, "w") as file:
    for color in dominant_colors:
        file.write(str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + "\n")

print("\nDominant Color Text File Generation Completed.\n")

file.close() # Close file