# Dockerfile

# Use a imagem Python como base
FROM python:3

# Configuração do ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Diretório de trabalho dentro do contêiner
WORKDIR /code

# Instalar dependências do projeto
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copiar o projeto Django para o diretório de trabalho do contêiner
COPY . /code/
