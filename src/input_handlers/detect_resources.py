'''
This application takes care of listing valid resources in one image
@since 27-11-2018
@author amit.dali@gmail.com
'''

from resourcedetector import ResourceDetector
from deploytemplate import DeployTemplate
import argparse
import imutils
import cv2

default_width=300

def getInputs():
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True,
		help="path to the input image")
	args = vars(ap.parse_args())
	return args

def getImage(args):
	image = cv2.imread(args["image"])
	return image 

def getResizedImage(args):
	image = getImage(args)
	resized = imutils.resize(image, width=default_width)
	return resized

def getRatio(args):
	image = getImage(args)
	resized = getResizedImage(args)
	ratio = image.shape[0] / float(resized.shape[0])
	return ratio

def getThreshold(args):
	resized = getResizedImage(args)
	gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
	return thresh

def getContours(args):
	thresh = getThreshold(args)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	return cnts

def getResources(args):
	rd = ResourceDetector()
	ratio = getRatio(args)
	resources = []
	cnts = getContours(args)
	for c in cnts:
		M = cv2.moments(c)
		cX = int((M["m10"] / M["m00"]) * ratio)
		cY = int((M["m01"] / M["m00"]) * ratio)
		resource = rd.detect(c)
		resources.append(resource)
		print('Resources='+resource)
	return resources

def main():
	inputs = getInputs()
	resources = getResources(inputs)
	deployTemplate = DeployTemplate()
	for resource in resources:
		if(resource == "compute"):
			deployTemplate.createStack()
		
main()
