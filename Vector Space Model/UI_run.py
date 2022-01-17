import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from gui import *


class ProjectUI(QMainWindow, Main_GUI):
    def __init__(self, parent=None):
        super(ProjectUI, self).__init__(parent)
        self.setupUi(self)
        self.search_btn.clicked.connect(self.search_event)

    # Populate list with data
    def populate_list(self):
        pass

    # on search button click
    def search_event(self):
        if self.query_input.text() != "":
            self.populate_list()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = ProjectUI()
    myWin.show()
    sys.exit(app.exec_())