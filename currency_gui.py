import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import *
import ingester as ing

class CurrencyConverterGui(QMainWindow):

    def __init__(self):
        super().__init__()
        # Object variables
        self.source_country_list = None
        self.target_country_list = None
        self.source_currency_field = None
        self.source_currency_symbol = None
        self.target_currency_field = None
        self.target_currency_symbol = None

        self.init_ui()
        self.show()

    def init_ui(self):
        self.source_country_list = QListWidget()
        self.target_country_list = QListWidget()
        self.source_country_list.itemClicked.connect(self.country_clicked)
        self.target_country_list.itemClicked.connect(self.country_clicked)

        self.load_countries()

        country_list_layout = QHBoxLayout()
        country_list_layout.addWidget(self.source_country_list)
        country_list_layout.addWidget(self.target_country_list)

        self.source_currency_field = QLineEdit()
        validator = QDoubleValidator()
        validator.setBottom(0)
        self.source_currency_field.setValidator(validator)

        self.source_currency_symbol = QLabel()

        convert_button = QPushButton("Convert ➡︎")
        convert_button.pressed.connect(self.convert_button_pressed)

        self.target_currency_field = QLineEdit()
        self.target_currency_symbol = QLabel()

        currency_layout = QHBoxLayout()
        currency_layout.setAlignment(Qt.AlignVCenter)
        currency_layout.addWidget(self.source_currency_field)
        currency_layout.addWidget(self.source_currency_symbol)
        currency_layout.addWidget(convert_button)
        currency_layout.addWidget(self.target_currency_field)
        currency_layout.addWidget(self.target_currency_symbol)

        layout = QVBoxLayout()
        layout.addLayout(country_list_layout)
        layout.addLayout(currency_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def get_currency_id(self, list_widget) -> str:
        selected_items = list_widget.selectedItems()
        if len(selected_items) == 0:
            # TO DO error message to user
            return None

        item_text = selected_items[0].text()
        currency_id = item_text.split()[-1]
        # [EUR]
        currency_id = currency_id[1:-1]
        return (currency_id)


    def convert_button_pressed(self):
        # determine the source and target currency IDs
        source_currency_id = self.get_currency_id(self.source_country_list)
        target_currency_id = self.get_currency_id((self.target_country_list))

        if source_currency_id is None or target_currency_id is None:
            self.statusBar().showMessage("Source and Target country must be selected.", 3000)
            return

        print(source_currency_id)
        print(target_currency_id)


        # retrieve the source currency amount
        # call the ingester to get conversion rate
        # multiple conversion rate by the source currency amount
        # put the result in the target currency amount box
        print("Convert button pressed")

    def country_clicked(self, item):
        selected_string = item.text()
        selection_list = selected_string.split()
        symbol = selection_list[-2]
        if item.listWidget() is self.source_country_list:
            self.source_currency_symbol.setText(symbol)
        else:
            self.target_currency_symbol.setText(symbol)


    def load_countries(self):
            # Call ingester to get the list of countries
            ingester = ing.Ingester()
            countries = ingester.get_countries()
            # Add for loop to add each country
            country_string_list = []
            for country in countries:
                country_string_list.append(f"{country['name']} {country['currencySymbol']} [{country['currencyId']}]")
            country_string_list.sort()
            for country_string in country_string_list:
                self.source_country_list.addItem(country_string)
                self.target_country_list.addItem(country_string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CurrencyConverterGui()
    sys.exit(app.exec_())
