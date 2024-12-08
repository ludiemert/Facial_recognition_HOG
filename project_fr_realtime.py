import cv2
import face_recognition as fr
import os

encoders = []
nomes = []

# Criar encoders para as imagens na pasta 'Pessoas'
def criarEncoders():
    lista = os.listdir('Pessoas')
    for arquivo in lista:
        imAual = fr.load_image_file(f'Pessoas/{arquivo}')
        imAual = cv2.cvtColor(imAual, cv2.COLOR_BGR2RGB)
        faces = fr.face_encodings(imAual)
        if len(faces) > 0:
            encoders.append(faces[0])
            nomes.append(os.path.splitext(arquivo)[0])
            print(f"Encoder criado para: {nomes[-1]}")
        else:
            print(f"Nenhum rosto encontrado na imagem: {arquivo}")

# Comparar faces da webcam com os encoders
def compararWebcam():
    video = cv2.VideoCapture(0)

    while True:
        ret, img = video.read()
        if not ret:
            break

        imgP = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgP = cv2.cvtColor(imgP, cv2.COLOR_BGR2RGB)

        faceLocs = fr.face_locations(imgP)
        encodesCurFrame = fr.face_encodings(imgP, faceLocs)

        for encodeFace, faceLoc in zip(encodesCurFrame, faceLocs):
            matches = fr.compare_faces(encoders, encodeFace, tolerance=0.5)
            faceDis = fr.face_distance(encoders, encodeFace)

            matchIndex = None
            if len(faceDis) > 0:
                matchIndex = faceDis.argmin()

            if matchIndex is not None and matches[matchIndex]:
                name = nomes[matchIndex].upper()
                print(f"Reconhecido: {name}")
                y1, x2, y2, x1 = [coord * 4 for coord in faceLoc]
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), -1)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('Webcam', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

# Executar as funções
criarEncoders()
compararWebcam()
