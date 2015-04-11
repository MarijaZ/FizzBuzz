#napisi stevilko med 1 in 100
z = (raw_input("Povej stevilo od 1 do 100 je deljivo: "))
for z in range(1, 100):  # za vsako stevilo od 1 v rangu od 0 do 1
    if z % 3:
        print ("fizz")
    elif z % 5:
        print ("buzz")
    elif z % 3 and z % 5:
        print ("fizzbuzz")


