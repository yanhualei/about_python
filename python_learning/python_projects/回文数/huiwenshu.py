
"""判断一个数的回文数"""



def HWS(nums):
	num = str(nums)
	if num[::-1] == num:
		return num + "\t yes"
	else:
		return num + "\t no"
while True:
	try:
		user_input = int(input("请输入数字:\n"))
		if user_input == "q" or user_input == "exit" or user_input == "quit":
			print("已退出,谢谢使用!")
			break
		t = HWS(user_input)
		print(t)
	except:
		print("------输入数字,谢谢------")


