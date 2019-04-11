# -*- coding: utf-8 -*-
# -----------------------------Импорт модулей-----------------------------------

from PyQt5 import QtSql
from PyQt5 import QtCore
import os
import os.path
import shutil

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QTableWidget, QComboBox, \
    QSpinBox, QPushButton, QListWidgetItem, QDoubleSpinBox, QLineEdit, QGridLayout, QHBoxLayout, \
    QFrame, QGroupBox, QTabWidget, QHBoxLayout, QScrollArea

# -----------------------------------Форма--------------------------------------

class mirrorMeshDict_y_form_class(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.interface_lng_val = parent.interface_lng_val
        self.con = parent.con
        self.full_dir = parent.full_dir
        self.par = parent
        flag = False
        if 'mirrorMeshDict_y' in self.con.tables():
            
            query = QtSql.QSqlQuery()
            query.exec("SELECT * FROM mirrorMeshDict_y")
            flag = True
            if query.isActive():
                query.first()
                
                name_list = []
                value_list = []
				
                while query.isValid():
                    name_res = query.value('name')
                    value_res = query.value('value')
					
                    name_list.append(name_res)
                    value_list.append(value_res)
                   
                    query.next()
					

            #self.data_reprint()

		
        main_lbl = QLabel()
		
		# planeType
        planeType_lbl = QLabel()
        planeType_hbox = QHBoxLayout()
        self.planeType_edit = QComboBox()
        self.planeType_edit.setFixedSize(150, 25)
        planeType_list = ["pointAndNormal", "demo"]
        self.planeType_edit.addItems(planeType_list)
        planeType_hbox.addWidget(planeType_lbl)
        planeType_hbox.addWidget(self.planeType_edit)
        
		#pointAndNormalDict
        pAND_lbl = QLabel()
		
		#point
        point_lbl = QLabel()
        self.x1 = QLineEdit()
        self.x1.setFixedSize(50, 25)
        self.y1 = QLineEdit()
        self.y1.setFixedSize(50, 25)
        self.z1 = QLineEdit()
        self.z1.setFixedSize(50, 25)
        point_hbox = QHBoxLayout()
        point_hbox.addWidget(point_lbl)
        point_hbox.addWidget(self.x1)
        point_hbox.addWidget(self.y1)
        point_hbox.addWidget(self.z1)
        
		#normal
        normal_lbl = QLabel()
        self.x2 = QLineEdit()
        self.x2.setFixedSize(50, 25)
        self.y2 = QLineEdit()
        self.y2.setFixedSize(50, 25)
        self.z2 = QLineEdit()
        self.z2.setFixedSize(50, 25)
        
        normal_hbox = QHBoxLayout()
        normal_hbox.addWidget(normal_lbl)
        normal_hbox.addWidget(self.x2)
        normal_hbox.addWidget(self.y2)
        normal_hbox.addWidget(self.z2)
		
        pAND_grid = QGridLayout()
        pAND_grid.addLayout(point_hbox, 0, 0, alignment=QtCore.Qt.AlignCenter)
        pAND_grid.addLayout(normal_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
        pAND_frame = QFrame()
        pAND_frame.setFixedSize(250, 100)
        pAND_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        pAND_frame.setFrameShape(QFrame.Panel)
        pAND_frame.setFrameShadow(QFrame.Sunken)
        pAND_frame.setLayout(pAND_grid)
		
		# planeTolerance
        planeTolerance_lbl = QLabel()
        self.planeTolerance_edit = QLineEdit()
        self.planeTolerance_edit.setFixedSize(150, 25)
        
        if flag == True:
            planeType_mas = self.planeType_edit.count()   
            for i in range(planeType_mas):
                if self.planeType_edit.itemText(i) == value_list[0]:
                    self.planeType_edit.setCurrentIndex(i)
					
            self.x1.setText(value_list[1].split()[0])
            self.y1.setText(value_list[1].split()[1])
            self.z1.setText(value_list[1].split()[2])
			
            self.x2.setText(value_list[2].split()[0])
            self.y2.setText(value_list[2].split()[1])
            self.z2.setText(value_list[2].split()[2])
			
            self.planeTolerance_edit.setText(value_list[3])
			
        planeTolerance_grid = QGridLayout()
        planeTolerance_grid.addWidget(planeTolerance_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
        planeTolerance_grid.addWidget(self.planeTolerance_edit, 0, 1, alignment=QtCore.Qt.AlignCenter)
		
        btnSave = QPushButton()
        btnSave.setFixedSize(80, 25)
        btnSave.clicked.connect(self.on_btnSave_clicked)
        buttons_hbox = QHBoxLayout()
        buttons_hbox.addWidget(btnSave)

        if self.interface_lng_val == 'Russian':
            btnSave.setText("Сохранить")
            main_lbl.setText("Укажите параметры плоскости")
            planeType_lbl.setText("planeType:")
            pAND_lbl.setText("pointAndNormalDict")
            point_lbl.setText("point:")
            normal_lbl.setText("normal:")
            planeTolerance_lbl.setText("planeTolerance:")
			
        elif self.interface_lng_val == 'English':	
            btnSave.setText("Save")
            main_lbl.setText("Specify the parameters of the plane")
            planeType_lbl.setText("planeType:")
            pAND_lbl.setText("pointAndNormalDict")
            point_lbl.setText("point:")
            normal_lbl.setText("normal:")
            planeTolerance_lbl.setText("planeTolerance:")	
			
        mMD_grid = QGridLayout()
        mMD_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
        mMD_grid.addLayout(planeType_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
        mMD_grid.addWidget(pAND_lbl, 2, 0, alignment=QtCore.Qt.AlignCenter)	
        mMD_grid.addWidget(pAND_frame, 3, 0, alignment=QtCore.Qt.AlignCenter)
        mMD_grid.addLayout(planeTolerance_grid, 4, 0, alignment=QtCore.Qt.AlignCenter)
        mMD_grid.addLayout(buttons_hbox, 5, 0, alignment=QtCore.Qt.AlignCenter) 
        mMD_grid.setRowStretch(6, 2)
        mMD_frame = QFrame()
        mMD_frame.setFixedSize(670, 510)
        mMD_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        mMD_frame.setFrameShape(QFrame.Panel)
        mMD_frame.setFrameShadow(QFrame.Sunken)
        mMD_frame.setLayout(mMD_grid)

        mMD_vbox = QVBoxLayout()
        mMD_vbox.addWidget(mMD_frame)

		# ---------------------Размещение на форме всех компонентов-------------------------#

        form = QFormLayout()
        form.addRow(mMD_vbox)
        self.setLayout(form)

		
    def on_btnSave_clicked(self):	
        planeType_txt = self.planeType_edit.currentText()
		
        msg_list = []
		
        x1_txt = self.x1.text()
        y1_txt = self.y1.text()
        z1_txt = self.z1.text()
		
        x2_txt = self.x2.text()
        y2_txt = self.y2.text()
        z2_txt = self.z2.text()
		
        xyz1_list = []
        xyz1_list.append(x1_txt)
        xyz1_list.append(y1_txt)
        xyz1_list.append(z1_txt)
		
        xyz2_list = []
        xyz2_list.append(x2_txt)
        xyz2_list.append(y2_txt)
        xyz2_list.append(z2_txt)
		
        planeTolerance_txt = self.planeTolerance_edit.text()
		
        if x1_txt == '':
            if self.interface_lng_val == 'Russian':
                msg = 'Укажите значение x для параметра point'
            elif self.interface_lng_val == 'English':
                msg = 'Specify the x value for the point parameter'
            msg_list.append(msg)
			
        if y1_txt == '':
            if self.interface_lng_val == 'Russian':
                msg = 'Укажите значение y для параметра point'
            elif self.interface_lng_val == 'English':
                msg = 'Specify the y value for the point parameter'
            msg_list.append(msg)
			
        if z1_txt == '':
            if self.interface_lng_val == 'Russian':
                msg = 'Укажите значение z для параметра point'
            elif self.interface_lng_val == 'English':
                msg = 'Specify the z value for the point parameter'
            msg_list.append(msg)
			
        if x2_txt == '':
            if self.interface_lng_val == 'Russian':
                msg = 'Укажите значение x для параметра normal'
            elif self.interface_lng_val == 'English':
                msg = 'Specify the x value for the normal parameter'
            msg_list.append(msg)
			
        if y2_txt == '':
            if self.interface_lng_val == 'Russian':
                msg = 'Укажите значение y для параметра normal'
            elif self.interface_lng_val == 'English':
                msg = 'Specify the y value for the normal parameter'
            msg_list.append(msg)
			
        if z2_txt == '':
            if self.interface_lng_val == 'Russian':
                msg = 'Укажите значение z для параметра normal'
            elif self.interface_lng_val == 'English':
                msg = 'Specify the z value for the normal parameter'
            msg_list.append(msg)
			
        if planeTolerance_txt == '':
            if self.interface_lng_val == 'Russian':
                msg = 'Укажите значение для параметра planeTolerance'
            elif self.interface_lng_val == 'English':
                msg = 'Specify the value for the planeTolerance parameter'
            msg_list.append(msg)
			
        for msg in msg_list:
            msg_lbl = QLabel('<span style="color:red">' + msg + '</span>')
            self.par.item = QListWidgetItem()
            self.par.listWidget.addItem(self.par.item)
            self.par.listWidget.setItemWidget(self.par.item, msg_lbl)

        if '' not in xyz1_list and '' not in xyz2_list and planeTolerance_txt != '':
            if 'mirrorMeshDict_y' not in self.con.tables():
                query = QtSql.QSqlQuery()
				
                xyz1_str = x1_txt + ' ' + y1_txt + ' ' + z1_txt
                xyz2_str = x2_txt + ' ' + y2_txt + ' ' + z2_txt
                				
                query.exec("CREATE TABLE mirrorMeshDict_y(name, value)")
                query.exec("INSERT INTO mirrorMeshDict_y(name, value) VALUES ('%s', '%s')" % ('planeType', planeType_txt))
                query.exec("INSERT INTO mirrorMeshDict_y(name, value) VALUES ('%s', '%s')" % ('point', xyz1_str))
                query.exec("INSERT INTO mirrorMeshDict_y(name, value) VALUES ('%s', '%s')" % ('point', xyz2_str))
                query.exec("INSERT INTO mirrorMeshDict_y(name, value) VALUES ('%s', '%s')" % ('planeTolerance', planeTolerance_txt))

            else:
                query = QtSql.QSqlQuery()
				
                xyz1_str = x1_txt + ' ' + y1_txt + ' ' + z1_txt
                xyz2_str = x2_txt + ' ' + y2_txt + ' ' + z2_txt

                query.prepare("DROP TABLE mirrorMeshDict_y")
                query.exec_()
				
                query.exec("CREATE TABLE mirrorMeshDict_y(name, value)")
			
                query.exec("INSERT INTO mirrorMeshDict_y(name, value) VALUES ('%s', '%s')" % ('planeType', planeType_txt))
                query.exec("INSERT INTO mirrorMeshDict_y(name, value) VALUES ('%s', '%s')" % ('point', xyz1_str))
                query.exec("INSERT INTO mirrorMeshDict_y(name, value) VALUES ('%s', '%s')" % ('point', xyz2_str))
                query.exec("INSERT INTO mirrorMeshDict_y(name, value) VALUES ('%s', '%s')" % ('planeTolerance', planeTolerance_txt))					
						   
            # записываем файл mirrorMeshDict.x
            if os.path.exists(self.full_dir + '/system/mirrorMeshDict.y'):
                os.remove(self.full_dir + '/system/mirrorMeshDict.y')
		
            shutil.copyfile("./matches/Shablon/system/mirrorMeshDict.y", self.full_dir + '/system/mirrorMeshDict.y')
		
            mMD_x = open(self.full_dir + '/system/mirrorMeshDict.y', 'a')

            planeType_bl = '\n' + 'planeType' + '       ' + planeType_txt + ';' + '\n'
		
            pAND_bl = '\n' + 'pointAndNormalDict' + '\n' + '{' + '\n' + '    ' + 'point' + '   ' + '(' + x1_txt + ' ' + y1_txt + ' ' + z1_txt + ');' + '\n' + \
            '    ' + 'normal' + '  ' + '(' + x2_txt + ' ' + y2_txt + ' ' + z2_txt + ');' + '\n' + '}' + '\n\n'
						   
            planeTolerance_bl = 'planeTolerance' + '  ' + planeTolerance_txt + ';' + '\n\n'
						  

            mMD_x.write(planeType_bl + pAND_bl + planeTolerance_bl)
            close_str = '// ************************************************************************* //'
            mMD_x.write(close_str)

            mMD_x.close()
			
            if self.interface_lng_val == 'Russian':
                msg = 'Файл mirrorMeshDict.y сохранен'
            elif self.interface_lng_val == 'English':
                msg = 'The mirrorMeshDict.y file saved</span>'
				
            self.par.listWidget.clear()
            msg_lbl = QLabel('<span style="color:green">' + msg + '</span>')
            self.par.item = QListWidgetItem()
            self.par.listWidget.addItem(self.par.item)
            self.par.listWidget.setItemWidget(self.par.item, msg_lbl)
				
            self.data_reprint()

    def data_reprint(self):

        self.par.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.par.cdw)

        self.par.cdw.setWidget(self.par.outf_scroll)
        outf = open(self.full_dir + '/system/mirrorMeshDict.y')

        data = outf.read()

        if self.interface_lng_val == 'Russian':
            self.par.outf_lbl.setText("Файл " + "<font color='peru'>" + 'mirrorMeshDict.y' + "</font>")
        elif self.interface_lng_val == 'English':
            self.par.outf_lbl.setText("<font color='peru'>" + 'mirrorMeshDict.y' + "</font>" + " file")
        self.par.outf_edit.setText(data)

        self.par.cdw.setTitleBarWidget(self.par.cdw_frame)
        outf.close() 


        