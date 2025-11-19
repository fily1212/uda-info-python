# Convertitore Unità di Misura - SOLUZIONE

# Fattori di conversione
CONVERSIONI = {
    # Lunghezza
    'km_m': 1000,
    'm_cm': 100,
    'cm_mm': 10,
    'm_inch': 39.3701,
    'km_mi': 0.621371,

    # Massa
    'kg_g': 1000,
    'g_mg': 1000,
    'kg_lb': 2.20462,

    # Tempo
    'h_min': 60,
    'min_s': 60,
    'h_s': 3600,

    # Velocità
    'kmh_ms': 1/3.6,
    'ms_kmh': 3.6,

    # Energia
    'J_cal': 0.239006,
    'kJ_kcal': 0.239006,

    # Temperatura (formule speciali)
}

def converti_lunghezza(valore, da, a):
    """Conversioni lunghezza"""
    conversioni = {
        ('km', 'm'): lambda x: x * 1000,
        ('m', 'km'): lambda x: x / 1000,
        ('m', 'cm'): lambda x: x * 100,
        ('cm', 'm'): lambda x: x / 100,
        ('cm', 'mm'): lambda x: x * 10,
        ('mm', 'cm'): lambda x: x / 10,
        ('km', 'mi'): lambda x: x * 0.621371,
        ('mi', 'km'): lambda x: x / 0.621371,
    }

    chiave = (da, a)
    if chiave in conversioni:
        return conversioni[chiave](valore)
    return None

def converti_velocita(valore, da, a):
    """Conversioni velocità"""
    if da == 'km/h' and a == 'm/s':
        return valore / 3.6
    elif da == 'm/s' and a == 'km/h':
        return valore * 3.6
    return None

def converti_temperatura(valore, da, a):
    """Conversioni temperatura"""
    if da == 'C' and a == 'F':
        return valore * 9/5 + 32
    elif da == 'F' and a == 'C':
        return (valore - 32) * 5/9
    elif da == 'C' and a == 'K':
        return valore + 273.15
    elif da == 'K' and a == 'C':
        return valore - 273.15
    return None

def converti_massa(valore, da, a):
    """Conversioni massa"""
    conversioni = {
        ('kg', 'g'): lambda x: x * 1000,
        ('g', 'kg'): lambda x: x / 1000,
        ('g', 'mg'): lambda x: x * 1000,
        ('mg', 'g'): lambda x: x / 1000,
        ('kg', 'lb'): lambda x: x * 2.20462,
        ('lb', 'kg'): lambda x: x / 2.20462,
    }

    chiave = (da, a)
    return conversioni.get(chiave, lambda x: None)(valore)

def main():
    print("=== CONVERTITORE UNITÀ DI MISURA ===\n")
    print("1. Lunghezza (km, m, cm, mm, mi)")
    print("2. Velocità (km/h, m/s)")
    print("3. Temperatura (C, F, K)")
    print("4. Massa (kg, g, mg, lb)")

    scelta = input("\nScegli categoria (1-4): ")

    if scelta == "1":
        valore = float(input("Valore: "))
        da = input("Da (km/m/cm/mm/mi): ").lower()
        a = input("A (km/m/cm/mm/mi): ").lower()

        risultato = converti_lunghezza(valore, da, a)
        if risultato is not None:
            print(f"\n📏 {valore} {da} = {risultato:.4f} {a}")

    elif scelta == "2":
        valore = float(input("Valore: "))
        da = input("Da (km/h o m/s): ")
        a = input("A (km/h o m/s): ")

        risultato = converti_velocita(valore, da, a)
        if risultato is not None:
            print(f"\n🏃 {valore} {da} = {risultato:.2f} {a}")

    elif scelta == "3":
        valore = float(input("Valore: "))
        da = input("Da (C/F/K): ").upper()
        a = input("A (C/F/K): ").upper()

        risultato = converti_temperatura(valore, da, a)
        if risultato is not None:
            print(f"\n🌡️ {valore}°{da} = {risultato:.2f}°{a}")

    elif scelta == "4":
        valore = float(input("Valore: "))
        da = input("Da (kg/g/mg/lb): ").lower()
        a = input("A (kg/g/mg/lb): ").lower()

        risultato = converti_massa(valore, da, a)
        if risultato is not None:
            print(f"\n⚖️ {valore} {da} = {risultato:.4f} {a}")

    # Conversioni comuni
    print("\n📋 Conversioni comuni:")
    print(f"   100 km/h = {converti_velocita(100, 'km/h', 'm/s'):.2f} m/s")
    print(f"   0°C = {converti_temperatura(0, 'C', 'F'):.0f}°F")
    print(f"   1 km = {converti_lunghezza(1, 'km', 'mi'):.2f} miglia")

if __name__ == "__main__":
    main()
