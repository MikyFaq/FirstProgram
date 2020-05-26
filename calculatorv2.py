#Калькулятор - calculator v2
what = input ("Что делаем?What are we doing?(+,-,*,/): ")
a = float(input ("(Enter the first number:)Введите первое число: "))
b = float(input ("(Enter the Second number:)Введите второе число: "))
if what == "+":
	c = a + b
	print ("(Result:)Результат : " + str(c))
elif what == "-":
	c = a - b
	print ("(Result:)Результат : " + str(c))
elif what == "*":
	c = a * b
	print ("(Result:)Результат : " + str(c))
elif what == "/":
	c = a / b
	print ("(Result:)Результат : " + str(c))
else:
	print ("(Invalid operation selected. Try again later.)Выбрана неверная операция. Повторите попытку позднее.")
