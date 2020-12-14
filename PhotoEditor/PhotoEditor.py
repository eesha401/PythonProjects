
from PIL import Image, ImageFilter, ImageDraw, ImageChops
from math import sqrt


'''
INPUT -> image of choice, dimensions of desired resize as a string (eg: '500x300')
OUTPUT -> resized image
'''
def resizify(image, dimensions):
	x_index = dimensions.index('x') #extracts the dimensions from string input
	dim_width, dim_height = int(dimensions[0:x_index]), int(dimensions[x_index+1:])

	if dim_height > image.height or dim_width > image.width:
		return 'Invalid Input: Dimensions too large'
	else:
		return image.resize((dim_height, dim_width)).show()

'''
INPUT -> image of choice, sizes = desired demensions of cropped picture (tuple)'

OUTPUT -> cropped image
'''
def cropify(image, sizes):
	crop_image = image.crop(sizes)
	return crop_image.show()


'''
INPUT -> image of choice, radius = blur radius aka how blurry the user wants the image to be
OUTPUT -> blurred image
'''
def blurify(image, radius):
	return image.filter(ImageFilter.GaussianBlur(radius)).show()

'''
INPUT -> image of choice
OUTPUT -> black and white filter applied to image
'''
def grayscaleify(image):
	return image.convert('L').show()
