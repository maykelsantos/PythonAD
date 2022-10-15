# Comando round

# Quando trabalhamos com números 'float', podemos arredondar o valor usando comando nativo

valor1 = 154.84545
valor2 = 626.88484
print(
    ('R$ ' + str(
        round(valor1, 2) + round(valor2, 2)
    )
    )
)
