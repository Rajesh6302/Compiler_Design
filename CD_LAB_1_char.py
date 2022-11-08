def remove_comment(s):
    i = 0
    comment_line_inside = False
    comment_block_level = 0
    result = []
    while i < len(s):
        if s[i] == '/' and i + 1 < len(s) and s[i + 1] == '*':
            comment_block_level += 1
        elif s[i] == '/' and s[i - 1] == '*':
            comment_block_level -= 1
        elif s[i] == '/' and i + 1 < len(s) and s[i + 1] == '/':
            comment_line_inside = True
        elif s[i] == '\n' and comment_line_inside == True:
            comment_line_inside = False
        elif not comment_line_inside and comment_block_level == 0:
            result.append(s[i])
        i += 1
    return ''.join(result)


def lexical_analyser(s):
    string = remove_comment(s)

    tokens = 0
    word = ""
    symbol = [':', ';', '{', '}', '(', ')', ',', '.', '[', ']']
    operator = ['+', '-', '/', '*', '%', '=']
    keyword = ['int', 'void', 'String', 'return', 'char', 'float', 'for', 'if', 'else', 'while', 'do']
    identifiers, keywords, operators, delimiters, literals, constants = [], [], [], [], [], []
    for i in string:
        if i != " " and i != "\n":
            word += i
            if word in symbol:
                delimiters.append(word)
                tokens += 1
                word = ""
        elif word in keyword:
            keywords.append(word)
            tokens += 1
            word = ""
        elif word in operator:
            operators.append(word)
            tokens += 1
            word = ""
        elif word.isnumeric():
            constants.append(word)
            tokens += 1
            word = ""
        elif len(word) > 0 and word[0] == "\"":
            literals.append(word)
            tokens += 1
            word = ""
        elif len(word) > 0:
            identifiers.append(word)
            tokens += 1
            word = ""

    print('keywords are : ', list(set(keywords)))
    print('Operators are : ', list(set(operators)))
    print('Constants are : ', list(set(constants)))
    print('Delimiters are : ', list(set(delimiters)))
    print('Literals are : ', list(set(literals)))
    print('identifiers are : ', list(set(identifiers)))
    print('total number of tokens : ', tokens)


f = open('code1.txt')
code = f.read()
print(code)
lexical_analyser(code)