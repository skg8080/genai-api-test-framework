from swagger_parser import load_swagger, extract_user_apis, extract_api_details

swagger = load_swagger("swagger/petstore_swagger.json")
user_apis = extract_user_apis(swagger)
api_details = extract_api_details(user_apis)

for api in api_details:
    print(api)
