import subprocess
import sys

def add_watermark(video_input, watermark_image, video_output, position="topright"):
    # Define the positions for the watermark
    positions = {
        "topleft": "(main_w-overlay_w)/12:(main_h-overlay_h)/12",
        "topright": "main_w-overlay_w-(main_w-overlay_w)/12:(main_h-overlay_h)/12",
        "bottomleft": "(main_w-overlay_w)/12:main_h-overlay_h-(main_h-overlay_h)/12",
        "bottomright": "main_w-overlay_w-(main_w-overlay_w)/12:main_h-overlay_h-(main_h-overlay_h)/12",
        "center": "(main_w-overlay_w)/2:(main_h-overlay_h)/2"
    }
    
    if position not in positions:
        print(f"Invalid position: {position}")
        sys.exit(1)
    
    position_filter = positions[position]
    
    command = [
        'ffmpeg', '-i', video_input, '-i', watermark_image,
        '-filter_complex', f'"overlay={position_filter}"',
        '-codec:a', 'copy', video_output
    ]
    
    subprocess.run(" ".join(command), shell=True, check=True)
    
    print(f"Watermark added to video: {video_output}")

# Example usage:
video_input_path = "test.mp4"
watermark_image_path = "test2.png"
video_output_path = "test3.mp4"
watermark_position = "topright"  # Change this to topleft, bottomleft, bottomright, center as needed

add_watermark(video_input_path, watermark_image_path, video_output_path, watermark_position)
