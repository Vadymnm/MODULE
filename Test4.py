from module_41 import sum_, dif_, mult_, div_
from module_42 import pov2_, povn_, sqrt_, log_
from module_43 import fact_, fibonacci_, round_

a = 16
b = 13
n = 4
print('a =', a, 'b =', b, 'n =', n)

c = sum_(a,b)
print('сумма a+b:',c)
c = dif_(a,b)
print('разность a-b:',c)
c = mult_(a,b)
print('произведение:',c)
c = div_(a,b)
print('деление a/b:',c)
# =======================
c = pov2_(a)
print('квадрат a:',c)
c = povn_(a,n)
print('a в степени "n":',c)
c = sqrt_(a)
print('квадратный корень из а:',c)
c = log_(a)
print('логорифм(10) а:',c)
# =======================
print('Округление')
round_(a,b,n)
c = fact_(a)
print('факториал а:',c)
c = fibonacci_(a)
print('фибоначчи а:',c)
# =======================
# =======================#
# =======================