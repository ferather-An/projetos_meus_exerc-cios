"Aqui está um código Python que converte imagens HEIC para JPEG usando a biblioteca Pillow e pillow_heif. Você pode usar este código para converter suas imagens HEIC em um diretório específico."
# Certifique-se de ter Pillow e pillow_heif instalados:
"pip install Pillow pillow_heif"
"Andrezinho da cria, que fez esse script"

import os
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()
s
input_folder = "D:/imagens" #troca esse caminho pelo seu diretório das imagens. Exemplo: "C:/Users/Andrezinho/Downloads/imagens"
output_folder = os.path.join(input_folder, "convertidos")
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".heic"):
        input_path = os.path.join(input_folder, filename)
        
        image = Image.open(input_path)
        
        new_filename = os.path.splitext(filename)[0] + ".jpg"
        output_path = os.path.join(output_folder, new_filename)
        
        image.save(output_path, format="JPEG")
        print(f"Convertido: {filename} -> {new_filename}")

print("Conversão concluída!")
