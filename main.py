import csv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,
    QMessageBox, QComboBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employee Workload Statistics System")
        self.setGeometry(100, 100, 1000, 700)
        self.setupUI()
        self.load_data()

    def setupUI(self):
        # Set up the window and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Header label
        header = QLabel("Employee Workload Statistics System")
        header.setAlignment(Qt.AlignCenter)
        header.setFont(QFont("Arial", 18, QFont.Bold))
        layout.addWidget(header)

        # Input fields
        self.input_id = self.create_input_field("Employee ID:", layout)
        self.input_name = self.create_input_field("Product Name:", layout)
        self.input_category = self.create_combo_box("Product Category:", ["Electronics", "Furniture", "Clothing"], layout)
        self.input_completed = self.create_input_field("Products Completed:", layout)
        self.input_quality = self.create_combo_box("Product Quality:", ["High", "Medium", "Low"], layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.add_button("Save", self.save_data, button_layout)
        self.add_button("Update", self.update_data, button_layout)
        self.add_button("Delete", self.delete_data, button_layout)
        self.add_button("View Statistics", self.view_statistics, button_layout)
        layout.addLayout(button_layout)

        # Data Table
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Employee ID", "Product Name", "Category", "Completed", "Quality"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.cellClicked.connect(self.fill_form_from_table)

    def create_input_field(self, label_text, layout):
        label = QLabel(label_text)
        layout.addWidget(label)
        input_field = QLineEdit()
        layout.addWidget(input_field)
        return input_field

    def create_combo_box(self, label_text, items, layout):
        label = QLabel(label_text)
        layout.addWidget(label)
        combo_box = QComboBox()
        combo_box.addItems(items)
        layout.addWidget(combo_box)
        return combo_box

    def add_button(self, text, function, layout):
        button = QPushButton(text)
        button.clicked.connect(function)
        layout.addWidget(button)

    def fill_form_from_table(self, row):
        self.input_id.setText(self.table.item(row, 0).text())
        self.input_name.setText(self.table.item(row, 1).text())
        self.input_category.setCurrentText(self.table.item(row, 2).text())
        self.input_completed.setText(self.table.item(row, 3).text())
        self.input_quality.setCurrentText(self.table.item(row, 4).text())

    def save_data(self):
        try:
            employee_id = self.input_id.text().strip()
            product_name = self.input_name.text().strip()
            category = self.input_category.currentText()
            completed = self.input_completed.text().strip()
            quality = self.input_quality.currentText()

            if not (employee_id and product_name and completed.isdigit()):
                raise ValueError("Please fill all fields correctly.")

            with open('employee_data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([employee_id, product_name, category, completed, quality])

            self.clear_inputs()
            self.load_data()
            QMessageBox.information(self, "Success", "Data saved successfully!")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save data: {str(e)}")

    def update_data(self):
        row = self.table.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Error", "Please select a record to update.")
            return
        try:
            employee_id = self.input_id.text().strip()
            product_name = self.input_name.text().strip()
            category = self.input_category.currentText()
            completed = self.input_completed.text().strip()
            quality = self.input_quality.currentText()

            if not (employee_id and product_name and completed.isdigit()):
                raise ValueError("Please fill all fields correctly.")

            self.table.setItem(row, 0, QTableWidgetItem(employee_id))
            self.table.setItem(row, 1, QTableWidgetItem(product_name))
            self.table.setItem(row, 2, QTableWidgetItem(category))
            self.table.setItem(row, 3, QTableWidgetItem(completed))
            self.table.setItem(row, 4, QTableWidgetItem(quality))

            self.save_table_data_to_file()
            QMessageBox.information(self, "Success", "Data updated successfully!")
            self.clear_inputs()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update data: {str(e)}")

    def delete_data(self):
        row = self.table.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Error", "Please select a record to delete.")
            return
        self.table.removeRow(row)
        self.save_table_data_to_file()
        QMessageBox.information(self, "Success", "Record deleted successfully!")

    def view_statistics(self):
        data = self.load_data_as_list()
        if not data:
            QMessageBox.information(self, "Statistics", "No data available.")
            return

        data.sort(key=lambda x: (-int(x[3]), x[0]))  # Sort by completed (desc) and Employee ID (asc)

        statistics = "Workload Statistics by Completion Quantity:\n"
        prev_completed = None
        rank_count = 0
        for row in data:
            completed = int(row[3])
            if completed != prev_completed:
                if prev_completed is not None:
                    statistics += f"\nTotal Employees with {prev_completed} Completed: {rank_count}\n"
                rank_count = 0
                statistics += f"\nRank {completed}:"
                prev_completed = completed
            rank_count += 1
            statistics += f"\n  Employee ID: {row[0]}"

        statistics += f"\n\nTotal Employees with {prev_completed} Completed: {rank_count}\n"

        QMessageBox.information(self, "Statistics", statistics)

    def load_data_as_list(self):
        data = []
        try:
            with open('employee_data.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            pass
        return data

    def save_table_data_to_file(self):
        try:
            with open('employee_data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for row in range(self.table.rowCount()):
                    row_data = [self.table.item(row, col).text() for col in range(self.table.columnCount())]
                    writer.writerow(row_data)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save data: {str(e)}")

    def load_data(self):
        self.table.setRowCount(0)
        data = self.load_data_as_list()
        for row_data in data:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for column, data in enumerate(row_data):
                self.table.setItem(row, column, QTableWidgetItem(data))

    def clear_inputs(self):
        self.input_id.clear()
        self.input_name.clear()
        self.input_completed.clear()
        self.input_category.setCurrentIndex(0)
        self.input_quality.setCurrentIndex(0)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
