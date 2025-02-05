import tempfile
import pytest
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    # Gerar um diretório temporário único usando uuid
    user_data_dir = tempfile.mkdtemp(prefix=str(uuid.uuid4()))
    options.add_argument(f"--user-data-dir={user_data_dir}")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_login_sucesso(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)

    assert "inventory.html" in driver.current_url, "Erro: O login falhou!"
