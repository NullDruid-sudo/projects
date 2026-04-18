# 🎛️ Hand Gesture Volume Control (Linux)

Control your system volume using **hand gestures** detected from your webcam.

This project uses **MediaPipe Hand Tracking** and **OpenCV** to detect the distance between your **thumb and index finger** and converts that distance into system volume using `pactl`.

Think of it like an invisible volume knob floating in the air.

---

## 📸 How It Works

1. The webcam captures video frames.
2. MediaPipe detects hand landmarks.
3. The distance between:
   - **Thumb tip**
   - **Index finger tip**
4. That distance is mapped to **0–100% system volume**.
5. Volume is updated using **PulseAudio (`pactl`)**.

When your fingers move apart → volume increases.  
When they move closer → volume decreases.

---

## 🧠 Features

- Real-time **hand tracking**
- **Gesture-based volume control**
- **Visual feedback**
- Displays **distance between fingers**
- Shows **live FPS**
- Works on **Linux with PulseAudio**

---

## 🖥️ Demo Behavior

| Gesture | Result |
|------|------|
| Fingers close together | Low volume |
| Fingers far apart | High volume |
| Middle point turns yellow | Distance threshold reached |

---

## 📦 Requirements

Install the required Python libraries:

```bash
pip install opencv-python mediapipe numpy
