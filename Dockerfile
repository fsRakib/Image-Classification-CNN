# Multi-stage Dockerfile for Cat vs Dog Classifier
# This creates a production-ready Docker image for both API and Streamlit app

# Base stage with Python and common dependencies
FROM python:3.11-slim AS base

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# ============================================
# API Stage (FastAPI Backend)
# ============================================
FROM base AS api

# Copy API requirements
COPY requirements-api.txt .

# Install API dependencies
RUN pip install --no-cache-dir -r requirements-api.txt

# Copy necessary files
COPY api.py .
COPY dogs_vs_cats_production_model.keras . 

# Expose API port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run FastAPI with uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

# ============================================
# Streamlit App Stage (Frontend)
# ============================================
FROM base AS streamlit

# Copy both requirements files
COPY requirements.txt .
COPY requirements-api.txt .

# Install all dependencies (Streamlit + API client needs)
RUN pip install --no-cache-dir -r requirements.txt -r requirements-api.txt

# Copy application files
COPY streamlit_app.py .
COPY api_client.py .
COPY dogs_vs_cats_production_model.keras .

# Expose Streamlit port
EXPOSE 8501

# Health check for Streamlit
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# ============================================
# Production Full-Stack Stage (API + Streamlit)
# ============================================
FROM base AS fullstack

# Install supervisor to manage multiple processes
RUN apt-get update && apt-get install -y --no-install-recommends \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Copy both requirements files
COPY requirements.txt .
COPY requirements-api.txt .

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt -r requirements-api.txt

# Copy all application files
COPY api.py .
COPY streamlit_app.py .
COPY api_client.py .
COPY dogs_vs_cats_production_model.keras .

# Create supervisor configuration
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose both ports
EXPOSE 8000 8501

# Run supervisor to manage both services
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
