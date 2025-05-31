import cv2
from tracker import SimpleTracker

cap = cv2.VideoCapture("video.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

tracker = SimpleTracker()

total_count = 0

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    roi = frame[100:720, 500:1280]
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detections = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            if w > 30 and h > 30:
                detections.append((x, y, x+w, y+h))

    objects = tracker.update(detections)

    for obj_id, (cx, cy) in objects.items():
        cv2.circle(roi, (cx, cy), 5, (0, 255, 255), -1)
        cv2.putText(roi, f"ID {obj_id}", (cx - 10, cy - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

        # Count each ID once
        if obj_id not in tracker.counted_ids:
            total_count += 1
            tracker.counted_ids.add(obj_id)

    cv2.putText(roi, f"Total Count: {total_count}", (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    frame[100:720, 500:1280] = roi
    out.write(frame)
    cv2.imshow("Tracked  video", frame)

    if cv2.waitKey(30) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
