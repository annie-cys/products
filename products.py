products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
    	break
    price = input('請輸入價格:')
    #如果輸入q就不用價格,提早break
    products.append([name, price]) #直接在裡面創作小清單裝入大清單
print(products)

#存取二維清單
products[0][0] #products清單中的第0個小清單中的第零個東西