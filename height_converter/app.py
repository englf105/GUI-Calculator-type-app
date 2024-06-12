from cProfile import label

import sys
from PyQt6.QtGui import QFont, QFontDatabase

from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLabel,
    QDoubleSpinBox,
    QSpinBox,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
    QMainWindow,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metric vs Imperial converter")
        
        #install fonts
        self.set_fonts("Raleway-Regular.ttf")

        title_label = QLabel("Metric vs Imperial converter")
        title_label.setFont(QFont("Raleway", 12))

        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create and connect the combo box to switch between pages
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Metric to imperial", "Imperial to metric"])
        self.pageCombo.setFont(QFont("Raleway", 9))
        self.pageCombo.activated.connect(self.switchPage)

        # Create the stacked layout
        self.stackedLayout = QStackedLayout()
        
        # Create the first page
        self.page1 = QWidget()
        self.page1Layout = QFormLayout()
        self.page1.setFont(QFont("Raleway", 9))
        self.cm_input = QDoubleSpinBox()
        self.cm_input.setFont(QFont("Raleway", 9))
        self.cm_input.setMaximum(1000)
        self.cm_input.valueChanged.connect(self.convert_metric)
        self.converted_metric = QLabel()
        self.converted_metric.setFont(QFont("Raleway", 9))
        self.page1Layout.addRow("Your Height:", QLabel())
        self.page1Layout.addRow("Centimeters:", self.cm_input)
        self.page1Layout.addRow("Converted Height:", self.converted_metric)
        self.page1.setLayout(self.page1Layout)
        self.stackedLayout.addWidget(self.page1)
        
        # Create the second page
        self.page2 = QWidget()
        self.page2Layout = QFormLayout()
        self.page2.setFont(QFont("Raleway", 9))
        self.feet_input = QSpinBox()
        self.feet_input.setFont(QFont("Raleway", 9))
        self.feet_input.setMaximum(1000)
        self.feet_input.valueChanged.connect(self.convert_imperial)
        self.inches_input = QDoubleSpinBox()
        self.inches_input.setFont(QFont("Raleway", 9))
        self.inches_input.setMaximum(1000)
        self.inches_input.valueChanged.connect(self.convert_imperial)
        self.converted_imperial = QLabel()
        self.page2Layout.addRow("Your Height:", QLabel())
        self.page2Layout.addRow("Feet:", self.feet_input)
        self.page2Layout.addRow("Inches:", self.inches_input)
        self.page2Layout.addRow("Converted Height:", self.converted_imperial)
        self.page2.setLayout(self.page2Layout)
        self.stackedLayout.addWidget(self.page2)
        
        # Add the combo box and the stacked layout to the top-level layout
        layout.addWidget(title_label)
        layout.addWidget(self.pageCombo)
        layout.addLayout(self.stackedLayout)

    def set_fonts(self, font_name: str) -> None:
        
        font_dir = "fonts/"
        font_path = font_dir + font_name
        success = QFontDatabase.addApplicationFont(font_path)
        
        # If failed to add font
        if success == -1:
            print(f"{font_name} not loaded./n Try path {font_path} ")

    # Function that switches pages
    def switchPage(self):
        self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())

    # Function that recieves a value in the metric system then converts it to the imperial system
    def convert_metric(self):

        # Takes the value from the Qspinbox
        cm = self.cm_input.value()

        # Converts the height from centimeters into inches
        total_height = round(cm / 2.54, 2)

        # Seperates the inches into both feet and remaining inches
        imperial_height_feet = int(total_height / 12)
        imperial_height_inches = round(float(total_height % 12), 2)

        # Formats feet and inches into proper syntax 
        new_format = str(imperial_height_feet) + "'" + str(imperial_height_inches) + '"'

        # Displays the new height back in the label
        self.converted_metric.setText(str(new_format))

    # Function that recieves a value in the imperial system then converts it to the metric system
    def convert_imperial(self):

        # Takes the values from the Qspinboxes
        inches = self.inches_input.value()
        feet = self.feet_input.value()

        # Turns the feet into inches so that it can be converted
        imperial_total = feet * 12 + inches

        # Converts the height from inches into centimeters
        total_height = round(imperial_total * 2.54, 2)

        # Displays the new height back in the label
        self.converted_imperial.setText(str(total_height))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

