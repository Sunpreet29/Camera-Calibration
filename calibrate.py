import cv2
import numpy as np
import glob
 
# Define the dimensions of checkerboard
CHECKERBOARD = (8, 6)  # (columns, rows) of inner corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Create object points (0,0,0 ... 7,5,0 for 8x6 checkerboard)
objp = np.zeros((CHECKERBOARD[0]*CHECKERBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

# Store 3D points in real world space & 2D points in image plane
objpoints = []  # 3D
imgpoints = []  # 2D

images = glob.glob('captured_images/*.png')  # folder with checkerboard images

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the checkerboard corners
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    if ret:
        objpoints.append(objp)

        # Refine corner locations
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)

        # Optionally draw and display corners
        cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
        cv2.imshow('Corners', img)
        cv2.waitKey(1000)

cv2.destroyAllWindows()

ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None
)

print("Camera matrix:\n", camera_matrix)
print("Distortion coefficients:\n", dist_coeffs)