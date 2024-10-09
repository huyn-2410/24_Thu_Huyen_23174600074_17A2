class Date:
    def __init__(self,ngay=1,thang=1,nam=2000):
        self.ngay=ngay
        self.thang=thang
        self.nam=nam
    def display(self):
        print(f"Ngày {self.ngay}/{self.thang}/{self.nam}")

    def tinh_nam_nhuan(self):
        return (self.nam%4==0 and self.nam%100!=0)or(self.nam%400==0)
    def ngay_tiep(self):
        ngay_trong_thang=[31,28,31,30,31,30,31,30,31,30,31,30] 
        if self.tinh_nam_nhuan():
            ngay_trong_thang[1]=29

        self.ngay+=1
        if self.ngay>ngay_trong_thang[self.thang-1]:
            self.ngay = 1
            self.month += 1
            if self.thang > 12:
                self.thang = 1
                self.nam += 1

obj=Date(8,10,2024)

obj.display()
obj.ngay_tiep()
obj.display()

