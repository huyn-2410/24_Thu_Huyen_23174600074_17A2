class dagiac:
    def __init__(self,so_canh):
        self._so_canh=so_canh
        self.canh=[]
    def nhap_canh(self):
        for i in range(self.canh):
            canh=float(input("nhập số cạnh của đa giác:"))
            self.canh.append()
    def display(self):
        print("Đa giác có {} cạnh với độ dài:",format(self.canh()))

class hinhbinhhanh(dagiac):
    def __init__(self,canh_a,canh_b,chieu_cao):
        super().__init__(4)
        self.canh_a=canh_a
        self.canh_b=canh_b
        self.chieu_cao=chieu_cao
    def chu_vi(self):
        return 2*(self.canh_a+self.canh_b)   
    def dien_tich(self):
        return (self.canh_a*self.chieu_cao) 
    def display(self):
        print("Hình bình hành cạnh a ={}, cạnh b={},chiều cao={}",self.canh_a,self.canh_b,self.chieu_cao)
        print("Chu vi vủa hình bình hành là:",format(self.chu_vi()))
        print("Diện tích của hình bình hành là:",format(self.dien_tich()))

class hinhchunhat(hinhbinhhanh) :
    def __init__(self,chieu_dai,chieu_rong):
        super().__init__(chieu_dai,chieu_rong,chieu_rong)       # hình chữ nhật có chiều rộng bằng chiều cao
        self.chieu_dai=chieu_dai
        self.chieu_rong=chieu_rong
    def dien_tich(self):
        return self.chieu_dai*self.chieu_rong
    def display(self):
        print ("hình chữ nhật có chiều dài={},chiều rộng={}",self.chieu_dai,self.chieu_rong)
        print("chu vi hình chữ nhật là:",format(self.chu_vi()))
        print("diện tích của hình chữ nhật là",format(self.dien_tich()))
              
class hinhvuong(hinhchunhat):
    def __init__(self,canh):
        super().__init__(canh)
        self.canh=canh
    def dien_tich(self):
        return self.canh*2
    def display(self):
        


              