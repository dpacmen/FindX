import numpy as np
import argparse
import cv2, imutils

#argument parser 

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--puzzle", required = True,
	help = "Path to puzzle image")
ap.add_argument("-w", "--waldo", required = True,
	help = "Path to waldo image")
args = vars(ap.parse_args())

puzzle = cv2.imread(args["puzzle"])
waldo = cv2.imread(args["waldo"])

wHeight, wWidth = waldo.shape[:2]

result = cv2.matchTemplate(puzzle, waldo, cv2.TM_CCOEFF)
(_,_, minLoc, maxLoc) = cv2.minMaxLoc(result)

tl = maxLoc
br = (tl[0] + wWidth, tl[1] + wHeight)
selected_region = puzzle[tl[1]:br[1], tl[0]:br[0]]

cv2.imshow("puzzle", imutils.resize(puzzle, height = 700))
cv2.imshow("Waldo", waldo)
cv2.waitKey(0)

