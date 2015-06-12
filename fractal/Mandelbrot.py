#-*- coding:utf-8 -*-
import pylab as pl


min=-1.6	#x and y range	
max=1.6




def m_show(x, y):
	pl.xlim(min, max)
	pl.ylim(min, max)
	pl.plot(x, y, '.')
	pl.show()


def check(c):
	z = c
	n=0
	while (n<50 and abs(z)<2):
		#complex dynamical
		z = z*z+c
		n=n+1
	
	#n>=50 stay finite
	#n<50  infinite
	if n>=50:
		return 1
	else:
		return 0



def Mandelbrot():
	x=list()
	y=list()
	for k in pl.frange(min, max, 0.02):
		for l in pl.frange(min, max, 0.02):
			#c = x + iy
			c =k + (l*1j)
			if check(c)==1:
				x.append(k)
				y.append(l)

	m_show(x, y)



if __name__ == '__main__':
	Mandelbrot()
