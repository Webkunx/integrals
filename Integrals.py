from math import pow, sqrt, pi , sin

""" f - function in integral , a - bottom limit, b - top limit,
n - number of steps,  """

f1 = lambda x: pow(x, 2)*sqrt(16 - pow(x,2))
f2 = lambda x , y: 12*y*sin(2*x*y)


def wrapper(res, er):
	print(f'Result calculated w/ my method:{res},\
difference w/ real result:{er}')



def rectangles1(f, a, b , n, real_result=0): # Rectangle method for integrals
	h = (b-a)/n
	result = f(a+ 0.5*h)
	for i in range(1,n):
		result += f(a+i*h+0.5*h)
	result *= h
	return result, result - real_result




def count_amount_of_steps(f, f_to_count, a, b, real, accuracy, c=0, d=0): 
	""" Count amount of steps for methods. f - method"""
	n = 1
	if c == 0 and d ==0:
		while True:
			if abs(f(f_to_count, a , b, n)[0] - real) < accuracy:
				print(n)
				break
			else:
				n += 1
	else:
		while True:
			if abs(f(f_to_count, a , b, c,d, n)[0] - real) < accuracy:
				print(n)
				break
			else:
				n += 1



def trapezium1(f, a, b, n, real_result=0):# Trapezium method for integrals
	h = (b-a)/n
	result=(f(a)+f(b))/2
	for i in range(1, n):
		result += f(a+i*h)
	result *= h
	return result, result - real_result

	

def  simpson1(f, a, b, n, real_result=0): # Simpson's method for integrals
	h = (b-a)/n
	result = f(a) + f(b)
	for i in range(2,n-1,2):
		result += 2*f(a+i*h)
	for i in range(1,n,2):
		result += 4*f(a+i*h)
	result *= h/3
	return result, result - real_result



# def rectangles2(f, a, b, c, d, nx, ny):
# 	hx= (b-a)/nx
# 	hy= (d - c)/ ny
# 	result = 0
# 	for i in range(nx):
# 		for j in range(ny):
# 			xi = a + hx*0.5 + hx* i
# 			yj = c + hy*0.5 + hy * j
# 			result += hx*hy*f(xi,yj)
# 	return result		
# rect2 = rectangles2(f2, 2, 3 , pi/4, pi/2, 30, 30)
# print(rect2)

# def trapezium2(f, a, b, c, d, nx, ny):
# 	hx= (b-a)/nx
# 	hy= (d - c)/ ny
# 	result = 0
# 	for i in range(nx):
# 		for j in range(ny):
# 			xi = a + hx* i
# 			yj = c + hy * j
# 			result += hx*hy*f(xi,yj)
# 	result += (f(a,c) + f(b,d))/2
# 	return result

# trap2 = trapezium2(f2, 2, 3 , pi/4, pi/2, 100, 100)
# print(trap2)



def simpson2(f, a, b, c, d, n, real_result=0): # Simpson's method for double integrals
	hx = (b-a)/n
	hy = (d-c)/n
	result = 0
	for i in range(1,n):
		for j in range(1,n):
			if i%2 == 1 and j%2 == 1:
				result += 4*f(a+hx*i, c + hy*j)
			elif i%2 == 0 and j%2 == 1:
				result += 8*f(a+hx*i, c + hy*j)
			elif i%2 == 1 and j%2 == 0:
				result += 8*f(a+hx*i, c + hy*j)		
			elif i%2 == 0 and j%2 == 0:
				result += 16*f(a+hx*i, c + hy*j)
	result= result*hx*hy/9
	return result, result - real_result			


# count_amount_of_steps(simpson2, f2, 2, 3 , -1, 0.02, pi/4, pi/2)

result_rectangles, er_rectangles = rectangles1(f1, 0 , 4 , 107, 16*pi)
print("Rectangles method")
wrapper(result_rectangles, er_rectangles)

result_trapezium , er_trapezium = trapezium1(f1, 0, 4, 242, 16*pi)
print("Trapezium method")
wrapper(result_trapezium, er_trapezium)

result_simpson1, er_simpson1 = simpson1(f1, 0 , 4 , 130, 16*pi)
print("Simpson1 method")
wrapper(result_simpson1, er_simpson1)

result_simpson2, er_simpson2 = simpson2(f2, 2, 3 , pi/4, pi/2, 38, -1)	
print("Simpson2 method")
wrapper(result_simpson2, er_simpson2)