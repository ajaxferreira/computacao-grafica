import cv2
import numpy as np


img = cv2.imread('imagem 3D Foguete.jpg')


print(img.shape)


pontos = np.array([[100, 50], [200, 50], [250, 150], [150, 200], [50, 150]], np.int32)

cv2.polylines(img, [pontos], isClosed=True, color=(255, 0, 0), thickness=2)

centro = (300, 200)  
raio = 50            
cor = (0, 255, 0)    
espessura = 3        

cv2.circle(img, centro, raio, cor, espessura)
cv2.imshow('Imagem com Poligono e Circulo', img)
cv2.waitKey(0)
cv2.destroyWindow('Imagem com Poligono e Circulo')
