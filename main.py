import os
import pandas as pd
import numpy as np
from PIL import Image
import cv2

# Define the data directory
data_dir = "data/"
output_dir = "out/"

# Function to process images
def process_image(image_path):
    # Load the image
    image = Image.open(image_path)
    
    # Perform image processing operations
    # Example: Convert to grayscale
    grayscale_image = image.convert("L")
    
    # Save the processed image
    save_path = os.path.join(output_dir, os.path.basename(image_path))
    grayscale_image.save(save_path)

# Function to process signals
def process_signal(signal_path):
    # Load the signal data
    signal_data = pd.read_csv(signal_path)
    
    # Perform signal processing operations
    # Example: Apply a filter
    filtered_signal = apply_filter(signal_data["signal"].values)
    
    # Save the processed signal
    save_path = os.path.join(output_dir, os.path.basename(signal_path))
    signal_data["filtered_signal"] = filtered_signal
    signal_data.to_csv(save_path, index=False)

# Helper function to apply a filter to a signal
def apply_filter(signal):
    # Implement your filter logic here
    # Example: Simple moving average filter
    window_size = 5
    filtered_signal = np.convolve(signal, np.ones(window_size) / window_size, mode="same")
    return filtered_signal

def main():
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Process images
    image_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith((".jpg", ".png"))]
    for image_file in image_files:
        process_image(image_file)
        print(f"Processed image: {image_file}")

    # Process signals
    signal_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".csv")]
    for signal_file in signal_files:
        process_signal(signal_file)
        print(f"Processed signal: {signal_file}")

    print("Processing complete.")

if __name__ == "__main__":
    main()