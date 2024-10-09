class Date:
    def __init__(self,ngay=1,thang=1,nam=2000):
        self.ngay=ngay
        self.thang=thang
        self.nam=nam
    def display(self):
        print(f" {self.ngay}/{self.thang}/{self.nam}")    

class Employee:
    def __init__(self,ho_ten,ngay_sinh,ngay_vao_cong_ty):
        self.ho_ten=ho_ten
        self.ngay_sinh=ngay_sinh
        self.ngay_vao_cong_ty=ngay_vao_cong_ty        
    def display(self):
        print("Họ và tên của nhân viên: ",self.ho_ten)
        print("Ngày tháng năm sinh của nhân viên: ",end=" ")
        self.ngay_sinh.display()
        print("Ngày vào công ty:",end=" ")
        self.ngay_vao_cong_ty.display()

   
ngay_sinh=Date(24,10,2005)
ngay_vao=Date(17,6,2024)
nhan_vien=Employee("Trần Thị Thu Huyền",ngay_sinh,ngay_vao)   
nhan_vien.display()

