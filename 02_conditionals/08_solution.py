password = "secure@pass"
ps = len(password)

if ps < 6:
    strength = "weak"
elif ps <= 10:
    strength = "medium"
else:
    strength = "strong"

print("password strength is : ", strength)