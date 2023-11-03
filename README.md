# Generate Advertisement Images

Generate cool images for your advertisement campaign. You can make a creative touch to your product and also combine it with your brand logo. Examples are given below for you to get inspired, then you can use the API to generate your own. Enjoy!   

## Tech Stack

- **Img2Img Generation**: Stable-Diffusion-XL
- **Image Editing and Manipulation**: PIL
- **API**: FastAPI
- **Deployment**: Docker and Google Cloud Run
- **Python 3.9**

## Examples
### Example 1 - Sneakers

Parameter | Value | Description
--- | --- | ---
base_image | ![Example 1](base_images/sneakers.png) | Base image for the prompt
prompt | sneakers covered in sakura leaves, warm colors | Prompt for the recreation
color | #27005D | Color for the template
punchline | Summer is coming! | Punchline for the advertisement
button_text | Buy now! | Text for the button
logo | ![Example 2](logos/sneako-company-logo.png) | Logo for the brand

### Output

![Example 3](outputs/sakuraleaves.png)


### Example 2 - Coffee

Parameter | Value | Description
--- | --- | ---
base_image | ![Example 1](base_images/coffecup.png) | Base image for the prompt
prompt | a coffee cup with dia de muertos patterns | Prompt for the recreation
color | #65451F | Color for the template
punchline | Coffee Coffee Coffee! | Punchline for the advertisement
button_text | Buy now! | Text for the button
logo | ![Example 2](logos/Untitled.jpeg) | Logo for the brand

### Output

![Example 3](outputs/diademuertos.png)


```
pip install pipreqs
pipreqs /path/to/project
```