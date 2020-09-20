pi = 3.14

def cylAll():
	def wallCyl():
		r = float(input("Введите радиус: "))
		h = float(input("Введите высоту: "))
		global stenka
		stenka = 2 * pi * r * h
	def cylFull():
		wallCyl()
		global rFull
		rFull = stenka * 2
	figure = int(input("1 - боковая стенка цилиндра\n2 - полная площадь цилиндра\n>: "))

	if figure == 1:
		print("боковая стенка цилиндра")
		wallCyl()
		print(f"стендка целикдра: {stenka}")
	if figure == 2:
		print("полная площадь цилиндра")
		cylFull()
		print(f"полная площадь цилиндра: {rFull}")
cylAll()