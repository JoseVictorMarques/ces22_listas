import sys

def complex_addition(z1, z2):
    "Calculates the addition of complex numbers"
    real= z1[0] + z2[0]
    imag= z1[1] + z2[1]
    z= (real, imag)
    return z
    


# Casos de Teste
z1=complex_addition((9,14),(5,6))
print(z1[0]," + ",z1[1],"i")
z2=complex_addition((10,4),(3,-6))
print(z2[0]," + ",z2[1],"i")
