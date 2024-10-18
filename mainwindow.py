import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QScrollArea, QLineEdit
import data_storage as ds

database = ds.Data_Storage('finanzen.db')
budget = database.fetch_data()

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
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
        main_font = QFont()
        main_font.setPointSize(15)

        # Überschuss und Einnahmen
        label_stylesheet = 'background-color: #32686d;' + 'border-radius: 6px;'
        revenue = budget.revenue
        excess = budget.get_excess()
        expenses = budget.get_total_expenditure()

        horizontal_layout_revenue_widget = QWidget()
        horizontal_layout_revenue = QHBoxLayout(horizontal_layout_revenue_widget)
        main_layout.insertWidget(2, horizontal_layout_revenue_widget)

        revenue_label = QLabel('Einnahmen: ' + str(revenue) + '€', self)
        revenue_label.setFont(welcome_font)
        revenue_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        revenue_label.setStyleSheet(label_stylesheet)
        horizontal_layout_revenue.insertWidget(0, revenue_label)

        expenses_label = QLabel('Ausgaben: ' + str(expenses) + '€', self)
        expenses_label.setFont(welcome_font)
        expenses_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        expenses_label.setStyleSheet(label_stylesheet)
        horizontal_layout_revenue.insertWidget(1, expenses_label)

        excess_label = QLabel('Überschuss: ' + str(excess) + '€', self)
        excess_label.setFont(welcome_font)
        excess_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        excess_label.setStyleSheet(label_stylesheet)
        horizontal_layout_revenue.insertWidget(2, excess_label)

        horizontal_layout_revenue_widget.setStyleSheet('background-color: lightblue; color: black;')
        


        #Horizontal layout
        horizontal_layout_widget = QWidget()
        horizontal_layout = QHBoxLayout(horizontal_layout_widget)
        main_layout.insertWidget(3, horizontal_layout_widget)
        horizontal_layout_widget.setStyleSheet('background-color: lightblue; color: black;')

    
        vertical_layout_widget_1 = QWidget()
        vertical_layout_widget_2 = QWidget()


        scroll_area_widget_0 = QWidget()
        scroll_area_0 = QScrollArea()
        scroll_area_0.setWidgetResizable(True)
        scroll_area_0.setWidget(scroll_area_widget_0)
        

        vertical_layout_0 = QVBoxLayout(scroll_area_widget_0)
        vertical_layout_1 = QVBoxLayout(vertical_layout_widget_1)
        vertical_layout_2 = QVBoxLayout(vertical_layout_widget_2)

        
        horizontal_layout.insertWidget(0, scroll_area_0)
        horizontal_layout.insertWidget(1, vertical_layout_widget_1)
        horizontal_layout.insertWidget(2, vertical_layout_widget_2)

        layout_background = 'background-color: #32686d; border-radius: 6px'
        scroll_area_widget_0.setStyleSheet(layout_background)
        vertical_layout_widget_1.setStyleSheet(layout_background)
        vertical_layout_widget_2.setStyleSheet(layout_background)

        #----------First Column---------------------------

        index = 0
        for category in budget.category:
            tmp_vertical_layout_widget = QWidget()
            tmp_vertical_layout = QVBoxLayout(tmp_vertical_layout_widget)
            tmp_vertical_layout_widget.setStyleSheet('background-color: #43ba88;' + 'border-radius: 6px;')
            category_name = category.name
            limit = category.limit
            tmp_label = QLabel(f"{category_name} - Limit: {limit}")
            tmp_expenses_layout_widget = QWidget()
            tmp_expenses_layout = QVBoxLayout(tmp_expenses_layout_widget)
            tmp_expenses_layout_widget.setStyleSheet('background-color: #9fcace;' + 'border-radius: 6px;')
            tmp_label.setFont(main_font)
            tmp_vertical_layout.insertWidget(0, tmp_label)
            tmp_vertical_layout.insertWidget(1, tmp_expenses_layout_widget)
            vertical_layout_0.insertWidget(index, tmp_vertical_layout_widget)
            expenses_index = 0
            for expense in category.expenses:
                value = expense[0]
                description = expense[1]
                tmp_expense_label = QLabel(f"{description}: {value}€")
                tmp_expense_label.setFont(main_font)
                tmp_expenses_layout.insertWidget(expenses_index, tmp_expense_label)
                expenses_index =+ 1
            index =+ 1


        # -------------------third column-------------------
        title_label = QLabel('Buchungen hinzufügen')
        title_label.setFont(welcome_font)
        title_label.setStyleSheet('background-color: lightblue; padding: 6px')
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        vertical_layout_2.insertWidget(0, title_label)

        category_layout_widget = QWidget()
        category_layout = QVBoxLayout(category_layout_widget)
        vertical_layout_2.insertWidget(1, category_layout_widget)

        category_label = QLabel('Geben Sie die Kategorie Ihrer Buchung ein')
        category_label.setFont(main_font)

        category_lineEdit = QLineEdit()
        category_lineEdit.setPlaceholderText('Kategorie ...')
        category_lineEdit.setFont(main_font)
        category_lineEdit.setStyleSheet('background-color: white; padding: 5px;')

        category_layout.insertWidget(0, category_label)
        category_layout.insertWidget(1, category_lineEdit)

        description_layout_widget = QWidget()
        description_layout = QVBoxLayout(description_layout_widget)
        vertical_layout_2.insertWidget(2, description_layout_widget)

        description_label = QLabel('Geben Sie die Beschreibung Ihrer Buchung ein')
        description_label.setFont(main_font)

        description_lineEdit = QLineEdit()
        description_lineEdit.setPlaceholderText('Beschreibung ...')
        description_lineEdit.setFont(main_font)
        description_lineEdit.setStyleSheet('background-color: white; padding: 5px;')

        description_layout.insertWidget(0, description_label)
        description_layout.insertWidget(1, description_lineEdit)

        value_layout_widget = QWidget()
        value_layout = QVBoxLayout(value_layout_widget)
        vertical_layout_2.insertWidget(3, value_layout_widget)

        value_label = QLabel('Geben Sie den Betrag der Buchung ein')
        value_label.setFont(main_font)

        value_lineEdit = QLineEdit()
        value_lineEdit.setPlaceholderText('Betrag ...')
        value_lineEdit.setFont(main_font)
        value_lineEdit.setStyleSheet('background-color: white; padding: 5px;')

        value_layout.insertWidget(0, value_label)
        value_layout.insertWidget(1, value_lineEdit)

        vertical_layout_2.addStretch(10)
        
        self.setCentralWidget(central_widget)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
