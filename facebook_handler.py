import requests
import os
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

my_store = os.getenv('FACEBOOK_STORE_PAGE')
page_id = os.getenv('FACEBOOK_PAGE_ID')
ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN')

def post_to_facebook(page_id, message):
    url = f'https://graph.facebook.com/v18.0/{page_id}/feed'
    payload = {
            'message': message,
            'access_token': ACCESS_TOKEN
        }
    response = requests.post(url, data=payload)

def post_with_image(page_id, image_url, message):
    url = f'https://graph.facebook.com/v18.0/{page_id}/photos?url={image_url}&message={message}'
    payload = {
            'image_url' : image_url,
            'message': message,
            'access_token': ACCESS_TOKEN       
        }
    
    response = requests.post(url, data=payload)

def create_album_and_upload_images(page_id, album_name, image_urls, message):
    # Create a new album
    album_create_url = f'https://graph.facebook.com/v18.0/{page_id}/albums'
    album_payload = {
        'name': album_name,
        'message': message,
        'access_token': ACCESS_TOKEN
    }
    album_response = requests.post(album_create_url, data=album_payload)
    album_id = album_response.json().get('id')

    # Upload images to the created album
    for image_url in image_urls:
        photo_upload_url = f'https://graph.facebook.com/v18.0/{album_id}/photos'
        photo_payload = {
            'url': image_url,
            'access_token': ACCESS_TOKEN
        }
        photo_response = requests.post(photo_upload_url, data=photo_payload)