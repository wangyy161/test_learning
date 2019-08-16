from PIL import Image

infile = 'G:\\111\\黑色背景金币.gif'
outfile = 'G:\\111\\黑色背景金币1.gif'
im = Image.open(infile)
(x, y) = im.size
x_s = 1920
y_s = 1080
out = im.resize((x_s, y_s), Image.ANTIALIAS)
out.save(outfile)

print('original size: ', x, y)
print('adjust size: ', x_s, y_s)