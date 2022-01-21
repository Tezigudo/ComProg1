'''
Program to discount

<50_000 --> 50%

100_000 > x > 50000 --> part I 50_000 50%
                        part II 50_000 30%
x>100_000 --> part I 50_000 50%
            part II 50_000 30%
            part III 10%
'''

# fee = float(input('Enter fee: '))
# print('Total discount = '+[f'{0:.2f}', f'{fee/2:.2f}'][fee>0])


# def cal_discount(fee):
#     return 0 if fee<0 else fee/2

# def print_result(dis):
#     return f'Total discount = {dis:.2f}'
    

# fee = float(input("Enter fee: "))
# print_result(cal_discount(fee))



# def cal_discount(fee):
#     part1, part2, part3 = [[0, fee][fee>0], 50_000][fee>50_000], [[0, fee-50_000][fee-50_000>0], 50_000][fee>100_000], [0, fee-100_000][fee-100_000>0]
#     dis1, dis2, dis3 = part1*.5, part2*.3, part3*.1
#     return dis1, dis2, dis3
    
# def print_result(dis1, dis2, dis3):
#     print(f'D1 = {dis1:.2f}')
#     print(f'D2 = {dis2:.2f}')
#     print(f'D3 = {dis3:.2f}')
#     print(f'Total discount = {dis1+dis2+dis3:.2f}')

# fee = float(input("Enter fee: "))

# # dis1, dis2, dis3 = cal_discount(fee)
# # print_result(dis1, dis2, dis3)




# '''def cal_discount(fee):
#     part1, part2, part3 = [[0, fee][fee>0], 50_000][fee>50_000], [[0, fee-50_000][fee-50_000>0], 50_000][fee>100_000], [0, fee-100_000][fee-100_000>0]
#     dis1, dis2, dis3 = part1*.5, part2*.3, part3*.1
#     return dis1, dis2, dis3

# def cal_with_option(total, typ):
#     if typ.lower() == 'g':
#         return 0
# #     elif typ.lower() == 'f':
# #         return total*.4
# #     else:
# #         return total

# # def print_result(dis1, dis2, dis3, typ):
# #     print(f'D1 = {dis1:.2f}')
# #     print(f'D2 = {dis2:.2f}')
# #     print(f'D3 = {dis3:.2f}')
# #     print(f'Total discount = {dis1+dis2+dis3:.2f}')
#     print(f'Student type {typ} final discount {cal_with_option(dis1+dis2+dis3, typ):.2f}')
    
# fee = float(input("Enter fee: "))
# option = input("Student type: ")
# dis1, dis2, dis3 = cal_discount(fee)
# print_result(dis1, dis2, dis3, option)

# '''
# # fee = float(input('Enter fee: '))
# part1, part2, part3 = [[0, fee][fee>0], 50_000][fee>50_000], [[0, fee-50_000][fee-50_000>0], 50_000][fee>100_000], [0, fee-100_000][fee-100_000>0]
# # dis1, dis2, dis3 = part1*.5, part2*.3, part3*.1
# # print(f'D1 = {dis1:.2f}')



# # '''
# # 40%*dis --> forign
# # '''

# fee = 100
# def cal_price(adult, children):
#     return adult*100+children*fe*50
    


# def show_result(adult, child):
#     print(f'{adult} adults {child} children total {cal_price(adult, child)} Baht.')
    
# a = int(input('How many adults?: '))
# c = int(input('How many children?: '))

# show_result(a, c)

from urllib import request
from json import load
# from pandas import dataframe
student = load(request.urlopen('http://ske19-api.herokuapp.com/students'))['students']

for idss in student:
    print(student[idss])
