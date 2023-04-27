import xlsxwriter
import random

cl_1 = ()
cl_2 = ()
cl_3 = ()
cl_4 = ()

def add_list_to_tuple(my_tuple, my_list):
    new_tuple = my_tuple + (my_list,)
    return new_tuple

print('------------------------------------------------------')
a = int(input('Введите кол-во предметов:'))
print('------------------------------------------------------')
for i in range(1):
    print('Введите уроки для', i+1, 'класса:')
    for j in range(a):
        print('------------------------------------------------------')
        subject = input('Введите предмет:')
        teacher = input("Введите учителя:")
        hours = int(input('Введите кол-во часов данного предмета в неделю:'))
        if i == 0:
            for k in range(hours):
                cl_1 = add_list_to_tuple(cl_1, [subject,teacher])
        elif i == 1:
            for k in range(hours):
                cl_2 = add_list_to_tuple(cl_2, [subject,teacher])
        elif i == 2:
            for k in range(hours):
                cl_3 = add_list_to_tuple(cl_3, [subject,teacher])
        elif i == 3:
            for k in range(hours):
                cl_4 = add_list_to_tuple(cl_4, [subject,teacher])

cl_1_sh = tuple(random.sample(list(cl_1), len(cl_1)))
cl_2_sh = tuple(random.sample(list(cl_2), len(cl_2)))
cl_3_sh = tuple(random.sample(list(cl_3), len(cl_3)))
cl_4_sh = tuple(random.sample(list(cl_4), len(cl_4)))

workbook = xlsxwriter.Workbook('TEst.xlsx')
clas1 = workbook.add_worksheet()
clas2 = workbook.add_worksheet()
clas3 = workbook.add_worksheet()
clas4 = workbook.add_worksheet()

clas1.write('A1', 'Предмет')
clas1.write('B1', 'Учитель')

for i, (subjectss, teacherss) in enumerate(cl_1_sh, start=2):
    clas1.write(f'A{i}', subjectss)
    clas1.write(f'B{i}', teacherss)

clas2.write('A1', 'Предмет')
clas2.write('B1', 'Учитель')

for i, (subjectss, teacherss) in enumerate(cl_2_sh, start=2):
    clas2.write(f'A{i}', subjectss)
    clas2.write(f'B{i}', teacherss)
    
clas3.write('A1', 'Предмет')
clas3.write('B1', 'Учитель')

for i, (subjectss, teacherss) in enumerate(cl_3_sh, start=2):
    clas3.write(f'A{i}', subjectss)
    clas3.write(f'B{i}', teacherss)
    
clas4.write('A1', 'Предмет')
clas4.write('B1', 'Учитель')

for i, (subjectss, teacherss) in enumerate(cl_4_sh, start=2):
    clas4.write(f'A{i}', subjectss)
    clas4.write(f'B{i}', teacherss)

workbook.close()