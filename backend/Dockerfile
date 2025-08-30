# Usa a imagem oficial e correta do Python 3.12, versão 'slim' por ser menor.
FROM python:3.12-slim

# Define variáveis de ambiente para otimizar a execução do Python em contêineres.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho padrão dentro do contêiner.
WORKDIR /home/app

# Cria um grupo de sistema 'app' e um usuário de sistema 'app' sem privilégios de root.
RUN addgroup --system app && adduser --system --group app

# Atualiza o pip para a versão mais recente para garantir compatibilidade.
RUN pip install --upgrade pip

# Copia e instala as dependências de PRODUÇÃO.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia e instala as dependências de DESENVOLVIMENTO (necessárias para os testes).
COPY dev-requirements.txt .
RUN pip install --no-cache-dir -r dev-requirements.txt

# Copia todo o código da aplicação do seu computador para o diretório de trabalho no contêiner.
# O .dockerignore garante que pastas como '.venv' não sejam copiadas.
COPY . .

# Altera o proprietário de todos os arquivos para o nosso usuário não-root.
RUN chown -R app:app /home/app

# Muda o usuário padrão do contêiner para o nosso usuário com menos privilégios.
USER app

# Inicia o servidor Uvicorn para nossa aplicação FastAPI.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
