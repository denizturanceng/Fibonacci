def fibonacci(bitis_degeri):
    sayi_bir=0
    sayi_iki=1
    
    if (bitis_degeri < 0):
        print("Negatif sayı girilemez.")
    
    else:
        print("Fibonacci Dizisi:")
        while(sayi_bir <= bitis_degeri):
            
            print(sayi_bir)
            gecici_sayi=sayi_bir
            sayi_bir=sayi_bir+sayi_iki
            sayi_iki=gecici_sayi
            
bitis_degeri=int(input("Dizinin sonlanmasını istediğiniz sayıyı girin:"))    
fibonacci(bitis_degeri)
    