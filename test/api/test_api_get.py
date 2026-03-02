
def test_api_get(playwright):
    request = playwright.request.new_context()

    response = request.get("http://localhost:5000/api/tasks/14")

    assert response.status == 200
    json_data = response.json()
    print (json_data)
    assert json_data["task"] == "cjj"

    request.dispose()
    print("Test completed successfully.")