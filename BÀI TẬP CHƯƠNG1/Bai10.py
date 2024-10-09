import math
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def nhap_diem(self):
        self.x = float(input("Nhập tọa độ x: "))
        self.y = float(input("Nhập tọa độ y: "))
    
    def hien_thi(self):
        print(f"Tọa độ điểm: ({self.x}, {self.y})")
class Elip(Diem):
    def __init__(self, x=0, y=0, truc_lon=1, truc_nho=1):
        super().__init__(x, y)
        self.truc_lon = truc_lon
        self.truc_nho = truc_nho
    
    def nhap_thong_tin(self):
        self.nhap_diem()  # Nhập tọa độ tâm của elip
        self.truc_lon = float(input("Nhập độ dài trục lớn: "))
        self.truc_nho = float(input("Nhập độ dài trục nhỏ: "))
    
    def tinh_dien_tich(self):
        dien_tich = math.pi * self.truc_lon * self.truc_nho
        return dien_tich
    
    def hien_thi(self):
        print("Thông tin elip:")
        self.hien_thi()  # Hiển thị tọa độ của điểm
        print(f"Trục lớn: {self.truc_lon}, Trục nhỏ: {self.truc_nho}")
        print(f"Diện tích elip: {self.tinh_dien_tich()}")
class DuongTron(Elip):
    def __init__(self, x=0, y=0, ban_kinh=1):
        super().__init__(x, y, ban_kinh, ban_kinh) 
    
    def nhap_thong_tin(self):
        self.nhap_diem()  
        self.truc_lon = self.truc_nho = float(input("Nhập bán kính: "))
    
    def tinh_dien_tich(self):
        dien_tich = math.pi * self.truc_lon ** 2
        return dien_tich
    
    def hien_thi(self):
        print("Thông tin đường tròn:")
        self.hien_thi()  # Hiển thị tọa độ của điểm
        print(f"Bán kính: {self.truc_lon}")
        print(f"Diện tích đường tròn: {self.tinh_dien_tich()}")
        

elip = Elip()
elip.nhap_thong_tin()
elip.hien_thi()

duong_tron = DuongTron()
duong_tron.nhap_thong_tin()
duong_tron.hien_thi()
