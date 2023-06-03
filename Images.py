import cv2

img=cv2.imread("C:\\Users\\Tejas\\Pictures\\Screenshots\\Screenshot (1).png")
img=cv2.resize(img,(200,200))
cv2.imshow("Image",img)
print(img)
print(img[0])
print(type(img))
print(img.shape)
#200 - Height, 200 -Width, 3 channels
cv2.waitKey(0)
cv2.destroyAllWindows()