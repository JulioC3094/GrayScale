from scipy import misc
from numpy import array
import matplotlib.pyplot as plt #mostrar imagen
image = misc.imread('1.jpg')
image=gray=array(image)
height, width, channel = image.shape
print ('Imagen Original')
plt.imshow(image)
plt.title('Original')
plt.show()

for row in range(height):
    for column in range(width):
        #gray[row, column]=[gray[row, column][0]*0.299,gray[row, column][1]*0.587, gray[row, column][2]*0.0114]
        p=gray[row, column][0]*0.2126+gray[row, column][1]*0.7152+ gray[row, column][2]*0.0722
        gray[row, column]= [p,p,p]

misc.imsave('GrayScale.jpg', gray)
print('ScaleGray')
plt.imshow(gray)
plt.title('Escala a grises')
plt.show()
print('Listo')
