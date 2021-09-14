def F_2():
    print('2_1')
    print('2_2')
    return 3

def F_1():
    print('1_1')
    value = F_2()
    print('1_2')
    return

print('m_1')
F_1()
print('m_2')
F_2()