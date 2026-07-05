import socket
import time
from protocol import SensorData


def start_client():
    # 1. Tworzymy gniazdo TCP/IP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Łączymy się z naszym serwerem na porcie 9999
    print("Łączenie z serwerem...")
    client.connect(('localhost', 9999))

    # 3. Tworzymy obiekt z testowymi danymi
    msg = SensorData(sensor_id=101, temperature=24.8)

    # 4. MAGIA: Zamieniamy obiekt na postać binarną (pakujemy w bajty)
    binary_data = msg.serialize()
    print(f"[KLIENT] Obiekt zamieniony na bajty: {binary_data}")

    # 5. Wysyłamy surowe bajty przez sieć
    client.sendall(binary_data)
    print("[KLIENT] Dane zostały wysłane!")

    # Chwila oddechu i zamykamy połączenie
    time.sleep(1)
    client.close()


if __name__ == "__main__":
    start_client()