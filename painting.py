import time

def decreaseRed(picture):
    for pix in getPixels(picture):
        rValue = getRed(pix)
        setRed (pix, rValue * 0.5)

def createSequence():
    myPic = makePicture (getMediaPath( "test.jpg" ))
    repaint (myPic)
    time.sleep(3)

    decreaseRed (myPic)

    repaint (myPic)

    width = getWidth (myPic)
    print("this image is " + str(width) + " pixels wide")
