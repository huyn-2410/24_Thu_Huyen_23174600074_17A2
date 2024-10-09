class PS:
    def __init__(self, tu_so=0, mau_so=1):
        if mau_so == 0:
            print("Mẫu số phải khác 0")
        self.tu_so = tu_so
        self.mau_so = mau_so

    def nhap_phan_so(self):
        while True:
            try:
                self.tu_so = int(input("Nhập tử số: "))
                self.mau_so = int(input("Nhập mẫu số: "))
                if self.mau_so == 0:
                    print("Mẫu số phải khác 0. Vui lòng nhập lại.")
                else:
                    break
            except :
                print("Vui lòng nhập số nguyên.")

    def in_phan_so(self):
        print(f"phân số là:{self.tu_so}/{self.mau_so}")


ps2 = PS()
ps2.nhap_phan_so()
ps2.in_phan_so()  