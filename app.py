from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from image_edit import edit_advertisement
from stabilityapi import generate_imgtoimg

import secrets
import base64

app = FastAPI()

@app.post("/generate_advertisement/")
async def create_advertisement(
                            prompt: str,
                            base_image: UploadFile = File(...),
                            color: str = "#4F6F52",
                            punchline: str = "This is a great product!",
                            button_text: str = "Buy now!",
                            company_logo: UploadFile = File(...),

                        ):

    
    file_name = base_image.filename
    file_content = await base_image.read()
    img_base = generate_imgtoimg(prompt, color, file_content)

    with open(f"./{file_name}", "wb") as f:
        f.write(base64.b64decode(img_base))

    file_name = company_logo.filename
    file_content = await company_logo.read()

    with open(f"./{file_name}", "wb") as f:
        f.write(file_content)

    new_image = edit_advertisement(base_image.filename, color, company_logo.filename, punchline, button_text)
    
    file_name = secrets.token_hex(8)
    new_image.save(f"./{file_name}.png")

    return FileResponse(f"./{file_name}.png", media_type="image/png")

