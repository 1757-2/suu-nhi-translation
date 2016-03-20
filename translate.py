toTranslate = open("original.txt", 'r')


x = raw_input('an 1 de dich sang tieng Viet, 2 de dich sang tieng suu nhi, roi an enter de dich ')
strg = str(toTranslate.read())
toTranslate.close()

if x == "1":
	strg = strg.replace("4", "a")
	strg = strg.replace("3", "e")
	strg = strg.replace("1", "i")
	strg = strg.replace("0", "o")
	strg = strg.replace("vk", "vo")
	strg = strg.replace("ck", "chong")
	toWrite = open('translated.txt', 'w')
	toWrite.write(strg)
	toWrite.close()
	print "vao` file translated.txt de doc ban dep ko che"
elif x == "2":
	strg = strg.replace("a", "4")
	strg = strg.replace("e", "3")
	strg = strg.replace("i", "1")
	strg = strg.replace("o", "0")
	strg = strg.replace("vo", "vk")
	strg = strg.replace("chong", "ck")
	strg = strg.replace("yeu", "iu")
	toWrite = open('translated.txt', 'w')
	toWrite.write(strg)
	toWrite.close()
	print "vao` file translated.txt de doc ban dich"
else:
	print "may bi dien a, 1 hoac 2 thoi"

print strg


raw_input("an enter de thoat chuong trinh")
