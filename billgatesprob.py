setz = {1, 2, 3, 4, 5}


z = [(x,y,z) for x in setz for y in setz for z in setz]


def func(z):
	listt = []
	for i in z:
	   listt.append(i[2] - i[0])
	   listt.sort()
	return listt[-1]


func(z)

