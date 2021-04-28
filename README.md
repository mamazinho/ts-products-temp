TS-PRODUCTS_TEMP

## O Projeto está com dados de exemplo dentro do arquivo main.py, ou seja:
    $ python3 main.py

## Tecnologias
O projeto está usando o SQLAlchemy sem o Flask

## Como funciona
A conexão com o banco de dados ficam dentro das DAOs, no mesmo estilo usando o 'with' juntamente de __enter__ e __exit__ na classe Database
o arquivo settings.py possui alguma 'constantes' do projeto, como a declaração de engine do SQLAlchemy e do Base, usados dentro das models
Os aquivos de DAO são usados pelas controllers, que recebem parametros individuais e os agrupam no formato esperado pelas DAOs,
dentro de produto existe todo o controle de estoque e preço (que são as tabelas relacionadas).