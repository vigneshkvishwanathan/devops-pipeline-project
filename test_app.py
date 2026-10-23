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
