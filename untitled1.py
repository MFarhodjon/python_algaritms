mahsulotlar=["salat","go'sht","choynak","piyola","saryoq","kartoshka","non","piyoz","sabzi","shakar","mayanez"]
savat=[]
print("5 ta mahsulot kiritish imkonyatingiz bor")
bor_mahsulotlar=[]
yoq_mahsulotlar=[]
for i in range(5):
    savat.append(input())
if savat:
    for i in savat:
        if i in mahsulotlar:
            bor_mahsulotlar.append(i)
        else : yoq_mahsulotlar.append(i)    
if yoq_mahsulotlar:
    print("do'konimizda quyidagi mahsulotlar yo'q")
    print(yoq_mahsulotlar)
else :print("Do'konimizda siz so'ragan barch maxsulotlar bor")