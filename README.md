## Descrição
Esta aplicação fornece API HTTP REST, recebendo registros de Feedstock (insumos) e Composition (composições) inserindo as
informações no banco de dados para disponibilização de um catalogo de Insumos e Serviços que auxiliará na criação de Orçamento

## USO
Para executar essa aplicação, você precisará de:
* python 3.9+

(Somente para caso de Execução via Docker)
* Docker
* docker-compose

### Executar a aplicação localmente (Sem Docker):
1. Clone esse repositório.
2. Execute a instrução: `make init`
3. Inicialize o ambiente virtual com o comando: `poetry shell`
4. Execute a instrução `make migrate` no terminal para criar o banco
5. Execute a instrução `make run` para inicializar o servidor

### Executar a aplicação localmente (com Docker):
1. Executar o comando `docker-compose up`

### Testando a aplicação:
Para testar, basta executar a instrução `make test` no terminal


***
Obs:
* A autenticação da aplicação é feita através do e-mail e da senha do Revendedor cadastrado.
* Só é possível cadastrar um único usuario por email
