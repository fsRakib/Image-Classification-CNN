# 🐾 Cat vs Dog AI - Deep Learning Image Classifier

> **A production-ready deep learning application that classifies images as cats or dogs with ~92% accuracy.**  
> Deployed with **Railway** (backend) and **Streamlit Cloud** (frontend) for seamless access worldwide.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16+-orange.svg)](https://www.tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Railway](https://img.shields.io/badge/Railway-Deployed-purple.svg)](https://railway.app)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🌐 Live Demo

- **🎨 Web Application:** [https://cat-dog-prediction.streamlit.app/](https://cat-dog-prediction.streamlit.app/)
- **🚀 API Backend:** [https://web-production-c142d.up.railway.app/](https://web-production-c142d.up.railway.app/)
- **📚 API Documentation:** [https://web-production-c142d.up.railway.app/docs](https://web-production-c142d.up.railway.app/docs)

---

## 📖 Table of Contents

- [✨ Features](#-features)
- [🎬 Demo](#-demo)
- [🚀 Quick Start](#-quick-start)
- [📡 API Documentation](#-api-documentation)
- [💡 Usage Examples](#-usage-examples)
- [🏗️ Architecture](#️-architecture)
- [📁 Project Structure](#-project-structure)
- [🚢 Deployment](#-deployment)
- [🐛 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)

---

## ✨ Features

### 🎯 **Two Powerful Interfaces**

| Feature                      | Web App (Streamlit)       | REST API (FastAPI)                    |
| ---------------------------- | ------------------------- | ------------------------------------- |
| **User Interface**           | ✅ Interactive web UI     | ❌ API only (integrate with your app) |
| **Real-time Classification** | ✅ Instant visual results | ✅ JSON response                      |
| **Batch Processing**         | ❌ One image at a time    | ✅ Up to 10 images per request        |
| **Integration**              | ❌ Standalone app         | ✅ Any language/platform              |
| **Auto Documentation**       | ❌ N/A                    | ✅ Swagger UI + ReDoc                 |
| **Mobile Friendly**          | ✅ Responsive design      | ✅ Mobile apps can integrate          |
| **Cloud Deployment**         | ✅ Streamlit Cloud        | ✅ Railway                            |
| **Best For**                 | End-users, demos          | Developers, production systems        |

### 🎨 **Web Application Highlights**

- 🖼️ **Modern UI** with gradient animations and smooth transitions
- 🎯 **Drag-and-drop** image upload with instant preview
- 📊 **Confidence meters** with visual progress bars
- 📱 **Mobile responsive** design that works everywhere
- ⚡ **Auto model download** from Google Drive (111 MB, cached)
- 🚀 **Fast inference** ~100-300ms per image
- 🎨 **Animated result cards** color-coded by prediction
- 📈 **Detailed metrics** expandable technical information

### �� **REST API Highlights**

- 🌐 **RESTful endpoints** following industry best practices
- 📦 **Batch prediction** process up to 10 images in one request
- 🔓 **CORS enabled** ready for web and mobile apps
- ✅ **Input validation** file type, size, and format checks
- 💚 **Health checks** monitor API and model status
- 🛡️ **Production-ready** with comprehensive logging
- 📚 **Interactive docs** Swagger UI at `/docs` and ReDoc at `/redoc`
- ⚡ **Async support** high-performance with uvicorn
- 📊 **Detailed responses** confidence scores, probabilities, metadata

---

## 🎬 Demo

### Web Application

Try it live: [https://cat-dog-prediction.streamlit.app/](https://cat-dog-prediction.streamlit.app/)

Upload any cat or dog image and get instant AI predictions!

### API Response Example

```json
{
  "success": true,
  "filename": "cat.jpg",
  "prediction": "Cat",
  "confidence_percentage": 98.5,
  "probabilities": {
    "cat": 98.5,
    "dog": 1.5
  }
}
```

---

## 🚀 Quick Start

### Prerequisites

- ✅ **Python 3.8+** ([Download](https://www.python.org/downloads/))
- ✅ **pip** package manager
- ✅ **Git** ([Download](https://git-scm.com/downloads))
- ✅ **Internet connection** (for model download)

### Local Development

**1. Clone Repository**

```bash
git clone https://github.com/fsRakib/Image-Classification-CNN.git
cd Image-Classification-CNN
```

**2. Create Virtual Environment**

```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Run Backend API**

```bash
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

Access at: http://localhost:8000

**5. Run Streamlit Frontend** (Optional)

```bash
streamlit run streamlit_app.py
```

Access at: http://localhost:8501

---

## 📡 API Documentation

### Available Endpoints

| Endpoint         | Method | Description                         |
| ---------------- | ------ | ----------------------------------- |
| /                | GET    | API information                     |
| /health          | GET    | Health check                        |
| /model/info      | GET    | Model details                       |
| /predict         | POST   | Single image prediction             |
| /predict/batch   | POST   | Batch predictions (up to 10)        |

### Example: Single Prediction

```bash
curl -X POST "https://web-production-c142d.up.railway.app/predict" -F "file=@cat.jpg"
```

**Response:**

```json
{
  "success": true,
  "prediction": "Cat",
  "confidence_percentage": 98.5,
  "probabilities": { "cat": 98.5, "dog": 1.5 }
}
```

---

## 💡 Usage Examples

### Python

```python
import requests

url = "https://web-production-c142d.up.railway.app/predict"
with open("cat.jpg", "rb") as f:
    response = requests.post(url, files={"file": f})
    print(response.json())
```

### JavaScript

```javascript
const formData = new FormData();
formData.append("file", fileInput.files[0]);

fetch("https://web-production-c142d.up.railway.app/predict", {
  method: "POST",
  body: formData
})
.then(res => res.json())
.then(data => console.log(data));
```

---

## 🏗️ Architecture

### System Flow

```
User → Streamlit Cloud (UI) → Railway.app (API) → CNN Model → Prediction
```

### Model Details

- **Architecture:** Convolutional Neural Network (CNN)
- **Framework:** TensorFlow/Keras
- **Input:** 128×128×3 RGB images
- **Accuracy:** ~92%
- **Model Size:** 111 MB
- **Dataset:** 25,000 cat/dog images

---

## 📁 Project Structure

```
Image-Classification-CNN/
├── api.py                    # FastAPI backend
├── streamlit_app.py          # Streamlit frontend
├── api_client.py             # API client wrapper
├── requirements.txt          # Dependencies
├── Procfile                  # Railway config
├── railway.json              # Railway build settings
├── dogs_vs_cats_production_model.keras  # Model (111 MB)
└── README.md                 # Documentation
```

---

## 🚢 Deployment

### Current Deployment

- **Backend:** Railway.app (Auto-deploy from main branch)
- **Frontend:** Streamlit Cloud (Auto-deploy from main branch)

### Deploy Your Own

**Backend to Railway:**
1. Fork repository
2. Sign up on Railway.app
3. New project → Deploy from GitHub
4. Select repository (auto-detects config)

**Frontend to Streamlit Cloud:**
1. Sign up on Streamlit.io/cloud
2. New app → Select repository
3. Main file: streamlit_app.py
4. Add secret: `API_BASE_URL = "your-railway-url"`

---

## 🐛 Troubleshooting

### Common Issues

**Model Download Fails**
- Check internet connection
- Download manually: [Google Drive Link]
- Place in project root

**API Connection Error**
- Verify Railway backend is running
- Check Streamlit secrets configuration
- Test: `curl https://your-url/health`

**Module Not Found**
- Activate virtual environment
- Run: `pip install -r requirements.txt`

**Port Already in Use**
- Use different port: `uvicorn api:app --port 8001`
- Or kill process: `netstat -ano | findstr :8000`

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

---

## 📝 License

MIT License - see LICENSE file

---

## �� Acknowledgments

- Kaggle Dogs vs Cats dataset
- TensorFlow & Keras teams
- FastAPI & Streamlit teams
- Railway & Streamlit Cloud

---

## 📊 Project Stats

- **Model Size:** 111 MB
- **Training Images:** 25,000
- **Accuracy:** ~92%
- **Inference Time:** 100-300ms
- **Supported Formats:** JPG, JPEG, PNG
- **Max File Size:** 10MB

---

## 📧 Contact

**Developer:** Fahim Shahriar Rakib

- GitHub: [@fsRakib](https://github.com/fsRakib)
- Project: [Image-Classification-CNN](https://github.com/fsRakib/Image-Classification-CNN)
- Live Demo: [cat-dog-prediction.streamlit.app](https://cat-dog-prediction.streamlit.app/)

---

<div align="center">

**Made with ❤️ using TensorFlow, FastAPI, and Streamlit**

⭐ Star this repo if you found it helpful!

[Report Bug](https://github.com/fsRakib/Image-Classification-CNN/issues) · [Request Feature](https://github.com/fsRakib/Image-Classification-CNN/issues)

</div>
