import cv2
import numpy as np
import os
import re

# Aqui está a função para obter as imagens de treinamento
def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if re.match(r'.*\.\d+\.jpg$', f)]
    images = []
    labels = []
    for image_path in image_paths:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # Redimensionar a imagem para ter um tamanho fixo (por exemplo, 100x100)
        image = cv2.resize(image, (800, 800))
        images.append(image)
        labels.append(int(os.path.split(image_path)[-1].split(".")[1]))
    return images, labels

# Caminho para o conjunto de dados de treinamento
path = './dataset'

# Obter as imagens e os rótulos
images, labels = get_images_and_labels(path)

# Converter as listas em arrays numpy (OpenCV espera esses dados dessa forma)
images, labels = [np.array(lst) for lst in [images, labels]]

# Inicializar o reconhecedor facial
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Treinar o modelo
recognizer.train(images, labels)

#Salvar o modelo para usar no outo script:
recognizer.save('face_model.yml')
print('modelo criado e salvo!')
