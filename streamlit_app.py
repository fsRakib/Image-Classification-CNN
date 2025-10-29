import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io
import base64

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

# Load model with caching
@st.cache_resource
def load_trained_model():
    import os
    import gdown
    
    model_path = "dogs_vs_cats_production_model.keras"
    
    # If model doesn't exist locally, download from Google Drive
    if not os.path.exists(model_path):
        st.info("📥 Downloading model file (111 MB)... This may take a minute on first run.")
        try:
            # Download model from Google Drive
            model_url = "https://drive.google.com/uc?id=1NUmowM-IX9yRhsNad1G42042YAEzYVig"
            gdown.download(model_url, model_path, quiet=False)
            st.success("✅ Model downloaded successfully!")
        except Exception as e:
            st.error(f"Failed to download model: {e}")
            st.info("Please upload the model file to Google Drive and update the URL in streamlit_app.py")
            return None
    
    try:
        model = load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_trained_model()

if model is None:
    st.error("⚠️ Unable to load the AI model. Please check your connection.")
    st.stop()

# Instructions for paste
st.markdown("""
    <div style="text-align: center; padding: 0.5rem; margin-bottom: 1rem; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 12px;">
        <small style="color: #667eea; font-weight: 600;">� Tip: You can also paste an image from clipboard using <strong>Ctrl+V</strong> (Windows) or <strong>Cmd+V</strong> (Mac)</small>
    </div>
""", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader(
    "Drop an image here or click to browse", 
    type=["jpg", "jpeg", "png"],
    help="Supports JPG, JPEG, PNG formats - or paste from clipboard!",
    label_visibility="collapsed"
)

# Use session state to store pasted image
if 'pasted_image' not in st.session_state:
    st.session_state.pasted_image = None

# JavaScript for clipboard paste functionality
paste_component = st.components.v1.html("""
    <div id="paste-listener" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: -1;"></div>
    <script>
    let lastPastedData = null;
    
    document.addEventListener('paste', function(e) {
        const items = e.clipboardData.items;
        for (let i = 0; i < items.length; i++) {
            if (items[i].type.indexOf('image') !== -1) {
                const blob = items[i].getAsFile();
                const reader = new FileReader();
                reader.onload = function(event) {
                    const imageData = event.target.result;
                    if (imageData !== lastPastedData) {
                        lastPastedData = imageData;
                        window.parent.postMessage({
                            type: 'streamlit:setComponentValue',
                            value: imageData
                        }, '*');
                    }
                };
                reader.readAsDataURL(blob);
                e.preventDefault();
            }
        }
    });
    </script>
""", height=0)

# Handle pasted image
if paste_component:
    try:
        # Extract base64 data
        if ',' in paste_component:
            header, image_data = paste_component.split(',', 1)
            image_bytes = base64.b64decode(image_data)
            # Store in session state
            st.session_state.pasted_image = io.BytesIO(image_bytes)
            st.rerun()
    except Exception as e:
        pass

# Use pasted image if available and no file uploaded
if uploaded_file is None and st.session_state.pasted_image is not None:
    uploaded_file = st.session_state.pasted_image
    st.success("✅ Image pasted from clipboard!")

# Process uploaded or pasted image
if uploaded_file is not None:
    # Create responsive columns
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 📸 Your Image")
        # Display uploaded image
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, use_column_width=True)
    
    with col2:
        st.markdown("### 🤖 AI Prediction")
        
        # Preprocess image
        with st.spinner("🔍 Analyzing..."):
            # Resize image to model input size
            img_resized = img.resize((128, 128))
            
            # Convert to array and normalize
            img_array = np.array(img_resized) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            
            # Make prediction
            prediction = model.predict(img_array, verbose=0)[0][0]
            
            # Determine label and confidence
            if prediction > 0.5:
                label = "Dog"
                confidence = prediction
                emoji = "🐕"
                card_class = "dog-card"
            else:
                label = "Cat"
                confidence = 1 - prediction
                emoji = "🐱"
                card_class = "cat-card"
        
        # Display results with animation
        st.markdown(f"""
            <div class="prediction-card {card_class}">
                <div class="prediction-emoji">{emoji}</div>
                <div class="prediction-label">It's a {label}!</div>
                <div class="prediction-confidence">{confidence*100:.1f}% Confident</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Show detailed metrics
        st.metric("Prediction Score", f"{prediction:.4f}", delta=None)
        st.progress(float(confidence))
        
    # Additional info in expander
    with st.expander("ℹ️ Model Information"):
        st.markdown("""
        **Technical Details:**
        - **Input Size:** 128×128 pixels RGB
        - **Architecture:** Deep CNN with BatchNorm & Dropout
        - **Output:** Binary Classification
        - **Training Data:** 25,000 images
        - **Accuracy:** ~92%+
        
        **How it works:**
        1. Image is resized and normalized
        2. Neural network analyzes patterns
        3. Confidence score is calculated
        4. Result is displayed with certainty level
        """)

else:
    # Clear pasted image when new upload section is shown
    if st.session_state.pasted_image is not None:
        if st.button("🗑️ Clear pasted image"):
            st.session_state.pasted_image = None
            st.rerun()
    
    # Show helpful tips when no image is uploaded
    st.info("👆 Upload an image or paste from clipboard to get started!")
    
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
            <div style="font-size: 2rem;">📋</div>
            <strong>Paste</strong>
            <p style="font-size: 0.9rem; color: #6c757d;">Copy image & press Ctrl+V</p>
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

# Instructions
with st.expander("📖 How to Use"):
    st.markdown("""
    ### Getting Started
    
    **Method 1: Upload File**
    1. Drag & drop or click to browse
    2. Select a clear image of a cat or dog
    3. Wait for instant analysis
    
    **Method 2: Paste from Clipboard**
    1. Copy an image from anywhere (right-click → Copy Image)
    2. Press `Ctrl+V` (Windows) or `Cmd+V` (Mac) anywhere on the page
    3. Image will automatically upload and analyze
    
    ### Tips for Best Results
    - ✅ Use clear, well-lit photos
    - ✅ Ensure the animal is the main subject
    - ✅ Avoid heavily filtered images
    - ✅ JPG, JPEG, or PNG formats work best
    
    ### Supported Formats
    - 📸 JPEG/JPG
    - 🖼️ PNG
    - 📁 Max size: 200MB
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
