import cv2
import mediapipe as mp
import numpy as np
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Set up hand tracking
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Screen dimensions
screen_width, screen_height = pyautogui.size()

# Variables for smoothing mouse movement
smooth_x, smooth_y = 0, 0
smoothing_factor = 0.5  # Adjust for smoother or more responsive movement

# Variables for click function
click_threshold = 50  # Distance threshold for thumb and index finger to be considered touching
click_debounce_time = 0.3  # Debounce time in seconds
last_click_time = 0

# Main loop
cap = cv2.VideoCapture(0)
prev_click_state = False
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the positions of thumb and index fingers
            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]
            thumb_x, thumb_y = int(thumb_tip.x * screen_width), int(thumb_tip.y * screen_height)
            index_x, index_y = int(index_tip.x * screen_width), int(index_tip.y * screen_height)

            # Smooth the mouse movement
            smooth_x = smoothing_factor * smooth_x + (1 - smoothing_factor) * index_x
            smooth_y = smoothing_factor * smooth_y + (1 - smoothing_factor) * index_y

            # Move mouse pointer smoothly
            pyautogui.moveTo(int(smooth_x), int(smooth_y))

            # Check for click gesture (thumb and index fingers touching)
            distance = np.sqrt((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2)
            if distance < click_threshold:
                current_time = cv2.getTickCount() / cv2.getTickFrequency()
                if current_time - last_click_time > click_debounce_time:
                    pyautogui.click()
                    last_click_time = current_time

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
