import typing
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget

class MyGUI(QMainWindow):
    
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi(r'templates\t_clientes.ui', self)
        self.show()

        self.acept_boton.clicked.connect(self.si)
    
    def si(self):
        self.lineEdit.setEnabled(not False|self.lineEdit.isEnabled())
    
        
if __name__ == '__main__':
    app = QApplication([])
    window = MyGUI()
    app.exec_()