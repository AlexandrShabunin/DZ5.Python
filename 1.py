def calcul(q, w, operator):
    if operator == '+':
        return q + w
    elif operator == '-':
        return q - w
    elif operator == '*':
        return q * w
    else:
        return q / w


def is_correct_operator(operator):
    return operator == '0' or operator == '+' or operator == '-' or \
        operator == '*' or operator == '/'


def get_operator():
    return input('operator: ')


def run_calcul(q=None, w=None):
    if q is None:
        q = float(input('q: '))
    if w is None:
        w = float(input('w: '))
    operator = get_operator()

    if not is_correct_operator(operator):
        print('Wrong operator')
        run_calcul(q, w)
        return
    elif operator == '0':
        return
    elif operator == '/' and w == 0:
        print('No division by zero')
        run_calcul()
        return
    else:
        print(calcul(q, w, operator))
        run_calcul()


run_calcul()
