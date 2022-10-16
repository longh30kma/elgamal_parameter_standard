
from math import e
import math
import cryptomath_module as cryptoMath
import rabin_miller as rabinMiller
#TRONG PHẦN NÀY NHÓM SẼ KIỂM TRA SỐ NGUYÊN TỐ LẤY ĐƯỢC TỪ FILE TXT
#GIẢ THIÊT THAM SỐ ĐƯỢC CHO CHƯA BIẾT CÓ PHẢI LÀ SỐ NGUYÊN TỐ HAY KHÔNG
#ĐẦU TIÊN SẼ TÌM XEM CÓ PHẢI LÀ SỐ NGUYÊN TỐ HAY KHÔNG BẰNG RABIN - MILLER
#SAU ĐÓ SẼ KIỂM TRA ĐỘ DÀI BIT CỦA THAM SỐ BẰNG PHƯƠNG PHÁP TÍNH ĐƯỢC ĐƯA RA TRONG TÀI LIỆU "Key Length" 
#Lucent Technologies and Technische Universiteit Eindhoven, 1 North Gate Road, Mendham, NJ 07945-3104, USA.

min_primitive_root = 3

def tinhmu(nlen):
    x = math.log(2)
    expv = float(1.976*((nlen * x )**(1/3)) * ((math.log(nlen*x))**(2/3)))
    return expv
#hàm kiểm tra tính nguyên tố của tham số p
def testprime(p):
    if rabinMiller.isPrime(p):
        print('THOA MAN DIEU KIEN LA SO NGUYEN TO')
        print('--------TIEP TUC KIEM TRA DO DAI--------')
        return p
        
    print('KHONG THOA MAN DIEU KIEN LA SO NGUYEN TO')
#---------------Phần Main-----------------------
#tham số p được lấy từ file thamsop.txt
f = open("thamsop.txt",mode = 'r',encoding = 'utf-8')
p=f.read()
#đưa tham số từ dạng đàu vào là str sang dạng int
p=int(p)
print('THAM SO P DUOC CHO O DAY LA: ',p)#xuất tham số ra để đối chiếu xem việc đọc có đúng hay không
#hàm tinhmu sử dụng để tính ra mũ của e trong công thức, chúng em đã giải thích trong file readme.txt
testprime(p)
nlen1=p.bit_length() # LẤY SỐ ĐẾM ĐỘ DÀI BIT CỦA THAM SỐ P ĐẦU VÀO
if nlen1<2048: #nếu nhỏ hơn 1024 ta coi là không an toàn luôn vì 2048 là an toàn đến năm 2030 rồi
    print(" DO DAI CUA THAM SO KHONG AN TOAN ")
else:
    expv1=tinhmu(nlen1) #gọi hàm tính mũ để tính được mũ của e ở phần đầu vào
    expv2=tinhmu(1024)  #1024 là độ dài đến 2004
    y=2004 + ( math.log(10)+ (expv1-expv2)) / 0.93 #công thức này nhóm cũng sẽ giải thích ở ngoài
    print("THAM SO CO GIA TRI DEN NAM: " + str(int(y+1)))
   