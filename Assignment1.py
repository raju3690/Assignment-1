thriller=["Dark","Mindhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","Money Heist","War","Jack Ryan"]
comedy=["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang Theory","The Office","Space Force"]

n=input()
if n in thriller:
    print("It is a thriller")
elif n in comedy:
    print("It is a comedy")
else:
    print("It's neither comedy nor thriller")
