import time 
seconds = int(input("vanaf hoeveel seconden wil je terugtellen? "))
for i in range(seconds):
    print(str(seconds -i) +" seconden")
    time.sleep (1)
print("Rocket Launched!!!!!!!!!!!!!!!!!!!!!!!!!!")