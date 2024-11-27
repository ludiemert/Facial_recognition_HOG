import cv2
import face_recognition as fr # ela trab com padrao RGB

# carregar a primeira img
imgElon = fr.load_image_file('Elon.jpg')   # a func faz a leitura da img
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)  # mudar a escala de cor

#exibir a imagem
cv2.imshow('Elon',imgElon)
cv2.waitKey(0)
