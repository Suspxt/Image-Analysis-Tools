# import the necessary packages for image processing, data manipulation, etc.
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import cv2

# specify sample image directories
samples = 'Sample Images/'
campus_samples = 'Sample Images/02.24.2020 Campus Export/'

image1 = cv2.imread(campus_samples + 'DSC_0250.jpg', 1)
cv2.imshow('image', image1[:,:,::-1])
cv2.waitKey(0)
cv2.destroyAllWindows()

print(np.shape(image1))
i1_hist = cv2.calcHist(image1, [0, 1, 2], None, [256], [0, 256])
