import matplotlib.pyplot as plt

# Path to the text file
file_path = "Dominant-Colors.txt"

# Read the RGB codes from the text file
with open(file_path, "r") as file:
    rgb_codes = file.read().splitlines()

# Create a figure and axis
fig, ax = plt.subplots()

# Get the total number of RGB codes
total_codes = len(rgb_codes)

# Calculate the threshold to print progress
progress_threshold = total_codes / 100

# Set the width of the bars
bar_width = 1
# Set the height of the bars
bar_height = 75000

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

    # Check if the progress has changed by the threshold
    while percentage_done <= 99.50:
        if percentage_done % progress_threshold <= 1.0:
            # Display the percentage completion
            print(f"Progress: {(percentage_done*100):.2f}%")
        
    if percentage_done > 99.50:
        # Display the percentage completion
        print(f"Progress: Complete, please wait for image to be generated")

# Remove the axes
ax.axis('off')

# Set the aspect ratio to be equal
ax.set_aspect("equal")

# Adjust x-axis limits to eliminate whitespace
ax.set_xlim(-bar_width, total_codes)

# Adjust y-axis limits to crop the plot
ax.set_ylim(0, bar_height)

# Adjust subplot parameters to eliminate whitespace
plt.subplots_adjust(0, 0, 1, 1)

# output_filename = "combined_bars.png"
# plt.savefig(output_filename, dpi=300)

# Display the plot
plt.show()
