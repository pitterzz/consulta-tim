import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

# 1. Pede o número no início
numero = input("Digite o número: ")

print("Buscando...")

# 2. Instala automaticamente o ChromeDriver
chromedriver_autoinstaller.install()

# 3. Inicia o navegador com interface (pra você resolver o reCAPTCHA)
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

# 4. Acessa a tela de login
driver.get("https://capgeminibr.service-now.com/tim?id=tim_index")
print("Carregando tela de login...")

try:
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys("3662513")
    driver.find_element(By.NAME, "password").send_keys("Vitin@01")
    driver.find_element(By.XPATH, '//button[contains(text(), "Fazer login")]').click()
    print("Login realizado.")
except Exception as e:
    print("Erro no login:", e)
    driver.quit()
    exit()

# 5. Vai direto pra tela de consulta
time.sleep(6)
driver.get("https://capgeminibr.service-now.com/tim?id=tim_consulta_linha")
print("Página de consulta carregada.")

# 6. Espera o campo de input aparecer e preenche com o número digitado
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Linha que deseja consultar"]'))
    )
    campo = driver.find_element(By.XPATH, '//input[@placeholder="Linha que deseja consultar"]')
    campo.clear()
    campo.send_keys(numero)
    print("Número GSM inserido automaticamente.")
except Exception as e:
    print("Erro ao preencher número:", e)
    driver.quit()
    exit()

# 7. Aguarda você resolver o reCAPTCHA
input("Marque o reCAPTCHA na tela e depois aperte Enter aqui no CMD para continuar...")

# 8. Clica no botão "Pesquisar"
try:
    botao = driver.find_element(By.XPATH, '//button[contains(text(), "Pesquisar")]')
    botao.click()
    print("Pesquisa enviada.")
except Exception as e:
    print("Erro ao clicar em Pesquisar:", e)
    driver.quit()
    exit()

# 9. Aguarda resultado e exibe
time.sleep(5)
try:
    resultado = driver.find_element(By.XPATH, '//div[contains(@class, "container")]').text
    print("\nRESULTADO DA CONSULTA:\n", resultado)
except:
    print("Erro ao capturar o resultado ou ainda não carregou.")

input("\nPressione Enter para sair...")
driver.quit()