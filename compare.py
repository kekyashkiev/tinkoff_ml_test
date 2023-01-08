import numpy as np
import sys


if __name__ == '__main__':
    read, write = sys.argv[1:]
    files_path = open(read).read().split()
    i = 0
    plagiat_size = ''
    for i in range(0, len(files_path), 2):
        str1 = ''.join(open(files_path[i], encoding='UTF-8').read().split())
        str2 = ''.join(open(files_path[i + 1], encoding='UTF-8').read().split())

    file_write = open(write, 'w')
    file_write.write(plagiat_size)
    file_write.close()

def plagiat(str1, str2):
    size_x = len(str1) + 1
    size_y = len(str2) + 1
    matr = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matr [x, 0] = x
    for y in range(size_y):
        matr [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if str1[x-1] == str2[y-1]:
                matr [x,y] = min(
                    matr[x-1, y] + 1,
                    matr[x-1, y-1],
                    matr[x, y-1] + 1
                )
            else:
                matr [x,y] = min(
                    matr[x-1,y] + 1,
                    matr[x-1,y-1] + 1,
                    matr[x,y-1] + 1
                )
    print (matr)
    return (matr[size_x - 1, size_y - 1])



#не придумал идеальной метрики для вычисления процента оригинальности plagiat_size
#чем больше размер нижнего правого элемента,тем больше плагиата