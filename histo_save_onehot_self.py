import argparse

import numpy as np
import PIL
import psutil
from skimage import io
from tqdm import tqdm


def print_memory_usage(msg, verbose):
    if verbose:
        process = psutil.Process()
        print(f"{msg} - Memory Usage: {process.memory_info().rss / 1024**2:.2f} MB")

def load_image(image_path, verbose):
    PIL.Image.MAX_IMAGE_PIXELS = 1000000000000000
    print_memory_usage("After setting decompression limit", verbose)
    image = io.imread(image_path)
    print_memory_usage("After loading image", verbose)
    return image

def find_unique_values(image, verbose):
    unique_values = np.unique(image)
    print_memory_usage("After finding unique values", verbose)
    return unique_values

def process_and_save(image_path, unique_values, output_path, verbose):
    for value in tqdm(unique_values):
        image = load_image(image_path, verbose)
        print_memory_usage(f"Processing value {value}, after loading image", verbose)

        image[image != value] = 0
        image[image == value] = 255
        processed_image = image.astype(np.uint8)
        print_memory_usage(f"Processing value {value}, after processing image", verbose)

        save_path = f'{output_path}/processed_image_{value}.png'
        io.imsave(save_path, processed_image)
        if verbose:
            print(f'Saving image to {save_path}')
        print_memory_usage(f"Processing value {value}, after saving image", verbose)

        del image
        del processed_image
        print_memory_usage(f"Processing value {value}, after cleanup", verbose)

def main():
    parser = argparse.ArgumentParser(description="Process and save unique values of an image.")
    parser.add_argument("input_path", help="Path to the input image")
    parser.add_argument("output_path", help="Path to save processed images")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    args = parser.parse_args()

    image = load_image(args.input_path, args.verbose)
    unique_values = find_unique_values(image, args.verbose)
    del image

    process_and_save(args.input_path, unique_values, args.output_path, args.verbose)

if __name__ == "__main__":
    main()
