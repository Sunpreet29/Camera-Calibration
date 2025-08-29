import cv2
import os
from datetime import datetime

save_dir = "captured_images"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
x = 0   # Time stamp can also be used for unique filenames: datetime.now().strftime("%Y%m%d_%H%M%S")
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('RGB Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        filename = f"image_{x}.png"
        filepath = os.path.join(save_dir, filename)
        cv2.imwrite(filepath, frame)
        print(f"Saved {filepath}")
        x += 1
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()