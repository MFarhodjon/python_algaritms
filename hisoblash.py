def hisoblash(birinchi,ikkinchi,uchinchi):
    umumiy=birinchi+ikkinchi+uchinchi
    qoldiqlar=[];sanoq=0
    minus_qoldiqlar=[]
    for i in birinchi,ikkinchi,uchinchi:
        sanoq+=1
        if umumiy/3-i>=0:
            qoldiqlar.append(f"{sanoq}dagi inson {umumiy/3-i}cha to'laydi")
        else: minus_qoldiqlar.append(umumiy/3-i)
    if len(qoldiqlar)==1:qoldiqlar.append(f"{minus_qoldiqlar[0]} bir shaxsga {minus_qoldiqlar[1]} bir shaxsga")
    
    for i in qoldiqlar:print(i)
    print(umumiy/3)