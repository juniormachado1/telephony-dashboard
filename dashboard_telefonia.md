Dashboard de Telefonia Uma aplicação web full-stack para visualização de
métricas de chamadas telefônicas, construída com Python (FastAPI) e
React, totalmente containerizada com Docker.

Tabela de Conteúdos Sobre o Projeto

Arquitetura

Funcionalidades Implementadas

Stack de Tecnologias

Começando

Pré-requisitos

Instalação

Uso da Aplicação

Acessando os Serviços

Criando o Primeiro Usuário

Rodando os Testes

Documentação da API

Licença

Sobre o Projeto Este projeto foi desenvolvido como uma solução completa
para um case técnico, com o objetivo de construir uma aplicação web que
consome dados de uma API de chamadas telefônicas, armazena esses dados,
gerencia usuários e exibe as informações em um dashboard interativo.

A aplicação é dividida em um backend robusto em Python e um frontend
reativo em React, seguindo as melhores práticas de desenvolvimento,
segurança e arquitetura de software.

Arquitetura O projeto é orquestrado com Docker Compose e consiste em
três serviços containerizados independentes:

db (PostgreSQL): O banco de dados relacional responsável pela
persistência dos dados de usuários e chamadas.

api (FastAPI): O backend em Python, responsável pela lógica de negócio,
autenticação, comunicação com o banco de dados e por servir a API
RESTful para o frontend.

web (React + Nginx): O frontend em React (construído com Vite e
TypeScript), servido de forma otimizada por um servidor Nginx leve em
produção.

O fluxo de comunicação é o seguinte:

(Navegador do Usuário) ↔️ \[web: React App\] ↔️ \[api: FastAPI\] ↔️
\[db: PostgreSQL\]

Funcionalidades Implementadas ✅ Backend robusto com Python 3.12 &
FastAPI.

✅ Frontend moderno com React 18, TypeScript & Vite.

✅ Autenticação de Usuários com JWT (login com email e senha).

✅ CRUD de Usuários (acessível apenas por administradores).

✅ Ingestão de Dados de uma API externa simulada.

✅ Cálculo de Métricas e KPIs no backend (ASR, ACD, etc.).

✅ Dashboard com KPIs, Gráfico de Série Temporal e Tabela de Dados
paginada.

✅ Suíte de Testes Automatizados para o backend com Pytest (5 testes
cobrindo as principais funcionalidades).

✅ Ambiente 100% Containerizado com Docker, garantindo reprodutibilidade
e facilidade de setup.

Stack de Tecnologias Abaixo estão as principais tecnologias e
bibliotecas utilizadas no projeto:

Backend Framework: FastAPI

Banco de Dados: PostgreSQL

ORM: SQLAlchemy

Migrações: Alembic

Validação: Pydantic

Testes: Pytest, Pytest-Mock

Autenticação: Passlib (para hashing), Python-JOSE (para JWT)

Frontend Biblioteca: React 18

Linguagem: TypeScript

Build Tool: Vite

Componentes de UI: MUI (Material-UI)

Roteamento: React Router

Gerenciamento de Estado: Zustand

Cliente HTTP: Axios

Gráficos: Recharts

DevOps Containerização: Docker, Docker Compose

Começando Siga os passos abaixo para ter uma cópia do projeto rodando
localmente.

Pré-requisitos Você precisa ter as seguintes ferramentas instaladas na
sua máquina:

Git

Docker

Docker Compose

Instalação Clone o repositório:

Bash

git clone `<URL_DO_SEU_REPOSITORIO>`{=html} Navegue até a pasta do
projeto:

Bash

cd telephony-dashboard Crie o arquivo de variáveis de ambiente: Crie um
arquivo chamado .env na raiz do projeto e cole o seguinte conteúdo.

Snippet de código

# Configurações do PostgreSQL

POSTGRES_USER=admin POSTGRES_PASSWORD=supersecret POSTGRES_DB=telephony

# Configurações da API Backend

SECRET_KEY="uma_chave_secreta_super_forte_para_jwt_pode_ser_qualquer_coisa"
DATABASE_URL=postgresql://admin:supersecret@db:5432/telephony

# Configuração do Banco de Dados de Teste

TEST_DATABASE_URL=postgresql://admin:supersecret@db:5432/test_db
Construa e inicie os contêineres: Este comando irá construir as imagens
do backend e frontend e iniciar todos os serviços em segundo plano.

Bash

docker compose up -d --build Uso da Aplicação Após a conclusão do passo
anterior, o ambiente completo estará no ar.

Acessando os Serviços Frontend (Dashboard): http://localhost:3000

Backend (Documentação da API): http://localhost:8000/docs

Criando o Primeiro Usuário (Admin) Para poder fazer login, você precisa
criar o primeiro usuário administrador. Execute o seguinte comando no
seu terminal:

Bash

docker compose exec api python -m app.scripts.create_superuser
admin@superuser.com adminpassword Email: admin@superuser.com

Senha: adminpassword

Agora você pode usar essas credenciais para fazer login na aplicação em
http://localhost:3000.

Rodando os Testes Para rodar a suíte de testes automatizados do backend,
use o comando docker compose run. Ele cria um contêiner limpo para
garantir que os testes sejam isolados.

Bash

docker compose run --rm api pytest app/tests Você verá a saída do
Pytest, que deve indicar que os 5 testes passaram com sucesso.

Documentação da API A documentação da API é gerada automaticamente pelo
FastAPI e está disponível em formato Swagger UI. Você pode usá-la para
explorar e interagir com todos os endpoints de forma visual.

URL da Documentação: http://localhost:8000/docs


