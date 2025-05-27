from numpy import array, loadtxt, mean, gradient
# импорт данных из файла(при openFile = True импорт с помощью open, иначе np.loadtxt)
# return np.array, iput path str
def read_file(path,openFile = False):
    if openFile:
        with open(path, 'r') as file:
            arr = array([float(str[:-1]) for str in file.readlines()])
        return arr
    return array(loadtxt(path, dtype=float))
# функция расчета статистических показателей
# return np.array, input array y
def calculate_static(y):
    dic = {"mean":float(mean(y)), "min":float(min(y)), "max":float(max(y))}
    return dic
# функция расчета производной
# return np.array, input array x, array y
def derivative(x,y):
    return gradient(y,x)
# функция расчета определенного интеграла для y=f(x), методом прямоугольников.
def integral(x, y):
    sum = 0
    for i in range(len(x)-1):
        sum = (x[i+1]-x[i]) * (y[i]+y[i+1])/2
    return sum
# запись файла с результатами
def write_output(nameY, stvalue, deriv, interg):
    print(f"Начало записи в out_{nameY}.dat")
    with open(f"output/out_{nameY}.dat", 'w') as outfile:
        outfile.write(f"имя файла из которого брались значения функции: {nameY}.dat\n\
статистические показатели: {stvalue}\n\
значения производной: {deriv}\n\
значение определенного интеграла: {interg}\n\n")
        print(f"Конец записи записи в out_{nameY}.dat\n")