# 🚀 Deploying to Streamlit Cloud

## Step 1: Upload Model to Google Drive

1. Go to [Google Drive](https://drive.google.com)
2. Upload `dogs_vs_cats_production_model.keras` (111 MB)
3. Right-click the file → **Share** → **Get link**
4. Change access to **"Anyone with the link"**
5. Copy the link (format: `https://drive.google.com/file/d/FILE_ID/view?usp=sharing`)
6. Extract the `FILE_ID` from the URL

## Step 2: Update streamlit_app.py

Open `streamlit_app.py` and find this line (around line 52):
```python
model_url = "https://drive.google.com/uc?id=YOUR_FILE_ID_HERE"
```

Replace `YOUR_FILE_ID_HERE` with your actual file ID.

## Step 3: Commit and Push

```bash
git add streamlit_app.py requirements.txt
git commit -m "Add automatic model download from Google Drive"
git push
```

## Step 4: Streamlit Cloud will auto-deploy

The app will:
- Automatically download the model on first run
- Cache it for faster subsequent loads
- Work perfectly on Streamlit Cloud

## Alternative: Upload Model Directly to Streamlit

If you prefer, you can also:
1. Go to your Streamlit app settings
2. Add the model file in the "Advanced settings" → "Secrets"
3. But Google Drive method is simpler and works better for large files
