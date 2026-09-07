import requests
import json

def query_local_ollama(prompt, model="qwen2.5:32b", system_prompt="You are a helpful creative assistant."):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "system": system_prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "")
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama: {e}"

if __name__ == "__main__":
    test_prompt = "Hello! Summarize in one sentence what makes multilingual LLMs unique."
    print("Sending test request to local model...")
    result = query_local_ollama(test_prompt)
    print("\nModel Output:\n", result)
