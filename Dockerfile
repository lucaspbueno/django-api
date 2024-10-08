# Use uma imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código da aplicação para o diretório de trabalho
COPY . .

# Copie o script de inicialização
COPY entrypoint.sh .

# Torne o entrypoint executável dentro do contêiner
RUN chmod +x entrypoint.sh

# Exponha a porta que a aplicação vai rodar
EXPOSE 8000

# Defina o comando para rodar o servidor Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]