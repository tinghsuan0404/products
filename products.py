produsts = []
while True:
	name = input("請輸入商品名稱:")
	if name == "q":
		break
	price = input("請輸入商品價格:")
	p =[]
	p.append(name)
	p.append(price)#將輸入的產品加到清單中
	#p = [name, price]等於以上兩行
	produsts.append(p)
	#produsts.append([name, price])等於以上三行
print(produsts)

produsts[0][0]