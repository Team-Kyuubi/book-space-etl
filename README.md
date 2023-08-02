# ETL Book Space

Este repositório possui os códigos utilizados para realizar o processo de ETL da aplicação Book Space.

Etapas realizadas:

* Extract
  * Realizado o web scraping no site da Amazon utilizando Selenium
* Transform
  * Realizado o pré-processamento dos dados coletados via web scraping. Foi utilizada a biblioteca Pandas do Python
* Load
  * Realiado a integração com o banco de dados MongoDB para carregar os dados em um banco de dados localhost para testes

## Executar o banco de dados com Docker
1. Iniciar o Docker
2. Abrir um terminal
3. Executar o comando:
```bash
docker run -d --name mongo-db -p 27017:27017 -v "<path_raiz_do_projeto\docker-volume>":/data/db mongo:7.0.0-rc8-jammy
```