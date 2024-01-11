from collections.abc import Iterable
from django.db import models
import os
import cv2
from django.conf import settings
import numpy as np
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
import datetime


# Create your models here.

from django.db import models

class Trainee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    date_certified = models.DateField(null=True, blank=True)
    certificate = models.ImageField(upload_to='media', blank=True, null=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.date_certified is None:
            self.date_certified = datetime.date.today()
        # open the certificate image using opencv
        # add the name, course and date to the certificate
        template_path = os.path.join(settings.MEDIA_ROOT, 'certificate_with_logo.png')
        # Open the template image using OpenCV
        template_image = cv2.imread(template_path)

        text_name = f"Name: {self.name}"
        text_course = f"Course: {self.course}" 
        text_date = f"Date: {self.date_certified.strftime('%Y-%m-%d')}"
        coordinates_name = (350, 550) 
        coordinates_course = (350, 600)
        coordinates_date = (450, 720)

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (0, 0, 255)  # Red color in BGR
        thickness = 2

        cv2.putText(template_image, text_name, coordinates_name, font, font_scale, color, thickness, cv2.LINE_AA)
        cv2.putText(template_image, text_course, coordinates_course, font, font_scale, color, thickness, cv2.LINE_AA)
        cv2.putText(template_image, text_date, coordinates_date, font, font_scale, color, thickness, cv2.LINE_AA)


        # save to database
        # Convert back to PIL image
        pil_image = Image.fromarray(cv2.cvtColor(template_image, cv2.COLOR_BGR2RGB))

        # Save the modified image
        buffer = BytesIO()
        pil_image.save(buffer, format='JPEG')
        image_content = ContentFile(buffer.getvalue())

        # Save the image to the certificate field
        self.certificate.save(f"certificate_{self.name}.jpg", image_content, save=False)
        
        return super().save(*args, **kwargs)

