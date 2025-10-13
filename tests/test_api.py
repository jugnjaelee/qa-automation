import requests

def test_github_api():
    """GitHub API가 200 OK 응답을 반환하는지 확인"""
    response = requests.get("https://api.github.com")
    assert response.status_code == 200
    assert "current_user_url" in response.json()
