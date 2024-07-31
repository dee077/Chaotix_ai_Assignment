from celery import shared_task
import requests
import uuid
from .models import GeneratedImage
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@shared_task
def generate_image(prompt):
    url = "https://api.stability.ai/v2beta/stable-image/generate/ultra"
    headers = {
        "authorization": "Bearer sk-mkc5aw2rN6OPk4hdEbkP3zXNAf7E2VUa8ZpSXpe5DHoWlq2K",
        "accept": "image/*"
    }
    files = {"none": ''}
    data = {
        "prompt": prompt,
        "output_format": "webp",
    }

    try:
        response = requests.post(url, headers=headers, files=files, data=data)
        response.raise_for_status() 

        output_dir = "/app/images" 
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        filename = f"image_{uuid.uuid1().hex}.webp"
        file_path = os.path.join(output_dir, filename)

        logger.info(f"Image generated and saved as {filename}")
        
        with open(file_path, 'wb') as file:
            file.write(response.content)

        GeneratedImage.objects.create(prompt=prompt, filename=filename)
    
    except Exception as e:
        logger.error(f"Request failed: {e}")
        raise Exception(f"An unexpected error occurred: {str(e)}")
