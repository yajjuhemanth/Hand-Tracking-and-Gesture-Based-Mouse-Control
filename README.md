# No-Mouse
This repository contains a Python script for hand tracking using the MediaPipe library and OpenCV. The script enables real-time tracking of hand gestures, particularly focusing on moving the mouse cursor and performing clicks using hand gestures.
# Hand Tracking with MediaPipe and OpenCV

This Python script utilizes the MediaPipe library and OpenCV to track hand gestures in real-time. It enables users to control the mouse cursor's movement and perform clicks using hand gestures.

## Prerequisites

- Python 3.x
- OpenCV
- Mediapipe
- NumPy
- PyAutoGUI

You can install the required libraries via pip:


pip install opencv-python mediapipe numpy pyautogui
**#Usage**
Clone this repository to your local machine.
Navigate to the directory containing the script.
Run the script using the following command:

python no-mouse.py
Position your hand in front of the camera, and the script will track its movements.
Move your index finger to control the mouse cursor.
Touch your thumb and index finger to perform a click.

**#Configuration**
You can adjust the following parameters in the script:

smoothing_factor: Controls the smoothness of mouse movement. Adjust for smoother or more responsive movement.
click_threshold: Distance threshold for thumb and index finger to be considered touching.
click_debounce_time: Debounce time in seconds to prevent multiple clicks for a single gesture.


Feel free to modify and expand upon this README as needed!
