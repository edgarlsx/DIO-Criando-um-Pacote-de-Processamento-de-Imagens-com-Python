from PIL import Image

def open_image(file_path):
    """Abre uma imagem a partir de um caminho."""
    return Image.open(file_path)

def save_image(image, file_path):
    """Salva uma imagem em um caminho específico."""
    image.save(file_path)

def resize_image(image, size):
    """Redimensiona a imagem para um novo tamanho (largura, altura)."""
    return image.resize(size)
