#################################################
## script to write the percentages table title
#################################################
# with open('to_copy.txt', 'w') as f:

#     for i in range(6):  
#         f.write(f'Stra1_{i+1} DECIMAL(5,2),')
#     f.write('\\\n')

#     for i in range(6):  
#         f.write(f'Stra2_{i+1} DECIMAL(5,2),')
#     f.write('\\\n')

#     for i in range(6):  
#         f.write(f'Stra3_{i+1} DECIMAL(5,2),')
#     f.write('\\\n')

#     for i in range(6):
#         for j in range(5):
#             f.write(f'Stra4_{i+1}{j+1} DECIMAL(5,2),')
#     f.write('\\\n')

#     for i in range(6):
#         for j in range(5):
#             f.write(f'Stra5_{i+1}{j+1} DECIMAL(5,2),')
    

#################################################
## sql Updater
#################################################
with open('to_copy.txt', 'w') as f:
    for j in range(80):
        for i in range(6):  
            f.write(f'Stra1_{i+1} = result[{j+1}],')
            if i == 5:
                break
        break
        

#     for i in range(6):  
#         f.write(f'Stra2_{i+1} DECIMAL(5,2),')
#     f.write('\\\n')

#     for i in range(6):  
#         f.write(f'Stra3_{i+1} DECIMAL(5,2),')
#     f.write('\\\n')

#     for i in range(6):
#         for j in range(5):
#             f.write(f'Stra4_{i+1}{j+1} DECIMAL(5,2),')
#     f.write('\\\n')

#     for i in range(6):
#         for j in range(5):
#             f.write(f'Stra5_{i+1}{j+1} DECIMAL(5,2),')



