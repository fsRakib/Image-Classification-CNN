"""
API Client for Cat vs Dog Classifier Backend
Handles all communication with the FastAPI backend
"""

import requests
from typing import Dict, Any, Optional
from PIL import Image
import io


class ClassifierAPIClient:
    """
    Client for interacting with the Cat vs Dog Classifier API
    
    This client is designed to be framework-agnostic and can be used
    by any Python application (Streamlit, Flask, Django, CLI, etc.)
    """
    
    def __init__(self, base_url: str = "http://localhost:8000", timeout: int = 30):
        """
        Initialize API client
        
        Args:
            base_url: Base URL of the API server
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        **kwargs
    ) -> requests.Response:
        """
        Make HTTP request to API
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            **kwargs: Additional arguments for requests
            
        Returns:
            Response object
            
        Raises:
            requests.RequestException: On request failure
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(
            method=method,
            url=url,
            timeout=kwargs.pop('timeout', self.timeout),
            **kwargs
        )
        response.raise_for_status()
        return response
    
    def health_check(self) -> Dict[str, Any]:
        """
        Check API health status
        
        Returns:
            dict: Health status information
            
        Example:
            >>> client = ClassifierAPIClient()
            >>> status = client.health_check()
            >>> print(status['status'])
            'healthy'
        """
        try:
            response = self._make_request('GET', '/health', timeout=5)
            return {
                'available': True,
                'data': response.json()
            }
        except requests.exceptions.ConnectionError:
            return {
                'available': False,
                'error': 'Cannot connect to API server'
            }
        except requests.exceptions.Timeout:
            return {
                'available': False,
                'error': 'API server timeout'
            }
        except Exception as e:
            return {
                'available': False,
                'error': str(e)
            }
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the trained model
        
        Returns:
            dict: Model metadata and capabilities
            
        Example:
            >>> client = ClassifierAPIClient()
            >>> info = client.get_model_info()
            >>> print(info['model_name'])
            'Dogs vs Cats CNN Classifier'
        """
        response = self._make_request('GET', '/model/info')
        return response.json()
    
    def predict_from_file(self, file_path: str) -> Dict[str, Any]:
        """
        Predict from image file path
        
        Args:
            file_path: Path to image file
            
        Returns:
            dict: Prediction results
            
        Example:
            >>> client = ClassifierAPIClient()
            >>> result = client.predict_from_file('cat.jpg')
            >>> print(result['prediction'])
            'Cat'
        """
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f, 'image/jpeg')}
            response = self._make_request('POST', '/predict', files=files)
            return response.json()
    
    def predict_from_pil_image(
        self,
        image: Image.Image,
        filename: str = 'image.jpg'
    ) -> Dict[str, Any]:
        """
        Predict from PIL Image object
        
        Args:
            image: PIL Image object
            filename: Name for the image (optional)
            
        Returns:
            dict: Prediction results
            
        Example:
            >>> from PIL import Image
            >>> client = ClassifierAPIClient()
            >>> img = Image.open('dog.jpg')
            >>> result = client.predict_from_pil_image(img)
            >>> print(f"{result['prediction']}: {result['confidence_percentage']}%")
            'Dog: 95.2%'
        """
        # Convert PIL Image to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)
        
        files = {'file': (filename, img_byte_arr, 'image/jpeg')}
        response = self._make_request('POST', '/predict', files=files)
        return response.json()
    
    def predict_from_bytes(
        self,
        image_bytes: bytes,
        filename: str = 'image.jpg'
    ) -> Dict[str, Any]:
        """
        Predict from image bytes
        
        Args:
            image_bytes: Raw image bytes
            filename: Name for the image (optional)
            
        Returns:
            dict: Prediction results
        """
        files = {'file': (filename, image_bytes, 'image/jpeg')}
        response = self._make_request('POST', '/predict', files=files)
        return response.json()
    
    def predict_batch_from_files(
        self,
        file_paths: list[str]
    ) -> Dict[str, Any]:
        """
        Predict multiple images from file paths
        
        Args:
            file_paths: List of image file paths (max 10)
            
        Returns:
            dict: Batch prediction results
            
        Example:
            >>> client = ClassifierAPIClient()
            >>> results = client.predict_batch_from_files(['cat1.jpg', 'dog1.jpg'])
            >>> for result in results['results']:
            ...     print(f"{result['filename']}: {result['prediction']}")
        """
        if len(file_paths) > 10:
            raise ValueError("Maximum 10 images allowed per batch")
        
        files = []
        for path in file_paths:
            with open(path, 'rb') as f:
                files.append(('files', (path, f.read(), 'image/jpeg')))
        
        response = self._make_request('POST', '/predict/batch', files=files)
        return response.json()
    
    def close(self):
        """Close the session"""
        self.session.close()
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()


# Convenience functions for quick usage
def quick_predict(image_path: str, api_url: str = "http://localhost:8000") -> str:
    """
    Quick prediction from image path
    
    Args:
        image_path: Path to image file
        api_url: API base URL
        
    Returns:
        str: Prediction label ('Cat' or 'Dog')
        
    Example:
        >>> prediction = quick_predict('my_pet.jpg')
        >>> print(prediction)
        'Cat'
    """
    with ClassifierAPIClient(api_url) as client:
        result = client.predict_from_file(image_path)
        return result['prediction']


def quick_predict_with_confidence(
    image_path: str,
    api_url: str = "http://localhost:8000"
) -> tuple[str, float]:
    """
    Quick prediction with confidence score
    
    Args:
        image_path: Path to image file
        api_url: API base URL
        
    Returns:
        tuple: (prediction, confidence_percentage)
        
    Example:
        >>> prediction, confidence = quick_predict_with_confidence('my_pet.jpg')
        >>> print(f"{prediction} ({confidence}% confident)")
        'Dog (92.5% confident)'
    """
    with ClassifierAPIClient(api_url) as client:
        result = client.predict_from_file(image_path)
        return result['prediction'], result['confidence_percentage']


if __name__ == "__main__":
    # Example usage
    print("Cat vs Dog Classifier API Client")
    print("=" * 50)
    
    client = ClassifierAPIClient()
    
    # Check health
    health = client.health_check()
    if health['available']:
        print("✅ API is available and healthy")
        
        # Get model info
        info = client.get_model_info()
        print(f"\nModel: {info['model_name']}")
        print(f"Accuracy: {info['training_accuracy']}")
        print(f"Supported formats: {', '.join(info['supported_formats'])}")
    else:
        print(f"❌ API not available: {health['error']}")
        print("\nPlease start the API server:")
        print("  uvicorn api:app --reload")
