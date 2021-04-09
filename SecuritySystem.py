import cv2,dropbox,random,time
startTime=time.time()
def takePic():
    number=random.randint(0,100)
    videoCapture=cv2.VideoCapture(0)
    result=True
    while result:
        ret,frame=videoCapture.read()
        imgName="Img"+str(number)+".jpg"
        cv2.imwrite(imgName,frame)
        startTime=time.time()
        result=False
    return imgName
    print("SNAPSHOT TAKEN")
    videoCapture.release()
    cv2.destroyAllWindows()
def uploadFiles(imgName):
    access_token="LgWmF8De57UAAAAAAAAAAUqhKUquJUTePdeSW7uKhcCWkEeKGqQwDCddjz3i9-2t"
    file_from=imgName
    file_to="/SecuritySystemPictures/"+imgName
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
           dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
           print("FILE UPLOADED")
def main():
    while True:
        if (time.time()-startTime>=5):
            name=takePic()
            uploadFiles(name)
main()



     


