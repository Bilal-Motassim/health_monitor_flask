# utils.py

import requests

def send_prompt_to_llm(prompt, model="llama3", endpoint="http://localhost:11434/v1/chat/completions"):
    response = requests.post(
        endpoint,
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    response.raise_for_status()  # Raise an error for failed requests
    return response.json()["choices"][0]["message"]["content"]
