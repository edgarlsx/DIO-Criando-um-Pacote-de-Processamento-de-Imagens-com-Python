from image_processing import open_image, save_image, resize_image, apply_blur, apply_sharpen

# Exemplo de uso
if __name__ == "__main__":
    img = open_image("exemplo.jpg")
    resized_img = resize_image(img, (300, 300))
    blurred_img = apply_blur(resized_img, intensity=3)
    sharpened_img = apply_sharpen(blurred_img)
    save_image(sharpened_img, "saida.jpg")
