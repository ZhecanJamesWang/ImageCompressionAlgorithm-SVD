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
  # print pixel
  new_pixel = re_matrix(pixel)
  pixel_to_image(new_pixel)

  np.savetxt('values.txt', new_pixel, fmt="%s")
