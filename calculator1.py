def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    return a / b

print("===== CHƯƠNG TRÌNH TÍNH TOÁN CƠ BẢN =====")
print("Kết quả cộng:", cong(10, 5))
print("Kết quả trừ:", tru(10, 5))
print("Kết quả nhân:", nhan(10, 5))
print("Kết quả chia:", chia(10, 5))