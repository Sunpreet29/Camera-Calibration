# 📷 Camera-Calibration with OpenCV 

This project demonstrates how to **calibrate a webcam** using OpenCV and a checkerboard pattern.  
It computes the **camera matrix** and **distortion coefficients**, which can be used to undistort images or video streams.

---

## 🛠 Requirements

- Python 3.8+
- [OpenCV](https://pypi.org/project/opencv-python/)
- [NumPy](https://numpy.org/)

## Install dependencies:
1. Clone the repository into your desired folder.

2. A new anaconda environment can be created with the desired dependencies:

```bash
conda env create -f environment.yaml
```

3. Activate the environment after it is created successfully and change directory to 'Camera-Calibration'.
To find more information about the theory behind camera calibration, refer to this link:
[Camera calibration](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)

4. The file ```capture_image.py``` has by default camera device selected for taking pictures. The folder where pictures are captured can be changed.

5. Prepare a checkerboard pattern ready (either on a tablet screen or printed on a piece of paper). Run the python file ```capture_image.py```. Ensure to be in the correct directory beforehand.

```bash
python3 capture_image.py
``` 

6. Then press **s** key to capture images. Try to give different poses while taking the images and take at least 10 of them. Press **q** to stop the code.

7. Run  ```calibrate.py``` and then you can see the camera matrix parameters and the distortion coefficients.

```bash
python3 calibrate.py
```