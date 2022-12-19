import sys,subprocess,random,requests,re,cv2,numpy
import os
os.system('pyuic5 Main_Gui.ui -o Main_Gui.py')
from PyQt5 import QtCore,QtWidgets,QtGui,QtTest
from PyQt5.QtWidgets import QApplication,QMainWindow
from Main_Gui import Ui_Creat_By_RubyIV

from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *

from unidecode import unidecode

Folder = ["Image"]
for i in Folder:
    try: os.mkdir(i)
    except: ()

class MainWindow:
    def __init__(self):
        global DinneGui,DinneLdPlayer,DinneInfo
        self.main_win = QMainWindow()
        self.uic = DinneGui = Ui_Creat_By_RubyIV()
        self.LdPlayer = DinneLdPlayer =  LdPlayer("D:\LDPlayer\LDPlayer9")
        self.Info = DinneInfo = Info_Account()
        self.uic.setupUi(self.main_win)
        
        self.main_win.setWindowTitle("D_InstaSoft - Version: 2.4.8 - Tele: @ImDinne")
        try: self.main_win.setWindowIcon(QtGui.QIcon(':/newPrefix/zyro-image.png'))
        except: ()


        self.uic.MenuButton.clicked.connect(self.slide_LeftMenu)
        self.uic.pushButton_1.clicked.connect(self.Screen1)# Move Tab
        self.uic.pushButton_2.clicked.connect(self.Screen2)# Move Tab

        #Load Devices
        self.uic.pushButton.clicked.connect(self.LoadDevices)
        # Total Devices
        self.uic.spinBox_3.setValue(self.LdPlayer.TotalTabLdPlayer())
        # Button
        self.uic.pushButton_7.clicked.connect(self.Start_RegIg)



    def Start_RegIg(self):
        self.REGACCOUNT = {}
        DinneInfo.Show_Info_Account()
        self.Total_ThreadReg = DinneGui.spinBox.value()


        for i in range(self.Total_ThreadReg):
            DinneLdPlayer.OpenLDTab(index = i)
            DinneLdPlayer.ResizeLdPlayer(index = i,height=600,width=350,dpi=160)
        
        List_Devices = DinneLdPlayer.GetDevices()

        print(self.Total_ThreadReg)
        for i in range(self.Total_ThreadReg):
            print(f"===========>>>{i}")
            emulator = List_Devices[i]
            self.REGACCOUNT[emulator] = RegInstagram(emulator)
            self.REGACCOUNT[emulator].start()

        
        
    def LoadDevices(self):
        self.uic.AllDevices_QTextBrower.clear()
        allDevices = list(self.LdPlayer.GetDevices())
        sttDevices = 0
        for Device in allDevices:
            self.uic.AllDevices_QTextBrower.append(f'[{sttDevices}] - {Device}')
            sttDevices += 1  
        return sttDevices


   
    def Start(self):
        self.ExecuteLD(f"launch --{self.param} {self.NameOrId}")


    def show(self):
        self.main_win.show()
    def Screen1(self):
        self.uic.Page_Menu.setCurrentWidget(self.uic.Page1)
    def Screen2(self):
        self.uic.Page_Menu.setCurrentWidget(self.uic.Page2)

    def slide_LeftMenu(self):
        width=self.uic.Left_Menu.width()
        print(f'Widget-Size:{width}')
        if width == 50:
            newWidth = 150
        else:
            newWidth = 0

        self.animation = QPropertyAnimation(self.uic.Left_Menu,b"minimumWidth")
        self.animation.setDuration(1000)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        # self.uic.Table_Tab.setRowCount(30) 
        # self.uic.Table_Tab.setColumnCount(2)  

class Info_Account():
    def __init__(self) -> None:
        pass
    def no_accent_vietnamese(self,s):
        s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
        s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
        s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
        s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
        s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
        s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
        s = re.sub('[íìỉĩị]', 'i', s)
        s = re.sub('[ÍÌỈĨỊ]', 'I', s)
        s = re.sub('[úùủũụưứừửữự]', 'u', s)
        s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
        s = re.sub('[ýỳỷỹỵ]', 'y', s)
        s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
        s = re.sub('đ', 'd', s)
        s = re.sub('Đ', 'D', s)
        return s

    def __CreatePassword(self):
        self.pwd = unidecode(self.firstname.lower()).replace(" ", "").capitalize()+random.choice("!,@,#,$,%,&,~".split(","))+str(random.randint(10000, 99999))
    def __GetListLastNameVN(self):
        self.lastname = random.choice(["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý"])
        return self.lastname
    def __GetListFirstNameVN(self):
        self.firstname = random.choice(["Ái Hồng", "Ái Khanh", "Ái Linh", "Ái Nhân", "Ái Nhi", "Ái Thi", "Ái Thy", "Ái Vân", "An Bình", "An Di", "An Hạ", "An Hằng", "An Nhàn", "An Nhiên", "Anh Chi", "Ánh Dương", "Ánh Hoa", "Ánh Hồng", "Anh Hương", "Ánh Lệ", "Ánh Linh", "Anh Mai", "Ánh Mai", "Ánh Ngọc", "Ánh Nguyệt", "Anh Phương", "Anh Thảo", "Anh Thi", "Anh Thơ", "Ánh Thơ", "Anh Thư", "Anh Thy", "Ánh Trang", "Ánh Tuyết", "Ánh Xuân", "Bạch Cúc", "Bạch Hoa", "Bạch Kim", "Bạch Liên", "Bạch Loan", "Bạch Mai", "Bạch Quỳnh", "Bạch Trà", "Bạch Tuyết", "Bạch Vân", "Bạch Yến", "Ban Mai", "Băng Băng", "Băng Tâm", "Bảo Anh", "Bảo Bình", "Bảo Châu", "Bảo Hà", "Bảo Hân", "Bảo Huệ", "Bảo Lan", "Bảo Lễ", "Bảo Ngọc", "Bảo Phương", "Bảo Quyên", "Bảo Quỳnh", "Bảo Thoa", "Bảo Thúy", "Bảo Tiên", "Bảo Trâm", "Bảo Trân", "Bảo Trúc", "Bảo Uyên", "Bảo Vân", "Bảo Vy", "Bích Châu", "Bích Chiêu", "Bích Dào", "Bích Duyên", "Bích Hà", "Bích Hải", "Bích Hằng", "Bích Hạnh", "Bích Hảo", "Bích Hậu", "Bích Hiền", "Bích Hồng", "Bích Hợp", "Bích Huệ", "Bích Lam", "Bích Liên", "Bích Loan", "Bích Nga", "Bích Ngà", "Bích Ngân", "Bích Ngọc", "Bích Như", "Bích Phượng", "Bích Quân", "Bích Quyên", "Bích San", "Bích Thảo", "Bích Thoa", "Bích Thu", "Bích Thủy", "Bích Ty", "Bích Vân", "Bội Linh", "Cẩm Hạnh", "Cẩm Hiền", "Cẩm Hường", "Cẩm Liên", "Cẩm Linh", "Cẩm Ly", "Cẩm Nhi", "Cẩm Nhung", "Cam Thảo", "Cẩm Thúy", "Cẩm Tú", "Cẩm Vân", "Cẩm Yến", "Cát Cát", "Cát Linh", "Cát Ly", "Cát Tiên", "Chi Lan", "Chi Mai", "Dã Lan", "Dạ Lan", "Dạ Nguyệt", "Dã Thảo", "Dạ Thảo", "Dạ Thi", "Dạ Yến", "Di Nhiên", "Diễm Châu", "Diễm Chi", "Diễm Hằng", "Diễm Hạnh", "Diễm Hương", "Diễm Khuê", "Diễm Kiều", "Diễm Liên", "Diễm Lộc", "Diễm My", "Diễm Phúc", "Diễm Phước", "Diễm Phương", "Diễm Phượng", "Diễm Quyên", "Diễm Quỳnh", "Diễm Thảo", "Diễm Thư", "Diễm Thúy", "Diễm Trang", "Diễm Trinh", "Diễm Uyên", "Diên Vỹ", "Diệp Anh", "Diệp Vy", "Diệu Ái", "Diệu Anh", "Diệu Hằng", "Diệu Hạnh", "Diệu Hiền", "Diệu Hoa", "Diệu Hồng", "Diệu Hương", "Diệu Huyền", "Diệu Lan", "Diệu Linh", "Diệu Loan", "Diệu Nga", "Diệu Ngà", "Diệu Ngọc", "Diệu Nương", "Diệu Thiện", "Diệu Thúy", "Diệu Vân", "Duy Hạnh", "Duy Mỹ", "Duy Uyên", "Duyên Hồng", "Duyên My", "Duyên Mỹ", "Duyên Nương", "Dinh Hương", "Doan Thanh", "Doan Trang", "Dông Nghi", "Dông Nhi", "Dông Trà", "Dông Tuyền", "Dông Vy", "Gia Hân", "Gia Khanh", "Gia Linh", "Gia Nhi", "Gia Quỳnh", "Giáng Ngọc", "Giang Thanh", "Giáng Tiên", "Giáng Uyên", "Giao Kiều", "Giao Linh", "Hà Giang", "Hà Liên", "Hà Mi", "Hà My", "Hà Nhi", "Hà Phương", "Hạ Phương", "Hà Thanh", "Hà Tiên", "Hạ Tiên", "Hạ Uyên", "Hạ Vy", "Hạc Cúc", "Hải Ân", "Hải Anh", "Hải Châu", "Hải Dường", "Hải Duyên", "Hải Miên", "Hải My", "Hải Mỹ", "Hải Ngân", "Hải Nhi", "Hải Phương", "Hải Phượng", "Hải San", "Hải Sinh", "Hải Thanh", "Hải Thảo", "Hải Uyên", "Hải Vân", "Hải Vy", "Hải Yến", "Hàm Duyên", "Hàm Nghi", "Hàm Thơ", "Hằng Anh", "Hạnh Chi", "Hạnh Dung", "Hạnh Linh", "Hạnh My", "Hạnh Nga", "Hạnh Phương", "Hạnh San", "Hạnh Thảo", "Hạnh Trang", "Hạnh Vi", "Hảo Nhi", "Hiền Chung", "Hiền Hòa", "Hiền Mai", "Hiền Nhi", "Hiền Nương", "Hiền Thục", "Hiếu Giang", "Hiếu Hạnh", "Hiếu Khanh", "Hiếu Minh", "Hiểu Vân", "Hồ Diệp", "Hoa Liên", "Hoa Lý", "Họa Mi", "Hoa Thiên", "Hoa Tiên", "Hoài An", "Hoài Giang", "Hoài Hương", "Hoài Phương", "Hoài Thương", "Hoài Trang", "Hoàn Châu", "Hoàn Vi", "Hoàng Cúc", "Hoàng Hà", "Hoàng Kim", "Hoàng Lan", "Hoàng Mai", "Hoàng Miên", "Hoàng Oanh", "Hoàng Sa", "Hoàng Thư", "Hoàng Yến", "Hồng Anh", "Hồng Bạch Thảo", "Hồng Châu", "Hồng Dào", "Hồng Diễm", "Hồng Diệp", "Hồng Hà", "Hồng Hạnh", "Hồng Hoa", "Hồng Khanh", "Hồng Khôi", "Hồng Khuê", "Hồng Lâm", "Hồng Liên", "Hồng Linh", "Hồng Mai", "Hồng Nga", "Hồng Ngân", "Hồng Ngọc", "Hồng Như", "Hồng Nhung", "Hồng Oanh", "Hồng Phúc", "Hồng Phương", "Hồng Quế", "Hồng Tâm", "Hồng Thắm", "Hồng Thảo", "Hồng Thu", "Hồng Thư", "Hồng Thúy", "Hồng Thủy", "Hồng Vân", "Hồng Xuân", "Huệ An", "Huệ Hồng", "Huệ Hương", "Huệ Lâm", "Huệ Lan", "Huệ Linh", "Huệ My", "Huệ Phương", "Huệ Thương", "Hương Chi", "Hương Giang", "Hương Lâm", "Hương Lan", "Hương Liên", "Hương Ly", "Hương Mai", "Hương Nhi", "Hương Thảo", "Hương Thu", "Hương Thủy", "Hương Tiên", "Hương Trà", "Hương Trang", "Hương Xuân", "Huyền Anh", "Huyền Diệu", "Huyền Linh", "Huyền Ngọc", "Huyền Nhi", "Huyền Thoại", "Huyền Thư", "Huyền Trâm", "Huyền Trân", "Huyền Trang", "Huỳnh Anh", "Khả Ái", "Khả Khanh", "Khả Tú", "Khải Hà", "Khánh Chi", "Khánh Giao", "Khánh Hà", "Khánh Hằng", "Khánh Huyền", "Khánh Linh", "Khánh Ly", "Khánh Mai", "Khánh My", "Khánh Ngân", "Khánh Quyên", "Khánh Quỳnh", "Khánh Thủy", "Khánh Trang", "Khánh Vân", "Khánh Vi", "Khuê Trung", "Kiết Hồng", "Kiết Trinh", "Kiều Anh", "Kiều Diễm", "Kiều Dung", "Kiều Giang", "Kiều Hạnh", "Kiều Hoa", "Kiều Khanh", "Kiều Loan", "Kiều Mai", "Kiều Minh", "Kiều Mỹ", "Kiều Nga", "Kiều Nguyệt", "Kiều Nương", "Kiều Thu", "Kiều Trang", "Kiều Trinh", "Kim Anh", "Kim Ánh", "Kim Chi", "Kim Cương", "Kim Dung", "Kim Duyên", "Kim Hoa", "Kim Hương", "Kim Khanh", "Kim Lan", "Kim Liên", "Kim Loan", "Kim Ly", "Kim Mai", "Kim Ngân", "Kim Ngọc", "Kim Oanh", "Kim Phượng", "Kim Quyên", "Kim Sa", "Kim Thanh", "Kim Thảo", "Kim Thoa", "Kim Thu", "Kim Thư", "Kim Thủy", "Kim Thy", "Kim Trang", "Kim Tuyến", "Kim Tuyền", "Kim Tuyết", "Kim Xuân", "Kim Xuyến", "Kim Yến", "Kỳ Anh", "Kỳ Duyên", "Lam Hà", "Lam Khê", "Lam Ngọc", "Lâm Nhi", "Lâm Oanh", "Lam Tuyền", "Lâm Tuyền", "Lâm Uyên", "Lan Anh", "Lan Chi", "Lan Hương", "Lan Khuê", "Lan Ngọc", "Lan Nhi", "Lan Phương", "Lan Thương", "Lan Trúc", "Lan Vy", "Lệ Băng", "Lệ Chi", "Lệ Hoa", "Lệ Huyền", "Lệ Khanh", "Lệ Nga", "Lệ Nhi", "Lệ Quân", "Lệ Quyên", "Lê Quỳnh", "Lệ Thanh", "Lệ Thu", "Lệ Thủy", "Liên Chi", "Liên Hoa", "Liên Hương", "Liên Như", "Liên Phương", "Liên Trân", "Liễu Oanh", "Linh Châu", "Linh Chi", "Linh Dan", "Linh Duyên", "Linh Giang", "Linh Hà", "Linh Lan", "Linh Nhi", "Linh Phương", "Linh Phượng", "Linh San", "Linh Trang", "Loan Châu", "Lộc Uyên", "Lục Bình", "Lưu Ly", "Ly Châu", "Mai Anh", "Mai Châu", "Mai Chi", "Mai Hà", "Mai Hạ", "Mai Hiền", "Mai Hương", "Mai Khanh", "Mai Khôi", "Mai Lan", "Mai Liên", "Mai Linh", "Mai Loan", "Mai Ly", "Mai Nhi", "Mai Phương", "Mai Quyên", "Mai Tâm", "Mai Thanh", "Mai Thảo", "Mai Thu", "Mai Thy", "Mai Trinh", "Mai Vy", "Mậu Xuân", "Minh An", "Minh Châu", "Minh Duyên", "Minh Hà", "Minh Hằng", "Minh Hạnh", "Minh Hiền", "Minh Hồng", "Minh Huệ", "Minh Hương", "Minh Huyền", "Minh Khai", "Minh Khuê", "Minh Loan", "Minh Minh", "Minh Ngọc", "Minh Nguyệt", "Minh Nhi", "Minh Như", "Minh Phương", "Minh Phượng", "Minh Tâm", "Minh Thảo", "Minh Thu", "Minh Thư", "Minh Thương", "Minh Thúy", "Minh Thủy", "Minh Trang", "Minh Tuệ", "Minh Tuyết", "Minh Uyên", "Minh Vy", "Minh Xuân", "Minh Yến", "Mộc Miên", "Mộng Diệp", "Mộng Hằng", "Mộng Hoa", "Mộng Hương", "Mộng Lan", "Mộng Liễu", "Mộng Nguyệt", "Mộng Nhi", "Mộng Quỳnh", "Mộng Thi", "Mộng Thu", "Mộng Tuyền", "Mộng Vân", "Mộng Vi", "Mộng Vy", "Mỹ Anh", "Mỹ Diễm", "Mỹ Dung", "Mỹ Duyên", "Mỹ Hạnh", "Mỹ Hiệp", "Mỹ Hoàn", "Mỹ Huệ", "Mỹ Hường", "Mỹ Huyền", "Mỹ Khuyên", "Mỹ Kiều", "Mỹ Lan", "Mỹ Lệ", "Mỹ Loan", "Mỹ Lợi", "Mỹ Nga", "Mỹ Ngọc", "Mỹ Nhi", "Mỹ Nương", "Mỹ Phụng", "Mỹ Phương", "Mỹ Phượng", "Mỹ Tâm", "Mỹ Thuần", "Mỹ Thuận", "Mỹ Trâm", "Mỹ Trang", "Mỹ Uyên", "Mỹ Vân", "Mỹ Xuân", "Mỹ Yến", "Ngân Anh", "Ngân Hà", "Ngân Thanh", "Ngân Trúc", "Nghi Dung", "Nghi Minh", "Nghi Xuân", "Ngọc Ái", "Ngọc Anh", "Ngọc Ánh", "Ngọc Bích", "Ngọc Cầm", "Ngọc Dàn", "Ngọc Dào", "Ngọc Diệp", "Ngọc Diệp", "Ngọc Dung", "Ngọc Hà", "Ngọc Hạ", "Ngọc Hân", "Ngọc Hằng", "Ngọc Hạnh", "Ngọc Hiền", "Ngọc Hoa", "Ngọc Hoan", "Ngọc Hoàn", "Ngọc Huệ", "Ngọc Huyền", "Ngọc Khanh", "Ngọc Khánh", "Ngọc Khuê", "Ngọc Lam", "Ngọc Lâm", "Ngọc Lan", "Ngọc Lệ", "Ngọc Liên", "Ngọc Linh", "Ngọc Loan", "Ngọc Mai", "Ngọc Nhi", "Ngọc Nữ", "Ngọc Oanh", "Ngọc Phụng", "Ngọc Quế", "Ngọc Quyên", "Ngọc Quỳnh", "Ngọc San", "Ngọc Sương", "Ngọc Tâm", "Ngọc Thi", "Ngọc Thơ", "Ngọc Thy", "Ngọc Trâm", "Ngọc Trinh", "Ngọc Tú", "Ngọc Tuyết", "Ngọc Uyên", "Ngọc Uyển", "Ngọc Vân", "Ngọc Vy", "Ngọc Yến", "Nguyên Hồng", "Nguyên Thảo", "Nguyết Ánh", "Nguyệt Anh", "Nguyệt Ánh", "Nguyệt Cầm", "Nguyệt Cát", "Nguyệt Hà", "Nguyệt Hồng", "Nguyệt Lan", "Nguyệt Minh", "Nguyệt Nga", "Nguyệt Quế", "Nguyệt Uyển", "Nhã Hồng", "Nhã Hương", "Nhã Khanh", "Nhã Lý", "Nhã Mai", "Nhã Sương", "Nhã Thanh", "Nhã Trang", "Nhã Trúc", "Nhã Uyên", "Nhã Ý", "Nhã Yến", "Nhan Hồng", "Nhật Ánh", "Nhật Hà", "Nhật Hạ", "Nhật Lan", "Nhật Linh", "Nhật Mai", "Nhật Phương", "Nhất Thương", "Như Anh", "Như Bảo", "Như Hoa", "Như Hồng", "Như Loan", "Như Mai", "Như Ngà", "Như Ngọc", "Như Phương", "Như Quân", "Như Quỳnh", "Như Tâm", "Như Thảo", "Oanh Thơ", "Oanh Vũ", "Phi Nhung", "Phi Yến", "Phụng Yến", "Phước Bình", "Phước Huệ", "Phương An", "Phương Anh", "Phượng Bích", "Phương Châu", "Phương Chi", "Phương Diễm", "Phương Dung", "Phương Giang", "Phương Hạnh", "Phương Hiền", "Phương Hoa", "Phương Lan", "Phượng Lệ", "Phương Liên", "Phượng Liên", "Phương Linh", "Phương Loan", "Phượng Loan", "Phương Mai", "Phượng Nga", "Phương Nghi", "Phương Ngọc", "Phương Nhi", "Phương Nhung", "Phương Quân", "Phương Quế", "Phương Quyên", "Phương Quỳnh", "Phương Tâm", "Phương Thanh", "Phương Thảo", "Phương Thi", "Phương Thùy", "Phương Thủy", "Phượng Tiên", "Phương Trà", "Phương Trâm", "Phương Trang", "Phương Trinh", "Phương Uyên", "Phượng Uyên", "Phượng Vũ", "Phượng Vy", "Phương Yến", "Quế Anh", "Quế Chi", "Quế Lâm", "Quế Linh", "Quế Phương", "Quế Thu", "Quỳnh Anh", "Quỳnh Chi", "Quỳnh Dung", "Quỳnh Giang", "Quỳnh Giao", "Quỳnh Hà", "Quỳnh Hoa", "Quỳnh Hương", "Quỳnh Lam", "Quỳnh Lâm", "Quỳnh Liên", "Quỳnh Nga", "Quỳnh Ngân", "Quỳnh Nhi", "Quỳnh Như", "Quỳnh Nhung", "Quỳnh Phương", "Quỳnh Sa", "Quỳnh Thanh", "Quỳnh Thơ", "Quỳnh Tiên", "Quỳnh Trâm", "Quỳnh Trang", "Quỳnh Vân", "Sao Băng", "Sao Mai", "Sơn Ca", "Sơn Tuyền", "Sông Hà", "Sông Hương", "Song Oanh", "Song Thư", "Sương Sương", "Tâm Hằng", "Tâm Hạnh", "Tâm Hiền", "Tâm Khanh", "Tâm Linh", "Tâm Nguyên", "Tâm Nguyệt", "Tâm Nhi", "Tâm Như", "Tâm Thanh", "Tâm Trang", "Thạch Thảo", "Thái Chi", "Thái Hà", "Thái Hồng", "Thái Lâm", "Thái Lan", "Thái Tâm", "Thái Thanh", "Thái Thảo", "Thái Vân", "Thanh Bình", "Thanh Dân", "Thanh Giang", "Thanh Hà", "Thanh Hằng", "Thanh Hạnh", "Thanh Hảo", "Thanh Hiền", "Thanh Hiếu", "Thanh Hoa", "Thanh Hồng", "Thanh Hương", "Thanh Hường", "Thanh Huyền", "Thanh Kiều", "Thanh Lam", "Thanh Lâm", "Thanh Lan", "Thanh Loan", "Thanh Mai", "Thanh Mẫn", "Thanh Nga", "Thanh Ngân", "Thanh Ngọc", "Thanh Nguyên", "Thanh Nhã", "Thanh Nhàn", "Thanh Nhung", "Thanh Phương", "Thanh Tâm", "Thanh Thanh", "Thanh Thảo", "Thanh Thu", "Thanh Thư", "Thanh Thúy", "Thanh Thủy", "Thanh Trang", "Thanh Trúc", "Thanh Tuyền", "Thanh Tuyết", "Thanh Uyên", "Thanh Vân", "Thanh Vy", "Thanh Xuân", "Thanh Yến", "Thảo Hồng", "Thảo Hương", "Thảo Linh", "Thảo Ly", "Thảo Mai", "Thảo My", "Thảo Nghi", "Thảo Nguyên", "Thảo Nhi", "Thảo Quyên", "Thảo Trang", "Thảo Uyên", "Thảo Vân", "Thảo Vy", "Thi Cầm", "Thi Ngôn", "Thi Thi", "Thi Xuân", "Thi Yến", "Thiên Di", "Thiên Duyên", "Thiên Giang", "Thiên Hà", "Thiên Hương", "Thiên Khánh", "Thiên Kim", "Thiên Lam", "Thiên Lan", "Thiên Mai", "Thiên Mỹ", "Thiện Mỹ", "Thiên Nga", "Thiên Nương", "Thiên Phương", "Thiên Thanh", "Thiên Thảo", "Thiên Thêu", "Thiên Thư", "Thiện Tiên", "Thiên Trang", "Thiên Tuyền", "Thiều Ly", "Thiếu Mai", "Thơ Thơ", "Thu Duyên", "Thu Giang", "Thu Hà", "Thu Hằng", "Thu Hậu", "Thu Hiền", "Thu Hoài", "Thu Hồng", "Thu Huệ", "Thu Huyền", "Thư Lâm", "Thu Liên", "Thu Linh", "Thu Loan", "Thu Mai", "Thu Minh", "Thu Nga", "Thu Ngà", "Thu Ngân", "Thu Ngọc", "Thu Nguyệt", "Thu Nhiên", "Thu Oanh", "Thu Phong", "Thu Phương", "Thu Phượng", "Thu Sương", "Thư Sương", "Thu Thảo", "Thu Thuận", "Thu Thủy", "Thu Trang", "Thu Vân", "Thu Việt", "Thu Vọng", "Thu Yến", "Thuần Hậu", "Thục Anh", "Thục Dào", "Thục Dình", "Thục Doan", "Thục Khuê", "Thục Nhi", "Thục Oanh", "Thục Quyên", "Thục Tâm", "Thục Trang", "Thục Trinh", "Thục Uyên", "Thục Vân", "Thương Huyền", "Thương Nga", "Thương Thương", "Thúy Anh", "Thùy Anh", "Thụy Dào", "Thúy Diễm", "Thùy Dung", "Thùy Dương", "Thùy Giang", "Thúy Hà", "Thúy Hằng", "Thủy Hằng", "Thúy Hạnh", "Thúy Hiền", "Thủy Hồng", "Thúy Hương", "Thúy Hường", "Thúy Huyền", "Thụy Khanh", "Thúy Kiều", "Thụy Lâm", "Thúy Liên", "Thúy Liễu", "Thùy Linh", "Thủy Linh", "Thụy Linh", "Thúy Loan", "Thúy Mai", "Thùy Mi", "Thúy Minh", "Thủy Minh", "Thúy My", "Thùy My", "Thúy Nga", "Thúy Ngà", "Thúy Ngân", "Thúy Ngọc", "Thủy Nguyệt", "Thùy Nhi", "Thùy Như", "Thụy Nương", "Thùy Oanh", "Thúy Phượng", "Thúy Quỳnh", "Thủy Quỳnh", "Thủy Tâm", "Thủy Tiên", "Thụy Trâm", "Thủy Trang", "Thụy Trinh", "Thùy Uyên", "Thụy Uyên", "Thúy Vân", "Thùy Vân", "Thụy Vân", "Thúy Vi", "Thúy Vy", "Thy Khanh", "Thy Oanh", "Thy Trúc", "Thy Vân", "Tiên Phương", "Tiểu Quỳnh", "Tịnh Lâm", "Tịnh Nhi", "Tịnh Như", "Tịnh Tâm", "Tịnh Yên", "Tố Loan", "Tố Nga", "Tố Nhi", "Tố Quyên", "Tố Tâm", "Tố Uyên", "Trà Giang", "Trà My", "Trâm Anh", "Trầm Hương", "Trâm Oanh", "Trang Anh", "Trang Dài", "Trang Linh", "Trang Nhã", "Trang Tâm", "Triệu Mẫn", "Triều Nguyệt", "Triều Thanh", "Trúc Chi", "Trúc Dào", "Trúc Lam", "Trúc Lâm", "Trúc Lan", "Trúc Liên", "Trúc Linh", "Trúc Loan", "Trúc Ly", "Trúc Mai", "Trúc Phương", "Trúc Quỳnh", "Trúc Vân", "Trúc Vy", "Từ Ân", "Tú Anh", "Tú Ly", "Tú Nguyệt", "Tú Quyên", "Tú Quỳnh", "Tú Sương", "Tú Tâm", "Tú Trinh", "Tú Uyên", "Tuệ Lâm", "Tuệ Mẫn", "Tuệ Nhi", "Tường Vi", "Tường Vy", "Tùy Anh", "Tùy Linh", "Túy Loan", "Tuyết Anh", "Tuyết Băng", "Tuyết Chi", "Tuyết Hân", "Tuyết Hoa", "Tuyết Hương", "Tuyết Lâm", "Tuyết Lan", "Tuyết Loan", "Tuyết Mai", "Tuyết Nga", "Tuyết Nhi", "Tuyết Nhung", "Tuyết Oanh", "Tuyết Tâm", "Tuyết Thanh", "Tuyết Trầm", "Tuyết Trinh", "Tuyết Vân", "Tuyết Vy", "Tuyết Xuân", "Uyển Khanh", "Uyển My", "Uyển Nghi", "Uyển Nhã", "Uyên Nhi", "Uyển Nhi", "Uyển Như", "Uyên Phương", "Uyên Thi", "Uyên Thơ", "Uyên Thy", "Uyên Trâm", "Uyên Vi", "Vân Anh", "Vân Chi", "Vân Du", "Vân Hà", "Vân Hương", "Vân Khanh", "Vân Khánh", "Vân Linh", "Vân Ngọc", "Vân Nhi", "Vân Phi", "Vân Thanh", "Vân Thường", "Vân Thúy", "Vân Tiên", "Vân Trang", "Vân Trinh", "Vàng Lưu", "Vành Khuyên", "Vi Quyên", "Việt Hà", "Việt Hương", "Việt Khuê", "Việt Mi", "Việt Nga", "Việt Nhi", "Việt Thi", "Việt Trinh", "Việt Tuyết", "Việt Yến", "Vũ Hồng", "Vy Lam", "Vy Lan", "Xuân Bảo", "Xuân Dung", "Xuân Hân", "Xuân Hạnh", "Xuân Hiền", "Xuân Hoa", "Xuân Hương", "Xuân Lâm", "Xuân Lan", "Xuân Lan", "Xuân Liễu", "Xuân Linh", "Xuân Loan", "Xuân Mai", "Xuân Nghi", "Xuân Ngọc", "Xuân Nhi", "Xuân Nương", "Xuân Phương", "Xuân Tâm", "Xuân Thanh", "Xuân Thảo", "Xuân Thu", "Xuân Thủy", "Xuân Trang", "Xuân Uyên", "Xuân Vân", "Xuân Yến", "Xuyến Chi", "Yến Dan", "Yến Hồng", "Yến Loan", "Yên Mai", "Yến Mai", "Yến My", "Yên Nhi", "Yến Nhi", "Yến Oanh", "Yến Phương", "Yến Phượng", "Yến Thanh", "Yến Thảo", "Yến Trâm", "Yến Trinh"])
        return self.firstname
    def __CreateUserId(self):
        self.userid = unidecode(self.firstname.lower()).replace(" ", "")+str(random.randint(100000, 999999))
   
    def __MailGenarate(self):
        pwd = "Dinnedzz"
        Name = f'{self.__GetListFirstNameVN()} {self.__GetListLastNameVN()}'
        Username = self.no_accent_vietnamese(Name.lower())
        for i in range(4):
            num= str(random.randint(1,100))
            Username += num
        Result = {"Name":Name,"Username":Username.replace(" ","")}
        return Result

    def Get_Code(self,token):
        messages = requests.get("https://api.mail.tm/messages",headers={"authorization":"Bearer "+token}).json()
        return messages
   
    def Mail(self):
        Mail = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
        Mail = Mail.json()[0]
        print(Mail)
        return Mail
   
    def Show_Info_Account(self):
        Total_Thread = DinneGui.spinBox.value()
        DinneGui.Table_Tab.setRowCount(Total_Thread)
        for i in range(Total_Thread):
            Info = self.__MailGenarate()
            DinneGui.Table_Tab.setItem(i, 0, QTableWidgetItem(str(i)))
            DinneGui.Table_Tab.setItem(i, 1, QTableWidgetItem(str(Info['Name'])))
            DinneGui.Table_Tab.setItem(i, 2, QTableWidgetItem(str(self.Mail())))
            DinneGui.Table_Tab.setItem(i, 3, QTableWidgetItem(str(Info['Username'])))
            DinneGui.Table_Tab.setItem(i, 4, QTableWidgetItem(str("Dinne")))
   

class LdPlayer():
    def __init__(self,Path) -> None:
        self.pathLD = Path
    
    def GetDevices(self):
        listdevice = []
        devices = str(subprocess.check_output("adb devices", shell=True)).replace("b'List of devices attached\\r\\n", '').replace("'", '').split('\\r\\n')
        for device in devices:
            if device != '':
                listdevice.append(device.split('\\tdevice')[0])
        return listdevice

    def ExecuteLD(self, shell):
        return str(subprocess.Popen(f"ldconsole.exe list2 {shell}", stdout=subprocess.PIPE, shell=True, cwd=self.pathLD).stdout.read())

    def OpenLDTab(self, index):
        return str(subprocess.Popen(f"ldconsole.exe launch --index {index}", stdout=subprocess.PIPE, shell=True, cwd=self.pathLD).stdout.read())
  
    def ResizeLdPlayer(self, index, width, height, dpi):
        return str(subprocess.Popen(f"ldconsole.exe modify --index {index} --resolution {width},{height},{dpi}", stdout=subprocess.PIPE, shell=True, cwd=self.pathLD).stdout.read())
   
    def TotalTabLdPlayer(self):
        result = str(subprocess.run("ldconsole.exe list2", shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, cwd="D:\LDPlayer\LDPlayer9").stdout).split(',')
        SoDevices = int((len(result) - 10) / 9)
        print(SoDevices)
        return SoDevices

    def Pull_ApkFile(self,emulator,path):
        subprocess.check_call(f"adb -s {emulator} pull {path}", shell=True)


    def ScreenCapture(self, emulator):
        name = emulator
        if ":" in emulator:
            name = emulator.replace(":", "").replace(".", "")
        subprocess.check_call(f"adb -s {emulator} shell screencap /sdcard/Download/{name}.png", shell=True)
        subprocess.check_call(f"adb -s {emulator} pull /sdcard/Download/{name}.png Image/{name}.png", shell=True)
        return f"Image/{name}.png"

    def Click_Coordinates(self, emulator, x, y):
        
        subprocess.check_call(f"adb -s {emulator} shell input tap {x} {y}", shell=True)
    
    def FindImg(self, emulator ,target_pic_name):
        print(f'-- Emulator:[{emulator}] Find Image: {target_pic_name} ')
        img = cv2.imread(target_pic_name)
        img2 = cv2.imread(self.ScreenCapture(emulator))
        w, h = img.shape[1], img.shape[0]
        result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED) 
        location = numpy.where(result >= 0.8)
        data = list(zip(*location[::-1]))
        is_match = len(data) > 0
        if is_match:
            x, y = data[0][0], data[0][1]  
            return x + int(w/2), y + int(h/2)
        else:
            return False, False

    def DumXml(self,emulator):
        subprocess.check_call(f"adb -s {emulator} shell uiautomator dump")
        path = "\"\"%s\"\""%os.path.join(os.getcwd(), f"window_dump_{emulator}.xml")
        # self.AdbLd(f"pull /sdcard/window_dump.xml {path}")
        # return f'window_dump_{self.NameOrId}.xml'






class RegInstagram(QThread):
    signal = pyqtSignal(object)
    def __init__(self,emulator):
        super(RegInstagram, self).__init__()
        
        self.emulator = emulator 

    def run(self):
        print("==================Run==================")
        #DinneLdPlayer.Pull_ApkFile(emulator = self.emulator, path = "Source/Instagram_Lite.apk")
   

        Coor = list(DinneLdPlayer.FindImg(emulator = self.emulator, target_pic_name = "Source/Instagram.png"))
        print(Coor)
        DinneLdPlayer.Click_Coordinates(emulator = self.emulator, x = Coor[0], y = Coor[1])
        QtTest.QTest.qWait(2000)
        DinneLdPlayer.Click_Coordinates(emulator = self.emulator, x = 350, y = 650)
        print('__')


        
            




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())