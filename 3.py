def up(numv, upend_num=0, null_num=''):
    if numv == 0:
        print(f'Перевернутое число получится: {null_num}{upend_num}')
        return
    else:
        if numv % 10 == 0:
            null_num = '0'
        upend_num = upend_num * 10 + numv % 10
        return up(numv // 10, upend_num, null_num)


up(numv=int(input("Введите целое число: ")))
