from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pandas as pd
import time

driver_file_chrome = "C:\Program Files\chromedriver-win64\chromedriver.exe"

servico = Service(driver_file_chrome) 
controle = webdriver.ChromeOptions()  
controle.add_argument("--disable-gpu")
controle.add_argument("--window-size=1920,1080")

url_site = 'https://www.vivareal.com.br/venda/sp/sao-caetano-do-sul/apartamento_residencial/1-quarto/?transacao=venda&onde=,S%C3%A3o%20Paulo,S%C3%A3o%20Caetano%20do%20Sul,,,,,city,BR%3ESao%20Paulo%3ENULL%3ESao%20Caetano%20do%20Sul,-23.616443,-46.567958,&tipos=apartamento_residencial&pagina=1&banheiros=1,2,3,4&quartos=1,2,3,4&vagas=1,2,3,4&areaMinima=45&areaMaxima=80'

driver_file_chrome.get(url_site)
time.sleep(5)

dic_imoveis = {"Metragem":[], "Quartos":[], "Banheiros":[], "Vagas":[], "Valor":[], "IPTU e Condomínio":[], "Nome da Rua":[], "Bairro e Cidade":[]}
pagina_atual = 1
contador_imoveis = 0
limite = 100
while True:
    print(f'\n Coletando os dados da página: {pagina_atual}')
    
    try:
        WebDriverWait(driver_file_chrome, 10).untill(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-cy="rp-property-cd"]'))
        )
        print('Os elementos foram encontrados com sucesso')
    except TimeoutException:
        print('Tempo de espera expedido')
        break
    
    imoveis = driver_file_chrome.find_elements(By.CSS_SELECTOR, '[data-cy="rp-property-cd"]' )
    
    for imovel in imoveis:
                        
        try:
            metragem = imovel.find_element(By.CSS_SELECTOR, '[data-cy="propertyArea"]' )
        except Exception as e:
            metragem = "Não Informado"
        try:
            quartos = imovel.find_element(By.CSS_SELECTOR, '[data-cy="bedroomQuantity"]')
        except Exception as e:
            quartos = "Não Informado"
        try:
            banheiros = imovel.find_element(By.CSS_SELECTOR, '[data-cy="bathroomQuantity"]')
        except Exception as e:
            banheiros = "Não Informado"
        try:
            vagas = imovel.find_elemennt(By.CSS_SELECTOR, '[data-cy="parkingSpaceQuantity"]')
        except Exception as e:
            vagas = "Não Informado"
        try: 
            valor = imovel.find_element(By.CSS_SELECTOR, '[data-cy="Property-price"]')
        except Exception as e:
            valor = "Não Informado"
        try:
            iptu_e_condominio = imovel.find_element(By.CSS_SELECTOR, '[data-cy=""]')
        except Exception as e:
            iptu_e_condominio = "Não Informado"
        try: 
            nome_da_rua = imovel.find_element(By.CSS_SELECTOR, '[data-cy="rp-cardProperty-street-txt"]')
        except Exception as e:
            nome_da_rua = "Não Informado"
        try:
            bairro_e_cidade = imovel.find_element(By.CSS_SELECTOR, '[data-cy="rp-cardProperty-location-txt"]')
        except Exception as e:
            bairro_e_cidade = "Não Informado"
        try:
                    elemento = imovel.find_element(By.CSS_SELECTOR,'[data-cy="rp-cardProperty-price-txt"]')
                    paragrafos = elemento.find_elements(By.TAG_NAME,'p')
                    item1 = paragrafos[0].text.strip() if len(paragrafos) > 0 else None 
                    item2 = paragrafos[1].text.strip() if len(paragrafos) > 0 else None
        except Exception as e:
            print(f"Erro: {e}")
            item1 = None
            item2 = None

            print(f"{metragem} - {quartos} - {banheiros} - {vagas} - {valor} - {iptu_e_condominio} - {nome_da_rua} - {bairro_e_cidade}")

            dic_imoveis["Metragem"].append(metragem)
            dic_imoveis["Quartos"].append(quartos)
            dic_imoveis["Banheiros"].append(banheiros)
            dic_imoveis["Vagas"].append(vagas)
            dic_imoveis["Valor"].append(valor)
            dic_imoveis["IPTU e Condomínio"].append(iptu_e_condominio)
            dic_imoveis["Nome da Rua"].append(nome_da_rua)
            dic_imoveis["Bairro e Cidade"].append(bairro_e_cidade)
        
    while contador_imoveis < limite:    
        if contador_imoveis <= limite  
    

        
        
        