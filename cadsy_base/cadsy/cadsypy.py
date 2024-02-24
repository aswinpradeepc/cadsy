from inference_sdk import InferenceHTTPClient
import concurrent.futures
import cv2
import numpy as np
import os
client1 = InferenceHTTPClient(
    api_url="http://detect.roboflow.com",
    api_key="sZFjx8Fimj7ZtIWfDnwo"
)
client2 = InferenceHTTPClient(
    api_url="http://detect.roboflow.com",
    api_key="4WvQYKCiiFjRFkdUHdWw"
)

def resize_image_if_needed(image_path, max_width=640):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    if width > max_width:
        new_height = int((max_width / width) * height)
        resized_image = cv2.resize(image, (max_width, new_height), interpolation=cv2.INTER_AREA)
        temp_path = "temp_resized_image.jpg"
        cv2.imwrite(temp_path, resized_image)
        return temp_path
    else:
        return image_path

def infer(client, image_path, model_id):
    result = client.infer(image_path, model_id=model_id)
    return result['predictions']

def censor(image_path):
    resized_image_path = resize_image_if_needed(image_path)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(infer, client1, resized_image_path, "boobsdetector/1")
        future2 = executor.submit(infer, client2, resized_image_path, "dickdetector/3")
        
        detections1 = future1.result()
        detections2 = future2.result()

    image = cv2.imread(resized_image_path)

    detections = detections1 + detections2
    valid_detections = [d for d in detections if all(d.get(key) is not None for key in ['x', 'y', 'width', 'height']) and all(d[key] > 0 for key in ['width', 'height'])]

    if valid_detections:
        image = cv2.GaussianBlur(image, (23, 23), 30)

    cv2.imshow('Censored Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
