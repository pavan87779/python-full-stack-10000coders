cho = 100
tcho = cho
w = cho
while w>=3:
    extra_cho = w//3
    tcho+=extra_cho
    w = extra_cho+ w%3
print(tcho)