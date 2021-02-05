def credit_calc():
        amount = float(input("amount: "))
        downpayment = float(input("downpayment: "))
        interest = float(input("interest:"))
        interest1 = interest/100
        term = float(input("term: "))
        command = input("Если всё верно ввидите 'Да': ")
        pereplat = (amount-downpayment)*(interest1*term)
        #    Ежемесечный платёж без учёта первоначального взноса
        ej_plat = (pereplat+amount)/(term*12)
        #    Общая сумма с переплатой процентов
        obsh_sum = ej_plat*(term*12)
        #    Ежемесечный платёж c учётом первоначального взноса
        real_plat = (obsh_sum-downpayment)/(term*12)
        if command == "Да":
            print("Ежемесячный платёж: ", real_plat)
            print("Общую сумма выплаты: ", obsh_sum)
            print("Общий объём начисленных процентов: ", pereplat)
        else:
            print("Неверная команда!") 


credit_calc()            