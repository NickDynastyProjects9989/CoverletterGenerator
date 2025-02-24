# Use Python 3.10 as base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure Streamlit is installed
RUN pip install streamlit

# Load environment variables from .env
RUN echo "source /app/.env" >> ~/.bashrc

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["bash", "-c", "source /app/.env && streamlit run app.py --server.port=8501 --server.address=0.0.0.0"]

