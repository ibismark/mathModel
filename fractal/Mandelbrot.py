#-*- coding:utf-8 -*-

"""
マンデルブロ集合の描画プログラム
	複素力学系 Zn+1 = Zn * Zn + c　の漸化式において
	n -> 無限の時に |Zn| が発散せず有界な領域に止まるようなcの集合
	のことをマンデルブロ集合という

"""


import pylab as pl

#x and y range
xmin=-1.6
xmax=1.0
ymin=-1.6
ymax=1.6
#interbal
interbal = 0.02

def m_show(x, y):
	pl.xlim(xmin, xmax)
	pl.ylim(ymin, ymax)
	pl.plot(x, y, '.')
	pl.show()


def check(c):
	z = 0 + (0*1j)
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
	for k in pl.frange(xmin, xmax, interbal):
		for l in pl.frange(ymin, ymax, interbal):
			#c = x + iy
			c =k + (l*1j)
			if check(c)==1:
				x.append(k)
				y.append(l)

	m_show(x, y)

if __name__ == '__main__':
	Mandelbrot()
