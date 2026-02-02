def build_prompt(api_info):
    """
    Builds a controlled prompt for GenAI to generate PyTest API tests
    """

    endpoint = api_info["endpoint"]
    method = api_info["method"]
    summary = api_info["summary"]
    parameters = api_info["parameters"]
    responses = api_info["responses"]

    prompt = f"""
You are a Senior SDET and API automation expert.

Generate PyTest-based API test cases using Python requests library.

API Details:
- Base URL: https://petstore.swagger.io/v2
- Endpoint: {endpoint}
- HTTP Method: {method}
- Description: {summary}
- Parameters: {parameters}
- Expected Responses: {responses}

Rules:
1. Use pytest framework
2. Use requests library
3. Write at least one positive test case
4. Write at least one negative test case
5. Validate HTTP status codes
6. Do NOT add explanations or comments outside code
7. Output ONLY executable Python code
8. Use Python logging module to log test steps (request sent, response received)


The test file should be production-ready.
"""
    return prompt
