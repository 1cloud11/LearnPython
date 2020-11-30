with open('referat.txt', 'r', encoding='UTF-8') as f:
    content = f.read()
    count_symbols = len(content)
    
    temp_content1 = content.replace('\n', ' ')
    count_words = len(temp_content1.split(' '))
    
    print(count_symbols)
    print(count_words)

    temp_content2 = content.replace('.', '!')

    with open('referat2.txt', 'w', encoding='UTF-8') as new_file:
        new_file.write(temp_content2)








