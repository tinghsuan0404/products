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

for p in produsts:#大清單裡面的小清單
	print(p[0], "的價格是", p[1])