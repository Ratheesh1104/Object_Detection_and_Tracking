# Object Detection and Tracking Using OpenCV

This project presents a Python-based solution for detecting, tracking, and counting moving objects in video footage captured from a static camera. It leverages OpenCV’s background subtraction technique in combination with a custom centroid-based tracking algorithm to assign persistent IDs and accurately count unique moving objects in real time.

---

## 📌 Project Overview

The system processes video streams frame-by-frame to:

- Detect moving objects using background subtraction
- Track each object across frames using centroid-based ID assignment
- Maintain a cumulative count of unique objects detected
- Save a processed output video annotated with bounding boxes, object IDs, and a live count display

This implementation runs entirely offline and can be adapted for various surveillance and analytics use cases.

---

## ✅ Real-World Problem Addressed

In real-time environments, manual tracking and counting of objects is inefficient and error-prone. This project automates that task and provides a reliable, reusable baseline for multiple application domains:

### Surveillance & Security

- Detect and count people or vehicles in CCTV footage
- Monitor restricted areas automatically
- Analyze foot traffic in commercial or public zones

### Sports Analytics

- Track players and moving objects like balls
- Measure coverage zones, movement speeds, and play patterns
- Generate real-time insights for performance evaluation

### Industrial & Manufacturing

- Count units on conveyor belts or production lines
- Monitor material movement for inventory control
- Detect irregularities or breakdowns in workflow

### Traffic Management

- Measure vehicle count and traffic density at intersections
- Integrate with adaptive signal systems
- Detect anomalies such as congestion or wrong-way driving

---

## 🔧 Why This Approach?

- **Lightweight**: Runs efficiently on low-power or edge devices
- **Offline**: No reliance on cloud-based models or internet access
- **Customizable**: Easily adapted for different object types or environments
- **Extensible**: Can be upgraded with deep learning models like YOLO, MobileNet, etc.

---

## 🎯 Final Output Features

The system generates a fully annotated output video that includes:

- Bounding boxes around each detected object
- Persistent object IDs across frames
- Live display of total object count on the video
- Exported video file for further use or reporting

This solution serves as a foundational building block for more advanced object analytics systems and smart monitoring solutions.

---

## 📽️ Demo

![Demo Output](https://raw.githubusercontent.com/Ratheesh1104/Object_Detection_and_Tracking/main/output.gif)

---
