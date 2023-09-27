import numpy as np
from PIL import Image

# Define map dimensions
width = 512
height = 512

# Generate a 2D elevation map using a function
def generate_elevation_map(width, height):
    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    X, Y = np.meshgrid(x, y)
    elevation = np.sin(np.sqrt(X**2 + Y**2) * 10) * 0.5 + 0.5
    return elevation

elevation_map = generate_elevation_map(width, height)

# Normalize the elevation map to 0-255 range
elevation_map_normalized = (elevation_map * 255).astype(np.uint8)

# Create a grayscale image
image = Image.fromarray(elevation_map_normalized, mode='L')

# Save the image as a PNG file
image.save('hfield.png')

print("Elevation map saved as 'hfield.png'")


