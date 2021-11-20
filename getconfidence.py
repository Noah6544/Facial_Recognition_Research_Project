###IMPORTS
import mediapipe as mp
mp_face_mesh = mp.solutions.face_mesh
import cv2
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
import os
###IMPORTS

confidence = 0
###FILES/PATHS
store_image_path = "C:\\Users\path to where u want the new image to be stored\\place folder\\"
###FILES/PATHS
list = []
def get_confidence(list,data_text_file):
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
                #DO NOT PUT THIS IN THE ABOVE FOR LOOP, CREATES THE "that-one-bug where it ignores the function"
                data_text_file.write(str(file) + "," + str(detection.score[0] * 100) + "\n")
                #draws face/eye box/dots on image
                image = mp_drawing.draw_detection(annotated_image, detection)
                #shows images on screen.
                #cv2.imshow("Calculating Confidence.",annotated_image)
                #cv2.waitKey(1)
                #stores new annotated image in file path
                cv2.imwrite(store_image_path + str(idx) + '.png', annotated_image)
                #a variable that stores the %confidence
                confidence = detection.score[0]
                print("Confidence Assessment: " + str(confidence * 100) + "%")
