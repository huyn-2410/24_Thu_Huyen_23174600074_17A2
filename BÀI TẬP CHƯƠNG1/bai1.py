class Hinhchunhat:
    def __init__(self,chieu_dai=0,chieu_rong=0):
        self.chieu_dai= chieu_dai
        self.chieu_rong= chieu_rong

    def nhap_du_lieu(self):
        self.chieu_dai=float(input("chiều dài của hình chữ nhật là:"))
        self.chieu_rong=float(input("chièu rộng của hình chữ nhật là:"))
    
    def chu_vi(self):
        return 2*(self.chieu_dai+self.chieu_rong)
    def dien_tich(self):
        return (self.chieu_dai*self.chieu_rong)
    
       

hinh_chu_nhat=Hinhchunhat()
hinh_chu_nhat.nhap_du_lieu()
print("Chu vi của hình chữ nhật là:",format(hinh_chu_nhat.chu_vi()))
print("Diện tích của hình chữ nhật:",format(hinh_chu_nhat.dien_tich()))