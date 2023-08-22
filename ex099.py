def maior(* num):
    maior = cont = 0
    if len(num) >= 1:
        for i in num:
            if cont == 0:
                maior = i
            if i > maior:
                maior = i
            cont += 1
    print(f'O maior valor é {maior}, e foram informados {cont} ao todo.')


maior(3, 6, 7, -12, 45)
maior(1, -14, -15, 0)
maior(-3, -1, -88)
maior(2)
maior()