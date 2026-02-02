import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env file
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def clean_llm_output(code: str) -> str:
    """
    Sanitizes LLM-generated code so it is executable by PyTest.
    - Removes markdown code fences
    - Fixes common pytest hallucinations
    - Ensures required imports exist
    """

    if not code:
        return ""

    cleaned_lines = []

    # --- 1. Remove markdown code fences ---
    for line in code.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            continue
        cleaned_lines.append(line)

    cleaned_code = "\n".join(cleaned_lines).strip()

    # --- 2. Fix known pytest hallucinations ---
    if "pytest.current_test_time()" in cleaned_code:
        cleaned_code = cleaned_code.replace(
            "pytest.current_test_time()",
            "int(time.time())"
        )

    # --- 3. Ensure required imports ---
    imports = []

    if "time.time()" in cleaned_code and "import time" not in cleaned_code:
        imports.append("import time")

    if "uuid.uuid4()" in cleaned_code and "import uuid" not in cleaned_code:
        imports.append("import uuid")

    if "logging." in cleaned_code and "import logging" not in cleaned_code:
        imports.append("import logging")

    if imports:
        cleaned_code = "\n".join(imports) + "\n\n" + cleaned_code

    return cleaned_code


    

def generate_test_code(prompt):
    """
    Sends prompt to OpenRouter LLM and returns generated PyTest code
    """
    response = client.chat.completions.create(
        model="tngtech/deepseek-r1t2-chimera:free",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    raw_code = response.choices[0].message.content
    return clean_llm_output(raw_code)

    
