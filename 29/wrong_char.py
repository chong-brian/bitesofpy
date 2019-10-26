def get_index_different_char(chars):
    alphanumerics = []
    non_alphanumerics = []
    for char in chars:
        if str.isalnum(str(char)):
            alphanumerics.append(char)
        else:
            non_alphanumerics.append(char)
    print(alphanumerics)
    print(non_alphanumerics)
    if len(alphanumerics) == 1:
        return chars.index(alphanumerics[0])
    else:
        return chars.index(non_alphanumerics[0])
