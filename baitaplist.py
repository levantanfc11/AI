x =list()
x.append(18)
x.append("Huế")
y =[12, 45, -1, -0.56, "abc"]
x.extend(y)
print("Giá trị của x là:",x)
a = x[-1]
b = x[0]
print("Giá trị của phần tử cuối cùng và phần tử đầu tiên của x lần lượt là:",a,b)
print("Giá trị của phần tử đầu tiên đến phần tử thứ 5 của x là:",x[0:5])
print("Giá trị của phần từ thứ 3 đến cuối cùng của x là",x[2:])