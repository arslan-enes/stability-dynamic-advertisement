from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from app.image_edit import edit_advertisement
from app.stabilityapi import generate_imgtoimg
from io import BytesIO

import secrets
import base64


app = FastAPI()

@app.post("/generate_advertisement/")
async def generate_advertisement(
                            prompt: str,
                            base_image: UploadFile = File(...),
                            color: str = "#4F6F52",
                            punchline: str = "This is a great product!",
                            button_text: str = "Buy now!",
                            company_logo: UploadFile = File(...),

                        ):
    
    file_name = base_image.filename
    file_content = await base_image.read()
    file_content = generate_imgtoimg(prompt, color, file_content)
    base_image_content = base64.b64decode(file_content)


    file_name = company_logo.filename
    logo_content = await company_logo.read()


    new_image = edit_advertisement(base_image=base_image_content,
                                   color=color,
                                   company_logo=logo_content, 
                                   punchline= punchline, 
                                   button_text=button_text)


    img_bytes = BytesIO()
    new_image.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    return StreamingResponse(content=img_bytes, media_type="image/png")


