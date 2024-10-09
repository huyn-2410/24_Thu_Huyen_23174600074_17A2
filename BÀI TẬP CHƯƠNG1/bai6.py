class Stack:
    def __init__(self,size=10):
        self.size=size
        self.stack=[]
        self.top=-1

    def __del__(self):
        del self.stack
        print("Ngăn xếp đã bị xoá")
    def push(self,gia_tri):
        if self.isFull():
            print("ngăn xếp đã đầy")
        else:
            self.stack.append(float(gia_tri))  
            self.top += 1
            print(f"Đã thêm {gia_tri} vào ngăn xếp.")

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống, không có phần tử nào để lấy.")
            return None
        else:
            value = self.stack.pop() 
            self.top -= 1
            print(f"Đã lấy {value} ra khỏi ngăn xếp.")
            return value

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1
    def count(self):
        return self.top +1

    def print(self):
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Các phần tử trong ngăn xếp:")
            for i in range(self.top, -1, -1):  
                print(self.stack[i])

stack=Stack(7)
stack.push(6.7)
stack.print()
stack.pop()                