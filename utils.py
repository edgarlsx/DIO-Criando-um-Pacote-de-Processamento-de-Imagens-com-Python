def is_valid_image_format(file_path):
    """Verifica se o arquivo é uma imagem válida com base na extensão."""
    valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
    return any(file_path.endswith(ext) for ext in valid_extensions)
