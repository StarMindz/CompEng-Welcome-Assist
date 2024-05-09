import cv2
import os
print(".............Starting face detection................")

# Load pre-trained face detection model
print("Loading pre-trained face detection model")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture
print("Initializing video camera")
video_capture = cv2.VideoCapture(0)  # Use 0 for webcam, or provide video file path

# Create directory to save the frames with complete human faces
output_dir = 'complete_faces'
os.makedirs(output_dir, exist_ok=True)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    # print("Capturing frames from video feed")

    # Convert frame to grayscale for face detection
    # print("Converting to grayscale")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame with adjusted parameters
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    # Check if a complete human face is detected
    complete_face_detected = False
    for (x, y, w, h) in faces:
        # Check if the face extends from chest to head
        if y > h / 2:
            complete_face_detected = True
            break

    # Save the frame if a complete human face is detected
    if complete_face_detected:
        print("Complete Human Face Detected")
        
        # Save the frame
        print("Saving deected image")
        
        frame_filename = os.path.join(output_dir, f'frame_{len(os.listdir(output_dir))}.jpg')
        cv2.imwrite(frame_filename, frame)
        print("Complete human face Saved.")

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture
video_capture.release()
cv2.destroyAllWindows()
