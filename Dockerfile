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

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Run the script
ENTRYPOINT ["/entrypoint.sh"]
