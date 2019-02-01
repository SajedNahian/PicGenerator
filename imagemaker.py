fh = open('image.ppm','w')
fh.write('P3 500 500 255 ')
for i in range(500):
	for j in range(500):
		fh.write('{} {} {} '.format((i * j) % 256, (i * j + 2) % 256, (i * j + 3) % 256))