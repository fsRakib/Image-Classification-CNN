# 🐾 Cat vs Dog AI - Deep Learning Image Classifier

> **A production-ready deep learning application that classifies images as cats or dogs with ~92% accuracy.**  
> Choose between a beautiful **Streamlit web app** for end-users or a powerful **FastAPI REST API** for seamless integration with any application.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20+-orange.svg)](https://www.tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 Table of Contents

- [✨ Features](#-features)
- [🎬 Demo](#-demo)
- [🚀 Quick Start](#-quick-start)
  - [Prerequisites](#prerequisites)
  - [Clone & Setup](#-clone-the-repository)
  - [Web Application (Streamlit)](#1️⃣-web-application-streamlit)
  - [REST API (FastAPI)](#2️⃣-rest-api-fastapi)
  - [Docker Deployment](#3️⃣-docker-deployment-recommended)
- [📡 API Documentation](#-api-documentation)
  - [Available Endpoints](#available-endpoints)
  - [Response Format](#response-format)
  - [Error Handling](#error-handling)
- [💡 Usage Examples](#-usage-examples)
  - [Python Integration](#python-requests)
  - [JavaScript/React](#javascript-fetch-api)
  - [Mobile Apps](#mobile-flutterdart)
  - [cURL Commands](#curl)
- [🏗️ Model Architecture](#️-model-architecture)
- [🔄 Project Workflow](#-project-workflow)
- [📁 Project Structure](#-project-structure)
- [🔧 Technologies & Deployment](#-technologies-used)
- [🐛 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)
- [📧 Contact](#-contact)

---

## ✨ Features

### 🎯 **Two Powerful Interfaces - Choose What Fits Your Needs**

| Feature                      | Web App (Streamlit)       | REST API (FastAPI)                    |
| ---------------------------- | ------------------------- | ------------------------------------- |
| **User Interface**           | ✅ Interactive web UI     | ❌ API only (integrate with your app) |
| **Real-time Classification** | ✅ Instant visual results | ✅ JSON response                      |
| **Batch Processing**         | ❌ One image at a time    | ✅ Up to 10 images per request        |
| **Integration**              | ❌ Standalone app         | ✅ Any language/platform              |
| **Auto Documentation**       | ❌ N/A                    | ✅ Swagger UI + ReDoc                 |
| **Mobile Friendly**          | ✅ Responsive design      | ✅ Mobile apps can integrate          |
| **Docker Support**           | ✅ Available              | ✅ Production-ready                   |
| **Best For**                 | End-users, demos          | Developers, production systems        |

### 🎨 **Web Application Highlights**

- 🖼️ **Modern UI** with gradient animations and smooth transitions
- 🎯 **Drag-and-drop** image upload with instant preview
- 📊 **Confidence meters** with visual progress bars
- 📱 **Mobile responsive** design that works everywhere
- ⚡ **Auto model download** from Google Drive (111 MB, cached locally)
- 🚀 **Fast inference** ~100-300ms per image
- 🎨 **Animated result cards** color-coded by prediction (orange for cats, blue for dogs)
- 📈 **Detailed metrics** expandable technical information

### 🔌 **REST API Highlights**

- 🌐 **RESTful endpoints** following industry best practices
- 📦 **Batch prediction** process up to 10 images in one request
- 🔓 **CORS enabled** ready for web and mobile apps
- ✅ **Input validation** file type, size, and format checks
- 💚 **Health checks** monitor API and model status
- 🛡️ **Production-ready** with comprehensive logging and error handling
- 📚 **Interactive docs** Swagger UI at `/docs` and ReDoc at `/redoc`
- ⚡ **Async support** high-performance with uvicorn/gunicorn
- 🐳 **Docker ready** containerized for easy deployment
- 📊 **Detailed responses** confidence scores, probabilities, and metadata

---

## 🎬 Demo

### Web Application

![Streamlit Demo](https://via.placeholder.com/800x400?text=Streamlit+Web+App+Demo)

### API Response Example

```json
{
  "prediction": "Cat",
  "confidence_percentage": 92.15,
  "probabilities": {
    "cat": 92.15,
    "dog": 7.85
  }
}
```

---

## 🚀 Quick Start

### 🐳 Easiest Way: Docker (Recommended for Testers)

**No Python installation required! Just one command:**

```bash
docker run -d -p 8000:8000 -p 8501:8501 --name catdog-app fsrakib/image-classification-cnn:latest
```

Then open: **http://localhost:8501** 🎉

**Requirements:** Only [Docker Desktop](https://www.docker.com/products/docker-desktop) installed

👉 [Jump to Docker Deployment Section](#3️⃣-docker-deployment-recommended)

---

### 🐍 Alternative: Manual Setup (For Developers)

### Prerequisites

Before you begin, ensure you have:

- ✅ **Python 3.8 or higher** installed ([Download Python](https://www.python.org/downloads/))
- ✅ **pip** package manager (comes with Python)
- ✅ **Internet connection** (required for first-time model download - 111 MB)
- ✅ **Git** for cloning the repository ([Download Git](https://git-scm.com/downloads))

### 📥 Clone the Repository

```bash
git clone https://github.com/fsRakib/Image-Classification-CNN.git
cd Image-Classification-CNN
```

### 🔧 Create Virtual Environment (Recommended)

Creating a virtual environment keeps dependencies isolated and prevents conflicts with other projects.

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**

```bash
python -m venv venv
source venv/bin/activate
```

**You should see `(venv)` in your terminal prompt after activation.**

---

## 1️⃣ Web Application (Streamlit)

**Perfect for:** End-users, demos, quick testing, and visual presentations

### Install Dependencies

```bash
pip install -r requirements.txt
```

**This installs:**

- `streamlit` - Web application framework
- `tensorflow` - Deep learning framework
- `pillow` - Image processing
- `numpy` - Numerical operations
- `gdown` - Google Drive downloader

### Run the Application

```bash
streamlit run streamlit_app.py
```

**You'll see output like:**

```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.100:8501
```

### How to Use the Web App

1. 🌐 **Open your browser** to `http://localhost:8501`
2. 📤 **Upload an image** (JPG, JPEG, or PNG) using the file uploader
3. ⏱️ **Wait for analysis** (~100-300ms)
4. 📊 **View results** with:
   - Prediction label (Cat 🐱 or Dog 🐕)
   - Confidence percentage with visual meter
   - Animated result card (orange for cat, blue for dog)
   - Expandable technical details

**Visual Flow:**

```
Upload Image → Auto Preprocess → CNN Prediction → Beautiful Results
   🖼️              ⚙️                 🧠               ✨
```

### Features You'll Love

- **Instant feedback** - No page reloads needed
- **Clear visualizations** - Confidence bars and probability charts
- **Detailed metadata** - Image size, mode, processing info
- **Error handling** - Helpful messages if something goes wrong
- **Model auto-download** - First run downloads model automatically

---

## 2️⃣ REST API (FastAPI)

**Perfect for:** Developers, production systems, mobile apps, integration with existing applications

### Install Dependencies

```bash
pip install -r requirements-api.txt
```

**This installs:**

- `fastapi` - Modern web framework for APIs
- `uvicorn` - Lightning-fast ASGI server
- `python-multipart` - File upload support
- `tensorflow` - Deep learning framework
- `pillow` - Image processing
- `numpy` - Numerical operations
- `gdown` - Google Drive downloader

### Run the API Server

**Option 1: Direct Python execution**

```bash
python api.py
```

**Option 2: Using uvicorn (recommended for development)**

```bash
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

The `--reload` flag enables auto-restart on code changes.

**Option 3: Using helper scripts**

```powershell
# Windows PowerShell
.\start_api.ps1

# Linux/Mac
chmod +x start_api.sh
./start_api.sh
```

**Option 4: Production deployment with Gunicorn**

```bash
pip install gunicorn
gunicorn api:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Access the API

Once running, you can access:

- 🌐 **API Base URL:** http://localhost:8000
- 📚 **Interactive Swagger Docs:** http://localhost:8000/docs
- 📖 **ReDoc Documentation:** http://localhost:8000/redoc
- 💚 **Health Check:** http://localhost:8000/health

### Quick Test the API

**Using the test script:**

```bash
python test_api_quick.py
```

**Using cURL:**

```bash
curl -X POST "http://localhost:8000/predict" -F "file=@cat.jpg"
```

**Using Python:**

```python
import requests

with open("cat.jpg", "rb") as f:
    response = requests.post("http://localhost:8000/predict", files={"file": f})
    result = response.json()
    print(f"{result['prediction']} - {result['confidence_percentage']}%")
```

**Expected Response:**

```json
{
  "success": true,
  "filename": "cat.jpg",
  "prediction": "Cat",
  "confidence_percentage": 92.15,
  "probabilities": {
    "cat": 92.15,
    "dog": 7.85
  }
}
```

---

## 3️⃣ Docker Deployment (Recommended)

**Perfect for:** Production environments, cloud deployments, testers, ensuring consistency across different platforms

### Why Docker?

✅ **"Works Everywhere"** - Same environment on Windows, Linux, Mac, and Cloud  
✅ **No Dependency Hell** - All packages pre-installed in container  
✅ **Isolated Environment** - No conflicts with other projects  
✅ **One-Command Setup** - No Python installation needed  
✅ **Easy Scaling** - Deploy multiple instances instantly  
✅ **Cloud-Ready** - Deploy to AWS, GCP, Azure, Heroku in minutes  
✅ **Version Control** - Container images are versioned and reproducible

---

### 🚀 Quick Start for Testers (Easiest Method)

**No Python installation required! Just Docker.**

#### Step 1: Install Docker

Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop) for your operating system.

#### Step 2: Run the Application

Open your terminal/PowerShell and run this single command:

```bash
docker run -d -p 8000:8000 -p 8501:8501 --name catdog-app fsrakib/image-classification-cnn:latest
```

#### Step 3: Access the Application

Wait 30-60 seconds for services to start, then open your browser:

- 🌐 **Web Application:** http://localhost:8501
- 📚 **API Documentation:** http://localhost:8000/docs
- 💚 **API Health Check:** http://localhost:8000/health

#### Step 4: Test It!

1. Go to http://localhost:8501
2. Upload a cat or dog image
3. See the AI classification results instantly!

#### Managing the Container

```bash
# Check if container is running
docker ps

# View logs
docker logs catdog-app

# Stop the application
docker stop catdog-app

# Start again
docker start catdog-app

# Remove container
docker rm -f catdog-app
```

#### Troubleshooting

**If ports 8000 or 8501 are already in use:**

```bash
# Use different ports
docker run -d -p 9000:8000 -p 9501:8501 --name catdog-app fsrakib/image-classification-cnn:latest
```

Then access at: http://localhost:9501

**Container won't start?**

```bash
# Check logs for errors
docker logs catdog-app

# Try removing and running again
docker rm -f catdog-app
docker run -d -p 8000:8000 -p 8501:8501 --name catdog-app fsrakib/image-classification-cnn:latest
```

---

### 🛠️ For Developers: Build from Source

If you want to build the Docker image yourself:

#### Build the Full-Stack Image

```bash
# Clone the repository
git clone https://github.com/fsRakib/Image-Classification-CNN.git
cd Image-Classification-CNN

# Build the Docker image (takes 15-20 minutes)
docker build --target fullstack -t image-classification-cnn:latest .

# Run the container
docker run -d -p 8000:8000 -p 8501:8501 --name catdog-app image-classification-cnn:latest
```

#### Using Docker Compose

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

#### Access Your Application

- 🌐 **Web App:** http://localhost:8501
- 📚 **API Docs:** http://localhost:8000/docs
- 💚 **Health Check:** http://localhost:8000/health

### 📦 What's Inside the Docker Image?

The Docker image includes:

- ✅ Python 3.11 runtime
- ✅ FastAPI backend (API server on port 8000)
- ✅ Streamlit frontend (Web UI on port 8501)
- ✅ Pre-trained CNN model (111 MB)
- ✅ All required dependencies
- ✅ Supervisor process manager
- ✅ Health checks and auto-restart
- ✅ Optimized for production use

**Image Size:** ~1.5 GB  
**Download Time:** 5-15 minutes (depending on internet speed)  
**First Run:** May take 30-60 seconds to start services

### Docker Benefits Comparison

| Aspect            | Without Docker                     | With Docker                           |
| ----------------- | ---------------------------------- | ------------------------------------- |
| **Setup Time**    | 30-60 min (install dependencies)   | 2-5 min (just run one command)        |
| **Consistency**   | "Works on my machine" syndrome     | ✅ Works identically everywhere       |
| **Python Needed** | Yes, specific version required     | ❌ No Python installation needed      |
| **Dependencies**  | Manual pip install, conflicts      | ✅ Everything pre-packaged            |
| **Deployment**    | Manual setup on each server        | Single command deployment             |
| **Scaling**       | Configure each instance manually   | Auto-scaling ready with orchestration |
| **Updates**       | Update dependencies on each server | Pull new image, restart container     |
| **Rollback**      | Difficult, manual process          | Switch to previous container version  |

### 🔗 Docker Hub Repository

**Official Image:** [fsrakib/image-classification-cnn](https://hub.docker.com/r/fsrakib/image-classification-cnn)

```bash
# Pull the latest version
docker pull fsrakib/image-classification-cnn:latest

# Check image details
docker inspect fsrakib/image-classification-cnn:latest

# View image layers
docker history fsrakib/image-classification-cnn:latest
```

### 🌐 Production Deployment Options

The Docker image can be deployed to:

#### Cloud Platforms (One-Click Deploy)

- **Railway.app** - Free tier, easiest deployment ([Deploy Guide](https://railway.app))
- **Render.com** - Free tier available ([Deploy Guide](https://render.com))
- **Fly.io** - Global edge deployment ([Deploy Guide](https://fly.io))

#### Enterprise Cloud Platforms

- **AWS ECS/EKS** - Elastic Container Service or Kubernetes
- **Google Cloud Run** - Serverless container platform (2M free requests/month)
- **Azure Container Instances** - Simple container hosting
- **DigitalOcean App Platform** - Managed container deployment
- **Heroku** - Container registry deployment

#### Self-Hosted Options

- **Linux Server** - Any VPS with Docker installed
- **Kubernetes Cluster** - For advanced orchestration
- **Docker Swarm** - Built-in container orchestration

### � Testing Guide for Testers

#### What to Test

**Basic Functionality:**

- ✅ Upload clear cat images (various breeds)
- ✅ Upload clear dog images (various breeds)
- ✅ Check prediction accuracy
- ✅ Verify confidence scores
- ✅ Test response times

**Edge Cases:**

- ⚠️ Kittens and puppies (young animals)
- ⚠️ Blurry or low-quality images
- ⚠️ Partial views (only face/tail visible)
- ⚠️ Multiple animals in one image
- ⚠️ Black and white photos
- ⚠️ Drawings or cartoons

**Performance Testing:**

- Monitor prediction speed (~100-300ms expected)
- Test multiple consecutive uploads
- Check memory usage over time
- Verify application stability

**UI/UX Testing:**

- Check responsive design
- Test on different browsers
- Verify error messages are helpful
- Ensure smooth animations

#### How to Report Issues

If you find bugs or issues, please report them on [GitHub Issues](https://github.com/fsRakib/Image-Classification-CNN/issues) with:

1. **What you did:** Description of actions taken
2. **What you expected:** Expected behavior
3. **What happened:** Actual behavior
4. **Screenshot:** If applicable
5. **Docker logs:** Output from `docker logs catdog-app`
6. **Environment:** Browser, OS version
7. **Image used:** If possible, attach the test image

---

## � API Documentation

### Available Endpoints

The FastAPI server provides five main endpoints for different operations:

| Endpoint         | Method | Description                             | Auth Required |
| ---------------- | ------ | --------------------------------------- | ------------- |
| `/`              | GET    | API information and available endpoints | No            |
| `/health`        | GET    | Health check and model status           | No            |
| `/model/info`    | GET    | Detailed model information              | No            |
| `/predict`       | POST   | Single image prediction                 | No            |
| `/predict/batch` | POST   | Batch predictions (up to 10 images)     | No            |

### 1. Root Endpoint - API Information

Get basic API information and discover available endpoints.

**Request:**

```http
GET /
```

**Response:**

```json
{
  "message": "Cat vs Dog Classifier API",
  "version": "1.0.0",
  "status": "active",
  "description": "Deep learning API for classifying images as cats or dogs",
  "endpoints": {
    "predict": "/predict (POST)",
    "batch_predict": "/predict/batch (POST)",
    "health": "/health (GET)",
    "model_info": "/model/info (GET)",
    "docs": "/docs (Interactive Swagger UI)",
    "redoc": "/redoc (ReDoc Documentation)"
  },
  "model": {
    "type": "CNN",
    "accuracy": "~92%",
    "input_size": "128x128 RGB"
  }
}
```

### 2. Health Check

Monitor API and model status - essential for production deployments.

**Request:**

```http
GET /health
```

**Response:**

```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_path": "dogs_vs_cats_production_model.keras",
  "model_exists": true,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Use Cases:**

- Load balancer health checks
- Monitoring and alerting
- Kubernetes liveness/readiness probes
- Service mesh integration

### 3. Model Information

Get detailed information about the loaded model.

**Request:**

```http
GET /model/info
```

**Response:**

```json
{
  "model_name": "Dogs vs Cats CNN Classifier",
  "model_type": "Convolutional Neural Network",
  "input_shape": [128, 128, 3],
  "output_classes": ["Cat", "Dog"],
  "model_size_mb": 111.24,
  "framework": "TensorFlow/Keras",
  "training_accuracy": "~92%",
  "supported_formats": ["jpg", "jpeg", "png"],
  "max_file_size_mb": 10,
  "preprocessing": {
    "resize": "128x128",
    "normalization": "0-1 range",
    "color_mode": "RGB"
  }
}
```

### 4. Single Image Prediction

Classify a single image and get detailed results.

**Request:**

```http
POST /predict
Content-Type: multipart/form-data

file: <image file>
```

**cURL Example:**

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -F "file=@cat_image.jpg"
```

**Python Example:**

```python
import requests

with open("cat.jpg", "rb") as f:
    response = requests.post(
        "http://localhost:8000/predict",
        files={"file": f}
    )
    print(response.json())
```

**Response:**

```json
{
  "success": true,
  "filename": "cat_image.jpg",
  "prediction": "Cat",
  "confidence_percentage": 87.34,
  "raw_score": 0.1266,
  "probabilities": {
    "cat": 87.34,
    "dog": 12.66
  },
  "metadata": {
    "image_size": [800, 600],
    "image_mode": "RGB",
    "model_input_size": [128, 128],
    "file_size_kb": 245.3,
    "processing_time_ms": 156
  }
}
```

**Response Fields Explained:**

- `success` - Boolean indicating if prediction was successful
- `filename` - Original filename of uploaded image
- `prediction` - Classification result ("Cat" or "Dog")
- `confidence_percentage` - Confidence level (0-100%)
- `raw_score` - Raw model output (0.0-1.0, where >0.5 = Dog)
- `probabilities` - Percentage breakdown for both classes
- `metadata` - Additional information about image and processing

### 5. Batch Prediction

Process multiple images in a single request (maximum 10 images).

**Request:**

```http
POST /predict/batch
Content-Type: multipart/form-data

files: <image file 1>
files: <image file 2>
files: <image file 3>
```

**cURL Example:**

```bash
curl -X POST "http://localhost:8000/predict/batch" \
  -F "files=@cat1.jpg" \
  -F "files=@dog1.jpg" \
  -F "files=@cat2.jpg"
```

**Python Example:**

```python
import requests

files = [
    ("files", open("cat1.jpg", "rb")),
    ("files", open("dog1.jpg", "rb")),
    ("files", open("cat2.jpg", "rb"))
]

response = requests.post(
    "http://localhost:8000/predict/batch",
    files=files
)
print(response.json())
```

**Response:**

```json
{
  "success": true,
  "total_images": 3,
  "successful_predictions": 3,
  "failed_predictions": 0,
  "processing_time_ms": 421,
  "results": [
    {
      "filename": "cat1.jpg",
      "success": true,
      "prediction": "Cat",
      "confidence_percentage": 92.15,
      "probabilities": {
        "cat": 92.15,
        "dog": 7.85
      }
    },
    {
      "filename": "dog1.jpg",
      "success": true,
      "prediction": "Dog",
      "confidence_percentage": 88.42,
      "probabilities": {
        "cat": 11.58,
        "dog": 88.42
      }
    },
    {
      "filename": "cat2.jpg",
      "success": true,
      "prediction": "Cat",
      "confidence_percentage": 95.67,
      "probabilities": {
        "cat": 95.67,
        "dog": 4.33
      }
    }
  ]
}
```

### Response Format

All successful responses follow this structure:

```json
{
  "success": true,
  "data": {
    /* endpoint-specific data */
  }
}
```

### Error Handling

The API returns standard HTTP status codes and descriptive error messages.

#### Common Error Codes

| Status Code | Meaning             | Typical Causes                              |
| ----------- | ------------------- | ------------------------------------------- |
| 200         | Success             | Request processed successfully              |
| 400         | Bad Request         | Invalid file type, missing file, size limit |
| 413         | Payload Too Large   | File exceeds 10MB limit                     |
| 500         | Internal Error      | Model loading failed, prediction error      |
| 503         | Service Unavailable | Model not loaded yet                        |

#### Error Response Format

**400 Bad Request - Invalid File Type:**

```json
{
  "detail": "Invalid file type. Allowed types: jpg, jpeg, png"
}
```

**400 Bad Request - No File Provided:**

```json
{
  "detail": "No file uploaded"
}
```

**413 Payload Too Large:**

```json
{
  "detail": "File too large. Maximum size: 10MB"
}
```

**500 Internal Server Error:**

```json
{
  "detail": "Prediction failed: [specific error message]"
}
```

**503 Service Unavailable:**

```json
{
  "detail": "Model not loaded. Please check server logs."
}
```

### Rate Limiting & Best Practices

**Recommendations for Production:**

1. **Implement Rate Limiting** - Prevent abuse and ensure fair usage
2. **Add Authentication** - Use API keys or JWT tokens
3. **Enable HTTPS** - Secure data transmission
4. **Configure CORS** - Restrict allowed origins
5. **Monitor Performance** - Track response times and errors
6. **Set Up Logging** - Log all requests for debugging and analytics

**Example Rate Limiting Configuration (using slowapi):**

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/predict")
@limiter.limit("100/hour")  # 100 requests per hour
async def predict_image(request: Request, file: UploadFile):
    # ... prediction logic
```

### Interactive API Documentation

FastAPI automatically generates interactive documentation:

**Swagger UI** (`/docs`):

- Try out endpoints directly in browser
- See request/response schemas
- Test with your own images
- View all available operations

**ReDoc** (`/redoc`):

- Clean, readable documentation
- Better for reference and sharing
- Printable format
- Detailed schema descriptions

### CORS Configuration

The API is configured to allow cross-origin requests from all origins (`*`). For production, restrict this:

```python
# In api.py, modify the CORS middleware:
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://yourdomain.com",
        "https://app.yourdomain.com",
        "http://localhost:3000"  # For local development
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

---

## 💡 Usage Examples

Integrate the Cat vs Dog Classifier API into your applications with these examples across different languages and platforms.

### Python (requests)

The most straightforward way to use the API in Python applications.

```python
import requests
import json

# Base URL
API_URL = "http://localhost:8000"

# 1. Health Check
def check_health():
    response = requests.get(f"{API_URL}/health")
    print("Health Status:", response.json())

# 2. Get Model Info
def get_model_info():
    response = requests.get(f"{API_URL}/model/info")
    info = response.json()
    print(f"Model: {info['model_name']}")
    print(f"Accuracy: {info['training_accuracy']}")

# 3. Single Image Prediction
def predict_single(image_path):
    with open(image_path, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{API_URL}/predict", files=files)

    result = response.json()
    if result["success"]:
        print(f"Prediction: {result['prediction']}")
        print(f"Confidence: {result['confidence_percentage']}%")
        print(f"Probabilities: {result['probabilities']}")
    else:
        print(f"Error: {result.get('detail', 'Unknown error')}")

# 4. Batch Prediction
def predict_batch(image_paths):
    files = [("files", open(path, "rb")) for path in image_paths]
    response = requests.post(f"{API_URL}/predict/batch", files=files)

    result = response.json()
    print(f"Processed {result['total_images']} images:")
    for item in result["results"]:
        print(f"  {item['filename']}: {item['prediction']} ({item['confidence_percentage']}%)")

    # Close all files
    for _, file in files:
        file.close()

# Usage
if __name__ == "__main__":
    check_health()
    get_model_info()
    predict_single("cat.jpg")
    predict_batch(["cat1.jpg", "dog1.jpg", "cat2.jpg"])
```

### JavaScript (Fetch API)

For web applications and Node.js backends.

```javascript
// Configuration
const API_URL = "http://localhost:8000";

// 1. Health Check
async function checkHealth() {
  const response = await fetch(`${API_URL}/health`);
  const data = await response.json();
  console.log("Health:", data);
}

// 2. Single Image Prediction
async function predictImage(fileInput) {
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const response = await fetch(`${API_URL}/predict`, {
    method: "POST",
    body: formData,
  });

  const result = await response.json();

  if (result.success) {
    console.log(`${result.prediction} - ${result.confidence_percentage}%`);
    return result;
  } else {
    throw new Error(result.detail);
  }
}

// 3. Batch Prediction
async function predictBatch(fileList) {
  const formData = new FormData();

  for (let file of fileList) {
    formData.append("files", file);
  }

  const response = await fetch(`${API_URL}/predict/batch`, {
    method: "POST",
    body: formData,
  });

  const result = await response.json();
  return result.results;
}

// 4. With Error Handling
async function safePredictImage(file) {
  try {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(`${API_URL}/predict`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || "Prediction failed");
    }

    return await response.json();
  } catch (error) {
    console.error("Error:", error.message);
    return null;
  }
}
```

### React Component

Complete React component with file upload and results display.

```jsx
import { useState } from "react";

function CatDogClassifier() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const API_URL = "http://localhost:8000";

  const handleFileSelect = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      setPreview(URL.createObjectURL(file));
      setResult(null);
      setError(null);
    }
  };

  const handlePredict = async () => {
    if (!selectedFile) return;

    setLoading(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append("file", selectedFile);

      const response = await fetch(`${API_URL}/predict`, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || "Prediction failed");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="classifier-container">
      <h1>🐱🐕 Cat vs Dog Classifier</h1>

      {/* File Upload */}
      <div className="upload-section">
        <input
          type="file"
          accept="image/jpeg,image/jpg,image/png"
          onChange={handleFileSelect}
        />
        <button onClick={handlePredict} disabled={!selectedFile || loading}>
          {loading ? "Analyzing..." : "Classify Image"}
        </button>
      </div>

      {/* Preview */}
      {preview && (
        <div className="preview">
          <img src={preview} alt="Preview" style={{ maxWidth: "400px" }} />
        </div>
      )}

      {/* Loading */}
      {loading && <div className="loading">🔄 Analyzing image...</div>}

      {/* Error */}
      {error && <div className="error">❌ Error: {error}</div>}

      {/* Results */}
      {result && result.success && (
        <div className={`result ${result.prediction.toLowerCase()}`}>
          <h2>
            {result.prediction === "Cat" ? "🐱" : "🐕"} {result.prediction}!
          </h2>
          <div className="confidence">
            <div className="confidence-bar">
              <div
                className="confidence-fill"
                style={{ width: `${result.confidence_percentage}%` }}
              />
            </div>
            <p>Confidence: {result.confidence_percentage}%</p>
          </div>
          <div className="probabilities">
            <p>🐱 Cat: {result.probabilities.cat}%</p>
            <p>🐕 Dog: {result.probabilities.dog}%</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default CatDogClassifier;
```

### cURL

Command-line examples for testing and automation.

```bash
# Health Check
curl http://localhost:8000/health

# Model Information
curl http://localhost:8000/model/info

# Single Prediction
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -F "file=@cat_image.jpg"

# Batch Prediction
curl -X POST "http://localhost:8000/predict/batch" \
  -F "files=@cat1.jpg" \
  -F "files=@dog1.jpg" \
  -F "files=@cat2.jpg"

# Save Response to File
curl -X POST "http://localhost:8000/predict" \
  -F "file=@image.jpg" \
  -o result.json

# Pretty Print JSON Response (with jq)
curl -X POST "http://localhost:8000/predict" \
  -F "file=@image.jpg" | jq '.'
```

### Mobile (Flutter/Dart)

For Flutter mobile applications on iOS and Android.

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:io';

class CatDogClassifierService {
  static const String baseUrl = 'http://localhost:8000';

  // Single Image Prediction
  Future<Map<String, dynamic>> predictImage(File imageFile) async {
    try {
      var request = http.MultipartRequest(
        'POST',
        Uri.parse('$baseUrl/predict'),
      );

      // Add file
      request.files.add(
        await http.MultipartFile.fromPath('file', imageFile.path)
      );

      // Send request
      var streamedResponse = await request.send();
      var response = await http.Response.fromStream(streamedResponse);

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Prediction failed: ${response.body}');
      }
    } catch (e) {
      throw Exception('Error: $e');
    }
  }

  // Batch Prediction
  Future<Map<String, dynamic>> predictBatch(List<File> imageFiles) async {
    var request = http.MultipartRequest(
      'POST',
      Uri.parse('$baseUrl/predict/batch'),
    );

    for (var file in imageFiles) {
      request.files.add(
        await http.MultipartFile.fromPath('files', file.path)
      );
    }

    var streamedResponse = await request.send();
    var response = await http.Response.fromStream(streamedResponse);

    return json.decode(response.body);
  }

  // Health Check
  Future<bool> checkHealth() async {
    try {
      var response = await http.get(Uri.parse('$baseUrl/health'));
      var data = json.decode(response.body);
      return data['status'] == 'healthy';
    } catch (e) {
      return false;
    }
  }
}

// Usage Example
void main() async {
  final service = CatDogClassifierService();

  // Check if API is healthy
  bool isHealthy = await service.checkHealth();
  print('API Health: $isHealthy');

  // Predict single image
  File image = File('/path/to/cat.jpg');
  var result = await service.predictImage(image);
  print('Prediction: ${result['prediction']}');
  print('Confidence: ${result['confidence_percentage']}%');
}
```

### Android (Kotlin + Retrofit)

For native Android applications.

```kotlin
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.*
import okhttp3.MultipartBody
import okhttp3.RequestBody
import java.io.File

// Data Models
data class PredictionResponse(
    val success: Boolean,
    val filename: String,
    val prediction: String,
    val confidence_percentage: Double,
    val probabilities: Probabilities
)

data class Probabilities(
    val cat: Double,
    val dog: Double
)

data class HealthResponse(
    val status: String,
    val model_loaded: Boolean
)

// API Interface
interface CatDogApi {
    @Multipart
    @POST("predict")
    suspend fun predictImage(
        @Part file: MultipartBody.Part
    ): PredictionResponse

    @Multipart
    @POST("predict/batch")
    suspend fun predictBatch(
        @Part files: List<MultipartBody.Part>
    ): BatchPredictionResponse

    @GET("health")
    suspend fun checkHealth(): HealthResponse
}

// Retrofit Setup
object ApiClient {
    private const val BASE_URL = "http://localhost:8000/"

    val api: CatDogApi by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(CatDogApi::class.java)
    }
}

// Usage in ViewModel or Repository
class CatDogRepository {
    private val api = ApiClient.api

    suspend fun classifyImage(file: File): PredictionResponse {
        val requestFile = file.asRequestBody("image/jpeg".toMediaTypeOrNull())
        val body = MultipartBody.Part.createFormData("file", file.name, requestFile)
        return api.predictImage(body)
    }

    suspend fun checkApiHealth(): Boolean {
        return try {
            val response = api.checkHealth()
            response.status == "healthy"
        } catch (e: Exception) {
            false
        }
    }
}

// Usage in Activity/Fragment
lifecycleScope.launch {
    try {
        val file = File("/path/to/image.jpg")
        val result = repository.classifyImage(file)

        // Update UI
        binding.predictionText.text = result.prediction
        binding.confidenceText.text = "${result.confidence_percentage}%"

    } catch (e: Exception) {
        // Handle error
        Toast.makeText(context, "Error: ${e.message}", Toast.LENGTH_LONG).show()
    }
}
```

### iOS (Swift + Alamofire)

For native iOS applications.

```swift
import Alamofire
import UIKit

// Response Models
struct PredictionResponse: Codable {
    let success: Bool
    let filename: String
    let prediction: String
    let confidence_percentage: Double
    let probabilities: Probabilities
}

struct Probabilities: Codable {
    let cat: Double
    let dog: Double
}

struct HealthResponse: Codable {
    let status: String
    let model_loaded: Bool
}

// API Service
class CatDogAPIService {
    static let shared = CatDogAPIService()
    private let baseURL = "http://localhost:8000"

    // Single Image Prediction
    func predictImage(image: UIImage, completion: @escaping (Result<PredictionResponse, Error>) -> Void) {
        guard let imageData = image.jpegData(compressionQuality: 0.8) else {
            completion(.failure(NSError(domain: "", code: -1, userInfo: [NSLocalizedDescriptionKey: "Invalid image"])))
            return
        }

        AF.upload(
            multipartFormData: { multipartFormData in
                multipartFormData.append(imageData, withName: "file", fileName: "image.jpg", mimeType: "image/jpeg")
            },
            to: "\(baseURL)/predict"
        )
        .validate()
        .responseDecodable(of: PredictionResponse.self) { response in
            switch response.result {
            case .success(let result):
                completion(.success(result))
            case .failure(let error):
                completion(.failure(error))
            }
        }
    }

    // Health Check
    func checkHealth(completion: @escaping (Bool) -> Void) {
        AF.request("\(baseURL)/health")
            .validate()
            .responseDecodable(of: HealthResponse.self) { response in
                if case .success(let health) = response.result {
                    completion(health.status == "healthy")
                } else {
                    completion(false)
                }
            }
    }
}

// Usage in ViewController
class ClassifierViewController: UIViewController {

    func classifySelectedImage(_ image: UIImage) {
        // Show loading indicator
        showLoadingIndicator()

        CatDogAPIService.shared.predictImage(image: image) { [weak self] result in
            // Hide loading indicator
            self?.hideLoadingIndicator()

            switch result {
            case .success(let prediction):
                // Update UI with results
                self?.displayPrediction(prediction)

            case .failure(let error):
                // Show error alert
                self?.showError(error.localizedDescription)
            }
        }
    }

    func displayPrediction(_ prediction: PredictionResponse) {
        let emoji = prediction.prediction == "Cat" ? "🐱" : "🐕"
        resultLabel.text = "\(emoji) \(prediction.prediction)"
        confidenceLabel.text = String(format: "%.1f%% confident", prediction.confidence_percentage)

        // Update progress bar
        confidenceProgressBar.setProgress(Float(prediction.confidence_percentage / 100), animated: true)
    }
}
```

### Node.js (Express Backend)

Integrate into your Node.js backend.

```javascript
const express = require("express");
const multer = require("multer");
const FormData = require("form-data");
const axios = require("axios");
const fs = require("fs");

const app = express();
const upload = multer({ dest: "uploads/" });

const API_URL = "http://localhost:8000";

// Proxy endpoint for image classification
app.post("/api/classify", upload.single("image"), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: "No image uploaded" });
    }

    // Create form data
    const formData = new FormData();
    formData.append("file", fs.createReadStream(req.file.path));

    // Send to classification API
    const response = await axios.post(`${API_URL}/predict`, formData, {
      headers: formData.getHeaders(),
    });

    // Clean up uploaded file
    fs.unlinkSync(req.file.path);

    // Return result
    res.json(response.data);
  } catch (error) {
    console.error("Classification error:", error);
    res.status(500).json({ error: "Classification failed" });
  }
});

// Health check endpoint
app.get("/api/health", async (req, res) => {
  try {
    const response = await axios.get(`${API_URL}/health`);
    res.json(response.data);
  } catch (error) {
    res.status(503).json({ status: "unhealthy" });
  }
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
```

---

### High-Level Flow

```
┌─────────────────┐
│  User Opens App │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│ Load/Download CNN Model │  (111 MB, cached)
└────────┬────────────────┘
         │
         ▼
┌─────────────────┐
│ Upload Image    │  (JPG/PNG)
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│ Preprocess Image        │
│ • Convert to RGB        │
│ • Resize to 128×128     │
│ • Normalize (0-1)       │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ CNN Prediction          │
│ • Forward pass          │
│ • Get probability       │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Classify Result         │
│ • Score > 0.5 = Dog 🐕  │
│ • Score ≤ 0.5 = Cat 🐱  │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Display Results         │
│ • Animated card         │
│ • Confidence meter      │
│ • Detailed metrics      │
└─────────────────────────┘
```

### Detailed Component Workflow

#### 1. **Model Loading** (`load_trained_model()`)

- Checks if model file exists locally
- Downloads from Google Drive if missing
- Loads Keras model into memory
- Caches using `@st.cache_resource` for performance

#### 2. **Image Preprocessing** (`preprocess_image()`)

```python
Input: PIL Image (any size)
  ↓
Convert to RGB
  ↓
Resize to 128×128 pixels
  ↓
Normalize: pixel_values / 255.0
  ↓
Add batch dimension: (1, 128, 128, 3)
  ↓
Output: NumPy array ready for model
```

#### 3. **Prediction** (`predict_image()`)

```python
Input: Model + PIL Image
  ↓
Preprocess image
  ↓
Run model.predict()
  ↓
Get probability score (0.0 to 1.0)
  ↓
Classify: if score > 0.5 → Dog, else → Cat
  ↓
Calculate confidence: max(score, 1-score)
  ↓
Output: {prediction, label, confidence, emoji, card_class}
```

#### 4. **UI Rendering**

- Side-by-side columns: Image preview | Prediction card
- Animated gradient cards (orange for cat, blue for dog)
- Real-time confidence visualization
- Expandable technical details

## 🏗️ Model Architecture

### Training Overview

- **Dataset:** 25,000 labeled images of cats and dogs
- **Training Accuracy:** ~92%
- **Framework:** TensorFlow/Keras
- **Architecture:** Deep Convolutional Neural Network (CNN)
- **Input Shape:** 128×128×3 (RGB images)
- **Output:** Single probability (binary classification)

### CNN Architecture Highlights

```
Input (128x128x3)
    ↓
Conv2D + ReLU + BatchNorm
    ↓
MaxPooling2D
    ↓
Conv2D + ReLU + BatchNorm
    ↓
MaxPooling2D
    ↓
Dropout (regularization)
    ↓
Flatten
    ↓
Dense + ReLU
    ↓
Dropout
    ↓
Dense + Sigmoid (output)
    ↓
Probability (0.0 - 1.0)
  • Score > 0.5 = Dog 🐕
  • Score ≤ 0.5 = Cat 🐱
```

### Key Features

- **Batch Normalization** - Stable and faster training
- **Dropout Layers** - Prevents overfitting
- **MaxPooling** - Reduces spatial dimensions
- **ReLU Activation** - Non-linear transformations
- **Sigmoid Output** - Binary probability

### Model File Details

- **Format:** Keras (.keras)
- **Size:** 111 MB
- **Download:** Automatic from Google Drive
- **Google Drive ID:** `1NUmowM-IX9yRhsNad1G42042YAEzYVig`
- **Storage:** Cached locally after first download

### Training Notebook

The complete training process is available in:

- **File:** `Dogs_vs_Cats_Image_Classification_CNN.ipynb`
- **Includes:** Data preprocessing, augmentation, training, evaluation

---

## 🔄 Project Workflow

### High-Level Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERACTION                          │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┴───────────────┐
         │                               │
         ▼                               ▼
┌─────────────────┐           ┌─────────────────┐
│  Web Interface  │           │   REST API      │
│   (Streamlit)   │           │   (FastAPI)     │
└────────┬────────┘           └────────┬────────┘
         │                               │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │   Model Loading/Caching       │
         │   • Check if model exists     │
         │   • Download from GDrive      │
         │   • Load into memory          │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │   Image Preprocessing         │
         │   • Convert to RGB            │
         │   • Resize to 128×128         │
         │   • Normalize (0-1)           │
         │   • Add batch dimension       │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │   CNN Prediction              │
         │   • Forward pass              │
         │   • Get probability (0-1)     │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │   Result Classification       │
         │   • Score > 0.5 = Dog 🐕      │
         │   • Score ≤ 0.5 = Cat 🐱      │
         │   • Calculate confidence      │
         └───────────────┬───────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │   Return Results              │
         │   • Web: Visual display       │
         │   • API: JSON response        │
         └───────────────────────────────┘
```

### Detailed Component Workflow

#### 1. **Model Loading** (`load_trained_model()`)

```python
1. Check if model file exists locally
   ├─ YES → Load model from disk
   └─ NO  → Download from Google Drive
            ├─ Use gdown library
            ├─ Save to local disk
            └─ Load model into memory

2. Cache model using @st.cache_resource (Streamlit)
   or global variable (FastAPI)

3. Return loaded model
```

#### 2. **Image Preprocessing** (`preprocess_image()`)

```python
Input: PIL Image (any size, any mode)
  ↓
Step 1: Convert to RGB
  • Handles: RGBA, Grayscale, etc.
  • Output: RGB mode
  ↓
Step 2: Resize to 128×128
  • Uses: PIL.Image.resize()
  • Interpolation: LANCZOS (high quality)
  ↓
Step 3: Convert to NumPy array
  • Shape: (128, 128, 3)
  ↓
Step 4: Normalize pixel values
  • Formula: pixel_value / 255.0
  • Range: [0.0, 1.0]
  ↓
Step 5: Add batch dimension
  • Shape: (1, 128, 128, 3)
  ↓
Output: NumPy array ready for model
```

#### 3. **Prediction Process**

```python
Input: Preprocessed image array
  ↓
CNN Forward Pass
  ├─ Conv layers extract features
  ├─ Pooling reduces dimensions
  ├─ Dropout prevents overfitting
  └─ Dense layers classify
  ↓
Output: Probability score (0.0 to 1.0)
  ↓
Classification Logic:
  if score > 0.5:
      prediction = "Dog"
      confidence = score * 100
  else:
      prediction = "Cat"
      confidence = (1 - score) * 100
  ↓
Return: {
    "prediction": "Cat" or "Dog",
    "confidence": 0-100%,
    "raw_score": 0.0-1.0,
    "probabilities": {"cat": X%, "dog": Y%}
}
```

---

## 📁 Project Structure

```
Image-Classification-CNN/
│
├── 📄 Core Application Files
│   ├── streamlit_app.py              # Streamlit web interface (UI for end-users)
│   └── api.py                         # FastAPI REST API server (for integrations)
│
├── 📋 Dependencies
│   ├── requirements.txt               # Streamlit app dependencies
│   └── requirements-api.txt           # FastAPI dependencies
│
├── 🐳 Docker & Deployment
│   ├── Dockerfile                     # Container image definition
│   └── docker-compose.yml             # Multi-container orchestration
│
├── 🧪 Testing & Examples
│   ├── test_api.py                    # Comprehensive unit tests (pytest)
│   ├── test_api_quick.py              # Quick API verification script
│   └── api_client_example.py          # Python client usage examples
│
├── 🚀 Convenience Scripts
│   ├── start_api.ps1                  # Windows PowerShell launcher
│   └── start_api.sh                   # Linux/Mac bash launcher
│
├── 🤖 Model Files
│   ├── dogs_vs_cats_production_model.keras  # Trained CNN model (111 MB)
│   └── Dogs_vs_Cats_Image_Classification_CNN.ipynb  # Training notebook
│
├── 📖 Documentation
│   └── README.md                      # This comprehensive guide
│
└── 📁 __pycache__/                    # Python bytecode cache (auto-generated)
```

### File Descriptions

| File/Directory            | Purpose                                 | When to Use                              |
| ------------------------- | --------------------------------------- | ---------------------------------------- |
| **streamlit_app.py**      | Interactive web UI with visual feedback | End-users, demos, presentations          |
| **api.py**                | RESTful API server                      | App integration, mobile apps, automation |
| **requirements.txt**      | Streamlit dependencies                  | Installing web application               |
| **requirements-api.txt**  | FastAPI dependencies                    | Installing REST API                      |
| **Dockerfile**            | Container image specification           | Docker deployments, cloud hosting        |
| **docker-compose.yml**    | Container orchestration config          | Easy local/production deployment         |
| **test_api.py**           | Comprehensive test suite                | CI/CD pipelines, quality assurance       |
| **test_api_quick.py**     | Rapid API health check                  | Post-deployment verification             |
| **api_client_example.py** | Integration code samples                | Learning API usage patterns              |
| **start_api scripts**     | Platform-specific launchers             | Quick server startup                     |
| **model.keras**           | Trained model weights                   | Auto-downloaded on first run             |
| **Training notebook**     | Model development process               | Understanding architecture, retraining   |

### Dependencies Breakdown

**requirements.txt** (Web App):

```
streamlit>=1.28.0       # Web application framework
tensorflow>=2.13.0      # Deep learning engine
pillow>=10.0.0          # Image processing
numpy>=1.24.0           # Numerical computations
gdown>=4.7.1            # Google Drive downloader
```

**requirements-api.txt** (REST API):

```
fastapi>=0.104.0        # Modern web framework
uvicorn[standard]>=0.24.0  # ASGI server
python-multipart>=0.0.6 # File upload support
tensorflow>=2.13.0      # Deep learning engine
pillow>=10.0.0          # Image processing
numpy>=1.24.0           # Numerical computations
gdown>=4.7.1            # Google Drive downloader
```

**Why Separate Requirements Files?**

| Aspect          | Benefit                                      |
| --------------- | -------------------------------------------- |
| **Size**        | Smaller installations for specific use cases |
| **Conflicts**   | Prevents dependency version conflicts        |
| **Clarity**     | Clear separation of concerns                 |
| **Docker**      | Smaller container images                     |
| **Development** | Install only what you need                   |

---

## 🔧 Technologies Used

### Core Framework & Languages

- **Python 3.8+** - Primary programming language
- **TensorFlow 2.13+** - Deep learning framework for model training and inference
- **Keras** - High-level neural networks API (part of TensorFlow)

### Web Frameworks

- **Streamlit 1.28+** - Rapid web app development for data science
- **FastAPI 0.104+** - Modern, fast web framework for building APIs
- **Uvicorn** - Lightning-fast ASGI server

### Image Processing & ML

- **NumPy** - Fundamental package for numerical computing
- **Pillow (PIL)** - Python Imaging Library for image manipulation
- **OpenCV** (optional) - Computer vision library for advanced preprocessing

### Development & Testing

- **pytest** - Testing framework
- **black** - Code formatter
- **flake8** - Linter for code quality
- **mypy** - Static type checker

### Deployment & DevOps

- **Docker** - Containerization platform
- **Docker Compose** - Multi-container orchestration
- **Gunicorn** - Production WSGI server
- **Nginx** (recommended) - Reverse proxy and load balancer

### Model Details

- **Architecture**: Convolutional Neural Network (CNN)
- **Input**: 128×128×3 RGB images
- **Output**: Binary classification (Cat vs Dog)
- **Layers**: Conv2D, MaxPooling2D, Dropout, Dense, BatchNormalization
- **Activation**: ReLU (hidden), Sigmoid (output)
- **Optimizer**: Adam
- **Loss Function**: Binary Crossentropy
- **Metrics**: Accuracy (~92%)
- **Model Size**: 111 MB
- **Training Dataset**: 25,000 labeled images from Kaggle

### Cloud & Hosting Options

Compatible with major cloud platforms:

- **AWS** - EC2, ECS, Lambda, Elastic Beanstalk
- **Google Cloud** - Compute Engine, Cloud Run, App Engine
- **Azure** - Virtual Machines, Container Instances, App Service
- **Heroku** - Easy deployment with buildpacks
- **Railway** - Modern PaaS with automatic deployments
- **Render** - Free tier available for testing
- **DigitalOcean** - App Platform for managed deployments
- **Vercel/Netlify** - Serverless functions (with adaptations)

---

## 🔄 Project Workflow

### Complete Application Flow

```
┌─────────────────────────────────────────────────────────────┐
│                      USER INTERACTION                        │
│  • Web Browser (Streamlit)  OR  • API Client (Any Platform) │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┴───────────────┐
         │                               │
         ▼                               ▼
┌─────────────────────┐         ┌─────────────────────┐
│  Streamlit Web UI   │         │   FastAPI Server    │
│  • File uploader    │         │   • RESTful routes  │
│  • Visual feedback  │         │   • JSON responses  │
│  • Result display   │         │   • Batch support   │
└──────────┬──────────┘         └──────────┬──────────┘
           │                               │
           └───────────────┬───────────────┘
                           │
                           ▼
           ┌───────────────────────────────┐
           │   Model Loading & Caching     │
           │  1. Check if model exists     │
           │  2. Download from GDrive      │
           │  3. Load into memory          │
           │  4. Cache for performance     │
           └───────────────┬───────────────┘
                           │
                           ▼
           ┌───────────────────────────────┐
           │   Image Preprocessing         │
           │  1. Validate file type        │
           │  2. Convert to RGB            │
           │  3. Resize to 128×128         │
           │  4. Normalize (0-1 range)     │
           │  5. Add batch dimension       │
           └───────────────┬───────────────┘
                           │
                           ▼
           ┌───────────────────────────────┐
           │   CNN Prediction              │
           │  • Convolutional layers       │
           │  • Feature extraction         │
           │  • Pooling & dropout          │
           │  • Dense classification       │
           │  • Sigmoid output (0-1)       │
           └───────────────┬───────────────┘
                           │
                           ▼
           ┌───────────────────────────────┐
           │   Result Classification       │
           │  • Score > 0.5 = Dog 🐕       │
           │  • Score ≤ 0.5 = Cat 🐱       │
           │  • Calculate confidence       │
           │  • Compute probabilities      │
           └───────────────┬───────────────┘
                           │
         ┌─────────────────┴─────────────────┐
         │                                   │
         ▼                                   ▼
┌────────────────────┐            ┌────────────────────┐
│  Streamlit UI      │            │   API Response     │
│  • Animated card   │            │   • JSON payload   │
│  • Confidence bar  │            │   • Metadata       │
│  • Emoji display   │            │   • Status codes   │
│  • Expandable info │            │   • Error handling │
└────────────────────┘            └────────────────────┘
```

### Detailed Processing Pipeline

#### 1. Model Loading (`load_trained_model()`)

```python
┌─ Check local filesystem
│  ├─ Model exists?
│  │  ├─ YES → Load from disk
│  │  └─ NO  → Download from Google Drive
│  │           ├─ Use gdown library
│  │           ├─ Show progress bar
│  │           └─ Save to local disk
│  │
│  ├─ Load model with TensorFlow
│  ├─ Verify model architecture
│  └─ Cache in memory
│
└─ Return: Loaded Keras model
```

#### 2. Image Preprocessing (`preprocess_image()`)

```python
Input: PIL Image (any size, any format)
  │
  ├─ Step 1: Mode Conversion
  │   ├─ Check current mode (RGB, RGBA, L, etc.)
  │   ├─ Convert to RGB if needed
  │   └─ Output: RGB image
  │
  ├─ Step 2: Resize
  │   ├─ Target: 128×128 pixels
  │   ├─ Method: LANCZOS (high quality)
  │   └─ Output: 128×128 RGB image
  │
  ├─ Step 3: Array Conversion
  │   ├─ Convert PIL to NumPy array
  │   └─ Shape: (128, 128, 3)
  │
  ├─ Step 4: Normalization
  │   ├─ Formula: pixel_value / 255.0
  │   ├─ Range: [0, 255] → [0.0, 1.0]
  │   └─ Reason: Neural networks prefer normalized inputs
  │
  ├─ Step 5: Batch Dimension
  │   ├─ Add dimension for batch processing
  │   └─ Shape: (1, 128, 128, 3)
  │
  └─ Output: NumPy array ready for model inference
```

#### 3. CNN Prediction Process

```python
Input: Preprocessed image array (1, 128, 128, 3)
  │
  ├─ Convolutional Layers
  │   ├─ Extract low-level features (edges, textures)
  │   ├─ Apply ReLU activation
  │   └─ Batch normalization for stability
  │
  ├─ Pooling Layers
  │   ├─ Reduce spatial dimensions
  │   └─ Retain important features
  │
  ├─ Dropout Layers
  │   ├─ Prevent overfitting
  │   └─ Random neuron deactivation
  │
  ├─ Flatten Layer
  │   └─ Convert 2D features to 1D vector
  │
  ├─ Dense Layers
  │   ├─ High-level feature combination
  │   └─ Classification logic
  │
  ├─ Sigmoid Output
  │   └─ Output: Single value [0.0, 1.0]
  │
  ├─ Classification Logic
  │   ├─ if score > 0.5:
  │   │   ├─ prediction = "Dog"
  │   │   └─ confidence = score × 100
  │   └─ else:
  │       ├─ prediction = "Cat"
  │       └─ confidence = (1 - score) × 100
  │
  └─ Output: {
        "prediction": "Cat" or "Dog",
        "confidence_percentage": 0-100%,
        "raw_score": 0.0-1.0,
        "probabilities": {"cat": X%, "dog": Y%}
      }
```

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### Issue 1: Model Download Fails

**Symptoms:**

```
Error: Failed to download model
ConnectionError: Unable to reach Google Drive
```

**Solutions:**

1. **Check Internet Connection**

   ```powershell
   # Test connectivity
   ping google.com
   ```

2. **Manual Download**

   - Visit: https://drive.google.com/uc?id=1NUmowM-IX9yRhsNad1G42042YAEzYVig
   - Download the file
   - Place in project root as `dogs_vs_cats_production_model.keras`

3. **Firewall/Proxy Issues**

   ```powershell
   # Set proxy (if needed)
   $env:HTTP_PROXY="http://proxy.company.com:8080"
   $env:HTTPS_PROXY="http://proxy.company.com:8080"
   ```

4. **Alternative Download Method**
   ```python
   import gdown
   url = "https://drive.google.com/uc?id=1NUmowM-IX9yRhsNad1G42042YAEzYVig"
   output = "dogs_vs_cats_production_model.keras"
   gdown.download(url, output, quiet=False)
   ```

---

#### Issue 2: Import/Module Errors

**Symptoms:**

```
ModuleNotFoundError: No module named 'streamlit'
ModuleNotFoundError: No module named 'tensorflow'
```

**Solutions:**

1. **Verify Virtual Environment**

   ```powershell
   # Check if venv is activated
   # You should see (venv) in prompt

   # If not activated:
   .\venv\Scripts\Activate.ps1  # Windows
   source venv/bin/activate      # Linux/Mac
   ```

2. **Install Dependencies**

   ```bash
   # For web app
   pip install -r requirements.txt

   # For API
   pip install -r requirements-api.txt

   # Force reinstall
   pip install --force-reinstall -r requirements.txt
   ```

3. **Check Python Version**

   ```bash
   python --version  # Should be 3.8 or higher

   # If multiple Python versions:
   python3.10 -m pip install -r requirements.txt
   ```

4. **Update pip**
   ```bash
   python -m pip install --upgrade pip
   ```

---

#### Issue 3: Port Already in Use

**Symptoms:**

```
Error: Address already in use
OSError: [Errno 98] Address already in use
```

**Solutions:**

1. **Change Port (Streamlit)**

   ```bash
   streamlit run streamlit_app.py --server.port 8502
   ```

2. **Change Port (FastAPI)**

   ```bash
   uvicorn api:app --port 8001
   ```

3. **Find and Kill Process (Windows)**

   ```powershell
   # Find process on port 8000
   netstat -ano | findstr :8000

   # Kill process (replace PID with actual process ID)
   taskkill /PID <PID> /F
   ```

4. **Find and Kill Process (Linux/Mac)**

   ```bash
   # Find process on port 8000
   lsof -i :8000

   # Kill process
   kill -9 <PID>
   ```

---

#### Issue 4: Low Prediction Accuracy

**Symptoms:**

```
Model predicting incorrectly
Confidence seems random
Results don't match visual inspection
```

**Solutions:**

1. **Check Image Quality**

   - Ensure images are clear and well-lit
   - Animal should be the main subject
   - Avoid heavily filtered or obscured images
   - Remove images with multiple animals

2. **Verify Image Format**

   - Use JPG, JPEG, or PNG formats
   - Avoid corrupted or partial images
   - Check file size (not too small)

3. **Test with Known Images**

   ```python
   # Download test images
   import requests

   # Clear cat image
   cat_url = "https://example.com/clear_cat.jpg"
   response = requests.get(cat_url)
   with open("test_cat.jpg", "wb") as f:
       f.write(response.content)
   ```

4. **Model Limitations**
   - Model trained on standard cat/dog images
   - May struggle with:
     - Cartoon/drawn animals
     - Extreme angles or crops
     - Multiple animals in frame
     - Non-standard breeds

---

#### Issue 5: TensorFlow Warnings

**Symptoms:**

```
WARNING:tensorflow:...
Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
```

**Solutions:**

1. **Suppress Warnings (if safe to ignore)**

   ```python
   import os
   os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 0=all, 1=info, 2=warning, 3=error
   ```

2. **Install Optimized TensorFlow**

   ```bash
   # For better CPU performance
   pip install intel-tensorflow
   ```

3. **Use GPU Version (if CUDA available)**
   ```bash
   pip uninstall tensorflow
   pip install tensorflow-gpu
   ```

---

#### Issue 6: Docker Build Fails

**Symptoms:**

```
ERROR: failed to solve: process "/bin/sh -c pip install..." did not complete successfully
```

**Solutions:**

1. **Check Docker Resources**

   - Increase memory allocation in Docker Desktop
   - Increase disk space

2. **Clear Docker Cache**

   ```bash
   docker system prune -a
   docker volume prune
   ```

3. **Build with No Cache**

   ```bash
   docker build --no-cache -t cat-dog-api .
   ```

4. **Check Dockerfile Syntax**
   - Ensure requirements files exist
   - Verify paths are correct
   - Check for typos in commands

---

#### Issue 7: API CORS Errors

**Symptoms:**

```
Access to fetch at 'http://localhost:8000/predict' from origin 'http://localhost:3000' has been blocked by CORS policy
```

**Solutions:**

1. **Check CORS Configuration in api.py**

   ```python
   from fastapi.middleware.cors import CORSMiddleware

   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],  # Allow all origins (development only)
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

2. **Production CORS (specific origins)**

   ```python
   allow_origins=[
       "https://yourdomain.com",
       "http://localhost:3000",  # React dev server
   ]
   ```

3. **Test CORS with cURL**
   ```bash
   curl -H "Origin: http://localhost:3000" \
        -H "Access-Control-Request-Method: POST" \
        -H "Access-Control-Request-Headers: Content-Type" \
        -X OPTIONS \
        http://localhost:8000/predict
   ```

---

#### Issue 8: Memory Errors

**Symptoms:**

```
MemoryError: Unable to allocate array
ResourceExhausted: OOM when allocating tensor
```

**Solutions:**

1. **Reduce Batch Size**

   ```python
   # In batch prediction, process fewer images
   MAX_BATCH_SIZE = 5  # Instead of 10
   ```

2. **Clear Memory Between Predictions**

   ```python
   import gc
   import tensorflow as tf

   # After prediction
   gc.collect()
   tf.keras.backend.clear_session()
   ```

3. **Limit TensorFlow GPU Memory**

   ```python
   import tensorflow as tf

   gpus = tf.config.list_physical_devices('GPU')
   if gpus:
       tf.config.experimental.set_memory_growth(gpus[0], True)
   ```

---

### Getting Help

If you're still experiencing issues:

1. **Check Logs**

   ```bash
   # Streamlit
   streamlit run streamlit_app.py --logger.level=debug

   # FastAPI
   uvicorn api:app --log-level debug

   # Docker
   docker logs <container_name>
   ```

2. **Run Tests**

   ```bash
   pytest test_api.py -v
   python test_api_quick.py
   ```

3. **GitHub Issues**

   - Search existing issues
   - Create new issue with:
     - Error message
     - Python version
     - OS and environment
     - Steps to reproduce

4. **Contact**
   - GitHub: [@fsRakib](https://github.com/fsRakib)
   - Project: [Image-Classification-CNN](https://github.com/fsRakib/Image-Classification-CNN)

---

## 🤝 Contributing

We welcome contributions from the community! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

### How to Contribute

1. **Fork the Repository**

   ```bash
   # Click 'Fork' button on GitHub
   git clone https://github.com/YOUR_USERNAME/Image-Classification-CNN.git
   cd Image-Classification-CNN
   ```

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourAmazingFeature
   ```

3. **Make Your Changes**

   - Write clean, documented code
   - Follow existing code style
   - Add tests if applicable
   - Update documentation

4. **Test Your Changes**

   ```bash
   # Run existing tests
   pytest test_api.py -v

   # Test manually
   python streamlit_app.py  # Test web app
   python api.py             # Test API
   ```

5. **Commit Your Changes**

   ```bash
   git add .
   git commit -m "Add: Your descriptive commit message"
   ```

   **Commit Message Guidelines:**

   - `Add:` New features
   - `Fix:` Bug fixes
   - `Update:` Updates to existing features
   - `Docs:` Documentation changes
   - `Test:` Adding or updating tests

6. **Push to Your Fork**

   ```bash
   git push origin feature/YourAmazingFeature
   ```

7. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Describe your changes
   - Link any related issues

### Contribution Ideas

We'd love to see contributions in these areas:

**Feature Enhancements:**

- 🎯 Multi-class classification (cats, dogs, other animals)
- 📊 Confidence visualization improvements
- 🖼️ Image augmentation preview in UI
- 📈 Model performance metrics dashboard
- 🔄 Real-time video classification
- 🎨 Dark mode for Streamlit app
- 🌍 Internationalization (i18n) support

**API Improvements:**

- 🔐 Authentication system (API keys, JWT)
- ⚡ Rate limiting implementation
- 📝 Request logging and analytics
- 🚀 GraphQL API endpoint
- 🔗 Webhook support for async predictions
- 📊 Prometheus metrics endpoint

**Infrastructure:**

- ☸️ Kubernetes deployment manifests
- 🔄 CI/CD pipeline (GitHub Actions)
- 📦 Helm charts for easy deployment
- 🐳 Multi-stage Docker builds
- 🧪 Integration tests
- 📏 Code coverage reports

**Documentation:**

- 📹 Video tutorials
- 🎓 Jupyter notebook examples
- 🌐 API client libraries (JavaScript, Java, Go)
- 📱 Mobile app integration guides
- 🏗️ Architecture decision records

**Model Improvements:**

- 🧠 Fine-tuning for specific breeds
- 🔄 Transfer learning with other models
- 📊 Model compression for faster inference
- 🎯 Explainable AI (grad-CAM visualizations)

### Code Style Guidelines

- Follow [PEP 8](https://pep8.org/) for Python code
- Use type hints where appropriate
- Write descriptive docstrings
- Keep functions focused and small
- Add comments for complex logic

### Bug Reports

Found a bug? Please open an issue with:

- Clear, descriptive title
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Error messages and stack traces
- Screenshots (if applicable)

### Feature Requests

Have an idea? Open an issue with:

- Description of the feature
- Use case and benefits
- Possible implementation approach
- Mockups or examples (if applicable)

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for complete details.

### What This Means

✅ **Commercial use** - Use in commercial projects  
✅ **Modification** - Modify and adapt the code  
✅ **Distribution** - Distribute original or modified versions  
✅ **Private use** - Use for private projects

**Conditions:**

- Include the original copyright notice
- Include the license text

**Limitations:**

- No liability or warranty
- No trademark rights

### MIT License Summary

```
MIT License

Copyright (c) 2024 Rakib

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🙏 Acknowledgments

This project wouldn't be possible without these amazing resources and communities:

### Dataset

- **Kaggle** - [Dogs vs Cats Dataset](https://www.kaggle.com/c/dogs-vs-cats)
  - 25,000 labeled images for training
  - High-quality, diverse animal photos

### Frameworks & Libraries

- **TensorFlow Team** - Powerful deep learning framework
- **Keras** - High-level neural network API
- **Streamlit** - Rapid web app development
- **FastAPI** - Modern, fast web framework for APIs
- **NumPy** - Fundamental numerical computing
- **Pillow** - Image processing capabilities

### Inspiration & Learning

- **3Blue1Brown** - Neural network visualizations
- **Kaggle Kernels** - Community solutions and approaches
- **Fast.ai** - Deep learning course and best practices
- **TensorFlow Tutorials** - Official guides and examples

### Community

- **Stack Overflow** - Problem-solving and debugging
- **GitHub** - Code hosting and collaboration
- **Reddit r/MachineLearning** - Latest ML research and discussions
- **PyData Community** - Data science best practices

### Special Thanks

- All contributors who have helped improve this project
- Users who provided feedback and reported issues
- The open-source community for continuous innovation

---

## 📧 Contact & Support

### Get in Touch

**Primary Contact:**

- 👨‍💻 **GitHub**: [@fsRakib](https://github.com/fsRakib)
- 📂 **Project Repository**: [Image-Classification-CNN](https://github.com/fsRakib/Image-Classification-CNN)

### Ways to Get Help

1. **📖 Documentation**

   - Start with this README
   - Check code comments and docstrings
   - Review example files

2. **🐛 Issues**

   - Search [existing issues](https://github.com/fsRakib/Image-Classification-CNN/issues)
   - Create a [new issue](https://github.com/fsRakib/Image-Classification-CNN/issues/new) if needed
   - Include details: OS, Python version, error messages

3. **💬 Discussions**

   - General questions
   - Feature ideas
   - Showcase your projects using this API

4. **🚀 Pull Requests**
   - Bug fixes
   - New features
   - Documentation improvements

### Response Time

- Issues: Typically 24-48 hours
- Pull requests: Reviewed within 3-5 days
- General inquiries: Within a week

### Community Guidelines

When reaching out, please:

- ✅ Be respectful and professional
- ✅ Provide complete information
- ✅ Search for existing answers first
- ✅ Use clear, descriptive titles
- ✅ Include code examples and error messages
- ✅ Specify your environment (OS, Python version)

---

## 📊 Performance Metrics

### Model Performance

| Metric                | Value          | Details                        |
| --------------------- | -------------- | ------------------------------ |
| **Training Accuracy** | ~92%           | Validation set performance     |
| **Model Size**        | 111 MB         | Keras .keras format            |
| **Input Resolution**  | 128×128 pixels | RGB images, 3 channels         |
| **Parameters**        | ~8.5M          | Total trainable parameters     |
| **Inference Time**    | 100-300ms      | Per image (CPU), faster on GPU |

### API Performance

| Metric                | Value          | Conditions                    |
| --------------------- | -------------- | ----------------------------- |
| **Single Prediction** | ~150-250ms     | Including preprocessing (CPU) |
| **Batch Prediction**  | ~100-150ms/img | Up to 10 images (CPU)         |
| **Throughput**        | ~10-15 req/sec | Single worker, CPU only       |
| **Startup Time**      | ~3-5 seconds   | Model loading time            |
| **Memory Usage**      | ~1.5-2 GB      | With model loaded             |

### Supported Formats

| Format   | Support | Max Size | Notes                          |
| -------- | ------- | -------- | ------------------------------ |
| **JPG**  | ✅      | 10 MB    | Most common, recommended       |
| **JPEG** | ✅      | 10 MB    | Same as JPG                    |
| **PNG**  | ✅      | 10 MB    | Transparency converted to RGB  |
| **WEBP** | ❌      | N/A      | Not currently supported        |
| **GIF**  | ❌      | N/A      | Static only, animation ignored |

### Scaling Recommendations

**For Production:**

- Use **Gunicorn** with multiple workers
- Enable **GPU** acceleration for 5-10x speedup
- Implement **Redis** caching for repeated images
- Use **load balancer** (Nginx) for horizontal scaling
- Deploy on **container orchestration** (Kubernetes)

**Expected Performance with Optimization:**

- **GPU**: ~20-50ms per image
- **Multiple Workers**: 50-100 req/sec
- **Caching**: Sub-10ms for cached results

---

## 🎯 Roadmap

### Coming Soon (v2.0)

- [ ] **Multi-animal Classification** - Expand beyond cats and dogs
- [ ] **Model Explainability** - Grad-CAM visualizations
- [ ] **API Authentication** - Secure endpoints with API keys
- [ ] **Batch Upload UI** - Streamlit multi-file support
- [ ] **Model Versioning** - A/B testing different models
- [ ] **Performance Dashboard** - Real-time analytics

### Future Plans

- [ ] **Mobile Apps** - Native iOS and Android apps
- [ ] **Browser Extension** - Right-click image classification
- [ ] **Discord/Slack Bot** - Chat integration
- [ ] **Edge Deployment** - TensorFlow Lite for mobile
- [ ] **Video Classification** - Real-time video analysis
- [ ] **Fine-tuning API** - Custom model training

---

## 🌟 Star History

If you find this project helpful, please consider giving it a ⭐ on GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=fsRakib/Image-Classification-CNN&type=Date)](https://star-history.com/#fsRakib/Image-Classification-CNN&Date)

---

## 📚 Additional Resources

### Learn More

- 📖 [TensorFlow Documentation](https://www.tensorflow.org/guide)
- 📖 [FastAPI Documentation](https://fastapi.tiangolo.com/)
- 📖 [Streamlit Documentation](https://docs.streamlit.io/)
- 📖 [CNN Architecture Explained](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)

### Related Projects

- [Image Classification with PyTorch](https://github.com/pytorch/vision)
- [TensorFlow Model Garden](https://github.com/tensorflow/models)
- [Keras Applications](https://keras.io/api/applications/)

---

<div align="center">

### 🎉 Thank You for Using Cat vs Dog AI! 🎉

Made with ❤️ using **TensorFlow**, **FastAPI**, and **Streamlit**

**Deep Learning** • **Computer Vision** • **AI**

---

**⭐ Star this repo if you found it helpful!**

**🐛 Report issues** • **💡 Suggest features** • **🤝 Contribute**

[GitHub](https://github.com/fsRakib/Image-Classification-CNN) | [Issues](https://github.com/fsRakib/Image-Classification-CNN/issues) | [Discussions](https://github.com/fsRakib/Image-Classification-CNN/discussions)

---

_Last Updated: October 2024_

</div>
