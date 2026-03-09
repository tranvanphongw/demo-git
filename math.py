# Cộng trừ nhân chia 2 số a và b 
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    return a / b
# Nhập 2 số từ người dùng
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
# Thực hiện các phép tính và in kết quả
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {subtract(a, b)}")
print(f"{a} * {b} = {multiply(a, b)}")
print(f"{a} / {b} = {divide(a, b)}")

print("Chương trình đã hoàn thành.") #add dòng đã hoàn thành vào cuối chương trình