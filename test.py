# dependencies
import numpy as np
import Image
import sys

def image_to_gray():
  image = Image.open('image.jpg').convert('LA')
  return image

def store_pixel_values(gray):
  global length,width
  height, width = gray.size
  length=height*width
  image = gray.load()
  pixel = []
  for i in range(width):
    for j in range(height):
      pixel.append(image[i,j])
  return pixel

def return_single_vals(values):
  pixel = []
  for i in values:
    # print i[0] 
    pixel.append(i[0])
  return pixel

def re_matrix(pixel):
  global length,width
  new_pixel = []
  line=[]
  for i in range(length):
      line.append(pixel[i])
      if (i+1)%width==0:
        new_pixel.append(line)
        line=[]
  return new_pixel


if __name__ == '__main__':
  gray = image_to_gray()
  values = store_pixel_values(gray)
  pixel = return_single_vals(values)
  new_pixel=re_matrix(pixel)
  # print len(new_pixel)
  # print len(new_pixel[599])
  # print new_pixel
  np.savetxt('values.txt', new_pixel, fmt="%s")

  new_pixel=np.matrix(new_pixel)
  U, s, V = np.linalg.svd(new_pixel, full_matrices=True)

  V1=np.transpose(V)
  X=np.matrix(0)
  # print X.shape
  j=100
  for i in range(j):
    X=np.add(s[i]*np.matrix(U[:,i])*np.matrix(V1[i,:]),X)




  # print s.shape
  # print V1.shape
  # print U.shape
  print X.shape




  # np.savetxt('rank1_comb.txt', rank1_comb, fmt="%s")

