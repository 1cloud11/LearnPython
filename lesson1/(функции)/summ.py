def get_summ(one, two, delimiter='&'):
    return f'{one} {delimiter} {two}'

result = str(get_summ('Learn', 'python'))

print(result)
print(result.upper())

