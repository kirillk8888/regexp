def calculate(data, findall):
    matches = findall(r"(b|a|c){1}([+-])?=(b|a|c)?([+-]?\d*)")  # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        p = 0
        if s == '-':
            s = -1
            p = 1
        elif s == '+':
            s = 1
            p = 1
        else:
            s = 1
         
        data[v1] = data[v1] * p + (data.get(v2, 0) + int(n or 0)) * s
    return data
