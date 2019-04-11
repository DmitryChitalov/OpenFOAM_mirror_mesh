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

class topoSetDict_form_class(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.interface_lng_val = parent.interface_lng_val
        self.con = parent.con
        self.full_dir = parent.full_dir
        self.par = parent

        if 'createPatchDict' in self.con.tables():
            
            query = QtSql.QSqlQuery()
            query.exec("SELECT * FROM createPatchDict")
            if query.isActive():
                query.first()
                self.size = 0

                nets_back_list = []
				
                while query.isValid():
                    self.size += 1
                    nets_res = query.value('nets')
                    nets_back_list.append(nets_res)

                    query.next()

        name_val_list = []
        type_val_list = []
        action_val_list = []
        source_val_list = []
        sourceInfo_val_list = []
        # вывод значений параметров
        if 'topoSetDict' in self.con.tables():
            query = QtSql.QSqlQuery()
            query.exec ("SELECT * FROM topoSetDict")
            if query.isActive():
                query.first()


                while query.isValid():
                    name_res = query.value('name')
                    name_val_list.append(name_res)

                    type_res = query.value('type')
                    type_val_list.append(type_res)

                    action_res = query.value('action')
                    action_val_list.append(action_res)

                    source_res = query.value('source')
                    source_val_list.append(source_res)

                    sourceInfo_res = query.value('sourceInfo')
                    sourceInfo_val_list.append(sourceInfo_res)

                    query.next()

                    # application
                    #application_mas = self.application.count()
                    #for i in range(application_mas):
                        #if self.application.itemText(i) == value_list[0]:
                            #self.application.setCurrentIndex(i)

                    # startFrom
                    #startFrom_mas = self.startFrom.count()
                    #for i in range(startFrom_mas):
                        #if self.startFrom.itemText(i) == value_list[1]:
                            #self.startFrom.setCurrentIndex(i)

                    # startTime
                    #self.startTime.setValue(value_list[2])



        main_grid = QGridLayout()
        self.name_list = []
        self.type_list = []
        self.action_list = []
        self.source_list = []
        self.source_info_list = []

        self.points1_list = []
        self.points2_list = []
        k = 0
        b = 1
        while k < self.size:

            tSD_grid = QGridLayout()

            tSD_frame = QFrame()
            tSD_frame.setFixedSize(510, 230)
            tSD_frame.setLayout(tSD_grid)

            main_lbl = QLabel()



            name_lbl = QLabel()
            name_edit = QLineEdit()
            name_edit.setFixedSize(150, 25)
            name_edit.setEnabled(False)
            name_edit.setText(nets_back_list[0])
            name_hbox = QHBoxLayout()
            name_hbox.addWidget(name_lbl)
            name_hbox.addWidget(name_edit)
            self.name_list.append(name_edit)
            tSD_grid.addLayout(name_hbox, 0, 0)
            if name_val_list != []:
                name_edit.setText(name_val_list[k])

            type_lbl = QLabel()
            type_edit = QComboBox()
            type_edit.setFixedSize(150, 25)
            type_list = ["faceSet", "demo"]
            type_edit.addItems(type_list)
            type_hbox = QHBoxLayout()
            type_hbox.addWidget(type_lbl)
            type_hbox.addWidget(type_edit)
            self.type_list.append(type_edit)
            tSD_grid.addLayout(type_hbox, 1, 0)

            if type_val_list != []:
                type_mas = type_edit.count()
                for i in range(type_mas):
                    if type_edit.itemText(i) == type_val_list[k]:
                        type_edit.setCurrentIndex(i)

            action_lbl = QLabel()
            action_edit = QComboBox()
            action_edit.setFixedSize(150, 25)
            action_list_v = ["new", "demo"]
            action_edit.addItems(action_list_v)
            action_hbox = QHBoxLayout()
            action_hbox.addWidget(action_lbl)
            action_hbox.addWidget(action_edit)
            self.action_list.append(action_edit)
            tSD_grid.addLayout(action_hbox, 2, 0)

            if action_val_list != []:
                action_mas = action_edit.count()
                for i in range(action_mas):
                    if action_edit.itemText(i) == action_val_list[k]:
                        action_edit.setCurrentIndex(i)

            source_lbl = QLabel()
            source_edit = QComboBox()
            source_edit.setFixedSize(150, 25)
            source_list_v = ["boxToFace", "demo"]
            source_edit.addItems(source_list_v)
            source_hbox = QHBoxLayout()
            source_hbox.addWidget(source_lbl)
            source_hbox.addWidget(source_edit)
            self.source_list.append(source_edit)

            if source_val_list != []:
                source_mas = source_edit.count()
                for i in range(source_mas):
                    if source_edit.itemText(i) == source_val_list[k]:
                        source_edit.setCurrentIndex(i)

            sourceInfo_lbl = QLabel()
            sourceInfo = QComboBox()
            sourceInfo.setFixedSize(70, 25)
            sourceInfo_list = ["box", "demo"]
            sourceInfo.addItems(sourceInfo_list)
            sourceInfo_hbox = QHBoxLayout()
            sourceInfo_hbox.addWidget(sourceInfo_lbl)
            sourceInfo_hbox.addWidget(sourceInfo)
            self.source_info_list.append(sourceInfo)
            #tSD_grid.addLayout(sourceInfo_hbox, 4, 0)



            point1_list = []
            point_1_lbl = QLabel()
            x1 = QLineEdit()
            x1.setFixedSize(40, 25)
            y1 = QLineEdit()
            y1.setFixedSize(40, 25)
            z1 = QLineEdit()
            z1.setFixedSize(40, 25)
            point1_list.append(x1)
            point1_list.append(y1)
            point1_list.append(z1)

            #print(x1.text())
            #print(y1.text())
            #print(z1.text())

            point2_list = []
            point_2_lbl = QLabel()
            x2 = QLineEdit()
            x2.setFixedSize(40, 25)
            y2 = QLineEdit()
            y2.setFixedSize(40, 25)
            z2 = QLineEdit()
            z2.setFixedSize(40, 25)
            point2_list.append(x2)
            point2_list.append(y2)
            point2_list.append(z2)

            if sourceInfo_val_list != []:
                sourceInfo_mas = sourceInfo.count()
                for i in range(sourceInfo_mas):
                    if sourceInfo.itemText(i) == sourceInfo_val_list[k].split()[0]:
                        sourceInfo.setCurrentIndex(i)

                x1.setText(sourceInfo_val_list[k].split()[1])
                y1.setText(sourceInfo_val_list[k].split()[2])
                z1.setText(sourceInfo_val_list[k].split()[3])

                x2.setText(sourceInfo_val_list[k].split()[4])
                y2.setText(sourceInfo_val_list[k].split()[5])
                z2.setText(sourceInfo_val_list[k].split()[6])

            self.points1_list.append(point1_list)
            self.points2_list.append(point2_list)

            #point_hbox = QHBoxLayout()
            sourceInfo_hbox.addWidget(point_1_lbl)
            sourceInfo_hbox.addWidget(x1)
            sourceInfo_hbox.addWidget(y1)
            sourceInfo_hbox.addWidget(z1)
            sourceInfo_hbox.addWidget(point_2_lbl)
            sourceInfo_hbox.addWidget(x2)
            sourceInfo_hbox.addWidget(y2)
            sourceInfo_hbox.addWidget(z2)
            #tSD_grid.addLayout(point_hbox, 5, 0)
            tSD_grid.addLayout(source_hbox, 3, 0)
            tSD_grid.addLayout(sourceInfo_hbox, 4, 0)
            main_grid.addWidget(main_lbl, k, 0, alignment=QtCore.Qt.AlignCenter)
            main_grid.addWidget(tSD_frame, k+1, 0, alignment=QtCore.Qt.AlignCenter)

            if self.interface_lng_val == 'Russian':
                main_lbl.setText("Параметры патча " + str(b))


            elif self.interface_lng_val == 'English':

                main_lbl.setText("Patch " + str(b) + " parameters")

            k += 2
            b += 1

        # -------------------------Главный фрейм формы с элементами--------------------------#

        btnSave = QPushButton()
        btnSave.setFixedSize(80, 25)
        btnSave.clicked.connect(self.on_btnSave_clicked)
        buttons_hbox = QHBoxLayout()
        buttons_hbox.addWidget(btnSave)

        if self.interface_lng_val == 'Russian':
            btnSave.setText("Сохранить")
            name_lbl.setText("Имя патча:")
            type_lbl.setText("Тип:")
            source_lbl.setText("Ресурс:")
            action_lbl.setText("Действие:")
            sourceInfo_lbl.setText("Рес. инфо:")
            point_1_lbl.setText("xyz1:")
            point_2_lbl.setText("xyz2:")

        elif self.interface_lng_val == 'English':

            btnSave.setText("Save")
            name_lbl.setText("name:")
            type_lbl.setText("type:")
            source_lbl.setText("source:")
            action_lbl.setText("action:")
            sourceInfo_lbl.setText("sourceInfo:")
            point_1_lbl.setText("xyz1:")
            point_2_lbl.setText("xyz2:")






        main_grid.addLayout(buttons_hbox, self.size + 1, 0, alignment=QtCore.Qt.AlignCenter)
        main_frame = QFrame()
        main_frame.setFixedSize(670, 510)
        main_frame.setStyleSheet(open("./styles/properties_form_style.qss", "r").read())
        main_frame.setFrameShape(QFrame.Panel)
        main_frame.setFrameShadow(QFrame.Sunken)
        main_frame.setLayout(main_grid)

        main_vbox = QVBoxLayout()
        main_vbox.addWidget(main_frame)

        # ---------------------Размещение на форме всех компонентов-------------------------#

        form = QFormLayout()
        form.addRow(main_vbox)
        self.setLayout(form)

    def on_btnSave_clicked(self):
        #print(self.points1_list)
        #print('вах')
        #global name_val_list, type_val_list, constructFrom_val_list, set_val_list
        #i = 0
        #j = 1
        #msg_list = []
        #name_val_list = []
        #type_val_list = []
        #constructFrom_val_list = []
        #set_val_list = []
        msg_list = []
        h = 1
        m = 0
        for el in self.points1_list:
            if el[0].text() == '':
                if self.interface_lng_val == 'Russian':
                    msg = 'Укажите значение координаты x точки 1 патча' + str(h)
                elif self.interface_lng_val == 'English':
                    msg = 'Set the value of x of point ' + str(h)
                msg_list.append(msg)
            if el[1].text() == '':
                if self.interface_lng_val == 'Russian':
                    msg = 'Укажите значение координаты y точки 1 патча' + str(h)
                elif self.interface_lng_val == 'English':
                    msg = 'Set the value of y of point ' + str(h)
                msg_list.append(msg)
            if el[2].text() == '':
                if self.interface_lng_val == 'Russian':
                    msg = 'Укажите значение координаты z точки 1 патча' + str(h)
                elif self.interface_lng_val == 'English':
                    msg = 'Set the value of z of point ' + str(h)
                msg_list.append(msg)
            if self.points2_list[m][0].text() == '':
                if self.interface_lng_val == 'Russian':
                    msg = 'Укажите значение координаты x точки 2 патча' + str(h)
                elif self.interface_lng_val == 'English':
                    msg = 'Set the value of x of point ' + str(h)
                msg_list.append(msg)

            if self.points2_list[m][1].text() == '':
                if self.interface_lng_val == 'Russian':
                    msg = 'Укажите значение координаты y точки 2 патча' + str(h)
                elif self.interface_lng_val == 'English':
                    msg = 'Set the value of y of point ' + str(h)
                msg_list.append(msg)

            if self.points2_list[m][2].text() == '':
                if self.interface_lng_val == 'Russian':
                    msg = 'Укажите значение координаты z точки 2 патча' + str(h)
                elif self.interface_lng_val == 'English':
                    msg = 'Set the value of z of point ' + str(h)
                msg_list.append(msg)

            h += 1
            m += 1

        self.par.listWidget.clear()

        for msg in msg_list:
            msg_lbl = QLabel('<span style="color:red">' + msg + '</span>')
            self.par.item = QListWidgetItem()
            self.par.listWidget.addItem(self.par.item)
            self.par.listWidget.setItemWidget(self.par.item, msg_lbl)
        #print(msg_list)
        if msg_list == []:


            # заносим в базу
            if 'topoSetDict' not in self.con.tables():
                query = QtSql.QSqlQuery()

                query.exec("CREATE TABLE topoSetDict(name, type, action, source, sourceInfo)")

                b = 0
                for el in self.points1_list:
                    source_info_itog = self.source_info_list[b].currentText() + ' ' + str(self.points1_list[b][0].text()) + ' ' + \
                                       str(self.points1_list[b][1].text()) + ' ' + str(self.points1_list[b][2].text()) + ' ' + \
                                       str(self.points2_list[b][0].text()) + ' ' + str(self.points2_list[b][1].text()) + ' ' + \
                                       str(self.points2_list[b][2].text())

                    query.exec("INSERT INTO topoSetDict(name, type, action, source, sourceInfo) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
                        self.name_list[b].text(), self.type_list[b].currentText(), self.action_list[b].currentText(),
                        self.source_list.currentText(), source_info_itog))
                    b += 1

            else:
                query = QtSql.QSqlQuery()

                query.prepare("DROP TABLE topoSetDict")
                query.exec_()

                query.exec ("CREATE TABLE topoSetDict(name, type, action, source, sourceInfo)")

                b = 0
                for el in self.points1_list:
                    source_info_itog = self.source_info_list[b].currentText() + ' ' + str(self.points1_list[b][0].text()) + ' ' + \
                                       str(self.points1_list[b][1].text()) + ' ' + str(self.points1_list[b][2].text()) + ' ' + \
                                       str(self.points2_list[b][0].text()) + ' ' + str(self.points2_list[b][1].text()) + ' ' + \
                                       str(self.points2_list[b][2].text())


                    query.exec("INSERT INTO topoSetDict(name, type, action, source, sourceInfo) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
                            self.name_list[b].text(), self.type_list[b].currentText(),
                            self.action_list[b].currentText(),
                            self.source_list[b].currentText(), source_info_itog))
                    b += 1


            # записываем файл topoSetDict
            if os.path.exists(self.full_dir + '/system/topoSetDict'):
                os.remove(self.full_dir + '/system/topoSetDict')

            shutil.copyfile("./matches/Shablon/system/topoSetDict", self.full_dir + '/system/topoSetDict')

            tSD = open(self.full_dir + '/system/topoSetDict', 'a')

            actions_start_bl = '\n' + 'actions' + '\n' + '(' + '\n'

            actions_end_bl = ');' + '\n\n'
            d = 0
            patch_main_bl = ''
            for el in self.points1_list:
                p_start_lbl = '    ' + '{' + '\n'

                p_end_lbl = '    ' + '}' + '\n'

                name_lbl = '        ' + 'name' + '    ' + self.name_list[d].text() + ';' + '\n'
                type_lbl = '        ' + 'type' + '    ' + self.type_list[d].currentText() + ';' + '\n'
                action_lbl = '        ' + 'action' + '  ' + self.action_list[d].currentText() + ';' + '\n'
                source_lbl = '        ' + 'source' + '  ' + self.source_list[d].currentText() + ';' + '\n'
                source_info_lbl = '        ' + 'sourceInfo' + '\n' + '        ' + '{' + '\n' + \
                    '            ' + self.source_info_list[d].currentText() + ' ' + '(' + self.points1_list[d][0].text() + \
                    ' ' + self.points1_list[d][1].text() + ' ' + self.points1_list[d][2].text() + ')' + \
                    '(' + self.points2_list[d][0].text() + ' ' + self.points2_list[d][1].text() + ' ' + self.points2_list[d][2].text() + ')' + \
                    ';' + '\n' + '        ' + '}' + '\n'

                itog_lbl = p_start_lbl + name_lbl + type_lbl + action_lbl + source_lbl + source_info_lbl + p_end_lbl
                patch_main_bl += itog_lbl

                d += 1

            tSD.write(actions_start_bl + patch_main_bl + actions_end_bl)
            close_str = '// ************************************************************************* //'
            tSD.write(close_str)

            tSD.close()

            self.par.cdw.setWidget(self.par.outf_scroll)
            outf = open(self.full_dir + '/system/topoSetDict')

            if self.interface_lng_val == 'Russian':
                msg = 'Файл topoSetDict сохранен'
            elif self.interface_lng_val == 'English':
                msg = 'The topoSetDict file saved</span>'

            self.par.listWidget.clear()
            msg_lbl = QLabel('<span style="color:green">' + msg + '</span>')
            self.par.item = QListWidgetItem()
            self.par.listWidget.addItem(self.par.item)
            self.par.listWidget.setItemWidget(self.par.item, msg_lbl)

            data = outf.read()

            if self.interface_lng_val == 'Russian':
                self.par.outf_lbl.setText("Файл " + "<font color='peru'>" + 'topoSetDict' + "</font>")
            elif self.interface_lng_val == 'English':
                self.par.outf_lbl.setText("<font color='peru'>" + 'topoSetDict' + "</font>" + " file")
            self.par.outf_edit.setText(data)

            self.par.cdw.setTitleBarWidget(self.par.cdw_frame)
            outf.close()




'''





















            
            if self.size >= 1:
                #print(self.size)
                self.patch_numb_edit.setValue(self.size)
			
                pn = self.patch_numb_edit.value()
                patches_grid = QGridLayout()
                patches_lbl = QLabel()
		
                pointSync_lbl = QLabel()
                self.pointSync_edit = QComboBox()
                self.pointSync_edit.setFixedSize(150, 25)
                pointSync_list = ['false', 'true']
                self.pointSync_edit.addItems(pointSync_list)
                pointSync_hbox = QHBoxLayout()
                pointSync_hbox.addWidget(pointSync_lbl)
                pointSync_hbox.addWidget(self.pointSync_edit)
		
                patches_grid.addWidget(patches_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
                patches_grid.addLayout(pointSync_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
		
                k = 1
                v = 2
                y = 0

				
                self.name_edit_list = []
                self.type_edit_list = []
                self.constructFrom_edit_list = []
                self.set_edit_list = []
        
                while k <= pn:
	
                    name_lbl = QLabel()
                    name_hbox = QHBoxLayout()
                    name_edit = QLineEdit()
                    name_edit.setFixedSize(150, 25)
                    name_hbox.addWidget(name_lbl)
                    name_hbox.addWidget(name_edit)
                    name_edit.setText(name_back_list[y])
			
                    type_lbl = QLabel()
                    type_hbox = QHBoxLayout()
                    type_edit = QComboBox()
                    type_edit.setFixedSize(150, 25)
                    type_list = ["patch"]
                    type_edit.addItems(type_list)
                    type_hbox.addWidget(type_lbl)
                    type_hbox.addWidget(type_edit)
                    type_mas = type_edit.count()   
                    for i in range(type_mas):
                        if type_edit.itemText(i) == type_back_list[y]:
                            type_edit.setCurrentIndex(i)
			
                    constructFrom_lbl = QLabel()
                    constructFrom_hbox = QHBoxLayout()
                    constructFrom_edit = QComboBox()
                    constructFrom_edit.setFixedSize(110, 25)
                    constructFrom_list = ["set"]
                    constructFrom_edit.addItems(constructFrom_list)
                    constructFrom_hbox.addWidget(constructFrom_lbl)
                    constructFrom_hbox.addWidget(constructFrom_edit)
                    constructFrom_mas = constructFrom_edit.count()   
                    for i in range(constructFrom_mas):
                        if constructFrom_edit.itemText(i) == cF_back_list[y]:
                            constructFrom_edit.setCurrentIndex(i)
			
                    set_lbl = QLabel()
                    set_hbox = QHBoxLayout()
                    set_edit = QLineEdit()
                    set_edit.setFixedSize(140, 25)
                    set_hbox.addWidget(set_lbl)
                    set_hbox.addWidget(set_edit)
                    set_edit.setText(nets_back_list[y])

                    self.name_edit_list.append(name_edit)
                    self.type_edit_list.append(type_edit)
                    self.constructFrom_edit_list.append(constructFrom_edit)
                    self.set_edit_list.append(set_edit)
			
                    patch_grid = QGridLayout()
                    patch_grid.addLayout(name_hbox, 0, 0)
                    patch_grid.addLayout(type_hbox, 1, 0)
                    patch_grid.addLayout(constructFrom_hbox, 2, 0)
                    patch_grid.addLayout(set_hbox, 3, 0)
				
                    patch_frame = QFrame()
                    patch_frame.setFixedSize(250, 130)
                    patch_frame.setLayout(patch_grid)
			
                    if self.interface_lng_val == 'Russian':
                
                        name_lbl.setText("Имя патча:")
                        type_lbl.setText("Тип патча:")
                        constructFrom_lbl.setText("Конструирование:")
                        set_lbl.setText("Поверхность:")
                
                    elif self.interface_lng_val == 'English':
                
                        name_lbl.setText("Patch name:")
                        type_lbl.setText("Patch type:")
                        constructFrom_lbl.setText("Construct from:")
                        set_lbl.setText("Face set:")
                		
                    patches_grid.addWidget(patch_frame, v, 0, alignment=QtCore.Qt.AlignCenter)
		
                    k += 1
                    v += 1
                    y += 1
			
                patches_btnSave = QPushButton()
                patches_btnSave.setFixedSize(80, 25)

                buttons_hbox = QHBoxLayout()
                buttons_hbox.addWidget(patches_btnSave)

                patches_grid.addLayout(buttons_hbox, len(self.name_edit_list) + 3, 0, alignment=QtCore.Qt.AlignCenter)
                patches_grid.setRowStretch(3, 6)

                self.patches_group = QGroupBox()
                self.patches_group.setLayout(patches_grid)
				
                prs_grid = QGridLayout()
                prs_grid.addWidget(patch_numb_lbl, 0, 0)
                prs_grid.addWidget(self.patch_numb_edit, 0, 1)
				
                prs_frame = QFrame()
                prs_frame.setFixedSize(250, 70)
                prs_frame.setLayout(prs_grid)
		
                initial_btnSave = QPushButton()
                initial_btnSave.setFixedSize(80, 25)

                buttons_hbox = QHBoxLayout()
                buttons_hbox.addWidget(initial_btnSave)
		
                initial_grid = QGridLayout()
                initial_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
                initial_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
                initial_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
                initial_grid.setRowStretch(3, 6)
				
                self.initial_group = QGroupBox()
                self.initial_group.setLayout(initial_grid)
				
                self.tab = QTabWidget()
                self.tab.insertTab(0, self.initial_group, "&initial")
                self.tab.insertTab(1, self.patches_group, "&new_patches")
                patches_btnSave.clicked.connect(self.on_patches_btnSave_clicked)
                initial_btnSave.clicked.connect(self.on_initial_btnSave_clicked)
		
                if self.interface_lng_val == 'Russian':
                    patches_lbl.setText("Укажите параметры патчей")
                    patches_btnSave.setText("Записать")
                    pointSync_lbl.setText("Точка синхронизации:")
                
                elif self.interface_lng_val == 'English':
                    patches_btnSave.setText("Write")
                    patches_lbl.setText("Set patches parameters")
                    pointSync_lbl.setText("Synchronization point:")
        else:	
            #self.par.listWidget.clear()
            #msg_lbl = QLabel('<span style="color:green">' + msg + '</span>')
            #self.par.item = QListWidgetItem()
            #self.par.listWidget.addItem(self.par.item)
            #self.par.listWidget.setItemWidget(self.par.item, msg_lbl)		

            prs_grid = QGridLayout()
            prs_grid.addWidget(patch_numb_lbl, 0, 0)
            prs_grid.addWidget(self.patch_numb_edit, 0, 1)
				
            prs_frame = QFrame()
            prs_frame.setFixedSize(250, 70)
            prs_frame.setLayout(prs_grid)
		
            initial_btnSave = QPushButton()
            initial_btnSave.setFixedSize(80, 25)

            buttons_hbox = QHBoxLayout()
            buttons_hbox.addWidget(initial_btnSave)
		
            initial_grid = QGridLayout()
            initial_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
            initial_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
            initial_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
            initial_grid.setRowStretch(3, 6)

            self.initial_group = QGroupBox()
            self.initial_group.setLayout(initial_grid)
		
		    #-----new_patches
		
		
		    ###табличный виджет для групп
            self.tab = QTabWidget()
		    #initial_group, spe_edit, nospe_lbl, nospe_edit, initial_btnSave, cTM_edit, nov_edit, spp_edit, nop_lbl, nop_edit, nob_edit, mpp_lbl, mpp_edit, nompp_lbl, nompp_edit, vertices_visible, blocks_visible, edges_visible, patches_visible, mergepatchpairs_visible = initial_class.out_frame_func(int_lng, prj_path, mesh_name_txt)
            self.tab.insertTab(0, self.initial_group, "&initial")
		    #spe_edit.stateChanged.connect(self.spe_state_changed)
		    #spp_edit.stateChanged.connect(self.spp_state_changed)
		    #mpp_edit.stateChanged.connect(self.mpp_state_changed)
            initial_btnSave.clicked.connect(self.on_initial_btnSave_clicked)
		
		
		#-------------------------Главный фрейм формы с элементами--------------------------#

        btnSave = QPushButton()
        btnSave.setFixedSize(80, 25)
        btnSave.clicked.connect(self.on_btnSave_clicked)
        buttons_hbox = QHBoxLayout()
        buttons_hbox.addWidget(btnSave)

        if self.interface_lng_val == 'Russian':
            initial_btnSave.setText("Записать")
            btnSave.setText("Сохранить")
            main_lbl.setText('Укажите количество патчей')
            patch_numb_lbl.setText('Количество патчей:')
        elif self.interface_lng_val == 'English':	
            initial_btnSave.setText("Write")
            btnSave.setText("Save")
            main_lbl.setText('Set patches number')
            patch_numb_lbl.setText('Patches number:')
   
        scrollLayout = QFormLayout()
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True) 
        scrollArea.setWidget(self.tab)
        scrollArea.setFixedSize(650, 460)	
			
        cPD_grid = QGridLayout()
        cPD_grid.addWidget(scrollArea, 0, 0, alignment=QtCore.Qt.AlignCenter)
        cPD_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
        cPD_frame = QFrame()
        cPD_frame.setFixedSize(670, 510)
        cPD_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        cPD_frame.setFrameShape(QFrame.Panel)
        cPD_frame.setFrameShadow(QFrame.Sunken)
        cPD_frame.setLayout(cPD_grid)

        cPD_vbox = QVBoxLayout()
        cPD_vbox.addWidget(cPD_frame)

		# ---------------------Размещение на форме всех компонентов-------------------------#

        form = QFormLayout()
        form.addRow(cPD_vbox)
        self.setLayout(form)
		
	############################Сохраняем начальные данные###################################
		
    def on_initial_btnSave_clicked(self):
        #print('вах')
        #global name_edit_list, type_edit_list, constructFrom_edit_list, set_edit_list
		#, pointSync_edit 
        self.tab.removeTab(1)
        pn = self.patch_numb_edit.value()
        patches_grid = QGridLayout()
        patches_lbl = QLabel()
		
        pointSync_lbl = QLabel()
        self.pointSync_edit = QComboBox()
        self.pointSync_edit.setFixedSize(150, 25)
        pointSync_list = ['false', 'true']
        self.pointSync_edit.addItems(pointSync_list)
        pointSync_hbox = QHBoxLayout()
        pointSync_hbox.addWidget(pointSync_lbl)
        pointSync_hbox.addWidget(self.pointSync_edit)
		
        patches_grid.addWidget(patches_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
        patches_grid.addLayout(pointSync_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
		
        k = 1
        v = 2
        self.name_edit_list = []
        self.type_edit_list = []
        self.constructFrom_edit_list = []
        self.set_edit_list = []
        
        while k <= pn:
	
            name_lbl = QLabel()
            name_hbox = QHBoxLayout()
            name_edit = QLineEdit()
            name_edit.setFixedSize(150, 25)
            name_hbox.addWidget(name_lbl)
            name_hbox.addWidget(name_edit)
			
            type_lbl = QLabel()
            type_hbox = QHBoxLayout()
            type_edit = QComboBox()
            type_edit.setFixedSize(150, 25)
            type_list = ["patch"]
            type_edit.addItems(type_list)
            type_hbox.addWidget(type_lbl)
            type_hbox.addWidget(type_edit)
			
            constructFrom_lbl = QLabel()
            constructFrom_hbox = QHBoxLayout()
            constructFrom_edit = QComboBox()
            constructFrom_edit.setFixedSize(110, 25)
            constructFrom_list = ["set"]
            constructFrom_edit.addItems(constructFrom_list)
            constructFrom_hbox.addWidget(constructFrom_lbl)
            constructFrom_hbox.addWidget(constructFrom_edit)
			
            set_lbl = QLabel()
            set_hbox = QHBoxLayout()
            set_edit = QLineEdit()
            set_edit.setFixedSize(140, 25)
            set_hbox.addWidget(set_lbl)
            set_hbox.addWidget(set_edit)

            self.name_edit_list.append(name_edit)
            self.type_edit_list.append(type_edit)
            self.constructFrom_edit_list.append(constructFrom_edit)
            self.set_edit_list.append(set_edit)
			
            patch_grid = QGridLayout()
            patch_grid.addLayout(name_hbox, 0, 0)
            patch_grid.addLayout(type_hbox, 1, 0)
            patch_grid.addLayout(constructFrom_hbox, 2, 0)
            patch_grid.addLayout(set_hbox, 3, 0)
				
            patch_frame = QFrame()
            patch_frame.setFixedSize(250, 130)
            patch_frame.setLayout(patch_grid)
			
            if self.interface_lng_val == 'Russian':
                
                name_lbl.setText("Имя патча:")
                type_lbl.setText("Тип патча:")
                constructFrom_lbl.setText("Конструирование:")
                set_lbl.setText("Поверхность:")
                
            elif self.interface_lng_val == 'English':
                
                name_lbl.setText("Patch name:")
                type_lbl.setText("Patch type:")
                constructFrom_lbl.setText("Construct from:")
                set_lbl.setText("Face set:")
                		
            patches_grid.addWidget(patch_frame, v, 0, alignment=QtCore.Qt.AlignCenter)
		
            k += 1
            v += 1
			
        patches_btnSave = QPushButton()
        patches_btnSave.setFixedSize(80, 25)

        buttons_hbox = QHBoxLayout()
        buttons_hbox.addWidget(patches_btnSave)

        patches_grid.addLayout(buttons_hbox, len(self.name_edit_list) + 3, 0, alignment=QtCore.Qt.AlignCenter)
        patches_grid.setRowStretch(3, 6)

        patches_group = QGroupBox()
        patches_group.setLayout(patches_grid)
		
        self.tab.insertTab(1, patches_group, "&new_patches")
        patches_btnSave.clicked.connect(self.on_patches_btnSave_clicked)
		
        if self.interface_lng_val == 'Russian':
            patches_lbl.setText("Укажите параметры патчей")
            patches_btnSave.setText("Записать")
            msg = 'Начальные данные сохранены'
            pointSync_lbl.setText("Точка синхронизации:")
                
        elif self.interface_lng_val == 'English':
            patches_btnSave.setText("Write")
            msg = 'Initial data saved'
            patches_lbl.setText("Set patches parameters")
            pointSync_lbl.setText("Synchronization point:")
			
        self.par.listWidget.clear()
        msg_lbl = QLabel('<span style="color:green">' + msg + '</span>')
        self.par.item = QListWidgetItem()
        self.par.listWidget.addItem(self.par.item)
        self.par.listWidget.setItemWidget(self.par.item, msg_lbl)			
	
	############################Сохраняем данные о патчах###################################
	
    def on_patches_btnSave_clicked(self):
        #print('вах')
        global name_val_list, type_val_list, constructFrom_val_list, set_val_list
        i = 0
        j = 1
        msg_list = []
        name_val_list = []
        type_val_list = []
        constructFrom_val_list = []
        set_val_list = []
        for el in self.name_edit_list:
            if el.text() == '':
                if self.interface_lng_val == 'Russian':
                    msg = 'Укажите имя патча ' + str(j)
                elif self.interface_lng_val == 'English':
                    msg = 'Set name of patch of number ' + str(j)
                msg_list.append(msg)
				
            if self.set_edit_list[i].text() == '':
                if self.interface_lng_val == 'Russian':
                    msg = 'Укажите имя поверхности ' + str(j)
                elif self.interface_lng_val == 'English':
                    msg = 'Define name of set of number ' + str(j)
                msg_list.append(msg)
			
            name_val_list.append(self.name_edit_list[i].text())
            type_val_list.append(self.type_edit_list[i].currentText())
            constructFrom_val_list.append(self.constructFrom_edit_list[i].currentText())
            set_val_list.append(self.set_edit_list[i].text())
			
            i += 1
            j += 1
			
        self.par.listWidget.clear()
                		
        for msg in msg_list:
            msg_lbl = QLabel('<span style="color:red">' + msg + '</span>')
            self.par.item = QListWidgetItem()
            self.par.listWidget.addItem(self.par.item)
            self.par.listWidget.setItemWidget(self.par.item, msg_lbl)

        if '' not in name_val_list and '' not in set_val_list:
            

            if 'createPatchDict' not in self.con.tables():
                query = QtSql.QSqlQuery()
                				
                query.exec("CREATE TABLE createPatchDict(name, type, constructFrom, nets, pointSync)")
                
					
                b = 0
                for el in self.name_edit_list:

                    query.exec("INSERT INTO createPatchDict(name, type, constructFrom, nets, pointSync) VALUES ('%s', '%s', '%s', '%s', '%s')" % (el.text() , self.type_edit_list[b].currentText(), self.constructFrom_edit_list[b].currentText(), self.set_edit_list[b].text(), self.pointSync_edit.currentText()))
                    b += 1

            else:
                query = QtSql.QSqlQuery()

                query.prepare("DROP TABLE createPatchDict")
                query.exec_()
				
                query.exec("CREATE TABLE createPatchDict(name, type, constructFrom, nets, pointSync)")
			
                b = 0
                for el in self.name_edit_list:
                    query.exec("INSERT INTO createPatchDict(name, type, constructFrom, nets, pointSync) VALUES ('%s', '%s', '%s', '%s', '%s')" % (el.text() , self.type_edit_list[b].currentText(), self.constructFrom_edit_list[b].currentText(), self.set_edit_list[b].text(), self.pointSync_edit.currentText()))
                    b += 1
					
            if self.interface_lng_val == 'Russian':
                msg = 'Параметры патчей сохранены'
                
            elif self.interface_lng_val == 'English':
                msg = 'Patches parameters saved'					
					
					
            self.par.listWidget.clear()
            msg_lbl = QLabel('<span style="color:green">' + msg + '</span>')
            self.par.item = QListWidgetItem()
            self.par.listWidget.addItem(self.par.item)
            self.par.listWidget.setItemWidget(self.par.item, msg_lbl)
			    
    def on_btnSave_clicked(self):
        global name_val_list, type_val_list, constructFrom_val_list, set_val_list
        i = 0
        j = 1
        msg_list = []
        name_val_list = []
        type_val_list = []
        constructFrom_val_list = []
        set_val_list = []
        for el in self.name_edit_list:
            if el.text() == '':
                if self.interface_lng_val == 'Russian':
                    msg = 'Укажите имя патча ' + str(j)
                elif self.interface_lng_val == 'English':
                    msg = 'Set name of patch of number ' + str(j)
                msg_list.append(msg)
				
            if self.set_edit_list[i].text() == '':
                if self.interface_lng_val == 'Russian':
                    msg = 'Укажите имя поверхности ' + str(j)
                elif self.interface_lng_val == 'English':
                    msg = 'Define name of set of number ' + str(j)
                msg_list.append(msg)
			
            name_val_list.append(self.name_edit_list[i].text())
            type_val_list.append(self.type_edit_list[i].currentText())
            constructFrom_val_list.append(self.constructFrom_edit_list[i].currentText())
            set_val_list.append(self.set_edit_list[i].text())
			
            i += 1
            j += 1		
		
		
		
		# записываем файл createPatchDict
        if os.path.exists(self.full_dir + '/system/createPatchDict'):
            os.remove(self.full_dir + '/system/createPatchDict')
		
        shutil.copyfile("./matches/Shablon/system/createPatchDict", self.full_dir + '/system/createPatchDict')
		
        cPD = open(self.full_dir + '/system/createPatchDict', 'a')

        pointSync_bl = '\n' + 'pointSync' + ' ' + self.pointSync_edit.currentText() + ';' + '\n'
		
        cPD_start_bl = '\n' + 'patches' + '\n' + '(' + '\n' 
        patch_main_bl = ''
        k = 0
        for el in self.name_edit_list:
            patch_n_start_lbl = '    ' + '{' + '\n'
            name_bl = '        ' + 'name' + ' ' + name_val_list[k] + ';' + '\n\n'
            type_bl = '        ' + 'patchInfo' + '\n' + '        ' + '{' + '\n' + '            ' + 'type' + ' ' + type_val_list[k] + ';' + '\n' + '        ' + '}' + '\n\n'
            constructFrom_bl = '        ' + 'constructFrom' + ' ' + constructFrom_val_list[k] + ';' + '\n\n'
            set_bl = '        ' + 'set' + ' ' + set_val_list[k] + ';' + '\n'
            patch_n_end_lbl = '    ' + '}' + '\n'
			
            patch_middle_bl = patch_n_start_lbl + name_bl + type_bl + constructFrom_bl + set_bl + patch_n_end_lbl
			
            patch_main_bl += patch_middle_bl
			
            k += 1
			
        cPD_end_bl = ');' + '\n\n' 

        cPD.write(pointSync_bl + cPD_start_bl + patch_main_bl + cPD_end_bl)
        close_str = '// ************************************************************************* //'
        cPD.write(close_str)

        cPD.close()
		
        self.par.cdw.setWidget(self.par.outf_scroll)
        outf = open(self.full_dir + '/system/createPatchDict')

        if self.interface_lng_val == 'Russian':
            msg = 'Файл createPatchDict сохранен'
        elif self.interface_lng_val == 'English':
            msg = 'The createPatchDict file saved</span>'
			
        self.par.listWidget.clear()
        msg_lbl = QLabel('<span style="color:green">' + msg + '</span>')
        self.par.item = QListWidgetItem()
        self.par.listWidget.addItem(self.par.item)
        self.par.listWidget.setItemWidget(self.par.item, msg_lbl)

        data = outf.read()

        if self.interface_lng_val == 'Russian':
            self.par.outf_lbl.setText("Файл " + "<font color='peru'>" + 'createPatchDict' + "</font>")
        elif self.interface_lng_val == 'English':
            self.par.outf_lbl.setText("<font color='peru'>" + 'createPatchDict' + "</font>" + " file")
        self.par.outf_edit.setText(data)

        self.par.cdw.setTitleBarWidget(self.par.cdw_frame)
        outf.close()


        if self.con.open():

            self.table = QTableWidget(19, 2)
            self.table.setColumnWidth(0, 150)
            self.table.setColumnWidth(1, 230)
            self.table.setFixedSize(674, 480)
            if self.interface_lng_val == 'Russian':
                self.table.setHorizontalHeaderLabels(["Параметр", "Значение"])
            elif self.interface_lng_val == 'English':
                self.table.setHorizontalHeaderLabels(["Parameter", "Value"])
				
            # application
            application_lbl = QLabel('application')
            self.application = QComboBox()
            application_list = ["compressibleInterFoam", "rhoCentralFoam", "sonicFoam", "icoFoam", "pisoFoam"]
            self.application.addItems(application_list)
            self.table.setCellWidget(0, 1, self.application)
            self.table.setCellWidget(0, 0, application_lbl)

            # startFrom
            startFrom_lbl = QLabel('startFrom')
            self.startFrom = QComboBox()
            startFrom_list = ["startTime", "latestTime"]
            self.startFrom.addItems(startFrom_list)
            self.table.setCellWidget(1, 1, self.startFrom)
            self.table.setCellWidget(1, 0, startFrom_lbl)

            # startTime
            startTime_lbl = QLabel('startTime')
            self.startTime = QSpinBox()
            self.table.setCellWidget(2, 1, self.startTime)
            self.table.setCellWidget(2, 0, startTime_lbl)

            # stopAt
            stopAt_lbl = QLabel('stopAt')
            self.stopAt = QComboBox()
            stopAt_list = ["endTime"]
            self.stopAt.addItems(stopAt_list)
            self.table.setCellWidget(3, 1, self.stopAt)
            self.table.setCellWidget(3, 0, stopAt_lbl)

            # endTime
            endTime_lbl = QLabel('endTime')
            self.endTime = QDoubleSpinBox()
            self.endTime.setRange(0, 10000)
            self.table.setCellWidget(4, 1, self.endTime)
            self.table.setCellWidget(4, 0, endTime_lbl)

            # deltaT
            deltaT_lbl = QLabel('deltaT')
            self.deltaT = QLineEdit()
            self.deltaT.setFixedSize(100, 25)
            #self.deltaT.setRange(0, 10000)
            self.table.setCellWidget(5, 1, self.deltaT)
            self.table.setCellWidget(5, 0, deltaT_lbl)

            # writeControl
            writeControl_lbl = QLabel('writeControl')
            self.writeControl = QComboBox()
            writeControl_list = ["timeStep", "adjustableRunTime"]
            self.writeControl.addItems(writeControl_list)
            self.table.setCellWidget(6, 1, self.writeControl)
            self.table.setCellWidget(6, 0, writeControl_lbl)

            # writeInterval
            writeInterval_lbl = QLabel('writeInterval')
            self.writeInterval = QDoubleSpinBox()
            self.writeInterval.setRange(0, 10000)
            self.table.setCellWidget(7, 1, self.writeInterval)
            self.table.setCellWidget(7, 0, writeInterval_lbl)

            # purgeWrite
            purgeWrite_lbl = QLabel('purgeWrite')
            self.purgeWrite = QSpinBox()
            self.purgeWrite.setRange(0, 10000)
            self.table.setCellWidget(8, 1, self.purgeWrite)
            self.table.setCellWidget(8, 0, purgeWrite_lbl)

            # writeFormat
            writeFormat_lbl = QLabel('writeFormat')
            self.writeFormat = QComboBox()
            writeFormat_list = ["ascii", "binary"]
            self.writeFormat.addItems(writeFormat_list)
            self.table.setCellWidget(9, 1, self.writeFormat)
            self.table.setCellWidget(9, 0, writeFormat_lbl)

            # writePrecision
            writePrecision_lbl = QLabel('writePrecision')
            self.writePrecision = QSpinBox()
            self.writePrecision.setRange(0, 10000)
            self.table.setCellWidget(10, 1, self.writePrecision)
            self.table.setCellWidget(10, 0, writePrecision_lbl)

            # writeCompression
            writeCompression_lbl = QLabel('writeCompression')
            self.writeCompression = QComboBox()
            writeCompression_list = ["off"]
            self.writeCompression.addItems(writeCompression_list)
            self.table.setCellWidget(11, 1, self.writeCompression)
            self.table.setCellWidget(11, 0, writeCompression_lbl)

            # timeFormat
            timeFormat_lbl = QLabel('timeFormat')
            self.timeFormat = QComboBox()
            timeFormat_list = ["general"]
            self.timeFormat.addItems(timeFormat_list)
            self.table.setCellWidget(12, 1, self.timeFormat)
            self.table.setCellWidget(12, 0, timeFormat_lbl)

            # timePrecision
            timePrecision_lbl = QLabel('timePrecision')
            self.timePrecision = QSpinBox()
            self.timePrecision.setRange(0, 10000)
            self.table.setCellWidget(13, 1, self.timePrecision)
            self.table.setCellWidget(13, 0, timePrecision_lbl)
			
			# runTimeModifiable
            runTimeModifiable_lbl = QLabel('runTimeModifiable')
            self.runTimeModifiable = QComboBox()
            runTimeModifiable_list = ["yes", "no"]
            self.runTimeModifiable.addItems(runTimeModifiable_list)
            self.table.setCellWidget(14, 1, self.runTimeModifiable)
            self.table.setCellWidget(14, 0, runTimeModifiable_lbl)
			
			# adjustTimeStep
            adjustTimeStep_lbl = QLabel('adjustTimeStep')
            self.adjustTimeStep = QComboBox()
            adjustTimeStep_list = ["yes", "no"]
            self.adjustTimeStep.addItems(adjustTimeStep_list)
            self.table.setCellWidget(15, 1, self.adjustTimeStep)
            self.table.setCellWidget(15, 0, adjustTimeStep_lbl)
			
			# maxCo
            maxCo_lbl = QLabel('maxCo')
            self.maxCo = QDoubleSpinBox()
            self.maxCo.setRange(0, 10000)
            self.table.setCellWidget(16, 1, self.maxCo)
            self.table.setCellWidget(16, 0, maxCo_lbl)
			
			# maxAlphaCo
            maxAlphaCo_lbl = QLabel('maxAlphaCo')
            self.maxAlphaCo = QDoubleSpinBox()
            self.maxAlphaCo.setRange(0, 10000)
            self.table.setCellWidget(17, 1, self.maxAlphaCo)
            self.table.setCellWidget(17, 0, maxAlphaCo_lbl)
			
			# maxDeltaT
            maxDeltaT_lbl = QLabel('maxDeltaT')
            self.maxDeltaT = QSpinBox()
            self.maxDeltaT.setRange(0, 10000)
            self.table.setCellWidget(18, 1, self.maxDeltaT)
            self.table.setCellWidget(18, 0, maxDeltaT_lbl)
			
            # вывод значений параметров
            if 'controlDict' in self.con.tables():						
                query = QtSql.QSqlQuery()
                query.exec("SELECT * FROM controlDict")
                if query.isActive():
                    query.first()
                    value_list = []
                    while query.isValid():
                        value_res = query.value('value')
                        value_list.append(value_res)
                        query.next()
					
                    # application
                    application_mas = self.application.count()   
                    for i in range(application_mas):
                        if self.application.itemText(i) == value_list[0]:
                            self.application.setCurrentIndex(i)
							
                    # startFrom
                    startFrom_mas = self.startFrom.count()   
                    for i in range(startFrom_mas):
                        if self.startFrom.itemText(i) == value_list[1]:
                            self.startFrom.setCurrentIndex(i)
							
                    # startTime
                    self.startTime.setValue(value_list[2])
					
                    # stopAt
                    stopAt_mas = self.stopAt.count()   
                    for i in range(stopAt_mas):
                        if self.stopAt.itemText(i) == value_list[3]:
                            self.stopAt.setCurrentIndex(i)
							
                    # endTime
                    self.endTime.setValue(value_list[4])
					
                    # deltaT
                    self.deltaT.setText(str(value_list[5]))
					
                    # writeControl
                    writeControl_mas = self.writeControl.count()   
                    for i in range(writeControl_mas):
                        if self.writeControl.itemText(i) == value_list[6]:
                            self.writeControl.setCurrentIndex(i)
							
                    # writeInterval
                    self.writeInterval.setValue(value_list[7])
					
                    # purgeWrite
                    self.purgeWrite.setValue(value_list[8])
					
                    # writeFormat
                    writeFormat_mas = self.writeFormat.count()   
                    for i in range(writeFormat_mas):
                        if self.writeFormat.itemText(i) == value_list[9]:
                            self.writeFormat.setCurrentIndex(i)
							
                    # writePrecision
                    self.writePrecision.setValue(value_list[10])
					
                    # writeCompression
                    writeCompression_mas = self.writeCompression.count()   
                    for i in range(writeCompression_mas):
                        if self.writeCompression.itemText(i) == value_list[11]:
                            self.writeCompression.setCurrentIndex(i)
							
                    # timeFormat
                    timeFormat_mas = self.timeFormat.count()   
                    for i in range(timeFormat_mas):
                        if self.timeFormat.itemText(i) == value_list[12]:
                            self.timeFormat.setCurrentIndex(i)
							
                    # timePrecision
                    self.timePrecision.setValue(value_list[13])
					
					# runTimeModifiable
                    runTimeModifiable_mas = self.runTimeModifiable.count()   
                    for i in range(runTimeModifiable_mas):
                        if self.runTimeModifiable.itemText(i) == value_list[14]:
                            self.runTimeModifiable.setCurrentIndex(i)

					# adjustTimeStep
                    adjustTimeStep_mas = self.adjustTimeStep.count()   
                    for i in range(adjustTimeStep_mas):
                        if self.adjustTimeStep.itemText(i) == value_list[15]:
                            self.adjustTimeStep.setCurrentIndex(i)

					# maxCo
                    self.maxCo.setValue(value_list[16])

					# maxAlphaCo
                    self.maxAlphaCo.setValue(value_list[17])

					# maxDeltaT
                    self.maxDeltaT.setValue(value_list[18])
				
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
        application_txt = self.application.currentText()
        startFrom_txt = self.startFrom.currentText()
        startTime_txt = self.startTime.value()
        stopAt_txt = self.stopAt.currentText()
        endTime_txt = self.endTime.value()
        deltaT_txt = self.deltaT.text()
        writeControl_txt = self.writeControl.currentText()
        writeInterval_txt = self.writeInterval.value()
        purgeWrite_txt = self.purgeWrite.value()
        writeFormat_txt = self.writeFormat.currentText()
        writePrecision_txt = self.writePrecision.value()
        writeCompression_txt = self.writeCompression.currentText()
        timeFormat_txt = self.timeFormat.currentText()
        timePrecision_txt = self.timePrecision.value()
        runTimeModifiable_txt = self.runTimeModifiable.currentText() 
        adjustTimeStep_txt = self.adjustTimeStep.currentText()
        maxCo_txt = self.maxCo.value()
        maxAlphaCo_txt = self.maxAlphaCo.value()
        maxDeltaT_txt = self.maxDeltaT.value()
		
        self.par.application = application_txt	
        
        if 'controlDict' not in self.con.tables():
            query = QtSql.QSqlQuery()
            query.exec("CREATE TABLE controlDict(param, value)")

            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('application', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('startFrom', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('startTime', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('stopAt', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('endTime', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('deltaT', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('writeControl', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('writeInterval', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('purgeWrite', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('writeFormat', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('writePrecision', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('writeCompression', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('timeFormat', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('timePrecision', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('runTimeModifiable', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('adjustTimeStep', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('maxCo', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('maxAlphaCo', ''))
            query.exec("INSERT INTO controlDict(param, value) VALUES ('%s','%s')" % ('maxDeltaT', ''))


        if 'controlDict' in self.con.tables():
            query = QtSql.QSqlQuery()

            query.prepare("UPDATE controlDict SET value=? WHERE param='application'")
            query.bindValue(0, application_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='startFrom'")
            query.bindValue(0, startFrom_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='startTime'")
            query.bindValue(0, startTime_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='stopAt'")
            query.bindValue(0, stopAt_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='endTime'")
            query.bindValue(0, endTime_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='deltaT'")
            query.bindValue(0, deltaT_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='writeControl'")
            query.bindValue(0, writeControl_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='writeInterval'")
            query.bindValue(0, writeInterval_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='purgeWrite'")
            query.bindValue(0, purgeWrite_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='purgeWrite'")
            query.bindValue(0, purgeWrite_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='writeFormat'")
            query.bindValue(0, writeFormat_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='writePrecision'")
            query.bindValue(0, writePrecision_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='writeCompression'")
            query.bindValue(0, writeCompression_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='timeFormat'")
            query.bindValue(0, timeFormat_txt)
            query.exec_()

            query.prepare("UPDATE controlDict SET value=? WHERE param='timePrecision'")
            query.bindValue(0, timePrecision_txt)
            query.exec_()
			
            query.prepare("UPDATE controlDict SET value=? WHERE param='runTimeModifiable'")
            query.bindValue(0, runTimeModifiable_txt)
            query.exec_()
			
            query.prepare("UPDATE controlDict SET value=? WHERE param='adjustTimeStep'")
            query.bindValue(0, adjustTimeStep_txt)
            query.exec_()
			
            query.prepare("UPDATE controlDict SET value=? WHERE param='maxCo'")
            query.bindValue(0, maxCo_txt)
            query.exec_()
			
            query.prepare("UPDATE controlDict SET value=? WHERE param='maxAlphaCo'")
            query.bindValue(0, maxAlphaCo_txt)
            query.exec_()
			
            query.prepare("UPDATE controlDict SET value=? WHERE param='maxDeltaT'")
            query.bindValue(0, maxDeltaT_txt)
            query.exec_()

        # записываем файл controlDict
        if os.path.exists(self.full_dir + '/system/controlDict'):
            os.remove(self.full_dir + '/system/controlDict')
		
        shutil.copyfile("./matches/Shablon/system/controlDict", self.full_dir + '/system/controlDict')
		
        cD = open(self.full_dir + '/system/controlDict', 'a')
        ###application###
        a_bl = '\n' + 'application     ' + application_txt + ';' + '\n\n'

        ###startFrom###
        sF_bl = 'startFrom       ' + startFrom_txt + ';' + '\n\n'

        ###startTime###
        sT_bl = 'startTime       ' + str(startTime_txt) + ';' + '\n\n'

        ###stopAt###
        sA_bl = 'stopAt          ' + stopAt_txt + ';' + '\n\n'

        ###endTime###
        sTi_bl = 'endTime         ' + str(endTime_txt) + ';' + '\n\n'

        ###deltaT###
        dT_bl = 'deltaT          ' + str(deltaT_txt) + ';' + '\n\n'

        ###writeControl###
        wC_bl = 'writeControl    ' + writeControl_txt + ';' + '\n\n'

        ###writeInterval###
        wI_bl = 'writeInterval   ' + str(writeInterval_txt) + ';' + '\n\n'

        ###purgeWrite###
        pW_bl = 'purgeWrite      ' + str(purgeWrite_txt) + ';' + '\n\n'

        ###writeFormat###
        wF_bl = 'writeFormat     ' + writeFormat_txt + ';' + '\n\n'

        ###writePrecision###
        wP_bl = 'writePrecision  ' + str(writePrecision_txt) + ';' + '\n\n'

        ###writeCompression###
        wCo_bl = 'writeCompression ' + writeCompression_txt + ';' + '\n\n'

        ###timeFormat###
        tF_bl = 'timeFormat      ' + timeFormat_txt + ';' + '\n\n'

        ###timePrecision###
        tP_bl = 'timePrecision   ' + str(timePrecision_txt) + ';' + '\n\n'
		
		###runTimeModifiable###
        rTM_bl = 'runTimeModifiable ' + runTimeModifiable_txt + ';' + '\n\n'
		
		###adjustTimeStep###
        aTS_bl = 'adjustTimeStep  ' + adjustTimeStep_txt + ';' + '\n\n'
		
		###maxCo###
        mC_bl = 'maxCo           ' + str(maxCo_txt) + ';' + '\n\n'
		
		###maxAlphaCo###
        mAC_bl = 'maxAlphaCo      ' + str(maxAlphaCo_txt) + ';' + '\n\n'
		
		###maxDeltaT###
        mDT_bl = 'maxDeltaT       ' + str(maxDeltaT_txt) + ';' + '\n\n'
		
        if deltaT_txt != '':

            cD.write(a_bl + sF_bl + sT_bl + sA_bl + sTi_bl + dT_bl + wC_bl + wI_bl + pW_bl + wF_bl + wP_bl + wCo_bl + tF_bl + tP_bl + rTM_bl + aTS_bl + mC_bl + mAC_bl + mDT_bl)
            close_str = '// ************************************************************************* //'
            cD.write(close_str)

            cD.close()

            self.par.cdw.setWidget(self.par.outf_scroll)
            outf = open(self.full_dir + '/system/controlDict')

            if self.interface_lng_val == 'Russian':
                msg_lbl = QLabel(
                    '<span style="color:green">Файл controlDict сохранен</span>')
            elif self.interface_lng_val == 'English':
                msg_lbl = QLabel(
                    '<span style="color:green">The controlDict file saved</span>')

            data = outf.read()

            if self.interface_lng_val == 'Russian':
                self.par.outf_lbl.setText("Файл " + "<font color='peru'>" + 'controlDict' + "</font>")
            elif self.interface_lng_val == 'English':
                self.par.outf_lbl.setText("<font color='peru'>" + 'controlDict' + "</font>" + " file")
            self.par.outf_edit.setText(data)

            self.par.cdw.setTitleBarWidget(self.par.cdw_frame)
            outf.close()
        else:
            if self.interface_lng_val == 'Russian':
                msg_lbl = QLabel(
                    '<span style="color:green">Укажите значение параметра deltaT</span>')
            elif self.interface_lng_val == 'English':
                msg_lbl = QLabel(
                    '<span style="color:green">Specify deltaT value</span>')
            
        self.par.listWidget.clear()
        self.par.item = QListWidgetItem()
        self.par.listWidget.addItem(self.par.item)
        self.par.listWidget.setItemWidget(self.par.item, msg_lbl)
'''