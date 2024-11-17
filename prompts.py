# prompts.py

json_structure = {
    "meal": {
        "ingredients": ["list of ingredients here"]
    },
    "response_format": {
        "carbs": "numeric value in grams",
        "fats": "numeric value in grams",
        "proteins": "numeric value in grams",
        "fibers": "numeric value in grams",
        "feedback": "One-sentence feedback about the healthiness of the meal and suggestions for improvement"
    }
}

def generate_health_feedback_prompt(ingredients):
    return f"""
    Given this list of ingredients: {ingredients}, estimate the macronutrient content and return only the values as a JSON object.
    Specify the amount of carbs, protein, fat, and fiber in grams, and include a one-sentence feedback on the meal healthiness.
    The response should strictly follow this JSON format: {json_structure}. Please respond with only the JSON object.
    """
