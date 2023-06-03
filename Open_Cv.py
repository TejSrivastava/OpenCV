import cv2

img= cv2.imread("C:\\Users\\Tejas\\Pictures\\volume output.png",-1)
img= cv2.resize(img,(400,400))
img =cv2.resize(img,(400,400),fx=2,fy=0.5)
img= cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Tejas Srivastava' ,img)
cv2.imwrite('New_img.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()



