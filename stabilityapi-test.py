import base64
import os
import requests
from dotenv import load_dotenv

load_dotenv()

engine_id = "stable-diffusion-xl-1024-v1-0"
api_host = os.getenv("API_HOST", "https://api.stability.ai")
api_key = os.getenv("STABILITY_API_KEY")

if api_key is None:
    raise Exception("Missing Stability API key.")

response = requests.post(
    f"{api_host}/v1/generation/{engine_id}/image-to-image",
    headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    },
    files={
        "init_image": open("./base_images/oldpalacestability.png", "rb")
    },
    data={
        "image_strength": 0.4,
        "init_image_mode": "IMAGE_STRENGTH",
        "text_prompts[0][text]": "frame the picture with flowers, nostalgic, yellow dominant, advertisement, leaflet",
        "cfg_scale": 7,
        "samples": 1,
        "steps": 30,
    }
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

for i, image in enumerate(data["artifacts"]):
    with open(f"./out/v1_img2img_{i}.png", "wb") as f:
        f.write(base64.b64decode(image["base64"]))
