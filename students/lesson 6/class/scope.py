#dont use vars like this
x = 20
def change():
    x = 30
    return x

print(x)
print(change())
print(x)

