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

## Update de Produto
O update do produto é nomeado, caso queira atualizar somente o nome, basta passar para a controller de produto o ID do produto e o campo name.
Caso queira atualizar somente o estoque ou o preço basta informar somente os parametros "actual_price" ou "actual_stock", as DAOs de price e 
stock nunca devem ser chamadas fora desse contexto pois irá "bagunçar" o histórico.
O Update irá presumir que as categorias serão reenviadas, caso seja enviado nenhuma categoria ele permancerá com as antigas, se enviado somente
uma categoria as antigas serão apagadas.

## Deletar Produto
Não é possível deletar um produto por regra de negócio, ao chamar a função delete da controller de produto ela irá somente atualizar o campo
"active" do produto para false. Produtos inativos serão listados apenas caso efetuado busca por ID.