import math

class TamGiac:
    def __init__(self, a=1, b=1, c=1):
        self.a = a
        self.b = b
        self.c = c

    def nhap_canh(self):
        self.a = float(input("Nhập cạnh a: "))
        self.b = float(input("Nhập cạnh b: "))
        self.c = float(input("Nhập cạnh c: "))
    
    def tinh_chu_vi(self):
        return self.a + self.b + self.c
    
    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        dien_tich = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return dien_tich
    
    def hien_thi(self):
        print(f"Chu vi tam giác: {self.tinh_chu_vi()}")
        print(f"Diện tích tam giác: {self.tinh_dien_tich()}")

class TamGiacVuong(TamGiac):
    def __init__(self, a=1, b=1):
        super().__init__(a, b, math.sqrt(a**2 + b**2))  # Cạnh c là căn bậc 2 của a^2 + b^2

    def nhap_canh(self):
        self.a = float(input("Nhập cạnh góc vuông a: "))
        self.b = float(input("Nhập cạnh góc vuông b: "))
        self.c = math.sqrt(self.a**2 + self.b**2)  # Cập nhật cạnh huyền

    def hien_thi(self):
        print(f"Tam giác vuông với các cạnh: a = {self.a}, b = {self.b}, c = {self.c}")
        super().hien_thi()

class TamGiacCan(TamGiac):
    def __init__(self, canh_day=1, canh_bang=1):
        super().__init__(canh_bang, canh_bang, canh_day)  # Hai cạnh bằng nhau, và cạnh đáy
    
    def nhap_canh(self):
        self.c = float(input("Nhập cạnh đáy: "))
        self.a = self.b = float(input("Nhập hai cạnh bên bằng nhau: "))

    def hien_thi(self):
        print(f"Tam giác cân với cạnh đáy: {self.c}, cạnh bên: {self.a}")
        super().hien_thi()
class TamGiacDeu(TamGiacCan):
    def __init__(self, canh=1):
        super().__init__(canh, canh)  # Cả ba cạnh đều bằng nhau

    def nhap_canh(self):
        self.a = self.b = self.c = float(input("Nhập cạnh tam giác đều: "))

    def hien_thi(self):
        print(f"Tam giác đều với cạnh: {self.a}")
        super().hien_thi()

print("Tam giác vuông:")
tg_vuong = TamGiacVuong()
tg_vuong.nhap_canh()
tg_vuong.hien_thi()

print("\nTam giác cân:")
tg_can = TamGiacCan()
tg_can.nhap_canh()
tg_can.hien_thi()

print("\nTam giác đều:")
tg_deu = TamGiacDeu()
tg_deu.nhap_canh()
tg_deu.hien_thi()
