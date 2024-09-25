# DIO-NTT DATA - Engenharia de Dados com Python
# Criando-um-Pacote-de-Processamento-de-Imagens-com-Python
 
## Estrutura do Projeto
image_processing/ <br/> 
│ <br/> 
├── __init__.py <br/> 
├── core.py        # Funções principais de manipulação de imagem <br/> 
├── filters.py     # Filtros de imagem (blur, sharpen, etc) <br/> 
├── utils.py       # Funções utilitárias (ex: carregar e salvar imagem) <br/> 
└── examples.py    # Exemplo de uso do pacote <br/> 

## Instalação das bibliotecas necessárias:
instalar Pillow e OpenCV usando pip:
pip install pillow opencv-python

## Código do pacote de processamento de imagens:
__init__.py

# ___Como Usar o Pacote___
## Depois de criar a estrutura, você pode usar o pacote para realizar operações em imagens. Por exemplo:
from image_processing import open_image, save_image, apply_blur

## Carregar imagem
img = open_image('minha_imagem.jpg')

## Aplicar filtro de desfoque
blurred_img = apply_blur(img, intensity=7)

## Salvar a imagem alterada
save_image(blurred_img, 'minha_imagem_blur.jpg')
