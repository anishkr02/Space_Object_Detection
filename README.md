# Detection using YOLO

A real-time trash detection system that classifies different types of waste materials using YOLO object detection.

![Detection Results](Screenshot_2025-10-30_183112.png)

## Project Overview

This project implements a trash detection system capable of identifying and classifying various types of waste materials in real-time. The system can process both video files and live webcam feeds to detect items like metal, plastic pouches, foil pouches, and other plastic materials.

## Features

- **Real-time Detection**: Process video streams and webcam feeds in real-time
- **Multiple Material Detection**: Identify various waste categories including:
  - Metal
  - Plastic pouches
  - Foil pouches
  - General plastic items
- **Flexible Input Sources**: Support for both video files and live webcam
- **Fast Inference**: Optimized performance with YOLO model
- **Visual Feedback**: Real-time bounding boxes and confidence scores

## Installation

### Prerequisites

- Python 3.7+
- OpenCV
- Ultralytics YOLO

### Dependencies

```bash
pip install ultralytics opencv-python
```

## Project Structure

```
Space_Object-Detection/
├── detect_best.pt          # Trained YOLO model weights
├── test.py                  # Main detection script
├── Screenshot_2025-10-30_183112.png  # Example detection output
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Usage

1. **Run the detection script**:
```bash
python test.py
```

2. **Choose input mode**:
   - Enter `v` for video file detection
   - Enter `w` for webcam detection

3. **For video mode**: Place your video file (`Video2.mp4`) in the project directory

4. **Controls**:
   - Press `q` to quit the application

## Code Overview

### Main Functions

- `detect_from_video(video_path)`: Processes video files for trash detection
- `detect_from_webcam()`: Uses webcam for real-time detection

### Key Components

```python
# Load trained model
model = YOLO("detect_best.pt")

# Run inference
results = model(frame)

# Visualize results
annotated_frame = results[0].plot()
```

## How to Use

1. Ensure your trained model weights (`detect_best.pt`) are in the project directory
2. Run the script and select your preferred input method
3. The system will display real-time detection with bounding boxes and labels (as shown in the screenshot above)
4. Press 'q' to exit the application

## Notes

- The model is trained to detect specific trash categories with high accuracy
- Performance may vary based on hardware capabilities
- For best results, ensure good lighting conditions when using webcam
- The screenshot demonstrates successful detection of multiple waste items with confidence scores

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available under the [MIT License](LICENSE).

---
