import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from prompt_engineering import get_system_prompt, get_user_prompt
from template import html_template

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY)
model_name = "gpt-4o"  # or your chosen model
temperature = 0.7
max_tokens = 2000  # Increase if necessary for complete output

def call_openai_api(system_prompt, user_prompt):
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

# Load resume data from JSON file
with open("resume.json", "r") as f:
    resume = json.load(f)
    
with open("action_verbs.json", "r") as f:
    action_verbs = json.load(f)

# Load job description from file
with open("job_description.txt", "r") as f:
    job_description = f.read().strip()

# Build the system and user prompts
system_prompt = get_system_prompt()
user_prompt = get_user_prompt(job_description, resume, action_verbs)

# Call the API with the system and user prompts
final_output = call_openai_api(system_prompt, user_prompt)

# Replace placeholders in the HTML template with the LLM's output
final_html = html_template.replace("<!-- Resume Content -->", final_output)
final_html = final_html.replace("'''", '')
final_html = final_html.replace("'''html", '')

# Write the final tailored resume HTML to a file
with open("tailored_resume.html", "w") as f:
    f.write(final_html)

# Optionally, convert the HTML to PDF
# converter.convert(final_html, "tailored_resume.pdf")