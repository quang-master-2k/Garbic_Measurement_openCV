import sys
import os
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QImage, QPixmap

class CaptureApp(QWidget):
    def __init__(self):
        super().__init__()

        self.capture = cv2.VideoCapture(0)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Capture App')
        self.setGeometry(100, 100, 640, 480)

        self.layout = QVBoxLayout()

        self.label = QLabel(self)
        self.layout.addWidget(self.label)

        self.capture_btn = QPushButton('Capture', self)
        self.capture_btn.clicked.connect(self.capture_image)
        self.layout.addWidget(self.capture_btn)

        self.setLayout(self.layout)

    def capture_image(self):
        ret, frame = self.capture.read()
        if ret:
            # Create a folder if it doesn't exist
            if not os.path.exists('CapImg'):
                os.makedirs('CapImg')

            # Save the captured image to the "CapImg" folder
            img_name = 'CapImg/captured_image.png'
            cv2.imwrite(img_name, frame)

            # Display the captured image
            img = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            self.label.setPixmap(pixmap)
        else:
            QMessageBox.warning(self, 'Warning', 'Failed to capture image.')

    def closeEvent(self, event):
        self.capture.release()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaptureApp()
    window.show()
    sys.exit(app.exec_())
