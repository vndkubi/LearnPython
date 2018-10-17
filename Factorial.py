#Viết một chương trình có thể tính giai thừa của một số cho trước.
#Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. 
#Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

number = int(input("Enter your number: "))

def cal(number):
	if number == 0:
		return 1
	else:
		return number * cal(number - 1)

print("Result: {}".format(cal(number)))