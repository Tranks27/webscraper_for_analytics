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
# with open('to_copy.txt', 'w') as f:
#     # for j in range(80):
#     #     # if j < 5
#     j = 2
#     ## Strategy 1
#     for i in range(6):  
#         f.write(f'Stra1_{i+1} = {{result[{j}]}},')
#         j = j+1

#     ## Strategy 2
#     f.write('\n')
#     for i in range(6):
#         f.write(f'Stra2_{i+1} = {{result[{j}]}},')
#         j = j+1

#     ## Strategy 3
#     f.write('\n')
#     for i in range(6):
#         f.write(f'Stra3_{i+1} = {{result[{j}]}},')
#         j = j+1

#     ## Strategy 4
#     f.write('\n')
#     for k in range(6):
#         for i in range(5):
#             f.write(f'Stra4_{k+1}{i+1} = {{result[{j}]}},')
#             j = j+1
            
#     ## Strategy 5
#     f.write('\n')
#     for k in range(6):
#         for i in range(5):
#             f.write(f'Stra5_{k+1}{i+1} = {{result[{j}]}},')
#             j = j+1



