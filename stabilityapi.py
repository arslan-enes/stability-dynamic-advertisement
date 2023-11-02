import base64
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_imgtoimg(prompt, color, base_image):

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
            "init_image": base_image,
        },
        data={
            "image_strength": 0.30,
            "init_image_mode": "IMAGE_STRENGTH",
            "text_prompts[0][text]": f"""

            {prompt},
            photoshoot, good lighting, high resolution, {color} dominant

            """,
            "text_prompts[0][weight]": 1,
            "text_prompts[1][text]": "out of frame, blurry, low resolution",
            "text_prompts[1][weight]": -1,
            "cfg_scale": 7,
            "samples": 1,
            "steps": 30,
        }
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    return data["artifacts"][0]['base64']
