def molar_mass(n, m):
    m_mass_c = 12.011
    m_mass_h = 1.0079
    return n*m_mass_c + m*m_mass_h


for i in range(2, 10):
    print(f"M(C{ i }H{ 2*i+2 }) = {round(molar_mass(i, 2*i+2), 3)} g/mol")
