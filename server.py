import socket
from protocol import SensorData


def start_server():
    # 1. Tworzymy gniazdo TCP/IP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Rezerwujemy port 9999 na naszym komputerze (localhost)
    server.bind(('localhost', 9999))
    server.listen(1)
    print("Serwer wystartował i nasłuchuje na porcie 9999...")

    # 3. Czekamy na połączenie od klienta
    conn, addr = server.accept()
    print(f"Połączono z klientem o adresie: {addr}")

    try:
        while True:
            # 4. Odbieramy surowe bajty z sieci
            data = conn.recv(1024)
            if not data:
                break

            # 5. MAGIA: Deserializacja pobranych bajtów na obiekt klasy SensorData
            sensor_msg = SensorData.deserialize(data)
            print(
                f"[SERWER] Otrzymano dane binarnie i odczytano -> ID Czujnika: {sensor_msg.sensor_id}, Temperatura: {sensor_msg.temperature}°C")
    finally:
        conn.close()
        server.close()
        print("Serwer zakończył pracę.")


if __name__ == "__main__":
    start_server()