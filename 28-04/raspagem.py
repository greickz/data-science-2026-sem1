from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pandas as pd
import time

driver_file_chrome = "C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe"  

servico = Service(driver_file_chrome)
controle = webdriver.ChromeOptions()
controle.add_argument("--disable-gpu")
controle.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=servico, options=controle)

url_site = 'https://www.vivareal.com.br/venda/sp/sao-caetano-do-sul/apartamento_residencial/1-quarto/?transacao=venda&onde=,S%C3%A3o%20Paulo,S%C3%A3o%20Caetano%20do%20Sul,,,,,city,BR%3ESao%20Paulo%3ENULL%3ESao%20Caetano%20do%20Sul,-23.616443,-46.567958,&tipos=apartamento_residencial&pagina=1&banheiros=1,2,3,4&quartos=1,2,3,4&vagas=1,2,3,4&areaMinima=45&areaMaxima=80'
driver.get(url_site)
time.sleep(5)

dic_imoveis = {
    "Metragem": [], "Quartos": [], "Banheiros": [], "Vagas": [], "Valor": [],
    "IPTU  E CONDOMÍNIO": [], "Nome da Rua": [], "Bairro e Cidade": []
}
pagina_atual = 1
contador_imoveis = 0
limite = 100

while contador_imoveis < limite:
    print(f'\nColetando os dados da página: {pagina_atual}')
    
    try:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-cy="rp-property-cd"]'))
        )
        print('Os elementos foram encontrados com sucesso')
    except TimeoutException:
        print('Tempo de espera expirado')
        break

    imoveis = driver.find_elements(By.CSS_SELECTOR, '[data-cy="rp-property-cd"]')

    for imovel in imoveis:
        if contador_imoveis >= limite:
            break

        try:
            metragem = imovel.find_element(By.CSS_SELECTOR, '[data-cy="rp-cardProperty-propertyArea-txt"] h3').text.strip()
        except:
            metragem = "Não Informado"
        try:
            quartos = imovel.find_element(By.CSS_SELECTOR, '[data-cy="rp-cardProperty-bedroomQuantity-txt"] h3').text.strip()
        except:
            quartos = "Não Informado"
        try:
            banheiros = imovel.find_element(By.CSS_SELECTOR, '[data-cy="rp-cardProperty-bathroomQuantity-txt"] h3').text.strip()
        except:
            banheiros = "Não Informado"
        try:
            vagas = imovel.find_element(By.CSS_SELECTOR, '[data-cy="rp-cardProperty-parkingSpacesQuantity-txt"] h3').text.strip()
        except:
            vagas = "Não Informado"
        try:
            nome_da_rua = imovel.find_element(By.CSS_SELECTOR, '[data-cy="rp-cardProperty-street-txt"]').text.strip()
        except:
            nome_da_rua = "Não Informado"
        try:
            bairro_e_cidade = imovel.find_element(By.CSS_SELECTOR, '[data-cy="rp-cardProperty-location-txt"]').text.strip()
        except:
            bairro_e_cidade = "Não Informado"
        try:
            elemento = imovel.find_element(By.CSS_SELECTOR,'[data-cy="rp-cardProperty-price-txt"]')
            paragrafos = elemento.find_elements(By.TAG_NAME,'p')
            item1 = paragrafos[0].text.strip() if len(paragrafos) > 0 else None 
            item2 = paragrafos[1].text.strip() if len(paragrafos) > 1 else None
        except Exception as e:
            print(f"Erro: {e}")
            item1 = None
            item2 = None
            
        print({bairro_e_cidade})

        dic_imoveis["Metragem"].append(metragem)
        dic_imoveis["Quartos"].append(quartos)
        dic_imoveis["Banheiros"].append(banheiros)
        dic_imoveis["Vagas"].append(vagas)
        dic_imoveis["Valor"].append(item1)
        dic_imoveis["IPTU  E CONDOMÍNIO"].append(item2)
        dic_imoveis["Nome da Rua"].append(nome_da_rua)
        dic_imoveis["Bairro e Cidade"].append(bairro_e_cidade)

        contador_imoveis += 1

    try:
        proxima_pagina = driver.find_element(By.CSS_SELECTOR, '[data-testid="next-page"]')
        driver.execute_script("arguments[0].scrollIntoView();", proxima_pagina)
        driver.execute_script("arguments[0].click();", proxima_pagina)
        pagina_atual += 1
        time.sleep(5)
    except:
        print("Não foi possível avançar para a próxima página.")
        break

df = pd.DataFrame(dic_imoveis)
df.to_excel("imoveis_sao_caetano.xlsx", index=False)
print("Dados salvos com sucesso!")

driver.quit()
