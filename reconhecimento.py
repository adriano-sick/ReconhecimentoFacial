import cv2, os

# Funcao para busca de arquivos
def encontrar_arquivo(name, path):
    for root, dirs, files in os.walk(path):
        if (name in files) or (name in dirs):
            print("O diretorio/arquivo {} encontra-se em: {}".format(name, root))
            return os.path.join(root, name)
    return encontrar_arquivo(name, os.path.dirname(path))

#funcao para listar/identificar os nomes
def get_name_dict(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    name_dict = {int(line.split(',')[0]): line.split(',')[1].strip() for line in lines}
    return name_dict

# Caminho para o arquivo de texto
path = './nomes.txt'

# Obter o dicionário de nomes
name_dict = get_name_dict(path)

# Importar arquivo XML
cv2path = os.path.dirname(cv2.__file__)
haar_path = encontrar_arquivo('haarcascades', cv2path)
xml_name = 'haarcascade_frontalface_alt2.xml' # XML do modelo pre treinado do OpenCv
xml_path = os.path.join(haar_path, xml_name)

# Inicializar o reconhecedor facial com parâmetros personalizados e carregar o modelo:
recognizer = cv2.face.LBPHFaceRecognizer_create(radius=2, neighbors=8, grid_x=16, grid_y=16, threshold=11.0)
recognizer.read('face_model.yml')

# TODO: Inicializar Classificador
clf = cv2.CascadeClassifier(xml_path)

# Inicializar webcam
cap = cv2.VideoCapture(0)

# Loop para leitura do conteúdo
while(not cv2.waitKey(20) & 0xFF == ord('c')):
        # Capturar proximo frame
        ret, frame = cap.read()

        # TODO: Converter para tons de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # TODO: Classificar
        faces = clf.detectMultiScale(gray)

       # Desenhar retangulo e nome
        for (x, y, w, h) in faces:
            # Prever o rosto usando o modelo treinado
            label, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            if confidence < 56:
                color = (0, 255, 0)  # Verde
                # Obter o nome do dono do rosto
                name = name_dict[label]
                # Desenhar o retângulo e o nome
                cv2.rectangle(frame, (x, y), (x+w, y+h), color)
                cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
            else:
                color = (255, 0, 0)  # Azul
                # Desenhar o retângulo
                cv2.rectangle(frame, (x, y), (x+w, y+h), color)


        # Visualizar
        cv2.imshow('frame',frame)

# Desligar a webcam
cap.release()

#Fechar janela do vídeo
cv2.destroyAllWindows()
cv2.waitKey(1)