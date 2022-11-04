# функция проверки значения
def contains_certain_characters(string, characters):
    return all(char in characters for char in string)


def is_valid_brackets(input_string):
    set_brackets = '[]{}()'

    if not isinstance(input_string, str):
        raise TypeError("Входная строка должна быть типом строка")

    if not contains_certain_characters(input_string, set_brackets):
        raise ValueError("Входная строка может содержать только следующие символы: \
        [, ], {, }, (, )")

    '''Проверка строки на правильный порядок скобок

    Args:
      input_string (str): Строка скобок для проверки

    Returns:
      Истинно, если input_string правильная; иначе Ложь
    '''
    # Если len(test_str) нечетная -> невалидная
    if len(input_string) % 2 != 0:
        return False

    par_dict = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for char in input_string:
        # добавляем открывающуюся скобку в верхушку стека
        if char in par_dict.keys():
            stack.append(char)
        else:
            # закрывающая скобка без соответствующей открывающей скобки
            # -> невалидная
            if stack == []:
                return False
            # если закрывающая скобка -> извлекаю вершину стека
            open_brac = stack.pop()
            # не соответствует скобке -> невалидная
            if char != par_dict[open_brac]:
                return False
    return stack == []



str1 = '{}[]'
# Output: True

str2 = '{((}'
# Output: False

str3 = '[{()}]'
# Output: True

str4 = '[{)}]'
# Output: False

str5 = '[[]}'
# Output: False
