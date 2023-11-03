from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from image_edit import edit_advertisement
from stabilityapi import generate_imgtoimg

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

    file_name = secrets.token_hex(8)
    new_image.save(f"./{file_name}.png")

    return FileResponse(f"./{file_name}.png", media_type="image/png")

