import functions
import os

Dir = 'C:/Users/Home/Desktop/python/data'
frames = []
namey = []
for file in os.listdir(Dir):
    frames.append(Dir + '/' + file)
    namey.append(file)
# print(frames)

#получаем иксы
arrx = functions.read_file(frames[0])
frames.pop(0)
namey.pop(0)

for name in frames:
    arry = functions.read_file(name, openFile=True)
    stvalue = functions.calculate_static(arry)
    der = functions.derivative(arrx, arry)
    integr = functions.integral(arrx, arry)

    # print(arrx)
    # print(arry)
    # print(stvalue)
    # print(der)
    # print(integr)

    functions.write_output(namey[0], stvalue, der, integr)
    namey.pop(0)