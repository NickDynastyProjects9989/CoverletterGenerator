# Use Python 3.10 as base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure Streamlit is installed
RUN pip install streamlit awscli

# Retrieve API key from AWS SSM Parameter Store at runtime
ENV AWS_REGION=us-east-1
RUN echo 'export GROQ_API_KEY=$(aws ssm get-parameter --name "GROQ_API_KEY" --with-decryption --query "Parameter.Value" --output text)' >> ~/.bashrc

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["bash", "-c", "source ~/.bashrc && streamlit run app.py --server.port=8501 --server.address=0.0.0.0"]
