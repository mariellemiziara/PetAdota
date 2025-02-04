import requests
import csv

dog_api_url = "https://dog.ceo/api/breeds/image/random"

dog_images = []

for _ in range(10):
    response = requests.get(dog_api_url)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "success":
            dog_images.append(data["message"])

dog_csv_file = "dog_images.csv"

with open(dog_csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Image URL"])
    for image_url in dog_images:
        writer.writerow([image_url])

print(f"Arquivo '{dog_csv_file}' criado com sucesso.")