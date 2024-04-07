from src import title
from PIL import Image
import os
print(title.titleName())
print("""                                                   - SILAMBU\n""")

def introPara():
     para = "----------This application is helpful for reading your images...----------\n"
     something = "HI , I WILL ACCESS YOUR COMPUTER ...."
     print(para,something)
     print("IF IT IS WORKING ONLY ON YOUR APPLICATION DOWNLOAD LOCATION ONLY .... V2 IS COMMING")

introPara()


def extensionChecker(inValue):
     imageExtentions = [".png",".jpg",".jpeg"]

     jpegFormat = inValue.rfind(imageExtentions[0])
     jpgFormat = inValue.rfind(imageExtentions[1])
     pngFormat = inValue.rfind(imageExtentions[2])

     if jpegFormat >= 1 or jpgFormat >= 1 or pngFormat >=1:
          curPath = os.getcwd()
          fullPath = curPath+"\{}".format(inValue)
          directory = os.path.exists(fullPath)
          if directory == True:
               img = Image.open(fullPath)
               img.show()
          else:
               print("No such file or directory: {}".format(fullPath))
     else:
          print("A file Extension must be {},{},{}".format(".jpg",".png","jpeg"))

def imageReader():
     try:
          data = input("image name : ")
          extensionChecker(data)
          
     except Exception as e:
          print(e)
imageReader()

