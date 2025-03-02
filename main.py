import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from prompt_engineering import get_system_prompt, get_user_prompt
from json_to_html_converter import json_to_html_converter

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Configuration
model_name = "gpt-4o"  # or your chosen model
temperature = 0.7
max_tokens = 10000

def call_openai_api(system_prompt, user_prompt):
    """Call the OpenAI API with the given prompts and return the response."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    try:
        response = openai_client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Error calling OpenAI API:", e)
        return ""

def main():
    # Load resume data from JSON file
    with open("resume.json", "r") as f:
        resume = json.load(f)
    
    # Load action verbs from JSON file
    with open("action_verbs.json", "r") as f:
        action_verbs = json.load(f)
    
    # Load job description from file
    with open("job_description.txt", "r") as f:
        job_description = f.read().strip()
    
    # Build the system and user prompts
    system_prompt = get_system_prompt()
    user_prompt = get_user_prompt(job_description, resume, action_verbs)
    
    print("Calling API to enhance the resume...")
    
    # Call the API with the system and user prompts
    llm_response = call_openai_api(system_prompt, user_prompt)
    
    # Parse the response as JSON
    try:
        cleaned_response = llm_response.replace("```", "").replace("```json", "")
        enhanced_resume = json.loads(llm_response)
        
        # Save the enhanced resume to a JSON file
        with open("enhanced_resume.json", "w") as f:
            json.dump(enhanced_resume, f, indent=2)
        
        print("Enhanced resume saved to 'enhanced_resume.json'")
    except json.JSONDecodeError as e:
        print("Error: The API response is not valid JSON.")
        print("Response:", llm_response)
        print("Error details:", e)
        
    json_to_html_converter()

if __name__ == "__main__":
    main()