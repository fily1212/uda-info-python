# Comunicazione Seriale - SOLUZIONE (Simulata)
import time

def calcola_baud_rate(bit_duration_ms):
    """Calcola baud rate da durata bit"""
    return 1000 / bit_duration_ms

def invia_byte_seriale(byte, baud_rate=9600, parity=None):
    """Simula invio byte su UART"""
    bit_duration = 1 / baud_rate

    print(f"\n🔌 TRASMISSIONE SERIALE UART")
    print(f"   Baud rate: {baud_rate}")
    print(f"   Byte: 0x{byte:02X} ({byte:08b})")

    # Frame UART: START + 8 DATA + PARITY? + STOP
    frame = []

    # START bit (0)
    frame.append(0)

    # DATA bits (LSB first)
    for i in range(8):
        bit = (byte >> i) & 1
        frame.append(bit)

    # PARITY bit (opzionale)
    if parity == 'even':
        parity_bit = sum(frame[1:]) % 2
        frame.append(parity_bit)
    elif parity == 'odd':
        parity_bit = (sum(frame[1:]) + 1) % 2
        frame.append(parity_bit)

    # STOP bit (1)
    frame.append(1)

    print(f"   Frame: {frame}")
    print(f"   Durata frame: {len(frame) * bit_duration * 1000:.2f} ms")

    # Visualizza timing
    print("\n   Timing diagram:")
    print("   " + "".join(str(b) for b in frame))

    return frame

def main():
    print("=== SIMULATORE UART ===\n")

    byte = int(input("Byte da trasmettere (0-255): ") or "65")
    baud = int(input("Baud rate (default 9600): ") or "9600")

    invia_byte_seriale(byte, baud_rate=baud, parity='even')

    # Esempi comuni
    print("\n📋 Baud rate comuni:")
    for br in [9600, 19200, 38400, 57600, 115200]:
        print(f"   {br} baud = {1000000/br:.2f} μs/bit")

if __name__ == "__main__":
    main()
