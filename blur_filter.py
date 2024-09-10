from PIL import Image

import sys
import matplotlib.pyplot as plt
import numpy as np


# Print matrix
def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" \t")
        print()


# Kernel convolution
def blur_algorithm(kernel, blur_matrix, row, col):
    r_value = np.int64(0)
    g_value = np.int64(0)
    b_value = np.int64(0)

    for i in range(kernel.shape[0]):
        for j in range(kernel.shape[1]):
            r_value += kernel[i, j, 0]
            g_value += kernel[i, j, 1]
            b_value += kernel[i, j, 2]

    r_value //= 9
    g_value //= 9
    b_value //= 9

    result_array = np.array([r_value, g_value, b_value])

    # Assign the result array to blur matrix
    blur_matrix[row, col] = result_array


# Check if no image is passed
if len(sys.argv) < 2:
    print("No image file.")
else:
    imgFile = sys.argv[1]

# Load image
img = np.asarray(Image.open(imgFile))

# Get rows, columns and rgb format from image matrix
img_rows, img_cols, img_rgb = img.shape

# Initialize temp image matrix with zeros or with specific value

# with zeros
# tmp_img = np.zeros((img_rows + 2, img_cols + 2, img_rgb), dtype=np.uint8)

# with specific value
tmp_img = np.full(
    (img_rows + 2, img_cols + 2, img_rgb), [128, 128, 128], dtype=np.uint8
)

# Center img matrix inside temp img matrix
tmp_img[1 : img_rows + 1, 1 : img_cols + 1, :] = img

# # Print image matrix

# print_matrix(img)
# print(f"\n{img.shape}\n")

# print_matrix(tmp_img)
# print(f"\n{tmp_img.shape}\n")

# Initialize kernel matrix
kernel = np.zeros((3, 3, img_rgb), dtype=np.uint8)

# Initialize blur img matrix
blur_img = np.zeros((img_rows, img_cols, img_rgb), dtype=np.uint8)

for row in range(img_rows):
    for col in range(img_cols):
        kernel = tmp_img[row : row + 3, col : col + 3]

        # print_matrix(kernel)
        # print()
        blur_algorithm(kernel, blur_img, row, col)

# Print final image matrix
# print(blur_img)

# Create a figure and axis object
fig, ax = plt.subplots(1, 2, figsize=(10, 5))  # 1 row, 2 columns

# Display the first image
ax[0].imshow(img)
ax[0].set_title("Original image")
ax[0].axis("off")

# Display the second image
ax[1].imshow(blur_img)
ax[1].set_title("Blur filter")
ax[1].axis("off")
plt.show()
