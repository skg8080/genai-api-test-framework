import json

def load_swagger(file_path):
    """
    Loads Swagger JSON file and returns it as a Python dictionary
    """
    with open(file_path, "r") as file:
        return json.load(file)

def extract_user_apis(swagger_data):
    """
    Extracts only /user related APIs from Swagger
    """
    user_apis = {}

    paths = swagger_data.get("paths", {})

    for endpoint, methods in paths.items():
        if endpoint.startswith("/user"):
            user_apis[endpoint] = methods

    return user_apis

def extract_api_details(user_apis):
    """
    Converts Swagger data into a simplified structure for GenAI
    """
    extracted_data = []

    for endpoint, methods in user_apis.items():
        for method, details in methods.items():
            api_info = {
                "endpoint": endpoint,
                "method": method.upper(),
                "summary": details.get("summary"),
                "parameters": details.get("parameters", []),
                "responses": list(details.get("responses", {}).keys())
            }
            extracted_data.append(api_info)

    return extracted_data
