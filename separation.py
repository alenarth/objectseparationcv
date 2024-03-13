import cv2

img = cv2.imread('objetos.jpg')
img = cv2.resize(img, (600,500))

imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgcany = cv2.Canny(imggray, 30,200)
imgClose = cv2.morphologyEx(imgcany, cv2.MORPH_CLOSE, (7,7))

contours,hierarc = cv2.findContours(imgClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

numOb = 1
for cnt in contours:
    #cv2.drawContours(img, cnt, -1, (255,0,0), 2)
    x,y,w,h = cv2.boundingRect(cnt)
    object = img[y:y+h, x:x+w]
    cv2.imwrite(f'objects/objeto{numOb}.jpg', object)
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    numOb +=1


cv2.imshow('Imagem', img)
cv2.imshow('ImagemCinza', imggray)
cv2.imshow('ImagemCany', imgcany)
cv2.waitKey(0)