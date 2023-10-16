from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('image_DB/Lucas.jpg')
plt.imshow(img1[:,:,::-1])
plt.show()

img2 = cv2.imread('image_DB/allao.PNG')
plt.imshow(img2[:,:,::-1])
plt.show()

resultado = DeepFace.verify(img1,img2)
print(resultado)