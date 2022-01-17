import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from gui import *
# from Ranking import *


class ProjectUI(QMainWindow, Main_GUI):
    def __init__(self, parent=None):
        super(ProjectUI, self).__init__(parent)
        self.setupUi(self)
        self.search_btn.clicked.connect(self.on_button_clicked)
        self.result_view.itemDoubleClicked.connect(self.on_item_double_clicked)

    # Populate list with data
    def populate_list(self, query):
        # data = ranking_return(query)[:20]
        data = "abc"
        for index in range(len(data)):
            self.result_view.addItem(data[index])

    # open document
    def on_item_double_clicked(self, item):
        pass

    # on search button click
    def on_button_clicked(self):
        if self.query_input.text() != "":
            self.populate_list(self.query_input.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = ProjectUI()
    myWin.show()
    sys.exit(app.exec_())