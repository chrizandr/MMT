import numpy as np
import cv2

from points import world_points_c1, world_points_c2, world_points_c3
from points import pixels_c1, pixels_c2, pixels_c3


def sensor_to_pixel(H, sensor_points):
    """Project sensor readings to pixel values."""
    pixel_points = []
    for (x, y) in sensor_points:
        A = np.array([[x], [y], [1]])
        i_pred = H.dot(A.T)
        i_pred = i_pred / i_pred[-1]
        pixel_points.append(i_pred)

    return np.array(pixel_points)


def calculate_homography(real_points, pixel_points):
    """Find the homography projection matrix."""
    X, stat = cv2.findHomography(real_points, pixel_points)
    return X


H_c1 = calculate_homography(world_points_c1, pixels_c1)
H_c2 = calculate_homography(world_points_c2, pixels_c2)
H_c3 = calculate_homography(world_points_c3, pixels_c3)
