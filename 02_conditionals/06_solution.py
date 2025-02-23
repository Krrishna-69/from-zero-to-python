dist = 5

if dist < 3:
    transport = "walk"
elif dist <= 15:
    transport = "bike"
else:
    transport = "Car"

print("AI recommends you the transport of : ", transport)