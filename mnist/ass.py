# -*- coding:utf-8 -*-
import cv2
img= cv2.imread('ass.jpg')          #(616, 690, 3)
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
"""rows=img.shape[0]
cols=img.shape[1]
for row in range(rows):
	for col in range(cols):
		if img.item(row,col,2)>img.item(row,col,0)+img.item(row,col,1) or img.item(row,col,2)+img.item(row,col,0)+img.item(row,col,1)>290:
			img[row,col]=[255,255,255]
		else:
			img[row,col]=[255,255,255]-img[row,col]"""
cv2.imshow('img',img)
cv2.imshow('dst')
cv2.imshow('gray',gray)
cv2.waitKey(0)
