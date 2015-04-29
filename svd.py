# dependencies
import numpy as np
import Image
import sys
import copy

def image_to_gray():
  # Converts the image to grayscale
  # returns the image
  image = Image.open('image.jpg').convert('LA')
  image.save('bw.png')
  return image

def store_pixel_values(gray):
  # gets the value of the pixel at a coordinate
  # returns all values with color value
  global LENGTH, WIDTH, HEIGHT
  HEIGHT, WIDTH = gray.size
  LENGTH = HEIGHT * WIDTH
  image = gray.load()
  pixel = []
  for i in range(WIDTH):
    for j in range(HEIGHT):
      pixel.append(image[i,j])
  return pixel

def return_single_vals(values):
  # removes the color value of pixels and just leaves gray
  # returns the values
  pixel = []
  for i in values:
    pixel.append(i[0])
  return pixel

def re_matrix(pixel):
  # converts the list of pixel values into proper matrix
  # returns the matrices
  global LENGTH, WIDTH, HEIGHT
  new_pixel = []
  line = []
  for i in range(LENGTH):
      line.append(pixel[i])
      if (i + 1) % WIDTH == 0:
        new_pixel.append(line)
        line = []
  return new_pixel

def svd(new_pixel, terms):
  global WIDTH, HEIGHT
  new_pixel = np.matrix(new_pixel)
  U, s, V = np.linalg.svd(new_pixel, full_matrices=False)
  X = np.matrix(0)
  j = terms
  for i in range(j):
    X = np.add(s[i] * np.matrix(U[:,i]) * np.matrix(V[i,:]), X)
  max_val = X.max()
  min_val = X.min()
  X = (np.abs(X) / (max_val - min_val)) * 255
  (WIDTH, HEIGHT) = X.shape
  for i in range(WIDTH):
    for j in range(HEIGHT):
      if X[i, j] > 255:
        X[i, j] = 255
      elif X[i, j] < 0:
        X[i, j] = 0
      if X[i, j]>=0 and X[i, j] <=255:
        pass
      else:
        X[i, j] = 0
  X=np.array(X)
  (WIDTH, HEIGHT) = X.shape
  output_list=[]
  output_list = copy.deepcopy(X)
  return output_list

def pixel_to_image(og_pixel):
  # create an image from the pixel values found previously
  # saves the new image
  global WIDTH, LENGTH
  image = Image.new('RGB', (WIDTH, WIDTH))
  image.save('output.png')
  pixels = image.load()
  for i in range(WIDTH-1):
    for j in range(WIDTH-1):
      pixels[j,i] = (int(og_pixel[j][i]), int(og_pixel[j][i]), int(og_pixel[j][i]))
  image.save('output.png')

if __name__ == '__main__':
  gray = image_to_gray()
  values = store_pixel_values(gray)
  pixel = return_single_vals(values)
  new_pixel = re_matrix(pixel)
  terms = int(raw_input("How many terms would you like to keep? (ex 100)\n"))
  svd_pixel = svd(new_pixel, terms)
  pixel_to_image(svd_pixel)

  np.savetxt('values.txt', svd_pixel, fmt="%s")