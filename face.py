import cv2
import numpy as np
import tensorflow as tf
import torch
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image



# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Load TensorFlow Lite model for face processing
# interpreter = tf.lite.Interpreter(model_path="model4.tflite")
# interpreter.allocate_tensors()


# Define labels for classification
labels = ['Abdullahi', 'Bayero', 'Sufyan', 'Yahya']

# Define the region of interest (ROI) for face detection
roi = (100, 100, 500, 500)  # (x, y, width, height)

# Global variable to control face detection loop
detect_faces_flag = True

def detect_faces(image_recognition_callback, cap):
    global detect_faces_flag
    
    
    while detect_faces_flag:

        print('detect_face running')
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale for faster processing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces within the ROI
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
       
        if len(faces) > 0:
            # Extract the first detected face
            (x, y, w, h) = faces[0]
            
            # Draw rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Extract face region
            face = frame[y:y+h, x:x+w]

            # Convert NumPy array to RGB PIL Image
            face_image = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)  # Convert to RGB format

            cv2.imwrite('fccc.jpg', face_image)

            face_image = Image.fromarray(face_image)  # Create PIL Image
            
            # Call the callback function with the detected face image
            image_recognition_callback(face_image)
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release video capture device
    # cap.release()
    # cv2.destroyAllWindows()


mtcnn = MTCNN(image_size=240, margin=0, min_face_size=20) 
resnet = InceptionResnetV1(pretrained='vggface2').eval()

database = torch.load("model/database.pt") 
print('database ->', database)
embedding_list, name_list = database

def perform_image_recognition(input):

    img = Image.open(input) if isinstance(input, str) else input
    face, prob = mtcnn(img, return_prob=True) 
    
    if face is not None:  # Check if face is detected
        emb = resnet(face.unsqueeze(0)).detach()

        distance_list = []
        for idx, emb_db in enumerate(embedding_list):
            dist = torch.dist(emb, emb_db).item()  # compute distance between input and each face in db
            distance_list.append(dist)

        idx_min = distance_list.index(min(distance_list))  # get index of the lowest distance 

        print('name_list[idx_min], min(distance_list) ->', name_list[idx_min], min(distance_list))
        return name_list[idx_min], min(distance_list)  # recognized name, distance (lower is better)
    else:
        # Handle case where no face is detected
        print("No face detected in the input image")
        return None, None
