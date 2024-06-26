# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasarim.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import easygui
import ai
import json

# kutuphaneler dahil edildi.
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        #pencere ayarları
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget") 
        #dosya sec butonu
        self.dosyasec_but = QtWidgets.QPushButton(self.centralwidget)
        self.dosyasec_but.setGeometry(QtCore.QRect(430, 10, 221, 41))
        self.dosyasec_but.setObjectName("dosyasec_but")
        self.dosyasec_but.clicked.connect(self.select) 
        # tespit butonu
        self.tespitet_but = QtWidgets.QPushButton(self.centralwidget)
        self.tespitet_but.setGeometry(QtCore.QRect(430, 60, 221, 41))
        self.tespitet_but.setObjectName("tespitet_but")
        self.tespitet_but.clicked.connect(self.tespitet)
        #sifirla butonu
        self.tespit_name = QtWidgets.QLabel(self.centralwidget)
        self.tespit_name.setGeometry(QtCore.QRect(440, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        # tespit edilen metni kodları
        self.tespit_name.setFont(font)
        self.tespit_name.setObjectName("tespit_name")
        # sifirla butonu 
        self.sifirla_but = QtWidgets.QPushButton(self.centralwidget)
        self.sifirla_but.setGeometry(QtCore.QRect(430, 110, 221, 41))
        self.sifirla_but.setObjectName("sifirla_but")
        self.sifirla_but.clicked.connect(self.sifirla)
        # dogruluk oranı metni kodları
        self.dogruluk_name = QtWidgets.QLabel(self.centralwidget)
        self.dogruluk_name.setGeometry(QtCore.QRect(440, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dogruluk_name.setFont(font)
        self.dogruluk_name.setObjectName("dogruluk_name")
        # tespit degeri metni kodları
        self.tespit_value = QtWidgets.QLabel(self.centralwidget)
        self.tespit_value.setGeometry(QtCore.QRect(450, 200, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tespit_value.setFont(font)
        self.tespit_value.setObjectName("tespit_value")
        # dogruluk degeri metni kodları
        self.dogruluk_value = QtWidgets.QLabel(self.centralwidget)
        self.dogruluk_value.setGeometry(QtCore.QRect(450, 270, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dogruluk_value.setFont(font)
        self.dogruluk_value.setObjectName("dogruluk_value")
        # resim kodlari
        self.resim = QtWidgets.QLabel(self.centralwidget)
        self.resim.setGeometry(QtCore.QRect(0, 10, 421, 291))
        self.resim.setText("")
        self.resim.setPixmap(QtGui.QPixmap(""))
        self.resim.setObjectName("resim")
        self.resim.setScaledContents(True)
        # tasarimin bulundugu pencere ile ilgili bir takim kodlar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # tasarimda yer alan itemlere text degeri atiyoruz.
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dosyasec_but.setText(_translate("MainWindow", "Dosya Seç"))
        self.tespitet_but.setText(_translate("MainWindow", "Tespit Et"))
        self.tespit_name.setText(_translate("MainWindow", "Tespit ="))
        self.sifirla_but.setText(_translate("MainWindow", "Sıfırla"))
        self.dogruluk_name.setText(_translate("MainWindow", "Doğruluk ="))
        self.tespit_value.setText(_translate("MainWindow", "Tespit Edilmedi"))
        self.dogruluk_value.setText(_translate("MainWindow", "Tespit Edilmedi"))

    def select(self): # select fonk. tasarımda dosya secme tusuna basınca yapılacaklar 
        #select tusuna tiklaninca --
        path = easygui.fileopenbox() # dosya secme sekmesini ac
        print(path) # secilen dosyanin uzantisini yazdır 
        self.resim.setPixmap(QtGui.QPixmap(path)) #tasarimda yer alan resime dosya yolunu gir
        f=open("dir.db","w") # dosya yolunu kaydedebilmek icin veritabanina (metin dosyasi) eris
        f.write(json.dumps(path)) # dosya yolunu tespit sirasinda tekrar kullanabilmek için kaydet
        f.flush() # dosyayi yenile
        f.close() # dosyayi kapat

    def tespitet(self): # tespit et fonk. tasarimda tespit et tusuna basinca yapılacaklar
        _translate = QtCore.QCoreApplication.translate 
        f = open("dir.db","r") # dosya secilirken tespit edilen dizinin yer aldıgı dosyayı ac
        data = f.read() # dosya secilirken tespit edilen dizini oku
        data = json.loads(data) # dosya dizini üzerinde bir takim islemler
        data = data.replace("\\","/") #yapay zekanin kullanabilecegi formata getir c:\asd\vcd yerine c:/asd/vcd
        print(data) # dosya uzantisini yazdir
        tespit,skor = ai.imagine(data) # ai kutuphanesi icindeki imagine fonksiyonunu data uzantisi ile calistir gelen veriyi tespit ve skor olarak geri cek.
        self.tespit_value.setText(_translate("MainWindow", str(tespit))) # uygulamada tespiti yazdır
        self.dogruluk_value.setText(_translate("MainWindow", str(skor))) # uygulamada skoru yazdir.

    def sifirla(self): # sifirla fonk. tasarimda sifirla tusuna basinca yapilacaklar
        _translate = QtCore.QCoreApplication.translate
        self.resim.setPixmap(QtGui.QPixmap("")) # resmi sil 
        self.tespit_value.setText(_translate("MainWindow", "Tespit Edilmedi")) # tespiti kaldir
        self.dogruluk_value.setText(_translate("MainWindow", "Tespit Edilmedi")) # dogrulugu kaldir