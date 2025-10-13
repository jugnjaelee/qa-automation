from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_title():
    driver = webdriver.Chrome()  # macOS에서는 자동 설치된 드라이버 사용
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
