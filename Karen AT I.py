while True:
    print("========================================")
    print("Buongiorno signore, come posso aiutarla?")
    print("========================================")
    print("'Calcolatrice'")
    print("'File'")
    print("'Informazioni'")
    print("'Esci'")
    home_input = input()
    if home_input == "Esci" or home_input=="esci":
        break
    elif home_input=="Informazioni" or home_input=="informazioni":
        while True:
            print("=====================================================================")
            print("Ciao sono Karen, questa è la mia primissima versione, Karen AT I, e \nper ora sono un semplice programma scritto su Python che non può fare \nmolto. Sono stata programmata da Lorenzo Manunza tra il 22/07/2019 e \nil 28/07/2019. Vedremo come sarò in futuro.")
            print("=====================================================================")
            print("'Chiudi'")
            info_input=input()
            if info_input=="Chiudi" or info_input=="chiudi":
                break
            elif info_input=="Lory1502":
                print("Wow, hai scoperto questo Easter Egg. Complimenti!!!")
            else:
                print("Input sconosciuto")
    elif home_input == "Calcolatrice" or home_input=="calcolatrice":
        while True:
            print("'Addizione'")
            print("'Sottrazione'")
            print("'Moltiplicazione'")
            print("'Divisione'")
            print("'Potenza'")
            print("'Radicale'")
            print("'Fattoriale'")
            print("'Chiudi'")
            calc_input = input()
            if calc_input == "Chiudi" or calc_input=="chiudi":
                break
            elif calc_input == "Addizione" or calc_input=="addizione":
                num1 = float(input("Scrivere il primo addendo:"))
                num2 = float(input("Scrivere il secondo addendo:"))
                result = str(num1 + num2)
                print("Il risultato è " + result)
            elif calc_input == "Sottrazione" or calc_input=="sottrazione":
                num1 = float(input("Scrivere il minuendo:"))
                num2 = float(input("Scrivere il sottraendo:"))
                result = str(num1 - num2)
                print("Il risultato è " + result)
            elif calc_input == "Moltiplicazione" or calc_input=="moltiplicazione":
                num1 = float(input("Scrivere il primo fattore:"))
                num2 = float(input("Scrivere il secondo fattore:"))
                result = str(num1 * num2)
                print("Il risultato è " + result)
            elif calc_input == "Divisione" or calc_input=="divisione":
                try:
                   num1 = float(input("Scrivere il dividendo:"))
                   num2 = float(input("Scrivere il divisore:"))
                   result = str(num1 / num2)
                   print("Il risultato è " + result)
                except ZeroDivisionError:
                   print("Non puoi dividere per zero")
            elif calc_input == "Potenza" or calc_input=="potenza":
                num1 = float(input("Scrivere la base:"))
                num2 = float(input("Scrivere l'esponente:"))
                result = str(num1 ** num2)
                print("Il risultato è " + result)
            elif calc_input == "Radicale" or calc_input=="radicale":
                num1 = float(input("Scrivere l'indice:"))
                num2 = float(input("Scrivere il radicando:"))
                result = str(num2 ** (num1 ** -1))
                print("Il risultato è " + result)
            elif calc_input=="Fattoriale" or calc_input=="fattoriale":
                def factorial(x):
                    if x == 1 or x == 0:
                        return 1
                    else:
                        return x * factorial(x - 1)
                num1 = float(input("Scrivere un numero:"))
                result = str(factorial(num1))
                print("Il risultato è " + result)
            else:
                print("Input sconosciuto")
    elif home_input == "File" or home_input == "file":
        while True:
            print("'Apri'")
            print("'Chiudi'")
            file_input = input()
            if file_input == "Chiudi" or file_input == "chiudi":
                break
            elif file_input == "Apri" or file_input == "apri":
                try:
                    filename = input("Scrivi il nome di un file:")
                    with open(filename + ".txt") as f:
                        text = f.read()
                    print(text)
                except:
                    print("File sconosciuto")
            else:
                print("Input sconosciuto")
    else:
        print("Input sconosciuto")

