# -*- coding: utf-8 -*-
# -----------------------------Импорт модулей-----------------------------------

from PyQt5 import QtSql
import os
import os.path
import shutil

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QTableWidget, QComboBox, \
    QSpinBox, QPushButton, QListWidgetItem

# -----------------------------------Форма--------------------------------------

class turbulenceProperties_form_class(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.interface_lng_val = parent.interface_lng_val
        self.con = parent.con
        self.full_dir = parent.full_dir
        self.par = parent

        if self.con.open():

            self.table = QTableWidget(4, 2)
            self.table.setColumnWidth(0, 150)
            self.table.setColumnWidth(1, 230)
            self.table.setFixedSize(674, 480)
            if self.interface_lng_val == 'Russian':
                self.table.setHorizontalHeaderLabels(["Параметр", "Значение"])
            elif self.interface_lng_val == 'English':
                self.table.setHorizontalHeaderLabels(["Parameter", "Value"])
            # simulationType
            simulationType_lbl = QLabel('simulationType')
            self.simulationType = QComboBox()
            simulationType_list = ["laminar", "RAS"]
            self.simulationType.addItems(simulationType_list)

            #RASModel
            RASModel_lbl = QLabel('RASModel')
            self.RASModel = QComboBox()
            RASModel_list = ["kkLOmega", "demo"]
            self.RASModel.addItems(RASModel_list)

            #turbulence
            turbulence_lbl = QLabel('turbulence')
            self.turbulence = QComboBox()
            turbulence_list = ["on", "off"]
            self.turbulence.addItems(turbulence_list)

            #printCoeffs
            printCoeffs_lbl = QLabel('printCoeffs')
            self.printCoeffs = QComboBox()
            printCoeffs_list = ["on", "off"]
            self.printCoeffs.addItems(printCoeffs_list)






            self.table.setCellWidget(0, 1, self.simulationType)
            self.table.setCellWidget(0, 0, simulationType_lbl)

            self.table.setCellWidget(1, 1, self.RASModel)
            self.table.setCellWidget(1, 0, RASModel_lbl)

            self.table.setCellWidget(2, 1, self.turbulence)
            self.table.setCellWidget(2, 0, turbulence_lbl)

            self.table.setCellWidget(3, 1, self.printCoeffs)
            self.table.setCellWidget(3, 0, printCoeffs_lbl)

            # вывод значений параметров
            if 'turbulenceProperties' in self.con.tables():						
                query = QtSql.QSqlQuery()
                query.exec("SELECT * FROM turbulenceProperties")
                if query.isActive():
                    query.first()
                    value_list = []
                    while query.isValid():
                        value_res = query.value('value')
                        value_list.append(value_res)
                        query.next()
					
                    # simulationType
                    simulationType_mas = self.simulationType.count()   
                    for i in range(simulationType_mas):
                        if self.simulationType.itemText(i) == value_list[0]:
                            self.simulationType.setCurrentIndex(i)

                    # RASModel
                    RASModel_mas = self.RASModel.count()
                    for i in range(RASModel_mas):
                        if self.RASModel.itemText(i) == value_list[1]:
                            self.RASModel.setCurrentIndex(i)

                    # turbulence
                    turbulence_mas = self.turbulence.count()
                    for i in range(turbulence_mas):
                        if self.turbulence.itemText(i) == value_list[2]:
                            self.turbulence.setCurrentIndex(i)

                    # printCoeffs
                    printCoeffs_mas = self.printCoeffs.count()
                    for i in range(printCoeffs_mas):
                        if self.printCoeffs.itemText(i) == value_list[3]:
                            self.printCoeffs.setCurrentIndex(i)
							
            btnSave = QPushButton()
            btnSave.setFixedSize(80, 25)
            btnSave.clicked.connect(self.on_btnSave_clicked)

            if self.interface_lng_val == 'Russian':
                btnSave.setText("Сохранить")
            elif self.interface_lng_val == 'English':
                btnSave.setText("Save")

            vbox = QVBoxLayout()
            vbox.addWidget(self.table)
            vbox.addWidget(btnSave)

# ---------------------Размещение на форме всех компонентов-------------------------

            form = QFormLayout()
            form.addRow(vbox)
            self.setLayout(form)

    def on_btnSave_clicked(self):
        simulationType_txt = self.simulationType.currentText()
        RASModel_txt = self.RASModel.currentText()
        turbulence_txt = self.turbulence.currentText()
        printCoeffs_txt = self.printCoeffs.currentText()
        
        if 'turbulenceProperties' not in self.con.tables():
            query = QtSql.QSqlQuery()
            query.exec("CREATE TABLE turbulenceProperties(param, value)")

            query.exec("INSERT INTO turbulenceProperties(param, value) VALUES ('%s','%s')" % ('simulationType', ''))
            query.exec("INSERT INTO turbulenceProperties(param, value) VALUES ('%s','%s')" % ('RASModel', ''))
            query.exec("INSERT INTO turbulenceProperties(param, value) VALUES ('%s','%s')" % ('turbulence', ''))
            query.exec("INSERT INTO turbulenceProperties(param, value) VALUES ('%s','%s')" % ('printCoeffs', ''))

        if 'turbulenceProperties' in self.con.tables():
            query = QtSql.QSqlQuery()

            query.prepare("UPDATE turbulenceProperties SET value=? WHERE param='simulationType'")
            query.bindValue(0, simulationType_txt)
            query.exec_()

            query.prepare("UPDATE turbulenceProperties SET value=? WHERE param='RASModel'")
            query.bindValue(0, RASModel_txt)
            query.exec_()

            query.prepare("UPDATE turbulenceProperties SET value=? WHERE param='turbulence'")
            query.bindValue(0, turbulence_txt)
            query.exec_()

            query.prepare("UPDATE turbulenceProperties SET value=? WHERE param='printCoeffs'")
            query.bindValue(0, printCoeffs_txt)
            query.exec_()

        # записываем файл turbulenceProperties
        if os.path.exists(self.full_dir + '/constant/turbulenceProperties'):
            os.remove(self.full_dir + '/constant/turbulenceProperties')
		
        shutil.copyfile("./matches/Shablon/constant/turbulenceProperties", self.full_dir + '/constant/turbulenceProperties')
		
        tP = open(self.full_dir + '/constant/turbulenceProperties', 'a')
		
        ###simulationType###
        sT_bl = '\n' + 'simulationType     ' + simulationType_txt + ';' + '\n'

        RAS_start_bl = '\n' + 'RAS' + '\n' + '{'

        ###RASModel###
        RASModel_bl = '\n' + '    ' + 'RASModel        ' + RASModel_txt + ';' + '\n\n'

        ###turbulence###
        turbulence_bl = '\n' + '    ' + 'turbulence      ' + turbulence_txt + ';' + '\n\n'

        ###printCoeffs###
        printCoeffs_bl = '\n' + '    ' + 'printCoeffs     ' + printCoeffs_txt + ';' + '\n'

        RAS_end_bl = '}' + '\n\n'

        tP.write(sT_bl + RAS_start_bl + RASModel_bl + turbulence_bl + printCoeffs_bl + RAS_end_bl)
        close_str = '// ************************************************************************* //'
        tP.write(close_str)

        tP.close()

        self.par.cdw.setWidget(self.par.outf_scroll)
        outf = open(self.full_dir + '/constant/turbulenceProperties')

        if self.interface_lng_val == 'Russian':
            msg_lbl = QLabel(
                '<span style="color:green">Файл turbulenceProperties сохранен</span>')
        elif self.interface_lng_val == 'English':
            msg_lbl = QLabel(
                '<span style="color:green">The turbulenceProperties file saved</span>')

        self.par.listWidget.clear()
        self.par.item = QListWidgetItem()
        self.par.listWidget.addItem(self.par.item)
        self.par.listWidget.setItemWidget(self.par.item, msg_lbl)

        data = outf.read()

        if self.interface_lng_val == 'Russian':
            self.par.outf_lbl.setText("Файл " + "<font color='peru'>" + 'turbulenceProperties' + "</font>")
        elif self.interface_lng_val == 'English':
            self.par.outf_lbl.setText("<font color='peru'>" + 'turbulenceProperties' + "</font>" + " file")
        self.par.outf_edit.setText(data)

        self.par.cdw.setTitleBarWidget(self.par.cdw_frame)
        outf.close()

