from mpmath import mp

"""PI_INT"""
# Configura a precisão para 100 casas decimais
mp.dps = 102  # 2 casas adicionais para garantir precisão

# Obtém o valor de pi como uma string
pi_str = str(mp.pi)

# Remove o ponto decimal e os primeiros 2 caracteres "3."
pi_decimal_part = pi_str[2:102]  # Pega as 100 primeiras casas decimais

# Converte a string das casas decimais para um inteiro
PI_INT = int(pi_decimal_part)

"""E_INT"""
# Configura a precisão para 100 casas decimais
mp.dps = 102  # 2 casas adicionais para garantir precisão

# Obtém o valor de e como uma string
e_str = str(mp.e)

# Remove o ponto decimal e os primeiros 2 caracteres "2."
e_decimal_part = e_str[2:102]  # Pega as 100 primeiras casas decimais

# Converte a string das casas decimais para um inteiro
E_INT = int(e_decimal_part)


def pi_real(n):
    if not (0 < n < 100):
        raise ValueError("n deve ser um número natural maior que 0 e menor que 100")
    
    # Obtemos a parte inteira e as casas decimais necessárias
    pi_str = str(PI_INT)
    integer_part = '3'
    decimal_part = pi_str[:n]
    
    # Formatando a string final
    result = f"{integer_part},{decimal_part}"
    return result


def e_real(n):
    if not (0 < n < 100):
        raise ValueError("n deve ser um número natural maior que 0 e menor que 100")
    
    # Obtemos a parte inteira e as casas decimais necessárias
    e_str = str(E_INT)
    integer_part = '2'
    decimal_part = e_str[:n]
    
    # Formatando a string final
    result = f"{integer_part},{decimal_part}"
    return result



