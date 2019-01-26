products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
    	break
    price = input('請輸入價格:')
    price = int(price)#型別轉換
    #如果輸入q就不用價格,提早break
    products.append([name, price]) #直接在裡面創作小清單裝入大清單
print(products)

#存取二維清單
products[0][0] #products清單中的第0個小清單中的第零個東西
for p in products:
	print(p[0], '的價格為', p[1])#products中還有小清單
	#p[0]是商品名稱, p[1]是價格
#'abc' + '123' = 'abc123'# 字串相加即為合併 
#'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding = 'utf-8') as f: # 只是打開
#會自動產生products.txt # w 寫入模式 #as f 把她當作f 簡稱
    f.write('商品,價格\n')#在for loop 前先寫欄位名稱
    #亂碼 - 編碼出問題encoding
    #寫入跟讀取檔案都牽扯到編碼
    #encoding = 'utf-8' 解決中文編碼問題
    for p in products :
	    f.write(p[0] + ',' + str(p[1]) + '\n')# \n換行符號 #真正寫入
		#合成一個大字串 #不用逗點做區隔會全部擠在同一格
	    #家法只能合併字串 ,不能合併整數