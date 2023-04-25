from selenium import webdriver
from selenium.webdriver.common.by import By


class Scraper:
    driver = ''

    def __init__(self):
        self.driver = webdriver.Chrome()

    def iniciar_busca(self, url):
        self.driver.get(url)

    def busca_por_id(self, id):
        resultado_busca = self.driver.find_element(By.ID, id)
        return resultado_busca.text

    def busca_por_xpath(self, xpath):
        resultado_busca = self.driver.find_element(By.XPATH, xpath)
        return resultado_busca.text

    def buscar_src_imagem(self, id):
        resultado_busca = self.driver.find_element(By.ID, id)
        return resultado_busca.get_attribute('src')

    def finalizar_busca(self):
        self.driver.quit()
