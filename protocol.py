import struct


class SensorData:
    def __init__(self, sensor_id, temperature):

        self.sensor_id = sensor_id

        self.temperature = temperature


    def serialize(self):
        # 'i' to int (4 bajty), 'f' to float (4 bajty)
        fmt = "=if"
        return struct.pack(fmt, self.sensor_id, self.temperature)

    @staticmethod
    def deserialize(data):
        fmt = "=if"
        unpacked = struct.unpack(fmt, data)
        return SensorData(*unpacked)
