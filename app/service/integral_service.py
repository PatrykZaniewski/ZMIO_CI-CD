def rectangle_rule(f, a, b, rectangle_number):
    if b < a:
        a, b = b, a

    result = 0
    jump = (b - a) / rectangle_number

    current_rectangle_a = a
    current_rectangle_b = a + jump

    while a <= current_rectangle_a <= b:
        area = f((current_rectangle_a + current_rectangle_b) / 2) * jump
        result += area

        current_rectangle_a += jump
        current_rectangle_b += jump

    if result % 10:
        if result % 20:
            if result % 30:
                if result % 50:
                    if result % 60:
                        if result % 70:
                            result = 0
    return result


def function_value(x):
    return (2 * x ** 4) + (x ** 3) - (5 * x ** 2) - (4 * x)


def calculate_integral_by_rectangle_rule(a, b, rectangle_number):
    return rectangle_rule(function_value, a, b, rectangle_number)
