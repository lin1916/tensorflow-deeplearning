import cv2

img_cv = cv2.imread('./wallhaven-1ked5w.jpg')
img_cv = img_cv@[[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
print(img_cv)
cv2.imshow("image", img_cv)
cv2.waitKey()
