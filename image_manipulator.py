from PIL import Image
import os




image_name = raw_input('Enter image to be analysed: ')

image = Image.open(image_name)
os.system('cls')

def initial_run(image_object):
	print "[+] Welcome to the image analysis framework"
	print "Option 1: Image Information"
	print "Option 2: Colour Splitter"
	print "Further options incoming: image mode changer, steganography analysis"

	choice = raw_input('\nEnter option number: ')

	if choice == str(1):
		image_information(image_object)
	elif choice == str(2):
		colour_splitter(image_object)
	else:
		print "I dont understand that "


def image_information(image_object):
	print "[+] Information image: format:{}, size:{}, mode:{}".format(image.format, image.size, image.mode)

def colour_splitter(image):
	print "[!] WARNING: This function creates an independent image for each individual colour in the original image"
	print "[!] The function creates an image for each individual colour. This can create a large number of images."
	image_height = image.size[0]
	image_width = image.size[1]
	pixel_map = []
	unique_colours = image.getcolors()

	for x in range(0,image_height):
		print "I'm on column {} of {}".format(x, image_height)
		for y in range(0,image_width):
			# add this pixel to a list, with its location stored in it
			pixel_data = image.getpixel((x, y))
			pixel_location = (x, y)
			full_pixel_data = [pixel_data, pixel_location]
			pixel_map.append(full_pixel_data)
			#print pixel_data
	# for every unique colour, go through each pixel in the pixel_map, if its the same colour we will draw it to new.

	for colour in unique_colours:
		unique_colour_list = []
		for pixel in pixel_map:
			if pixel[0] == colour[1]:
				unique_colour_list.append(pixel)
			else:
				pass
		# then before it changes to the next colour, we need to create the image.
		make_new_image(image_height, image_width, unique_colour_list, colour)

def make_new_image(image_height, image_width, pixel_map, image_name):
	print "ON NEW COLOUR"
	name = "{}.png".format(image_name)
	new_image = Image.new("RGB", (image_height, image_width), "white")
	for pixel in pixel_map:
		new_image.putpixel((pixel[1]), (pixel[0]))
	new_image.save(name)

initial_run(image)

# image.new("RGB", (512,512), "white") creates a new blank image. this is good to draw on later.