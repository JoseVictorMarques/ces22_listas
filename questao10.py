import sys

def complex_addition(z1, z2):
    "Calculates the addition of complex numbers"
    real= z1[0] + z2[0]
    imag= z1[1] + z2[1]
    z= (real, imag)
    return z
    


# Casos de Teste
z1=(9,14)
z2=(5,6)
z=complex_addition(z1,z2)
print(z[0]," + ",z[1],"i")