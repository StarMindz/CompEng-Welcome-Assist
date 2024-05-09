import sys
import os
import time
import atexit
import glob
import threading
import cv2

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow, QLabel
from PyQt5.QtCore import QObject, pyqtSignal, Qt, QTimer, QSize
from PyQt5.QtGui import QIcon,QPixmap,QImage

from face import detect_faces
from face import perform_image_recognition
from db_handler import query_profile_information


# known_labels = ['Abdullahi', 'Fatima', 'Sufyan', 'Yahya']
confidence_threshold = 0.8

detect_faces_flag = True
cam_url = "rtsp://admin:Abby1234*@192.168.1.1:554/foo.sdp"

import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

# Define a signal class for person detection
class PersonDetectionSignal(QObject):
    switch_to_profile_screen = pyqtSignal(dict)

# Create an instance of the signal class
person_detection_signal = PersonDetectionSignal()


def stop_detection(cap):
    global detect_faces_flag
    detect_faces_flag = False
    # Release video capture device
    if cap.isOpened():  # Check if the capture is opened before releasing
        cap.release()
    cv2.destroyAllWindows()


def get_image_files(folder):
    """
    Scan the given folder and store all files with image extensions in a list.

    Args:
        folder (str): The path to the folder to scan.

    Returns:
        list: A list containing the paths of all image files found.
    """
    image_files = []

    # Ensure the folder exists
    if not os.path.exists(folder):
        print("Folder does not exist.")
        return image_files

    # Iterate through all files in the folder
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        
        # Check if the file is a regular file and has an image extension
        if os.path.isfile(file_path) and any(file.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']):
            image_files.append(file_path)

    return image_files

def show_screen(screen_class_name, *args):
    # Check if there's a current widget being displayed
    current_widget = widget.currentWidget()
    if current_widget:
        current_widget.close()  # Close the current widget if it exists

    # Show the next screen
    current_screen = screen_class_name(*args)
    widget.addWidget(current_screen)
    widget.setCurrentWidget(current_screen)
    print(f"Showing {screen_class_name.__name__}")


class SlideshowWindow:
    def __init__(self, image_files, label):
        self.image_files = image_files
        self.current_index = 0
        self.label = label
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextImage)
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animateTransition)

        # Start the animation timer with your desired duration (in milliseconds)
        self.animation_timer.start(3000)

    def start(self):
        self.label.setPixmap(QPixmap())
        self.nextImage()
        self.timer.start(5000)  # Change the delay between slides (in milliseconds)

    def nextImage(self):
        if self.current_index >= len(self.image_files):
            self.current_index = 0
        image_path = self.image_files[self.current_index]
        pixmap = self.scaledPixmap(image_path, self.label.size())
        self.next_pixmap = pixmap
        self.label.setPixmap(pixmap)
        self.current_index += 1

    def animateTransition(self):
        opacity = self.label.windowOpacity()
        if opacity > 0:
            opacity -= 0.05  # Adjust the decrement value for smoother transition
            self.label.setWindowOpacity(opacity)
        else:
            self.label.setPixmap(self.next_pixmap)
            self.animation_timer.stop()
            self.label.setWindowOpacity(1.0)  # Reset opacity for next image

    def scaledPixmap(self, path, size):
        img = QImage(path)
        img = img.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return QPixmap.fromImage(img)

class DefaultScreen(QDialog):
    def __init__(self):
        super(DefaultScreen, self).__init__()
        loadUi("ui/default.ui", self)
        self.setWindowFlags(Qt.Window)
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        self.face_detection_thread = threading.Thread(target=self.start_face_detection)
        self.face_detection_thread.start()

    def start_face_detection(self):
        # cap = cv2.VideoCapture(cv2.CAP_DSHOW)
        cap = cv2.VideoCapture(cam_url, cv2.CAP_FFMPEG)
        global detect_faces_flag
        detect_faces_flag = True

        def image_recognition_callback(face_image):
            global detect_faces_flag
            
            if not detect_faces_flag:
                return
            
            label, confidence = perform_image_recognition(face_image)
            print(label)
            if label is not None and confidence >= confidence_threshold:
                profile_info = query_profile_information(label)
                print("Recognized:", profile_info)
                print('confidence ->', confidence)
                person_detection_signal.switch_to_profile_screen.emit   (profile_info)
                stop_detection(cap)
            else:
                print("Unknown, low confidence:", confidence)

        detect_faces(image_recognition_callback, cap)
    

    def show_screen_with_timeout(self, screen_class_name, *args):
        current_widget = widget.currentWidget()
        if current_widget:
            current_widget.close()

        current_screen = screen_class_name(*args)
        widget.addWidget(current_screen)
        widget.setCurrentWidget(current_screen)
        print(f"Showing {screen_class_name.__name__}")
        

    def switch_back_to_default_screen(self, screen_instance):
        screen_instance.start_face_detection()
        widget.setCurrentIndex(0)
        global detect_faces_flag
        detect_faces_flag = True


    def closeEvent(self, event):
        # Ensure camera is released when the application is closed
        global detect_faces_flag
        detect_faces_flag = False
        # cap.release()
        event.accept()


    def showEvent(self, event):
        super().showEvent(event)
        slideshow_images = get_image_files("slideshow_images_folder")
        if slideshow_images:
            self.slideshow_window = SlideshowWindow(slideshow_images, self.slideshow)
            self.slideshow_window.start()

class ProfileScreen(QDialog):
    def __init__(self, profile):
        super().__init__()
        loadUi("ui/profile.ui", self)
        self.setWindowFlags(Qt.Window)
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)
   
        self.display_profile(profile)

        # Start the timer when the profile screen is displayed
        self.switch_back_timer = QTimer()
        self.switch_back_timer.timeout.connect(self.show_default_screen)
        self.switch_back_timer.start(5000)  # 20 seconds in milliseconds

    def show_default_screen(self):
        # Stop the timer and switch back to the default screen
        self.switch_back_timer.stop()
        self.close()
        show_screen(DefaultScreen)

    def display_profile(self, profile):
        print('profile -> ', profile)
        print(f"Displaying Profile {profile.get('name', profile)}....")

        self.about.setStyleSheet("font-size: 14px;")
        self.position.setStyleSheet("font-size: 14px;")
        self.specialization.setStyleSheet("font-size: 14px;")
        self.contact.setStyleSheet("font-size: 14px;")
        
        self.about.setText(profile.get('about', ''))
        self.position.setText(profile.get('position', ''))
        self.specialization.setText(profile.get('specialization', ''))  
        self.contact.setText(profile.get('contact', ''))

        image_path = profile.get('imageUrl', '')
        pixmap = QPixmap(image_path)
        self.image.setPixmap(pixmap.scaledToWidth(self.image.width(), Qt.SmoothTransformation))


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("ui/default.ui", self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

class SlideshowWindow:
    def __init__(self, image_files, label):
        self.image_files = image_files
        self.current_index = 0
        self.label = label
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextImage)

    def start(self):
        self.label.setPixmap(QPixmap())
        self.nextImage()
        self.timer.start(2000)

    def nextImage(self):
        if self.current_index >= len(self.image_files):
            self.current_index = 0
        image_path = self.image_files[self.current_index]
        pixmap = self.scaledPixmap(image_path, self.label.size())
        self.label.setPixmap(pixmap)
        self.current_index += 1

    def scaledPixmap(self, path, size):
        img = QImage(path)
        img = img.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return QPixmap.fromImage(img)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("Running App....")
    widget = QtWidgets.QStackedWidget()
    print("App is Running....")
    show_screen(DefaultScreen)
    widget.show()

    person_detection_signal.switch_to_profile_screen.connect(lambda profile_info: show_screen(ProfileScreen, profile_info))

    # Connect the aboutToQuit signal to release the camera
    app.aboutToQuit.connect(stop_detection)


    try:
        sys.exit(app.exec_())
    except:
        print("Exiting App")
