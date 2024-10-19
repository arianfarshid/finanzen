import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QScrollArea, QLineEdit, QPushButton, QDialog, QDialogButtonBox
import data_storage as ds

database = ds.Data_Storage('finanzen.db')
budget = database.fetch_data()

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        self.category_lineEdit = QLineEdit()
        self.description_lineEdit = QLineEdit()
        self.value_lineEdit = QLineEdit()

        self.dialog = QDialog()
        self.dialog_category_label = QLabel()
        self.dialog_description_label = QLabel()
        self.dialog_value_label = QLabel()

        self.scroll_area_widget_0 = QWidget()
        self.vertical_layout_0 = QVBoxLayout(self.scroll_area_widget_0)

        self.excess_label = QLabel()
        self.expenses_label = QLabel()
        self.revenue_label = QLabel()

        self.main_font = QFont()
        

        super().__init__(*args, **kwargs)

        self.setWindowTitle('Finanzenverwaltung')
        self.setGeometry(100, 100, 1000, 600)
        

        central_widget = QWidget()
        main_layout = QVBoxLayout()

        central_widget.setLayout(main_layout)

        # Header
        header_label = QLabel('Finanzübersicht', self)
        header_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        header_font = QFont()
        header_font.setPointSize(40)
        header_label.setFont(header_font)
        header_label.setStyleSheet("background-color: lightblue; color: black")
        main_layout.insertWidget(0, header_label)
        
        # Welcome Label
        welcome = QLabel('Hier können Sie Ihre Einnahmen und Ausgaben verwalten')
        welcome.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        welcome_font = QFont()
        welcome_font.setPointSize(20)
        welcome.setFont(welcome_font)
        main_layout.insertWidget(1, welcome)

        # Main Font
        
        self.main_font.setPointSize(15)

        # Überschuss und Einnahmen
        label_stylesheet = 'background-color: #32686d;' + 'border-radius: 6px;'
        revenue = budget.revenue
        excess = budget.get_excess()
        expenses = budget.get_total_expenditure()

        horizontal_layout_revenue_widget = QWidget()
        horizontal_layout_revenue = QHBoxLayout(horizontal_layout_revenue_widget)
        main_layout.insertWidget(2, horizontal_layout_revenue_widget)

        self.revenue_label.setText('Einnahmen: ' + str(revenue) + '€')
        self.revenue_label.setFont(welcome_font)
        self.revenue_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.revenue_label.setStyleSheet(label_stylesheet)
        horizontal_layout_revenue.insertWidget(0, self.revenue_label)

        self.expenses_label.setText('Ausgaben: ' + str(expenses) + '€')
        self.expenses_label.setFont(welcome_font)
        self.expenses_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.expenses_label.setStyleSheet(label_stylesheet)
        horizontal_layout_revenue.insertWidget(1, self.expenses_label)

        self.excess_label.setText('Überschuss: ' + str(excess) + '€')
        self.excess_label.setFont(welcome_font)
        self.excess_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.excess_label.setStyleSheet(label_stylesheet)
        horizontal_layout_revenue.insertWidget(2, self.excess_label)

        horizontal_layout_revenue_widget.setStyleSheet('background-color: lightblue; color: black;')
        


        #Horizontal layout
        horizontal_layout_widget = QWidget()
        horizontal_layout = QHBoxLayout(horizontal_layout_widget)
        main_layout.insertWidget(3, horizontal_layout_widget)
        horizontal_layout_widget.setStyleSheet('background-color: lightblue; color: black;')

    
        vertical_layout_widget_1 = QWidget()
        vertical_layout_widget_2 = QWidget()


        scroll_area_0 = QScrollArea()
        scroll_area_0.setWidgetResizable(True)
        scroll_area_0.setWidget(self.scroll_area_widget_0)
        

        vertical_layout_1 = QVBoxLayout(vertical_layout_widget_1)
        vertical_layout_2 = QVBoxLayout(vertical_layout_widget_2)

        
        horizontal_layout.insertWidget(0, scroll_area_0)
        horizontal_layout.insertWidget(1, vertical_layout_widget_1)
        horizontal_layout.insertWidget(2, vertical_layout_widget_2)

        layout_background = 'background-color: #32686d; border-radius: 6px'
        self.scroll_area_widget_0.setStyleSheet(layout_background)
        vertical_layout_widget_1.setStyleSheet(layout_background)
        vertical_layout_widget_2.setStyleSheet(layout_background)

        #----------First Column---------------------------

        self.draw_categories()

        #-------------------second column-------------------
        headline_label = QLabel('Visaulisierung')
        headline_label.setFont(welcome_font)
        headline_label.setStyleSheet('background-color: lightblue; padding: 2px 10px;')
        vertical_layout_1.insertWidget(0, headline_label)

        vertical_layout_1.addStretch(20)


        # -------------------third column-------------------
        title_label = QLabel('Buchungen hinzufügen')
        title_label.setFont(welcome_font)
        title_label.setStyleSheet('background-color: lightblue; padding: 6px')
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        vertical_layout_2.insertWidget(0, title_label)

        category_layout_widget = QWidget()
        category_layout = QVBoxLayout(category_layout_widget)
        vertical_layout_2.insertWidget(1, category_layout_widget)
        category_layout_widget.setStyleSheet('background-color: #43ba88;')

        category_label = QLabel('Geben Sie die Kategorie Ihrer Buchung ein')
        category_label.setFont(self.main_font)

        self.category_lineEdit.setPlaceholderText('Kategorie ...')
        self.category_lineEdit.setFont(self.main_font)
        self.category_lineEdit.setStyleSheet('background-color: #9fcace; padding: 5px;')

        category_layout.insertWidget(0, category_label)
        category_layout.insertWidget(1, self.category_lineEdit)

        description_layout_widget = QWidget()
        description_layout = QVBoxLayout(description_layout_widget)
        vertical_layout_2.insertWidget(2, description_layout_widget)
        description_layout_widget.setStyleSheet('background-color: #43ba88;')

        description_label = QLabel('Geben Sie die Beschreibung Ihrer Buchung ein')
        description_label.setFont(self.main_font)

        self.description_lineEdit.setPlaceholderText('Beschreibung ...')
        self.description_lineEdit.setFont(self.main_font)
        self.description_lineEdit.setStyleSheet('background-color: #9fcace; padding: 5px;')

        description_layout.insertWidget(0, description_label)
        description_layout.insertWidget(1, self.description_lineEdit)

        value_layout_widget = QWidget()
        value_layout = QVBoxLayout(value_layout_widget)
        vertical_layout_2.insertWidget(3, value_layout_widget)
        value_layout_widget.setStyleSheet('background-color: #43ba88;')

        value_label = QLabel('Geben Sie den Betrag der Buchung ein')
        value_label.setFont(self.main_font)

        self.value_lineEdit.setPlaceholderText('Betrag ...')
        self.value_lineEdit.setFont(self.main_font)
        self.value_lineEdit.setStyleSheet('background-color: #9fcace; padding: 5px;')

        value_layout.insertWidget(0, value_label)
        value_layout.insertWidget(1, self.value_lineEdit)

        button = QPushButton()
        button.setText("Hinzufügen")
        button.setFont(self.main_font)
        button.setStyleSheet('background-color: #48a886; padding: 8px;')
        button.clicked.connect(self.show_dialog)


        vertical_layout_2.insertWidget(4, button)

        self.setCentralWidget(central_widget)

        self.show()

    def show_dialog(self):
        category_name = self.category_lineEdit.text()
        description = self.description_lineEdit.text()
        value = self.value_lineEdit.text()

        font = QFont()
        font.setPointSize(15)

        self.dialog_category_label.setText(f"Kategorie:\t\t{category_name}")
        self.dialog_description_label.setText(f"Beschreibung:\t\t{description}")
        self.dialog_value_label.setText(f"Betrag:\t\t\t{value}€")
        

        self.dialog_category_label.setFont(font)
        self.dialog_description_label.setFont(font)
        self.dialog_value_label.setFont(font)

        vertical_layout = QVBoxLayout(self.dialog)

        vertical_layout.insertWidget(0, self.dialog_category_label)
        vertical_layout.insertWidget(1, self.dialog_description_label)
        vertical_layout.insertWidget(2, self.dialog_value_label)
        vertical_layout.addStretch(1)

        button_box = QDialogButtonBox()
        ok_button = button_box.addButton(QDialogButtonBox.StandardButton.Ok)
        cancel_button = button_box.addButton(QDialogButtonBox.StandardButton.Cancel)

        ok_button.setFont(font)
        cancel_button.setFont(font)
        ok_button.setText('Hinzufügen')
        cancel_button.setText('Abbrechen')
        ok_button.clicked.connect(self.add_entry)

        vertical_layout.addWidget(button_box)

        self.dialog.setFixedSize(450, 200)
        self.dialog.setWindowTitle('Eintrag hinzufügen?')

        self.dialog.show()
        self.dialog.exec()


    def add_entry(self):
        category_name = self.category_lineEdit.text()
        description = self.description_lineEdit.text()
        value = float(self.value_lineEdit.text())
        
        budget.add_expenses_to_category(category_name, value, description)
        self.draw_categories()
        self.update_revenue()
        
        self.clear_lineEdits()
        self.dialog.accept()


    def clear_lineEdits(self): 
        self.category_lineEdit.clear()
        self.description_lineEdit.clear()
        self.value_lineEdit.clear()

    def draw_categories(self):
        index = 0
        for category in budget.category:
            tmp_vertical_layout_widget = QWidget()
            tmp_vertical_layout = QVBoxLayout(tmp_vertical_layout_widget)
            tmp_vertical_layout_widget.setStyleSheet('background-color: #43ba88;' + 'border-radius: 6px;')
            category_name = category.name
            limit = category.limit
            tmp_label = QLabel(F"{category_name}")
            tmp_expenses_layout_widget = QWidget()
            tmp_expenses_layout = QVBoxLayout(tmp_expenses_layout_widget)
            tmp_expenses_layout_widget.setStyleSheet('background-color: #9fcace;' + 'border-radius: 6px;')
            tmp_label.setFont(self.main_font)
            tmp_vertical_layout.insertWidget(0, tmp_label)
            tmp_vertical_layout.insertWidget(1, tmp_expenses_layout_widget)
            self.vertical_layout_0.insertWidget(index, tmp_vertical_layout_widget)
            expenses_index = 0
            for expense in category.expenses:
                value = expense[0]
                description = expense[1]
                tmp_horizontal_layout_widget = QWidget()
                tmp_horizontal_layout = QHBoxLayout(tmp_horizontal_layout_widget)
                tmp_expense_description_label = QLabel(f"{description}")
                tmp_expense_value_label = QLabel(f"{value}€")
                tmp_expense_description_label.setFont(self.main_font)
                tmp_expense_value_label.setFont(self.main_font)
                tmp_expense_value_label.setAlignment(Qt.AlignmentFlag.AlignRight)
                tmp_horizontal_layout.insertWidget(0, tmp_expense_description_label)
                tmp_horizontal_layout.insertWidget(1, tmp_expense_value_label)
                tmp_expenses_layout.insertWidget(expenses_index, tmp_horizontal_layout_widget)
                expenses_index =+ 1
            index =+ 1
    
    def update_revenue(self):
        excess = budget.get_excess()
        expenses = budget.get_total_expenditure()

        self.excess_label.setText('Überschuss: ' + str(excess) + '€')
        self.expenses_label.setText('Ausgaben: ' + str(expenses) + '€')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
