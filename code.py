import cv2
camera=cv2.VideoCapture(0)
ret, image=camera.read()
cv2.imwrite("myimage.jpg", image)
camera.release()
cv2.destroyAllWindows()
