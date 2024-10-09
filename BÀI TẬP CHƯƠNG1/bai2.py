class TS:
    def __init__(self,name=" ",diem_Toan=0,diem_Ly=0,diem_Hoa=0):
        self.name=name
        self.diem_Toan=diem_Toan
        self.diem_Ly=diem_Ly
        self.diem_Hoa=diem_Hoa

    def nhap_du_lieu(self):
        self.name=input("Nhập họ và tên thí sinh: ")
        self.diem_Hoa=float(input("nhập điểm Hoá của thí sinh:"))
        self.diem_Toan=float(input("nhập điểm Toán của thí sinh:"))
        self.diem_Ly=float(input("nhập điểm Lý của thí sinh:")) 

    def tinh_tong_diem(self):
        return (self.diem_Toan+self.diem_Hoa+self.diem_Ly)
    
    def thong_tin(self):
        print("Họ và tên:",self.name,end=" ")
        print("Tổng điểm của thí sinh:",self.tinh_tong_diem())
    
def danh_sach_thi_sinh():  
    danh_sach=[]
    so_thi_sinh=int(input("Số thí sinh là: "))
    for i in range(so_thi_sinh) :
        thi_sinh = TS()
        thi_sinh.thong_tin()
        danh_sach.append(thi_sinh)
    return danh_sach
def thi_sinh_trung_tuyen(danh_sach,diem_chuan=20):
    
   
    # Lọc ra những thí sinh có tổng điểm lớn hơn hoặc bằng điểm chuẩn
    danh_sach_trung_tuyen = list(filter(lambda ts: ts.tinh_tong_diem() >= diem_chuan, danh_sach))
    
    # Sắp xếp danh sách trúng tuyển theo tổng điểm giảm dần
    danh_sach_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)
    print("Danh sách trúng tuyển:\n")
    for ts in danh_sach_trung_tuyen:
        ts.thong_tin()

danh_sach=danh_sach_thi_sinh
thi_sinh_trung_tuyen(danh_sach)


