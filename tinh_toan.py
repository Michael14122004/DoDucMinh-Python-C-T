# DoDucMinh-Python-C-T
print("Hi")
while True:
    so = input("Nhap so ban can vao day")
    if so.isdigit():
        if int(so) < 100000:
            print(int(so)//10)
            break
        else:
            print("So qua lon de tinh") 
    else:
        print("Do khong phai la so")
        break 
