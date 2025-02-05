import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    # Não use o --user-data-dir ou configure conforme necessário
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_login_sucesso(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)

    assert "inventory.html" in driver.current_url, "Erro: O login falhou!"
