import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QLabel
from PySide6.QtGui import QPainter, QPen, QColor, QBrush, QImage, QPixmap
from PySide6.QtCore import Qt, QRectF


class DrawingWindow(QWidget): # QPainter
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Drawing Example")
        self.resize(200, 200)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(0, 0, 0), 2))  # Set pen properties
        painter.drawRect(10, 10, 100, 100)  # Draw a rectangle
        painter.setPen(QPen(QColor(255, 0, 0), 2))  # Change pen color
        painter.drawLine(10, 10, 110, 110)  # Draw a line
        painter.end()


class BrushExample(QWidget): # QBrush
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QBrush Example")
        self.resize(300, 200)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Using QBrush to fill a rectangle
        brush = QBrush(QColor(255, 0, 0, 128))  # Create a semi-transparent red brush
        painter.setBrush(brush)
        painter.drawRect(10, 10, 100, 100)  # Draw a rectangle filled with the brush

        # Changing the brush to a different color and style
        brush.setColor(QColor(0, 0, 255, 128))  # Change color to semi-transparent blue
        brush.setStyle(Qt.Dense4Pattern)  # Change the brush style
        painter.setBrush(brush)
        painter.drawRect(120, 10, 100, 100)  # Draw another rectangle with the updated brush

        painter.end()


class PenExample(QWidget): # QPen
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QPen Example")
        self.resize(300, 200)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Creating and using a QPen
        pen = QPen()  # Create a QPen object
        pen.setWidth(5)  # Set the pen width
        pen.setColor(QColor(255, 0, 0))  # Set the pen color to red
        pen.setStyle(Qt.DotLine)  # Set the pen style to dotted line
        painter.setPen(pen)
        painter.drawLine(10, 10, 100, 100)  # Draw a line with the pen

        # Changing the pen properties
        pen.setColor(QColor(0, 0, 255))  # Change the pen color to blue
        pen.setStyle(Qt.SolidLine)  # Change the pen style to solid line
        painter.setPen(pen)
        painter.drawRect(10, 120, 100, 50)  # Draw a rectangle with the updated pen

        painter.end()


class GraphicsSceneWindow(QWidget): # QGraphicsScene
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QGraphicsScene in a Separate Window")
        self.setGeometry(100, 100, 600, 400)

        # Create a QGraphicsScene
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(100, 100, 500, 300)  # Set the scene size

        # Add items to the scene
        rectItem = QGraphicsRectItem(100, 100, 100, 100)
        rectItem.setBrush(QBrush(QColor(255, 0, 0)))
        self.scene.addItem(rectItem)

        # Create a QGraphicsView to visualize the scene
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(0, 0, 700, 500)


class GraphicsViewWindow(QWidget): # QGraphicsScene
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QGraphicsView in Separate Window")
        self.setGeometry(100, 100, 600, 400)

        # Create a QGraphicsScene
        scene = QGraphicsScene(QRectF(0, 0, 500, 300), self)

        # Create a QGraphicsView and set it to display the scene
        view = QGraphicsView(scene, self)
        view.setGeometry(50, 50, 500, 300)  # Set the size and position of the view within the window

        # Optional: Customize the QGraphicsView
        view.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smoother drawing
        view.setBackgroundBrush(QBrush(QColor(230, 0, 0)))  # Set background color


class ImageDisplayWindow(QWidget): # QImage
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QImage Display")
        self.setGeometry(100, 100, 600, 400)

        # Create a QImage
        self.image = QImage(400, 300, QImage.Format_RGB32)
        self.image.fill(Qt.blue)  # Fill the image with blue color

        # Display QImage in the window
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setGeometry(100, 50, 400, 300)  # Adjust size and position to display the image

        ##########################################################################################
        imagePath = "C:/Users/Dmitriy S. VeRiM/Desktop/logo1.png"

        # Method 1: Load image using the load() method
        self.image = QImage()
        if not self.image.load(imagePath):
            raise IOError(f"Unable to load {imagePath}")

        # Method 2: Directly load image at creation (alternative, uncomment to use)
        # self.image = QImage(imagePath)

        # Verify the image was loaded
        if self.image.isNull():
            raise IOError(f"Failed to load image from {imagePath}")

        # Display QImage in the window
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.adjustSize()  # Adjust the label size to fit the image


class PixmapDisplayWindow(QWidget): # QPixmap
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QPixmap Display")
        self.setGeometry(100, 100, 600, 400)

        imagePath = "C:/Users/Dmitriy S. VeRiM/Desktop/logo1.png"

        # Create a QPixmap
        self.pixmap = QPixmap(imagePath)

        # Display QPixmap in the window
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.adjustSize()  # Adjust the label size to fit the pixmap


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the title and initial size of the main window
        self.setWindowTitle('PySide6 Application')
        self.setGeometry(100, 100, 280, 80)

        # Create a button and set its properties
        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.QImage_1)  # Connect the clicked signal to the slot

        # Create a layout and add widgets to it
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)

        # Create a central widget, set the layout, and make it the central widget of the main window
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

    def on_button_clicked(self): # Po prikoly
        print("Button was clicked")

    def paintEvent_1(self): # QPainter
        self.drawingWindow = DrawingWindow()
        self.drawingWindow.show()

    def QBrush_1(self): # QBrush
        self.drawingWindow = BrushExample()
        self.drawingWindow.show()

    def QPen_1(self): # QPen
        self.drawingWindow = PenExample()
        self.drawingWindow.show()

    def QGraphicsScene_1(self): # QGraphicsScene
        self.drawingWindow = GraphicsSceneWindow()
        self.drawingWindow.show()

    def QGraphicsView_1(self): # QGraphicsView
        self.drawingWindow = GraphicsViewWindow()
        self.drawingWindow.show()

    def QImage_1(self): # QImage
        self.drawingWindow = ImageDisplayWindow()
        self.drawingWindow.show()

    def QPixmap_1(self): # QPixmap
        self.drawingWindow = PixmapDisplayWindow()
        self.drawingWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

