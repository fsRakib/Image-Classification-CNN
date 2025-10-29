import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="Cat vs Dog Classifier",
    page_icon="🐾",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem;
        font-size: 1.2rem;
        border-radius: 10px;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
    }
    .cat-result {
        background-color: #FFE5E5;
        border: 3px solid #FF6B6B;
    }
    .dog-result {
        background-color: #E5F3FF;
        border: 3px solid #4A90E2;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🐾 Cat vs Dog Classifier")
st.markdown("Upload an image of a cat or dog, and let AI identify it!")

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
            # Replace this URL with your Google Drive file's download link
            # To get the link: Upload model to Google Drive > Right-click > Get link > Set to "Anyone with the link"
            # Then use the file ID in this format: https://drive.google.com/uc?id=FILE_ID
            model_url = "https://drive.google.com/uc?id=YOUR_FILE_ID_HERE"
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
    st.error("⚠️ Model file not found! Please ensure 'dogs_vs_cats_production_model.keras' is in the same directory.")
    st.stop()

# File uploader
uploaded_file = st.file_uploader(
    "Choose an image...", 
    type=["jpg", "jpeg", "png"],
    help="Upload a clear image of a cat or dog"
)

if uploaded_file is not None:
    # Create two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📸 Uploaded Image")
        # Display uploaded image
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, use_column_width=True)
    
    with col2:
        st.subheader("🔍 Analysis")
        
        # Preprocess image
        with st.spinner("Analyzing image..."):
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
                result_class = "dog-result"
            else:
                label = "Cat"
                confidence = 1 - prediction
                emoji = "🐱"
                result_class = "cat-result"
        
        # Display results
        st.markdown(f"""
            <div class="prediction-box {result_class}">
                <h1>{emoji}</h1>
                <h2>It's a {label}!</h2>
                <h3>Confidence: {confidence*100:.2f}%</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Show prediction details
        st.metric("Raw Prediction Score", f"{prediction:.4f}")
        st.progress(float(confidence))
        
        # Additional info
        st.info(f"""
        **Model Details:**
        - Input Size: 128x128 pixels
        - Architecture: CNN with BatchNormalization & Dropout
        - Output: Binary classification (Cat=0, Dog=1)
        """)

# Instructions
with st.expander("ℹ️ How to use"):
    st.markdown("""
    1. Click on **"Browse files"** to upload an image
    2. Select a clear image of a cat or dog (JPG, JPEG, or PNG)
    3. Wait for the AI to analyze the image
    4. View the prediction result with confidence score
    
    **Tips for best results:**
    - Use clear, well-lit images
    - Ensure the animal is the main subject
    - Avoid heavily filtered or edited images
    """)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using TensorFlow & Streamlit")
