"""
Example client code demonstrating how to use the Cat vs Dog Classifier API
"""

import requests
import json
from pathlib import Path


# API Configuration
API_BASE_URL = "http://localhost:8000"  # Change to your deployed URL


def test_health():
    """Test if the API is running and healthy"""
    response = requests.get(f"{API_BASE_URL}/health")
    print("Health Check:")
    print(json.dumps(response.json(), indent=2))
    print()


def test_model_info():
    """Get information about the model"""
    response = requests.get(f"{API_BASE_URL}/model/info")
    print("Model Information:")
    print(json.dumps(response.json(), indent=2))
    print()


def predict_single_image(image_path: str):
    """
    Predict a single image
    
    Args:
        image_path: Path to the image file
    """
    print(f"Predicting image: {image_path}")
    
    # Open and send the image file
    with open(image_path, "rb") as image_file:
        files = {"file": (Path(image_path).name, image_file, "image/jpeg")}
        response = requests.post(f"{API_BASE_URL}/predict", files=files)
    
    if response.status_code == 200:
        result = response.json()
        print("✅ Prediction successful!")
        print(f"   Prediction: {result['prediction']}")
        print(f"   Confidence: {result['confidence_percentage']}%")
        print(f"   Probabilities: Cat={result['probabilities']['cat']}%, Dog={result['probabilities']['dog']}%")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.json())
    print()


def predict_batch(image_paths: list):
    """
    Predict multiple images in a single request
    
    Args:
        image_paths: List of image file paths
    """
    print(f"Batch prediction for {len(image_paths)} images...")
    
    # Prepare multiple files
    files = [
        ("files", (Path(path).name, open(path, "rb"), "image/jpeg"))
        for path in image_paths
    ]
    
    response = requests.post(f"{API_BASE_URL}/predict/batch", files=files)
    
    # Close file handles
    for _, (_, file_obj, _) in files:
        file_obj.close()
    
    if response.status_code == 200:
        result = response.json()
        print("✅ Batch prediction successful!")
        for item in result["results"]:
            if item["success"]:
                print(f"   {item['filename']}: {item['prediction']} ({item['confidence_percentage']}%)")
            else:
                print(f"   {item['filename']}: Error - {item['error']}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.json())
    print()


def predict_from_url(image_url: str):
    """
    Predict an image from a URL
    
    Args:
        image_url: URL of the image
    """
    print(f"Predicting image from URL: {image_url}")
    
    # Download image from URL
    image_response = requests.get(image_url)
    
    if image_response.status_code == 200:
        # Send to prediction API
        files = {"file": ("image.jpg", image_response.content, "image/jpeg")}
        response = requests.post(f"{API_BASE_URL}/predict", files=files)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Prediction successful!")
            print(f"   Prediction: {result['prediction']}")
            print(f"   Confidence: {result['confidence_percentage']}%")
        else:
            print(f"❌ Prediction error: {response.status_code}")
            print(response.json())
    else:
        print(f"❌ Failed to download image from URL")
    print()


# Example usage with Python requests library
if __name__ == "__main__":
    print("=" * 60)
    print("Cat vs Dog Classifier API - Client Examples")
    print("=" * 60)
    print()
    
    # Test API health
    test_health()
    
    # Get model information
    test_model_info()
    
    # Example 1: Single image prediction
    # Replace with your actual image path
    # predict_single_image("path/to/your/cat_image.jpg")
    
    # Example 2: Batch prediction
    # image_list = [
    #     "path/to/cat1.jpg",
    #     "path/to/dog1.jpg",
    #     "path/to/cat2.jpg"
    # ]
    # predict_batch(image_list)
    
    # Example 3: Predict from URL
    # predict_from_url("https://example.com/cat_image.jpg")
    
    print("=" * 60)
    print("Note: Uncomment the examples above and provide image paths to test")
    print("=" * 60)
