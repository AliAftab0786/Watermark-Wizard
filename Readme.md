# Watermark Wizard 🎥✨

**Watermark Wizard: Effortlessly Add Watermarks to Your Videos**

## 📝 Description

Watermark Wizard is a simple yet powerful Python script that allows you to easily add watermarks to your videos. Using FFmpeg, this tool provides a straightforward way to overlay images onto videos in various positions, giving you full control over your content's branding.

## ✨ Features

- 🎯 Add watermarks to videos with ease
- 🔄 Multiple positioning options (top-left, top-right, bottom-left, bottom-right, center)
- 🛠 Utilizes FFmpeg for high-quality video processing
- 🐍 Simple Python interface

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- FFmpeg (must be installed and accessible in your system's PATH)

### Installation

1. Clone this repository:
git clone https://github.com/yourusername/watermark-wizard.git
2. Navigate to the project directory:
cd watermark-wizard
## 💻 Usage

```python
from watermark_wizard import add_watermark

video_input_path = "path/to/your/video.mp4"
watermark_image_path = "path/to/your/watermark.png"
video_output_path = "path/to/output/video.mp4"
watermark_position = "topright"  # Options: topleft, topright, bottomleft, bottomright, center

add_watermark(video_input_path, watermark_image_path, video_output_path, watermark_position)
🎛 Customization
You can easily customize the watermark position by changing the watermark_position parameter:

"topleft": Top-left corner
"topright": Top-right corner
"bottomleft": Bottom-left corner
"bottomright": Bottom-right corner
"center": Center of the video

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgements

FFmpeg for the powerful video processing capabilities
Would you like me to explain or elaborate on any part of this README?