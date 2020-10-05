from PIL import Image
import random
import requests
from io import BytesIO
import PIL
import boto3
import json


def rescale_image(added_image: PIL.Image) -> PIL.Image:
    added_image_width, added_image_height = added_image.size

    if added_image_width >= added_image_height:
        resize_factor = 400 / added_image_width

    else:
        resize_factor = 400 / added_image_height

    added_image_width = int(added_image_width * resize_factor)
    added_image_height = int(added_image_height * resize_factor)

    return added_image.resize((added_image_width, added_image_height))


class FridgeAccessor:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name

        s3 = boto3.resource("s3")
        self.bucket = s3.Bucket(bucket_name)
        self.fridge_object = self.bucket.Object("fridge.png")

    def get_current_fridge_image(self) -> PIL.Image:
        fridge_bytes = BytesIO()

        self.fridge_object.download_fileobj(fridge_bytes)

        fridge_image = Image.open(fridge_bytes, "r").convert("RGBA")

        return fridge_image

    def paste_image_to_fridge(self, image_url: str) -> PIL.Image:
        fridge_image = self.get_current_fridge_image()
        fridge_width, fridge_height = fridge_image.size

        added_image_bytes = BytesIO(requests.get(image_url).content)
        added_image = Image.open(added_image_bytes, "r").convert("RGBA")

        added_image = rescale_image(added_image)
        added_image_width, added_image_height = added_image.size

        x = random.randrange(added_image_width, fridge_width - added_image_width)
        y = random.randrange(added_image_height, fridge_height - added_image_height)

        fridge_image.paste(added_image, (x, y))

        return fridge_image


    def write_new_image_to_s3(self, image_url: str):
        fridge_image = self.paste_image_to_fridge(image_url)

        new_image_bytes = BytesIO()
        fridge_image.save(new_image_bytes, format="PNG")

        self.bucket.put_object(Key="fridge.png", Body=new_image_bytes.getvalue(), ACL='public-read')


def lambda_handler(event, context):
    # CHANGE THIS BUCKET NAME
    bucket_name = "cfiutak1-hackbu-demo"
    image_url = json.loads(event["body"])["image_url"]

    fridge = FridgeAccessor(bucket_name)
    fridge.write_new_image_to_s3(image_url)

    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
        },
        'body': image_url
    }
