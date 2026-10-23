import requests

def test_health_endpoint():
    #1. arrange: target our live app endpoint via our local loopback interface
    url = "http://localhost:5000/health"
    
    #2. act: programmatically trigger an HTTP GET request to our service
    response = requests.get(url)
    
    #3. assert: verify the HTTP response status code is exactly a 200 OK
    assert response.status_code == 200
    
    #4. assert: extract the JSON body payload and verify it matches specifications
    payload = response.json()
    assert payload["status"] == "healthy"
    assert payload["service"] == "devops-pipeline"
    
def test_invalid_endpoint_returns_404():
    # 1. Arrange: Target a non-existent URL directory path
    url = "http://localhost:5000/missing-route"
    
    # 2. Act: Execute the HTTP request to the live container
    response = requests.get(url)
    
    # 3. Assert: Verify the container engine accurately responds with a 404 Not Found
    assert response.status_code == 404

