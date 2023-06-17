import matplotlib.pyplot as plt
import re
import sys

file_name = input("\nEnter the name of the Dominant Color File (Without the \"_Dominant_Colors.txt\"): ")
movie_name = input("Enter the name of the movie: ")

movie_name = re.sub(r'[^\w\s]', '', movie_name) # Use RegEx to get rid of any punctuation in movie_name

movie_name = re.sub(' ', '_', movie_name).lower() # Use RegEx to replace spaces with underscores in movie_name

output_filename = movie_name + ".png"

print(f"\nLook for \"{output_filename}\" in the Output folder")

file_path = "../Dominant_Color_Files/" + file_name + "_Dominant_Colors.txt" # Create path to the text file
print(file_path)

# Read the RGB codes from the text file
with open(file_path, "r") as file:
    rgb_codes = file.read().splitlines()

fig, ax = plt.subplots() # Create a figure and axis

total_codes = len(rgb_codes) # Get the total number of RGB codes

bar_width = 1 # Set the width of the bars

bar_height = 75000 # Set the height of the bars

print("\n")

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

plt.show() # Display the plot

file.close() # Close file
print("\nCheck \"Image_Output\" folder")
