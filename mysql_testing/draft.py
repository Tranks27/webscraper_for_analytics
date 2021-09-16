with open('to_copy.txt', 'w') as f:

    for i in range(6):  
        f.write(f'Stra1_{i+1} DECIMAL(5,2),')
    f.write('\\\n')

    for i in range(6):  
        f.write(f'Stra2_{i+1} DECIMAL(5,2),')
    f.write('\\\n')

    for i in range(6):  
        f.write(f'Stra3_{i+1} DECIMAL(5,2),')
    f.write('\\\n')

    for i in range(6):
        for j in range(5):
            f.write(f'Stra4_{i+1}{j+1} DECIMAL(5,2),')
    f.write('\\\n')

    for i in range(6):
        for j in range(5):
            f.write(f'Stra5_{i+1}{j+1} DECIMAL(5,2),')
    
