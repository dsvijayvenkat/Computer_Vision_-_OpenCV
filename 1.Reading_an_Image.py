# Importing Required Libraries
import cv2
# define a class called ImageReader
class ImageReader:
    def __init__(self, filename):
        self.filename = filename
        
    def read_image(self):
        try:
            img = cv2.imread(self.filename)
            if img is None:
                raise Exception("Error: Unable to read image file")
        except Exception as e:
            print(str(e))
        else:
            return img

# create an instance of the ImageReader
reader = ImageReader(r"C:\PYTHON\AI_ML\OpenCV\Computer_vision.jpeg")
# call the read_image() method
img = reader.read_image()
if img is not None:
    # to show an image
    cv2.imshow("Image", img)
    # to dispaly upto defined time
    cv2.waitKey(0)
    # to close the open window
    cv2.destroyAllWindows()
# After executing this code seperate window will be open with an image which has given in the path.

# ### Reading an Image by allow the user to enter a link 

# Importing Required Libraries
import cv2
import urllib.request
import numpy as np

# define a class called ImageReader
class ImageReader:
    def __init__(self, url):
        self.url = url
        
    def read_image(self):
        try:
            resp = urllib.request.urlopen(self.url)
            img = np.asarray(bytearray(resp.read()), dtype="uint8")
            img = cv2.imdecode(img, cv2.IMREAD_COLOR)
            if img is None:
                raise Exception("Error: Unable to read image file")
        except Exception as e:
            print(str(e))
        else:
            return img

# create an instance of the ImageReader
url = input("Enter the URL of the image file: ")
reader = ImageReader(url)
img = reader.read_image()
if img is not None:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# After Executing above code It will ask you to enter an url link to diaplay an image.




