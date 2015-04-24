# dependencies
import numpy as np
import Image
import sys

def image_to_gray():
  # Converts the image to grayscale
  # returns the image
  image = Image.open('image.jpg').convert('LA')
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
  new_pixel = np.matrix(new_pixel)
  U, s, V = np.linalg.svd(new_pixel, full_matrices=False)
  X = np.matrix(0)
  j = terms
  for i in range(j):
    X = np.add(s[i] * np.matrix(U[:,i]) * np.matrix(V[i,:]), X)
  max_val = X.max()
  min_val = X.min()
  X = (np.absolute(X) / (max_val - min_val)) * 255
  for vals in range(X):
    for numbers in X[vals]:
      if numbers > 255:
        numbers = 255
      elif numbers < 0:
        numbers = 0
  return X.astype(int)

def pixel_to_image(og_pixel):
  # create an image from the pixel values found previously
  # saves the new image
  global LENGTH, WIDTH, HEIGHT 
  image = Image.new('RGB', (WIDTH, HEIGHT))
  image.save('output.png')
  pixels = image.load()
  for i in range(WIDTH):
    for j in range(HEIGHT):
      pixels[j,i] = (og_pixel[j][i], og_pixel[j][i], og_pixel[j][i])
  image.save('output.png')

if __name__ == '__main__':
  gray = image_to_gray()
  values = store_pixel_values(gray)
  pixel = return_single_vals(values)
  new_pixel = re_matrix(pixel)
  terms = int(raw_input("How many terms would you like to keep? (ex 100)\n"))
  svd_pixel = svd(new_pixel, terms)
  np.savetxt('test.txt', svd_pixel, fmt="%s")
  pixel_to_image(svd_pixel)

  np.savetxt('values.txt', svd_pixel, fmt="%s")
