import os #opperating system 作業系統 #電腦的政府 #擁有權限

def read_file(filename):
    products = [] #都要產生
    with open(filename , 'r', encoding='utf-8') as f:
            for line in f:
                if '商品,價格' in line:
                    continue # 繼續 跳到下一個迴圈, 跳過第一回7 8 行
                name, price = line.strip().split(',')#切割字串,用逗點
                products.append([name, price])
    return products
            #split切割完會一塊一塊的, 會變成清單

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
        	break
        price = input('請輸入價格:')
        price = int(price)#型別轉換
        #如果輸入q就不用價格,提早break
        products.append([name, price]) #直接在裡面創作小清單裝入大清單
    print(products)
    return products

#印出購買紀錄
def print_products(products):
    for p in products:
    	print(p[0], '的價格為', p[1])#products中還有小清單
    	#p[0]是商品名稱, p[1]是價格
    #'abc' + '123' = 'abc123'# 字串相加即為合併 
    #'abc' * 3 = 'abcabcabc'

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f: # 只是打開
    # w 寫入模式 #as f 把她當作f 簡稱
        f.write('商品,價格\n')#在for loop 前先寫欄位名稱
        #亂碼 - 編碼出問題encoding
        #寫入跟讀取檔案都牽扯到編碼
        #encoding = 'utf-8' 解決中文編碼問題
        for p in products :
    	    f.write(p[0] + ',' + str(p[1]) + '\n')# \n換行符號 #真正寫入
    		#合成一個大字串 #不用逗點做區隔會全部擠在同一格
    	    #家法只能合併字串 ,不能合併整

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('耶!找到檔案了')
        products = read_file(filename)
    else:
        print('找不到檔案......')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)


main()

#refactor 重構