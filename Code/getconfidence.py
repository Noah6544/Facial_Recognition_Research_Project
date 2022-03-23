import mediapipe as mp
mp_face_mesh = mp.solutions.face_mesh
import cv2
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
import os

#The entire backbone of this project.
#This function creates the numerical value of the % confidence of each image
#This is important because it creates the data which is used throughout the entirety of the project.
#I created this function by looking through mediapipe documents, I found a code sample, studied the code,
#then edited it to fit my own needs. ORIGINAL sample: https://google.github.io/mediapipe/solutions/face_detection

def get_confidence(list, data_text_file):
    #global confidence
    with mp_face_detection.FaceDetection(model_selection = 1, min_detection_confidence=0.1) as face_detection:
        for idx, file in enumerate(list):
            image = cv2.imread(file)
            # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
            results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if not results.detections:
                continue
            annotated_image = image.copy()
            for detection in results.detections:
                #DO NOT PUT THIS IN THE ABOVE FOR LOOP, CREATES THE "that-one-bug" where it ignores the function"

                     #writes the data detection score results (numerical % confidence) to the file, not needed currently
                data_text_file.write(str(file) + "," + str(detection.score[0] * 100) + ",")

                     #draws face/eye box/dots on image
                image = mp_drawing.draw_detection(annotated_image, detection)

                     #shows image WITH the DRAWN box on screen. annotated image DOES NOT have the box. not needed currently
                #cv2image = cv2.imread(image)
                #cv2.imshow(cv2image)

                    #shows annotated_image, which DOES NOT have the box around the face.
                cv2.imshow("Calculating Confidence.",annotated_image)
                cv2.waitKey(2000)

                    #creates new annotated image in file path, not needed currently.
                #cv2.imwrite(teststorepath + str(idx) + '.png', annotated_image)

                    #a variable that stores the %confidence as an integer
                confidence = detection.score[0]
                print("Confidence Assessment: " + str(confidence * 100) + "%")