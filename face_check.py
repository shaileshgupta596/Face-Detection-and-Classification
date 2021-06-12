import os
import cv2
def face_detector_function(img):
    gray_img=cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    face_haarcascade=cv2.CascadeClassifier("frontal_face.xml")
    faces_detected = face_haarcascade.detectMultiScale(gray_img ,1.9,3)
    return gray_img ,faces_detected

faces=[]
faceID=[]
directory= '''C:/Users/Harinarayan/Desktop/opencv/test_image'''
for path,subdirectory,filenames in os.walk(directory):
    for filename in filenames:
        
        if filename.startswith("."):
            #skipping the system file
            continue
        
        
        folder_name =os.path.basename(path)
        print(folder_name)
        # files consist inside the folder and we are printig above name of folder
        training_data_path=os.path.join(path,filename)
        #path of file 
        print(training_data_path)


        test_img =cv2.imread(training_data_path)
        #reading the image using image path

        if test_img is None:
            print("error in file loading")
            # some error in image do that in could not be loaded
            continue
     
        gray_img ,faces_detected=face_detector_function(test_img)
        # sending to face detector function written above

        if len(faces_detected)!=1:
            print("No single face")
            print(len(faces_detected))
            # we are concern with one face because it is a classification of two person
            continue

        (x,y,w,h)=faces_detected[0]#reading the dimension of face of single face
        roi_gray_img =gray_img[x:x+w ,y:y+h]# extracting only face region

        faces.append(roi_gray_img)
        #appending face image into faces list
        faceID.append(folder_name)
        #appending the id to faces i.e foldername

print(faces)
print(faceID)

       

        

        
        
        

        

        
