
from PIL import Image
import os

input_dir = './moji/test/labels1/'
out_dir = './moji/test/vis1/'
a = os.listdir(input_dir)

for i in a:
    print(i)
    I = Image.open(input_dir+i)
    L = I.convert('L')
    L.save(out_dir+i)
print('over')