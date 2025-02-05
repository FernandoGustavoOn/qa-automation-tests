import os
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
    
    # Garantir que o diretório seja limpo ao final
    options.add_argument("--no-first-run")
    options.add_argument("--disable-default-apps")

    # Inicializando o driver do Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    yield driver
    
    # Fechar o driver e limpar o diretório temporário
    driver.quit()
    if os.path.exists(user_data_dir):
        os.rmdir(user_data_dir)

def test_login_sucesso(driver):
    driver.get("https://www.saucedemo.com/")
    
    # Localizando os campos e preenchendo com as credenciais
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
    
    # Verificando se o login foi bem-sucedido
    assert "inventory.html" in driver.current_url, "Erro: O login falhou!"
