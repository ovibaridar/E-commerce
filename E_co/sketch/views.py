import cv2
import numpy as np
import os
from django.shortcuts import render
from django.conf import settings
from .models import SketchImage

def sketch(request):
    return render(request, 'sketch/skatch_home.html')

def sketch_conversion(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'].read()
        nparr = np.frombuffer(image, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Reduce lighting from the image using histogram equalization
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        equalized_img = cv2.equalizeHist(gray_img)

        # Apply adaptive thresholding for better sketch effect
        threshold_img = cv2.adaptiveThreshold(equalized_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

        inverted_img = 255 - threshold_img
        sketch_img = cv2.divide(255 - inverted_img, 255, scale=256)

        # Reduce the intensity of black pixels by 10%
        sketch_img = sketch_img * 0.9

        # Create a 4-channel image with an alpha channel
        h, w = sketch_img.shape
        sketch_img_with_alpha = np.zeros((h, w, 4), dtype=np.uint8)
        sketch_img_with_alpha[:, :, 0] = sketch_img
        sketch_img_with_alpha[:, :, 1] = sketch_img
        sketch_img_with_alpha[:, :, 2] = sketch_img
        sketch_img_with_alpha[:, :, 3] = 255  # Alpha channel set to fully opaque

        # Save the sketch image with transparent background in a folder
        save_folder = os.path.join(settings.MEDIA_ROOT, 'sketch_images/')
        os.makedirs(save_folder, exist_ok=True)
        save_path = os.path.join(save_folder, 'sketch.png')
        cv2.imwrite(save_path, sketch_img_with_alpha)

        # Create a new SketchImage object and save the sketch image to it
        sketch_image = SketchImage.objects.create(image='sketch_images/sketch.png')

        context = {'sketch_img_path': sketch_image.image.url}
        return render(request, 'sketch/skatch_home.html', context)

    return render(request, 'sketch/skatch_home.html')
