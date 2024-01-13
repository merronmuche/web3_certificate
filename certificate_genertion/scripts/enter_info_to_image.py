import cv2
import numpy as np

# Load the certificate image
image_path = '//home/meron/Documents/work/tenacademy/week5/myweb3/data/generated.png'
certificate = cv2.imread(image_path)

# Load the logo image 
logo_path = '/home/meron/Documents/work/tenacademy/week5/myweb3/data/10academy_logo.png'
logo = cv2.imread(logo_path)

# Check if the images are loaded correctly
if certificate is None or logo is None:
    raise ValueError("Could not open or find the image or the logo.")

# Define the text to be added
name = "Full Name: Meron Amsalu"
course_title = "Title: Data Engineering"
date = "10/01/2024Gc"

# Define the position for the text 
name_position = (350, 550)  
course_position = (350, 600)  
date_position = (450,720)

# Define the position for the logo 
logo_position = (200, 100)  
logo_scale = 0.5  

# Resize logo according to the scale
logo_height, logo_width = logo.shape[:2]
logo = cv2.resize(logo, (int(logo_width * logo_scale), int(logo_height * logo_scale)), interpolation=cv2.INTER_AREA)

# Overlay the logo on the certificate
x_offset, y_offset = logo_position
y1, y2 = y_offset, y_offset + logo.shape[0]
x1, x2 = x_offset, x_offset + logo.shape[1]

# The region of interest in the certificate image
roi = certificate[y1:y2, x1:x2]

# To overlay, we need to create a mask
# Create a mask of the logo and its inverse mask
mask = logo.copy()
mask[mask > 0] = 450
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
certificate_bg = cv2.bitwise_and(roi, mask_inv)

# Take only region of logo from logo image
logo_fg = cv2.bitwise_and(logo, mask)

# Put logo in ROI and modify the main image
dst = cv2.add(certificate_bg, logo_fg)
certificate[y1:y2, x1:x2] = dst

# Font settings for the text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1  # Adjust the scale according to the certificate
font_color = (0, 0, 0)  # Black color
line_type = 2

# Add the text to the certificate
cv2.putText(certificate, name, name_position, font, font_scale, font_color, line_type)
cv2.putText(certificate, course_title, course_position, font, font_scale, font_color, line_type)
cv2.putText(certificate, date, date_position, font, font_scale, font_color, line_type)


# Save the resulting image
output_path = 'certificate_with_name_course_logo.png'
cv2.imwrite(output_path, certificate)

# Display the image (optional, for testing purposes)
cv2.imshow('Certificate', certificate)
cv2.waitKey(0)
cv2.destroyAllWindows()
