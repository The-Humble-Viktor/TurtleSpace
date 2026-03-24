"""Helper to save the current turtle canvas as a PNG file."""
import os
from PIL import Image


def save(screen, filename):
    """Save the turtle screen to a PNG file in the output/ directory."""
    os.makedirs("output", exist_ok=True)
    eps_path = f"output/{filename}.eps"
    png_path = f"output/{filename}.png"
    canvas = screen.getcanvas()
    canvas.postscript(file=eps_path)
    img = Image.open(eps_path)
    img.save(png_path)
    os.remove(eps_path)
    print(f"Saved to {png_path}")
