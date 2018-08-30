import cv2
import numpy as np
import matplotlib.pyplot as plt
def grayScale(img):


    # adapt the way considering weights
    print(img.shape[0:2])
    newImg = np.zeros(img.shape[0:2],np.uint8)

    for i in range(newImg.shape[0]):
        for j in range(newImg.shape[1]):
            count =  0.3*img[i,j][0]+0.59*img[i,j][1]+0.11*img[i,j][2]
            # print(count)
            newImg[i,j] = 0.3*img[i,j][0]+0.59*img[i,j][1]+0.11*img[i,j][2]

            #newImg[i,j] = max(img[i,j][0],img[i,j][1],img[i,j][2])
    # show the pic after greyscaling

    # cv2.imshow("newImage",newImg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # print(newImg.shape)
    cv2.imwrite('./doc/img/greyscale/01.jpg',newImg)
    plt.figure(1)
    plt.subplot(211)
    plt.imshow(img)
    plt.title("oriImg")
    plt.subplot(212)
    plt.imshow(newImg,"gray")
    plt.title("grayImg")
    plt.show()
    return  newImg
#二值化图像，根据结果自定义二值化效果最好
def binary(img):
    th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,0)
    ret, th2 =  cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret1, th3 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    cv2.imwrite('./doc/img/binary/01.jpg',th3)
    plt.figure(2)
    plt.subplot(311)
    plt.imshow(th1,"gray")
    plt.title("global binary")
    plt.subplot(312)
    plt.imshow(th2,"gray")
    plt.title("local binary")
    plt.subplot(313)
    plt.imshow(th3,"gray")
    plt.title("custom binary")
    plt.show()
    return img

img = cv2.imread('./doc/img/ori/01.png')
grayimg = grayScale(img)
binary(grayimg)
