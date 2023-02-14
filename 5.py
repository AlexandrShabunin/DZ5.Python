kod = ''
table = ''
for char in range(32, 128):
    kod += '{}:{}\t'.format(char, chr(char))
    if not (char - 31) % 10:
        table += '{}\n'.format(kod)
        kod = ''
table += '{}\n'.format(kod)
print(table)