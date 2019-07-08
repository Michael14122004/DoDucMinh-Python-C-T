# DoDucMinh-Python-C-T
while True:
    ten = input("Nhap ten ban vao day: ")
    a = True 
    # 123
    for i in range(0, 10):
        # 0
        if str(i) in ten:
            print("Ten cua ban khong hop le")
            a = False 
            break
    #  a - false
    if a == True:
        print("Ten moi cua ban la", ten)
        break
