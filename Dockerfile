# Use Python 3.10 as base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure Streamlit and AWS CLI are installed
RUN pip install streamlit awscli

# Expose Streamlit port
EXPOSE 8501

# Fetch API Key from AWS SSM at container runtime
CMD ["sh", "-c", "
    GROQ_API_KEY=$(aws ssm get-parameter --name 'GROQ_API_KEY' --with-decryption --query 'Parameter.Value' --output text) &&
    export GROQ_API_KEY &&
    streamlit run app.py --server.port=8501 --server.address=0.0.0.0
"]
