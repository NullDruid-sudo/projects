# Hand Finger Counter using OpenCV and MediaPipe

A simple real-time computer vision project that detects a hand from a webcam feed and counts the number of fingers being shown. The program uses **MediaPipe Hands** for landmark detection and **OpenCV** for video processing and visualization.

The system also detects whether the hand is **Left or Right** and adjusts thumb detection logic accordingly for more accurate finger counting.

---

## Features

- Real-time hand tracking using MediaPipe
- Finger counting based on hand landmarks
- Automatic **Left / Right hand detection**
- Accurate **thumb detection depending on hand orientation**
- Live **FPS counter**
- Visual hand landmark rendering

---

## Technologies Used

- Python
- OpenCV
- MediaPipe

---

## How It Works

MediaPipe detects **21 hand landmarks** for every detected hand. These landmarks represent joints and tips of the fingers.

Finger detection works by comparing landmark positions.

### Thumb Detection

The thumb moves sideways, so detection depends on which hand is detected.

| Hand | Condition |
|-----|-----|
Right Hand | thumb_tip_x > thumb_joint_x |
Left Hand | thumb_tip_x < thumb_joint_x |

still prone to error

### Other Fingers

Other fingers bend vertically, so detection compares **Y coordinates**.

Finger is considered open if:
  tip_y < joint_y
Finger tips used:

| Finger | Landmark ID |
|------|------|
Index | 8 |
Middle | 12 |
Ring | 16 |
Pinky | 20 |
