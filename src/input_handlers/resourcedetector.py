import cv2

class ResourceDetector:
	def __init__(self):
		pass

	def detect(self, c):
		resource = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		if len(approx) == 3:
			resource = "triangle"

		elif len(approx) == 4:
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			resource = "compute" if ar >= 0.95 and ar <= 1.05 else "firewall"

		elif len(approx) == 5:
			resource = "storage"

		else:
			resource = "database"

		return resource