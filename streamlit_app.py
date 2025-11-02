"""
Streamlit Frontend for Cat vs Dog Image Classification
Connects to FastAPI backend for predictions

Architecture:
- Frontend (Streamlit): UI/UX only, no ML logic
- Backend (FastAPI): ML model inference, API endpoints
- API Client: Decoupled communication layer

This design allows the backend to serve multiple clients
(web, mobile, third-party apps) independently.
"""

import streamlit as st
from PIL import Image
from typing import Dict, Any
import os

# Import the API client
from api_client import ClassifierAPIClient

# Configuration - Environment-based settings
# Try Streamlit secrets first, then environment variables, then localhost
try:
    API_BASE_URL = st.secrets.get("API_BASE_URL", os.getenv("API_BASE_URL", "http://localhost:8000"))
    API_TIMEOUT = int(st.secrets.get("API_TIMEOUT", os.getenv("API_TIMEOUT", "30")))
except:
    API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))

# Initialize API client
api_client = ClassifierAPIClient(base_url=API_BASE_URL, timeout=API_TIMEOUT)

# Page configuration
st.set_page_config(
    page_title="Cat vs Dog AI",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern, minimalist, responsive UI
st.markdown("""
    <style>
    /* Main container */
    .main {
        padding: 1rem 2rem;
        max-width: 900px;
        margin: 0 auto;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Title styling */
    h1 {
        text-align: center;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        font-size: 2.5rem;
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #6c757d;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Upload section */
    .stFileUploader {
        border: 2px dashed #667eea;
        border-radius: 16px;
        padding: 2rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        transition: all 0.3s ease;
    }
    
    .stFileUploader:hover {
        border-color: #764ba2;
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        border: none;
        border-radius: 12px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Result cards */
    .prediction-card {
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        margin: 1.5rem 0;
        animation: slideUp 0.5s ease-out;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .cat-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        border: 3px solid #ff6b6b;
    }
    
    .dog-card {
        background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
        border: 3px solid #4a90e2;
    }
    
    .prediction-emoji {
        font-size: 4rem;
        margin-bottom: 1rem;
        animation: bounce 1s ease;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    
    .prediction-label {
        font-size: 2rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    .prediction-confidence {
        font-size: 1.5rem;
        font-weight: 600;
        opacity: 0.9;
    }
    
    /* Image preview */
    .stImage {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    }
    
    /* Info boxes */
    .stInfo {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
        border-radius: 8px;
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        height: 12px;
        border-radius: 6px;
    }
    
    /* Metric styling */
    [data-testid="stMetricValue"] {
        font-size: 1.5rem;
        font-weight: 700;
        color: #667eea;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #f8f9fa;
        border-radius: 8px;
        font-weight: 600;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main {
            padding: 0.5rem 1rem;
        }
        h1 {
            font-size: 2rem;
        }
        .prediction-emoji {
            font-size: 3rem;
        }
        .prediction-label {
            font-size: 1.5rem;
        }
    }
    
    /* Paste area */
    .paste-area {
        border: 2px dashed #667eea;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        margin: 1rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .paste-area:hover {
        border-color: #764ba2;
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    
    .paste-icon {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("<h1>🐾 Cat vs Dog AI</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload or paste an image, and let AI identify it instantly!</p>', unsafe_allow_html=True)

# ============================================================================
# API Wrapper Functions - Simplified interface using API client
# ============================================================================

def check_api_health() -> Dict[str, Any]:
    """
    Check if the API backend is available and healthy
    
    Returns:
        dict: Health status information
    """
    return api_client.health_check()


def get_model_info() -> Dict[str, Any]:
    """
    Get information about the model from the API
    
    Returns:
        dict: Model information or None if unavailable
    """
    try:
        return api_client.get_model_info()
    except Exception as e:
        st.error(f"Failed to fetch model info: {e}")
        return None


def predict_via_api(image: Image.Image, filename: str = "image.jpg") -> Dict[str, Any]:
    """
    Send image to API for prediction
    
    Args:
        image: PIL Image object
        filename: Name for the uploaded file
        
    Returns:
        dict: Prediction results or None if request fails
    """
    try:
        return api_client.predict_from_pil_image(image, filename)
    except Exception as e:
        st.error(f"❌ Prediction failed: {str(e)}")
        return None


# ============================================================================
# Startup Check - Verify API availability
# ============================================================================

@st.cache_data(ttl=60)  # Cache for 60 seconds
def verify_api_connection():
    """Check API health on app startup"""
    return check_api_health()


# Check API availability
api_status = verify_api_connection()

if not api_status["available"]:
    st.error("⚠️ **Backend API is not available**")
    st.error(f"Error: {api_status['error']}")
    st.info(f"""
    **Please start the FastAPI backend:**
    
    1. Open a terminal in the project directory
    2. Run: `uvicorn api:app --reload`
    3. Or run: `python api.py`
    
    The API should be available at: **{API_BASE_URL}**
    """)
    st.stop()
else:
    # Show subtle success indicator in sidebar
    with st.sidebar:
        st.success("✅ API Connected")
        st.caption(f"Endpoint: {API_BASE_URL}")

# Instructions for paste
# Short helpful tip (paste feature removed)
st.markdown("""
    <div style="text-align: center; padding: 0.5rem; margin-bottom: 1rem; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 12px;">
        <small style="color: #667eea; font-weight: 600;">Tip: Use the uploader below to provide an image.</small>
    </div>
""", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader(
    "Drop an image here or click to browse", 
    type=["jpg", "jpeg", "png"],
    help="Supports JPG, JPEG, PNG formats - or paste from clipboard!",
    label_visibility="collapsed"
)

# ============================================================================
# UI Helper Functions - Format API responses for display
# ============================================================================

def format_prediction_result(api_response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Transform API response into UI-friendly format
    
    Args:
        api_response: Response from API predict endpoint
        
    Returns:
        dict: Formatted data for UI display
    """
    prediction = api_response["prediction"]
    confidence = api_response["confidence_percentage"]
    
    # Determine emoji and card styling
    if prediction == "Dog":
        emoji = "🐕"
        card_class = "dog-card"
    else:
        emoji = "🐱"
        card_class = "cat-card"
    
    return {
        "label": prediction,
        "confidence": confidence / 100.0,  # Convert to 0-1 range for progress bar
        "confidence_percentage": confidence,
        "emoji": emoji,
        "card_class": card_class,
        "raw_score": api_response.get("raw_score", 0),
        "probabilities": api_response.get("probabilities", {}),
        "metadata": api_response.get("metadata", {})
    }


# ============================================================================
# Image Processing and Display
# ============================================================================

if uploaded_file is not None:
    # Create responsive columns
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### 📸 Your Image")
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, use_container_width=True)

    with col2:
        st.markdown("### 🤖 AI Prediction")
        with st.spinner("🔄 Analyzing via API..."):
            # Send image to API for prediction
            api_response = predict_via_api(img, uploaded_file.name)
        
        if api_response and api_response.get("success"):
            # Format the API response for display
            result = format_prediction_result(api_response)
            
            # Display results with animation
            st.markdown(f"""
                <div class="prediction-card {result['card_class']}">
                    <div class="prediction-emoji">{result['emoji']}</div>
                    <div class="prediction-label">It's a {result['label']}!</div>
                    <div class="prediction-confidence">{result['confidence_percentage']:.1f}% Confident</div>
                </div>
            """, unsafe_allow_html=True)

            # Show detailed metrics
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("🐱 Cat", f"{result['probabilities'].get('cat', 0):.1f}%")
            with col_b:
                st.metric("🐕 Dog", f"{result['probabilities'].get('dog', 0):.1f}%")
            
            st.progress(float(result['confidence']))
            
            # Show raw score in small text
            st.caption(f"Raw Score: {result['raw_score']:.4f}")
        else:
            st.warning("⚠️ Prediction failed. Please try again or check API connection.")

    # Additional info in expander
    with st.expander("ℹ️ Model Information"):
        # Fetch model info from API
        model_info = get_model_info()
        
        if model_info:
            st.markdown(f"""
            **Technical Details:**
            - **Model Name:** {model_info.get('model_name', 'N/A')}
            - **Architecture:** {model_info.get('model_type', 'N/A')}
            - **Input Size:** {model_info.get('input_shape', 'N/A')}
            - **Output Classes:** {', '.join(model_info.get('output_classes', []))}
            - **Model Size:** {model_info.get('model_size_mb', 'N/A')} MB
            - **Training Accuracy:** {model_info.get('training_accuracy', 'N/A')}
            - **Supported Formats:** {', '.join(model_info.get('supported_formats', []))}
            
            **How it works:**
            1. Image is uploaded to the backend API
            2. Image is preprocessed (resized & normalized)
            3. Deep CNN analyzes patterns and features
            4. Confidence score is calculated
            5. Result is returned and displayed
            
            **API Backend:**
            - **Framework:** {model_info.get('framework', 'N/A')}
            - **Endpoint:** {API_BASE_URL}
            """)
        else:
            st.markdown("""
            **Technical Details:**
            - **Input Size:** 128×128 pixels RGB
            - **Architecture:** Deep CNN with BatchNorm & Dropout
            - **Output:** Binary Classification
            - **Training Data:** 25,000 images
            - **Accuracy:** ~92%+
            
            **How it works:**
            1. Image is uploaded to the backend API
            2. Image is preprocessed (resized & normalized)
            3. Neural network analyzes patterns
            4. Confidence score is calculated
            5. Result is returned and displayed
            """)
else:
    # Show helpful tips when no image is uploaded
    st.info("👆 Upload an image to get started!")

    # Quick tips in columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2rem;">📁</div>
            <strong>Upload</strong>
            <p style="font-size: 0.9rem; color: #6c757d;">Drag & drop or browse files</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2rem;">⚡</div>
            <strong>Instant</strong>
            <p style="font-size: 0.9rem; color: #6c757d;">Get results in seconds</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2rem;">⚡</div>
            <strong>Instant</strong>
            <p style="font-size: 0.9rem; color: #6c757d;">Get results in seconds</p>
        </div>
        """, unsafe_allow_html=True)

    # Instructions (simplified)
    st.markdown("""
    ### Getting Started
    
    **Method: Upload File**
    1. Drag & drop or click to browse
    2. Select a clear image of a cat or dog
    3. Wait for instant analysis
    
    ### Tips for Best Results
    - ✅ Use clear, well-lit photos
    - ✅ Ensure the animal is the main subject
    - ✅ Avoid heavily filtered images
    - ✅ JPG, JPEG, or PNG formats work best
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #6c757d; padding: 1rem;'>"
    "Made with ❤️ using <strong>TensorFlow</strong> & <strong>Streamlit</strong><br>"
    "<small>Deep Learning • Computer Vision • AI</small>"
    "</div>", 
    unsafe_allow_html=True
)
