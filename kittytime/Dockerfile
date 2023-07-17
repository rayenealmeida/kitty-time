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

# Instalar o Django
RUN pip install django

# Copiar o projeto Django para o diretório de trabalho do contêiner
COPY . /code/

# Executar as migrações do Django
RUN python manage.py migrate

# Coletar arquivos estáticos (opcional)
# RUN python manage.py collectstatic --noinput

# Iniciar o servidor de desenvolvimento do Django (substitua por um servidor de produção na implantação real)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
