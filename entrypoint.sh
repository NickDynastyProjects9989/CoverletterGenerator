#!/bin/sh

# Fetch API Key from AWS SSM
export GROQ_API_KEY=$(aws ssm get-parameter --name "GROQ_API_KEY" --with-decryption --query "Parameter.Value" --output text)

# Run Streamlit App
exec streamlit run app.py --server.port=8501 --server.address=0.0.0.0
