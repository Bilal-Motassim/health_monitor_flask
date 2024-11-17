# main.py

from fastapi import FastAPI, File, UploadFile
from transformers import pipeline
from PIL import Image
import io

from prompts import generate_health_feedback_prompt
from utils import send_prompt_to_llm

app = FastAPI()

pipe = pipeline("image-classification", model="nateraw/food")

@app.post("/classify/")
async def classify_image(file: UploadFile = File(...)):
    # Read the uploaded image
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    # Classify the image to get ingredients
    result = pipe(image)
    ingredients = [res['label'] for res in result]

    # Generate prompt and get feedback from the LLM
    prompt = generate_health_feedback_prompt(ingredients)
    health_feedback = send_prompt_to_llm(prompt)

    return {"ingredients": ingredients, "health_feedback": health_feedback}
