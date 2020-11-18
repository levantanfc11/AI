### Nhap so nguyen duong tu ban phim ###
 
start = 1
while start:
 s = raw_input('Nhap so nguyen duong tu ban phim: ')
 try:
  num = int(s)
  if num <= 0:
   print("So ban nhap khong phai la so nguyen duong, moi ban nhap lai.\n")
  else: start = 0
 except:
  print('So ban nhap khong dung, moi nhap lai.\n')
 
### Chuyen doi so thap phan sang so nhi phan ###
 
bin = ''
while num:
 bin = str(num % 2) + bin
 num /= 2
 
### In so nhi phan sang man hinh ###
print('So nhi phan tuong ung la: ' + bin)