import random
small = input('請輸入終極密碼最小數字')
small = int(small)

big = input('請輸入終極密碼最大數字')
big = int(big)
r = random.randint(small, big)
x = 1
while True:
	answer = input('請問終極密碼是多少？ ')
	answer = int(answer)
	if answer == r:
		print('恭喜答對了～')
		break
	else:	
		print('猜錯了～您猜了',x ,'次')
		if answer > r:
			print('比答案大')
		elif answer < r:
			print('比答案小')
			

		x = x + 1