def calcolatrice(calcoli):
    try: 
        calcolo=eval(calcoli)
        calcoli="Il risultato è "+ str(calcolo)
        return calcoli
    except ValueError:
        return "Invalido!!"
    except NameError:
        return "Digita un numero valido!!"
    except ZeroDivisionError:
        return "Impossibile dividere per zero!!"
    except EnvironmentError:
        return "Digita un numero valido"