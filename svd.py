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

def svd(new_pixel, terms):
  new_pixel = np.matrix(new_pixel)
  U, s, V = np.linalg.svd(new_pixel, full_matrices=True)
  V1 = np.transpose(V)
  X = np.matrix(0)
  j = terms
  for i in range(j):
    X = np.add(s[i] * np.matrix(U[:,i]) * np.matrix(V1[i,:]), X)
  return X
  # np.savetxt('rank1_comb.txt', rank1_comb, fmt="%s")

if __name__ == '__main__':
  gray = image_to_gray()
  values = store_pixel_values(gray)
  pixel = return_single_vals(values)
  new_pixel = re_matrix(pixel)
  terms = int(raw_input("How many terms would you like to keep? (ex 100)\n"))
  new_pixel = svd(new_pixel, terms)
  np.savetxt('values.txt', new_pixel, fmt="%s")