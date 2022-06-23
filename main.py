from PyQt5.QtWidgets \
import QMainWindow,QApplication,QPushButton,QLineEdit,QTableWidgetItem,QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5 import uic
import sys
global row
global column
row = 0
class Ui(QMainWindow):
    def __init__(self):
        global table
        super(Ui,self).__init__()
        uic.loadUi("InvoicePage.ui",self)
        #define some widgets
        self.button=self.findChild(QPushButton, 'pushButton')
        self.table=self.findChild(QTableWidget, 'tableWidget')
        table=self.tableWidget

        #table.setRowCount(1)

        self.button.clicked.connect(self.openWindow)
        #self.entery()
        self.show()

    def openWindow(self):
        self.ui2 = SecondWindow()
        self.ui2.show()
        #if self.ui2.isVisible():
         #   self.hide()


class SecondWindow(QMainWindow):
    def __init__(self):
        super(SecondWindow,self).__init__()
        uic.loadUi("SlipInvoice.ui",self)

        #Button Connnection
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.openWindow2)
        self.button.clicked.connect(self.entery)

        #Entery Box
        self.entery1 =self.findChild(QLineEdit,  'lineEdit')
        self.entery2 = self.findChild(QLineEdit, 'lineEdit_2')
        self.entery3 = self.findChild(QLineEdit, 'lineEdit_3')
        self.entery4 = self.findChild(QLineEdit, 'lineEdit_4')
        self.entery5 = self.findChild(QLineEdit, 'lineEdit_5')
        self.entery6 = self.findChild(QLineEdit, 'lineEdit_6')
        self.entery7 = self.findChild(QLineEdit, 'lineEdit_7')
        self.entery8 = self.findChild(QLineEdit, 'lineEdit_8')
        self.entery9 = self.findChild(QLineEdit, 'lineEdit_9')
        self.entery10 = self.findChild(QLineEdit, 'lineEdit_10')

    def entery(self):
        global store,row,column
        global table
        a=(self.entery1.text())
        b=(self.entery2.text())
        c=(self.entery3.text())
        d=(self.entery4.text())
        e=(self.entery5.text())
        f=(self.entery6.text())
        g=(self.entery7.text())
        h=(self.entery8.text())
        i=(self.entery9.text())
        j=(self.entery10.text())

        if a and b and c and d and e and f and g and h and i and j is not None:
            rowcount=table.rowCount()
            table.insertRow(rowcount)
            table.setItem(rowcount, 0,QTableWidgetItem(a))
            table.setItem(rowcount, 1, QTableWidgetItem(b))
            table.setItem(rowcount, 2, QTableWidgetItem(c))
            table.setItem(rowcount, 3, QTableWidgetItem(d))
            table.setItem(rowcount, 4, QTableWidgetItem(e))
            table.setItem(rowcount, 5, QTableWidgetItem(f))
            table.setItem(rowcount, 6, QTableWidgetItem(g))
            table.setItem(rowcount, 7, QTableWidgetItem(h))
            table.setItem(rowcount, 8, QTableWidgetItem(i))
            table.setItem(rowcount, 9, QTableWidgetItem(j))
            rowcount+1




        #store=[a,b,c,d,e,f,g,h,i,j]
        #print(store)
        #store = [{"coustomer": a, "paymentdate": b, "duedate": c, "assignee": d,"balance": e, "paid": f, "invoice": g,"total": h,"status": i,"invoicedate": j}]
        #tabledata(store)

        #table.updatesEnabled()
        #table.setRowCount(row+1)

        #print(store)
        '''for result in store:
            table.setItem(row, 0, QTableWidgetItem(result["coustomer"]))
            table.setItem(row, 1, QTableWidgetItem(result["paymentdate"]))
            table.setItem(row, 2, QTableWidgetItem(result["duedate"]))
            table.setItem(row, 3, QTableWidgetItem(result["assignee"]))
            table.setItem(row, 4, QTableWidgetItem(result["balance"]))
            table.setItem(row, 5, QTableWidgetItem(result["paid"]))
            table.setItem(row, 6, QTableWidgetItem(result["invoice"]))
            table.setItem(row, 7, QTableWidgetItem(result["total"]))
            table.setItem(row, 8, QTableWidgetItem(result["status"]))
            table.setItem(row, 9, QTableWidgetItem(result["invoicedate"]))
            row = row + 1 '''
        


        #self.show()'''
    def openWindow2(self):
        '''self.ui2 = Ui()
        print('code is here')
        self.ui2.show()'''
        self.hide()

#app =QApplication(sys.argv)
#window =Ui()
#window1=SecondWindow()
#app.exec()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window1 = QMainWindow()
    ui = Ui()
    ui.show()
    sys.exit(app.exec_())