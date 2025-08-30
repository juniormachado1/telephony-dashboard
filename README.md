# Dashboard de Telefonia

Uma aplicação web full-stack para visualização de métricas de chamadas telefônicas, construída com **Python (FastAPI)** e **React**, totalmente containerizada com **Docker**.

---

## Tabela de Conteúdos
- [Dashboard de Telefonia](#dashboard-de-telefonia)
  - [Tabela de Conteúdos](#tabela-de-conteúdos)
  - [Sobre o Projeto](#sobre-o-projeto)
  - [Arquitetura](#arquitetura)
  - [Funcionalidades Implementadas](#funcionalidades-implementadas)
  - [Stack de Tecnologias](#stack-de-tecnologias)
    - [Backend](#backend)
    - [Frontend](#frontend)
    - [DevOps](#devops)
  - [Começando](#começando)
    - [Pré-requisitos](#pré-requisitos)
    - [Instalação](#instalação)
    - [Uso da Aplicação](#-uso-da-aplicação)
    - [Criando o Primeiro Usuário](#criando-o-primeiro-usuário)
    - [Rodando os Testes](#rodando-os-testes)
  - [Documentação da API](#-documentação-da-api)

---

## Sobre o Projeto
Este projeto foi desenvolvido como uma solução completa para um case técnico, com o objetivo de construir uma aplicação web que consome dados de uma API de chamadas telefônicas, armazena esses dados, gerencia usuários e exibe as informações em um **dashboard interativo**.

A aplicação é dividida em um backend robusto em **Python** e um frontend reativo em **React**, seguindo as melhores práticas de desenvolvimento, segurança e arquitetura de software.

---

## Arquitetura
O projeto é orquestrado com **Docker Compose** e consiste em **três serviços containerizados independentes**:

- **db (PostgreSQL):** Banco de dados relacional responsável pela persistência de dados de usuários e chamadas.  
- **api (FastAPI):** Backend em Python, responsável pela lógica de negócio, autenticação, comunicação com o banco e fornecimento da API RESTful.  
- **web (React + Nginx):** Frontend em React (construído com Vite e TypeScript), servido por um servidor Nginx leve em produção.  

Fluxo de Comunicação:
```
(Navegador do Usuário) ↔️ [web: React App] ↔️ [api: FastAPI] ↔️ [db: PostgreSQL]
```

---

## Funcionalidades Implementadas
- Backend robusto com **Python 3.12** & **FastAPI**
- Frontend moderno com **React 18**, **TypeScript** & **Vite**
- Autenticação de usuários com **JWT**
- CRUD de Usuários (somente para administradores)
- Ingestão de dados de API externa simulada
- Cálculo de métricas e KPIs (ASR, ACD, etc.)
- Dashboard com KPIs, gráfico temporal e tabela paginada
- Testes automatizados com **Pytest**
- Ambiente 100% containerizado com **Docker**

---

## Stack de Tecnologias

### Backend
- **Framework:** FastAPI
- **Banco de Dados:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migrações:** Alembic
- **Validação:** Pydantic
- **Testes:** Pytest, Pytest-Mock
- **Autenticação:** Passlib, Python-JOSE

### Frontend
- **Biblioteca:** React 18
- **Linguagem:** TypeScript
- **Build Tool:** Vite
- **UI:** Material-UI (MUI)
- **Roteamento:** React Router
- **Estado:** Zustand
- **HTTP Client:** Axios
- **Gráficos:** Recharts

### DevOps
- **Containerização:** Docker, Docker Compose

---

## Começando

### Pré-requisitos
Certifique-se de ter instalado:
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/juniormachado1/telephony-dashboard
```

2. **Entre na pasta do projeto:**
```bash
cd telephony-dashboard
```

3. **Crie o arquivo `.env`:**
```bash
# Configurações do PostgreSQL
POSTGRES_USER=admin
POSTGRES_PASSWORD=supersecret
POSTGRES_DB=telephony

# Configurações da API Backend
SECRET_KEY="uma_chave_secreta_super_forte_para_jwt_pode_ser_qualquer_coisa"
DATABASE_URL=postgresql://admin:supersecret@db:5432/telephony

# Configuração do Banco de Dados de Teste
TEST_DATABASE_URL=postgresql://admin:supersecret@db:5432/test_db
```

4. **Suba os contêineres:**
```bash
docker compose up -d --build
```

---

### Uso da Aplicação

Após subir os contêineres, acesse:  
- Frontend (Dashboard): [http://localhost:3000](http://localhost:3000)  
- Backend (API Docs): [http://localhost:8000/docs](http://localhost:8000/docs)

---

###  Criando o Primeiro Usuário

Crie um superusuário para acessar o sistema:
```bash
docker compose exec api python -m app.scripts.create_superuser admin@superuser.com adminpassword
```

Credenciais:
```
Email: admin@superuser.com
Senha: adminpassword
```

---

###  Rodando os Testes

```bash
docker compose run --rm api pytest app/tests
```

---

## Documentação da API

A documentação é gerada automaticamente pelo **FastAPI** em **Swagger UI**:  
 [http://localhost:8000/docs](http://localhost:8000/docs)

---



