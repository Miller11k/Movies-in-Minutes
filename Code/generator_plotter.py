import cv2
import numpy as np
import re
import sys
import matplotlib.pyplot as plt


# --------------------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------- Generating File -------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------------------- #

movie_name = input("\nEnter the name of the movie (for Dominant_Color.txt file): ") # Get User Input for Name of The Movie

movie_name = re.sub(r'[^\w\s]', '', movie_name) # Use RegEx to get rid of any punctuation in movie_name
movie_name = re.sub(' ', '_', movie_name).lower() # Use RegEx to replace spaces with underscores in movie_name

file_name = "../Dominant_Color_Files/" + movie_name + "_Dominant_Colors.txt" # Create a new file Name which is the movie_name + "_Dominant_Colors.txt"

print(f"* File created in Dominant_Color_Files will be named: \"{movie_name}_Dominant_Colors.txt\"")

movie_file = input("\n\nEnter movie file name (before \".mp4\"): ") # Get name of the movie file
print(f"* Movie File Name: \"{movie_file}.mp4\"\n")

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

print(f"Generating \"{movie_name}_Dominant_Colors.txt\":")

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

print("\n\nDominant Color Text File Generation Completed.\n")

file.close() # Close file



# --------------------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------- Plotting Image --------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------------------- #

print(" ----------------------------------------------------------------------------------------- ")

output_filename = movie_name + ".png"

print(f"File Path to Dominant Color Text File: {file_name}")

# Read the RGB codes from the text file
with open(file_name, "r") as file:
    rgb_codes = file.read().splitlines()

fig, ax = plt.subplots() # Create a figure and axis

total_codes = len(rgb_codes) # Get the total number of RGB codes

bar_width = 1 # Set the width of the bars

bar_height = 75000 # Set the height of the bars

print(f"\nGenerating \"{output_filename}\":")
# Iterate over the RGB codes and plot each as a bar
for i, rgb_code in enumerate(rgb_codes):
    # Convert the RGB code to a tuple of floats (between 0 and 1)
    r, g, b = map(int, rgb_code.split(","))
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Plot the bar
    ax.bar(i, bar_height, width=bar_width, color=(r, g, b))

    # Calculate the percentage completion
    percentage_done = (i + 1) / total_codes * 100

    # Print updating percentage completion
    sys.stdout.write(f"\r{percentage_done:.2f}% Complete")
    sys.stdout.flush()
        

ax.axis('off') # Remove the axes

ax.set_aspect("equal") # Set the aspect ratio to be equal

ax.set_xlim(-bar_width, total_codes) # Adjust x-axis limits to eliminate whitespace

ax.set_ylim(0, bar_height) # Adjust y-axis limits to crop the plot

plt.subplots_adjust(0, 0, 1, 1) # Adjust subplot parameters to eliminate whitespace

# Write the file to the output folder
output_location = "../Image_Output/" + output_filename
plt.savefig(output_location, dpi=300) # Save the plot to a file

# plt.show() # Display the plot

file.close() # Close file

print(f"\nLook for \"{output_filename}\" in the \"Image_Output\" folder.\n")
