#An OpenCV barcode and QR code scanner with ZBarPython
# import the necessary packages
from pyzbar import pyzbar
import argparse
import glob
from PIL import Image 
#import cv2

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
# args = vars(ap.parse_args())

# # load the input image
# image = cv2.imread(args["image"])
#image = Image.open(args["image"])
# print("Image ", image.filename)

# # find the barcodes in the image and decode each of the barcodes
# barcodes = pyzbar.decode(image)

# loop over the detected barcodes
# for barcode in barcodes:
# 	# extract the bounding box location of the barcode and draw the
# 	# bounding box surrounding the barcode on the image
# 	(x, y, w, h) = barcode.rect
# 	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
# 	# the barcode data is a bytes object so if we want to draw it on
# 	# our output image we need to convert it to a string first
# 	barcodeData = barcode.data.decode("utf-8")
# 	barcodeType = barcode.type
 
# 	# draw the barcode data and barcode type on the image
# 	text = "{} ({})".format(barcodeData, barcodeType)
# 	cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
# 		0.5, (0, 0, 255), 2)
 
# 	# print the barcode type and data to the terminal
# 	print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
 
# # show the output image
# cv2.imshow("Image", image)
# cv2.waitKey(0)

def findBarcodeValue(image):
    # find the barcodes in the image and decode each of the barcodes
    barcodes = pyzbar.decode(image)
    image_dict = {}
    barcode_dict = {}
    barcode_list = []
    # loop over the detected barcodes
    for barcode in barcodes:
    	# the barcode data is a bytes object so if we want to draw it on
    	# our output image we need to convert it to a string first
        barcode_dict['barcode_data'] = barcode.data.decode("utf-8")
        barcode_dict['barcode_type'] = barcode.type
        barcode_list.append(barcode_dict)

    image_dict['barcode_data'] = barcode_list
    image_dict['image_name'] = image.filename.split("\\")[1]
    print("Image Dict ", image_dict)
    return image_dict


# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
# args = vars(ap.parse_args())

# image_data = findBarcodeValue(Image.open(args["image"]))
# print(image_data)

image_list = []

for filename in glob.glob('Images/*.jpg'):
    image_dict = findBarcodeValue(Image.open(filename))
    image_list.append(image_dict)

print("Barcode value for all images ", image_list)
