from cProfile import label
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLabel,
    QSpinBox,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metric vs Imperial converter")

        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create and connect the combo box to switch between pages
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Metric to imperial", "Imperial to metric"])
        self.pageCombo.activated.connect(self.switchPage)

        # Create the stacked layout
        self.stackedLayout = QStackedLayout()
        
        # Create the first page
        self.page1 = QWidget()
        self.page1Layout = QFormLayout()
        self.cm_input = QSpinBox()
        self.cm_input.setMaximum(1000)
        self.cm_input.valueChanged.connect(self.convert_metric)
        self.converted_metric = QLabel()
        self.page1Layout.addRow("Your Height:", QLabel())
        self.page1Layout.addRow("Centimeters:", self.cm_input)
        self.page1Layout.addRow("Converted Height:", self.converted_metric)
        self.page1.setLayout(self.page1Layout)
        self.stackedLayout.addWidget(self.page1)
        
        # Create the second page
        self.page2 = QWidget()
        self.page2Layout = QFormLayout()
        self.feet_input = QSpinBox()
        self.feet_input.setMaximum(1000)
        self.feet_input.valueChanged.connect(self.convert_imperial)
        self.inches_input = QSpinBox()
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
        layout.addWidget(self.pageCombo)
        layout.addLayout(self.stackedLayout)

    def switchPage(self):
        self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())

    def convert_metric(self):
        cm = self.cm_input.value()
        total_height = round(cm / 2.54, 2)
        imperial_height_feet = int(total_height / 12)
        imperial_height_inches = round(float(total_height % 12), 2)
        new_format = str(imperial_height_feet) + "'" + str(imperial_height_inches) + '"'
        self.converted_metric.setText(str(new_format))

    def convert_imperial(self):
        inches = self.inches_input.value()
        feet = self.feet_input.value()
        imperial_total = feet * 12 + inches
        total_height = round(imperial_total * 2.54, 2)
        self.converted_imperial.setText(str(total_height))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

    