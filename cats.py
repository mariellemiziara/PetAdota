import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

cat_api_url = "https://api.thecatapi.com/v1/images/search?limit=5"

cat_images = []

response = requests.get(cat_api_url)
if response.status_code == 200:
    data = response.json()
    cat_images = [cat["url"] for cat in data]
else:
    print("Erro ao acessar a Cat API. Código de status:", response.status_code)

if cat_images:
    fig, axes = plt.subplots(1, 5, figsize=(15, 5))
    for ax, img_url in zip(axes, cat_images):
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            img = Image.open(BytesIO(img_response.content))
            ax.imshow(img)
            ax.axis("off")
        else:
            ax.set_title("Erro ao carregar imagem")
            ax.axis("off")

    plt.tight_layout()
    plt.show()
else:
    print("Nenhuma imagem foi carregada.")