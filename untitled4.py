dav={"o'zbekiston":"toshkent","qirg'iziston":"bishkek",
     "qozoqiston":"ostona","daniya":"kopengagen","germaniya":"berlin"}
a=input("Istalgan davlat nomini kiriting: ").lower()
print(dav.get(a,"Bizda bunday ma'lumot yo'q").capitalize())
