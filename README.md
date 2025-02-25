# Image Processor with Background Removal

This is a Python application that allows users to load images, remove their backgrounds using AI-powered processing, and save the processed images with quality control options. The application uses a modern GUI built with `ttkbootstrap` for styling and is powered by the `rembg` library for background removal.

## Features
- **Background Removal**: Automatically removes the background from images using an AI model.
- **Support for Multiple Image Formats**: Works with PNG, JPEG, and JPG files.
- **Quality Control**: Adjusts compression quality for both JPEG and PNG formats.
- **Intuitive GUI**: Modern interface with clear button controls and image display.
- **Error Handling**: Provides user feedback through dialogs for loading/saving operations and quality validation.

## Requirements
- Python 3.8+
- Required Libraries:
  - `Pillow` (PIL)
  - `rembg`
  - `ttkbootstrap`
  - `OpenCV` (cv2)
  - `numpy`

## Installation Instructions
1. Create a virtual environment:
   ```bash
   python -m venv image_env
   ```
2. Activate the environment:
   - **Windows:**
     ```bash
     image_env\Scripts\activate
     ```
   - **Linux/MacOS:**
     ```bash
     source image_env/bin/activate
     ```
3. Install requirements:
   ```bash
   pip install Pillow rembg ttkbootstrap opencv-python numpy
   ```

## Usage
Start the application by running:
```bash
python main.py
```

### Use the Interface:
1. **Load Image**: Browse for an image file and load it into the application.
2. **Remove Background**: Process the loaded image to remove the background.
3. **Adjust Quality**: Use the slider to set the desired compression level (1-100 for JPEG, 0-9 for PNG).
4. **Save Image**: Save the processed image using the chosen quality and format.

## Key Components
### User Interface
The application features a clean and modern UI with the following elements:
- **Buttons**: "Load Image", "Remove Background", and "Save Image"
- **Quality Control Slider**: Adjusts compression quality (automatically maps to PNG compression levels 0-9 when saving as PNG)
- **Image Display**: Shows both loaded and processed images with automatic resizing
- **Attribution**: Developer name displayed at the bottom of the window

### Background Removal Logic
The core functionality uses the `rembg` library, which leverages the `REM_BG_U2NET` model for real-time background removal. It operates as follows:
1. Load the original image using `Pillow`.
2. Remove the background using `rembg.remove()`.
3. Update the displayed image with the processed result.

### Quality Handling
The application automatically adjusts compression parameters based on the file format:
- **JPEG**: Uses a standard quality parameter (1-100).
- **PNG**: Converts the quality slider value (1-100) to a compression level (0-9) using the formula:
  ```python
  compression_level = int(quality * 0.09)
  ```
  with clamping between 0 and 9.

### Error Handling
The application includes the following error checks:
- **File Loading**: Ensures an image is loaded before processing.
- **File Saving**: Validates that an image has been processed before saving.
- **Unsupported Formats**: Shows a warning if an invalid file type is selected.
- **JPEG Processing**: Handles potential exceptions that may arise during JPEG background compositing.

## Future Enhancements
- Add support for batch processing multiple files.
- Include additional image processing features (e.g., color adjustment, resizing).
- Implement a progress indicator during long operations.
- Add support for more image formats (e.g., TIFF, BMP).
- Include undo/redo functionality for processed images.

## Developer Information
- **Author**: Eng Ihab Shahtout
- **License**: MIT License
- **Version**: 1.0.0

## Dependencies Table
| Library      | Purpose                                |
|-------------|----------------------------------------|
| Pillow      | Image processing and display          |
| rembg       | Background removal using AI           |
| ttkbootstrap| Modern UI styling                     |
| OpenCV      | Image handling                        |
| numpy       | Numerical operations                  |

## Contribution Guidelines
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -am 'Add your changes'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request for review.

