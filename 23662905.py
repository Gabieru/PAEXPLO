def is_valid_expression(s: str):
    expresion = s
    if expresion.count("(") == expresion.count(")"):
        for elemento in expresion:
            if elemento not in ["+", "-", "/", "*", "(", ")"]:
                if not elemento.isdigit():
                    return False
        return True
    else:
        return False
    






s = "4.5"
s1 = "((3-(4*((4+1)*8))/7"
print(is_valid_expression(s)) # Esta bien arroja True
print(is_valid_expression(s1)) # Falta parentesis, arroja false