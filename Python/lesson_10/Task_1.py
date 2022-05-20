class Matrix:
    def __init__(self, line_list):
        self.line_list = line_list

    def __str__(self):
        rez = ''
        for line in self.line_list:
            line_list_str = []
            for item in line:
                item = str(item).rjust(4, " ")
                line_list_str.append(item)
            rez = rez + '|' + ''.join(line_list_str) + '|\n'
        return rez

    def __add__(self, other):
        rez = []
        matrix_lenght = len(self.line_list)
        for line in range(0, matrix_lenght):
            line_len = len(self.line_list[line])
            new_line_list = []
            for item in range(0, line_len):
                try:
                    item_sum = self.line_list[line][item] + other.line_list[line][item]
                except IndexError:
                    print('Матрицы разного размера')
                    exit()
                new_line_list.insert(item, item_sum)
            rez.insert(line, new_line_list)
        return Matrix(rez)


m1 = Matrix([[1, 1], [2, 2], [3, 3]])
m2 = Matrix([[4, 4], [5, 5], [6, 6]])
m4 = Matrix([[4,3,2], [5,2,4], [6,7,9]])
#Матрицы одного размера
m3=m1+m2
print(m3)
#Матрицы разного размера
m5=m4+m1
print(m5)