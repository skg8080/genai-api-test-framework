from swagger_parser import load_swagger, extract_user_apis, extract_api_details
from prompt_builder import build_prompt

swagger = load_swagger("swagger/petstore_swagger.json")
user_apis = extract_user_apis(swagger)
api_details = extract_api_details(user_apis)

prompt = build_prompt(api_details[0])
print(prompt)
