# Image Optimizer

This is a simple image optimizer built using Python. The tool processes images in a specified input directory, optimizes them by converting them to JPEG format with reduced quality, and saves the optimized images to an output directory.

## Features

- Converts images to JPEG format.
- Reduces image quality to save storage space.
- Supports multiple image formats, including `.png`, `.jpg`, `.jpeg`, `.bmp`, and `.gif`.
- Processes all images in a directory automatically.

## How It Works

1. The script scans the `Input` directory for supported image files.
2. Each image is optimized by converting it to JPEG format and reducing its quality.
3. The optimized images are saved in the `Output` directory with `_optimized` added to their filenames.

## Requirements

- Python 3.8 or newer
- Required Python libraries:
  - `Pillow`
  - `tqdm`

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/image-optimizer.git
   cd image-optimizer
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Place the images you want to optimize in the `Input` directory.
2. Run the script:
   ```sh
   python main.py
   ```
3. The optimized images will be saved in the `Output` directory.

## Directory Structure

```
imageOptimizer/
├── Input/          # Directory for input images
├── Output/         # Directory for optimized images
├── main.py         # Main script
├── pyproject.toml  # Project configuration
├── README.md       # Project documentation
└── uv.lock         # Dependency lock file
```

## Example

If you have an image named `example.png` in the `Input` directory, the script will process it and save the optimized version as `example_optimized.jpg` in the `Output` directory.

## License

This project is open-source and available under the MIT License.

```

```
