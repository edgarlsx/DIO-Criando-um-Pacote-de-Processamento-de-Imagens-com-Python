import cv2
import numpy as np

def apply_blur(image, intensity=5):
    """Aplica um desfoque (blur) à imagem."""
    img_np = np.array(image)
    blurred = cv2.GaussianBlur(img_np, (intensity, intensity), 0)
    return Image.fromarray(blurred)

def apply_sharpen(image):
    """Aplica um filtro de nitidez à imagem."""
    img_np = np.array(image)
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    sharpened = cv2.filter2D(img_np, -1, kernel)
    return Image.fromarray(sharpened)
