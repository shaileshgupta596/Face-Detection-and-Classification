import cv2
import os
import numpy as np

def face_detector_function(img):
    gray_img=cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    #converting image into gray image
    face_haarcascade=cv2.CascadeClassifier("frontal_face.xml")
    #loading haarcascade of face which is having different face identification parameter
    faces_detected = face_haarcascade.detectMultiScale(gray_img ,1.9,3)
    #detecting number of faces in given image
    return gray_img ,faces_detected

def processing_of_training_data(directory):
    faces=[]
    faceID=[]
    directory= '''C:/Users/Harinarayan/Desktop/opencv/test_image'''
    for path,subdirectory,filenames in os.walk(directory):
        for filename in filenames:
            
            if filename.startswith("."):
                #skipping the system file
                continue
            
            
            folder_name =os.path.basename(path)
            #print(folder_name)
            # files consist inside the folder and we are printig above name of folder
            training_data_path=os.path.join(path,filename)
            #path of file 
            #print(training_data_path)


            test_img =cv2.imread(training_data_path)
            #reading the image using image path

            if test_img is None:
                #print("error in file loading")
                # some error in image do that in could not be loaded
                continue
         
            gray_img ,faces_detected=face_detector_function(test_img)
            # sending to face detector function written above

            if len(faces_detected)!=1:
                #print("No single face")
                #we are concern with one face because it is a classification to two person
                continue
    
            (x,y,w,h)=faces_detected[0]#reading the dimension of face of single face
            roi_gray_img =gray_img[x:x+w ,y:y+h]# extracting only face region

            faces.append(roi_gray_img)
            #appending face image into faces list
            faceID.append(int(folder_name))
            #appending the id to faces i.e foldername

    return faces ,faceID

            
    
def train_classifier_function(faces ,faceID):
    #creating a model
    face_recongnizer_model = cv2.face.LBPHFaceRecognizer_create()
    #using LBPHFaceRecognizer
    face_recongnizer_model.train(faces ,np.array(faceID))
    #training our model
    return face_recongnizer_model
    
def Draw_Rectangle(img ,face):
    (x,y,w,h)=face
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

def put_text_function(face,img,predicted_name):
    (x,y,w,h)=face
    cv2.putText(img,predicted_name,(x,y),cv2.FONT_HERSHEY_DUPLEX,5,(0,255,0),5)

#########################################################function end##############################################################
    
    
img = cv2.imread("SH.jpg")
# reading the image
gray_img,face_detected=face_detector_function(img)
#converting image into gray scale and detecting number of face

directory= '''test_image/'''
'''faces,faceID =processing_of_training_data(directory)'''
#collecting the training data in suitable form that will be send to classifier

'''face_recognizer_model=train_classifier_function(faces ,faceID)'''
#preparing model using above function

'''face_recognizer_model.save("facerecognizer.yml")'''
#uncomment the above three lines to make or create the model

#creating a call function
face_recognizer_model = cv2.face.LBPHFaceRecognizer_create()
#loading the model
face_recognizer_model.read("facerecognizer.yml")
identify={1:"mahendra",2:"virat" ,3:"rohit"}

for face in face_detected:
    (x,y,w,h)=face
    #reading the corrdinate of face deteted
    
    roi_gray_img = gray_img[x:x+w ,y:y+w]
    #taking only face area
    
    label ,confidence = face_recognizer_model.predict(roi_gray_img )
    print(label)
    print(confidence)
    #here we are passing traing image to model
    #it will return name of label and confidence value

    Draw_Rectangle(img ,face)
    #drawing rectangle function is called

    predicted_name=identify[label]
    put_text_function(face,img,predicted_name)
    #call of function which gives name to face

    
cv2.imshow("image",img)
#for showing image
cv2.waitKey(0)
#for interuption
cv2.destroyAllWindows()
########################################################Program End############################################################################
