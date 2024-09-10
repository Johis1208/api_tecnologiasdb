# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar los archivos de la aplicación
COPY . .

# Exponer el puerto para Streamlit
EXPOSE 8502

# Comando para ejecutar la aplicación Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8502", "--server.address=0.0.0.0"]
#streamlit run app.py --server.port=8502 --server.address=0.0.0.0