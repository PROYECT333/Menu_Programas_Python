print("Este programa sera utilizado para demostrar el uso de While, For e If")
while True:
    tecla = int(input("Presiona: 1-Metodos(1-sumar, 2-restar, 3-multiplicar, 4-dividir), 5-Verificar si eres mayor de edad, \n"
                  + "6-Indicar si el numero es positivo o negativo, 7-Indicar que numero es mayor, 8-Adivinar el numero (Presiona 0 para Salir\n"))
    if tecla == 1:
        n1 = int(input("Ingresa el primer numero:\n"))
        n2 = int(input("Ingresa el segundo numero:\n"))
        r1 = n1 + n2
        print("El resultado es:", r1)
    if tecla == 2:
        n1 = int(input("Ingresa el primer numero:\n"))
        n2 = int(input("Ingresa el segundo numero:\n"))
        r1 = n1 - n2
        print("El resultado es:", r1)
    if tecla == 3:
        n1 = int(input("Ingresa el primer numero:\n"))
        n2 = int(input("Ingresa el segundo numero:\n"))
        r1 = n1 * n2
        print("El resultado es:", r1)
    if tecla == 4:
        n1 = int(input("Ingresa el primer numero:\n"))
        n2 = int(input("Ingresa el segundo numero:\n"))
        r1 = n1 / n2
        print("El resultado es:", r1)
    if tecla == 5:
        n1 = int(input("Ingresa tu edad:"))
        if n1 >=18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
    if tecla == 6:
        n1 = int(input("Ingresa un numero:"))
        if n1 >= 0:
            print("El numero ingresado es positivo")
        if n1 <= 0:
            print("El numero ingresado es negativo")
    if tecla == 7:
        n1 = int(input("Ingresa el primer numero:"))
        n2 = int(input("Ingresa el segundo numero:"))
        n3 = int(input("Ingresa el tercer numero:"))
        if n1 > n2:
            print("El numero mayor es:", n1)
        elif n2 > n3:
            print("El numero mayor es:", n2)
        elif n3 > n1:
            print("El numero mayor es:", n3)
    if tecla == 8:
        print("Adivina que numero es el correcto:")
        numero = 5
        while True:
            n1 = int(input("Ingresa un numero:"))
            if n1 == 5:
                print("El numero es correcto")
                break
            
            else: print("incorrecto")
    if tecla == 0:
        SystemExit

        
    
    
    
    
        
        
            
    
        
    
    
    



