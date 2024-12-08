from encodings.utf_7 import encode

import cv2
import face_recognition as fr # ela trab com padrao RGB, ela faz varios
from face_recognition import face_distance

#processamentos dentro da imagens a primeira eh reconhecer o rost


# carregar a primeira img
imgElon = fr.load_image_file('Elon.jpg')   # a func faz a leitura da img
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)  # mudar a escala de cor
#imgTony = fr.load_image_file('Tony.jpg')   #img de teste
#imgTony = cv2.cvtColor(imgTony,cv2.COLOR_BGR2RGB)
imgElonTest = fr.load_image_file('ElonTest.jpg')   #img de teste
imgElonTest = cv2.cvtColor(imgElonTest,cv2.COLOR_BGR2RGB)


#funcao que retorna as coordenadas do rosto
faceLoc = fr.face_locations(imgElon)[0] # o 0 extrai a inf apenas de 1 face da posicao 1 do array
#methodo utilizando o algo HOG
cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(0,255,0),2) # 3 = representa o X e o Y representa o 0, e as coordenadas finais do retângulo ”já calculadas” (faceloc(1), faceloc(2))
#print(faceLoc)

#procedimento que vai extrair as 128 medidas do rosto da imagem = encodings
encodeElon = fr.face_encodings(imgElon)[0]  #retorna valores em array com as medidas da img, qdo for comparar com outra img vamos utilizar esse array com inf
#print(encodeElon)
encodeElonTest = fr.face_encodings(imgElonTest)[0]  # img teste
#encodeTony = fr.face_encodings(imgTony)[0]  # img teste

#comparar similaridade
#comparacao = fr.compare_faces([encodeElon],encodeTony)
comparacao = fr.compare_faces([encodeElon],encodeElonTest)


#comparacao = fr.compare_faces([encodeElon],encodeTony) # comparacao das img
comparacao = fr.compare_faces([encodeElon],encodeElonTest) # comparacao das img
#distancia = fr.face_distance([encodeElon],encodeTony) #distancia entre as imagens (indicacao que as pessoas nao sao correspondentes)
distancia = fr.face_distance([encodeElon],encodeElonTest) #distancia entre as imagens (indicacao que as pessoas nao sao correspondentes)


print(comparacao, distancia)


#exibir a imagem
cv2.imshow('Elon',imgElon)
#cv2.imshow('Tony',imgTony)
cv2.imshow('ElonTest',imgElonTest)
cv2.waitKey(0)
