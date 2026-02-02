import os
from swagger_parser import load_swagger, extract_user_apis, extract_api_details
from prompt_builder import build_prompt
from llm_client import generate_test_code

OUTPUT_DIR = "tests/generated"

def generate_tests():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    swagger = load_swagger("swagger/petstore_swagger.json")
    user_apis = extract_user_apis(swagger)
    api_details = extract_api_details(user_apis)

    for api in api_details:
        prompt = build_prompt(api)
        test_code = generate_test_code(prompt)

        endpoint_name = api["endpoint"].replace("/", "_").replace("{", "").replace("}", "")
        method = api["method"].lower()

        file_name = f"test_{endpoint_name}_{method}.py"
        file_path = os.path.join(OUTPUT_DIR, file_name)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(test_code)

        print(f"Generated: {file_name}")

if __name__ == "__main__":
    generate_tests()
