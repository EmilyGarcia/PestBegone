#Emily Garcia
#Feb 12 2016
#Combine to get rid of pesky tourist

def getListOfPixels(imageList, i):
  return getPixels(imageList[i])


##*******************************************************************

listOfPics = []
folder = "/Users/rogeliogarcia/Documents/School/CST205 (MW)/PestBegone/Images/tourist_photos/"

for counter in range(1, 10):
  image = folder + str(counter) + ".png"
  picObject = makePicture(image)
  listOfPics.append(picObject)

#get height and width of image
h = getHeight(listOfPics[0])
w =  getWidth(listOfPics[0])

#makes a new picture with height and width of original pictures
newPic = makeEmptyPicture(w, h)

#gets the pixels of each image and saves them into a list
image1Pixels = getListOfPixels(listOfPics, 0)
image2Pixels = getListOfPixels(listOfPics, 1)
image3Pixels = getListOfPixels(listOfPics, 2)
image4Pixels = getListOfPixels(listOfPics, 3)
image5Pixels = getListOfPixels(listOfPics, 4)
image6Pixels = getListOfPixels(listOfPics, 5)
image7Pixels = getListOfPixels(listOfPics, 6)
image8Pixels = getListOfPixels(listOfPics, 7)
image9Pixels = getListOfPixels(listOfPics, 8)
newImagePixels = getPixels(newPic)

totalPixels = h * w

#finds colors of indiv
for i in range(0, totalPixels):
  listOfRed = []
  listOfGreen = []
  listOfBlue = []

  pixel = image1Pixels[i]
  listOfRed.append(getRed(pixel))
  listOfGreen.append(getGreen(pixel))
  listOfBlue.append(getBlue(pixel))

  pixel = image2Pixels[i]
  listOfRed.append(getRed(pixel))
  listOfGreen.append(getGreen(pixel))
  listOfBlue.append(getBlue(pixel))

  pixel = image3Pixels[i]
  listOfRed.append(getRed(pixel))
  listOfGreen.append(getGreen(pixel))
  listOfBlue.append(getBlue(pixel))

  pixel = image4Pixels[i]
  listOfRed.append(getRed(pixel))
  listOfGreen.append(getGreen(pixel))
  listOfBlue.append(getBlue(pixel))

  pixel = image5Pixels[i]
  listOfRed.append(getRed(pixel))
  listOfGreen.append(getGreen(pixel))
  listOfBlue.append(getBlue(pixel))

  pixel = image6Pixels[i]
  listOfRed.append(getRed(pixel))
  listOfGreen.append(getGreen(pixel))
  listOfBlue.append(pixel)

  pixel = image7Pixels[i]
  listOfRed.append(getRed(pixel))
  listOfGreen.append(getGreen(pixel))
  listOfBlue.append(getBlue(pixel))

  pixel = image8Pixels[i]
  listOfRed.append(getRed(pixel))
  listOfGreen.append(getGreen(pixel))
  listOfBlue.append(getBlue(pixel))

  pixel = image9Pixels[i]
  listOfRed.append(getRed(pixel))
  listOfGreen.append(getGreen(pixel))
  listOfBlue.append(getBlue(pixel))

  listOfRed.sort()
  listOfGreen.sort()
  listOfBlue.sort()

  setBlue(newImagePixels[i], listOfBlue[4])
  setRed(newImagePixels[i], listOfRed[4])
  setGreen(newImagePixels[i], listOfGreen[4])


show(newPic)
