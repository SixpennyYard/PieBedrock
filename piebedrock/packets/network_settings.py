from piebedrock.packets.packet import GamePacket

class NetworkSettings(BedrockPacket):
    packet_id = 0x8F
    packet_type = "network_settings"

    def encode_payload(self):
        self.write_short(self.compression_threshold)
        self.write_short(self.compression_method) # 0 - ZLib, 1 - Snappy
        self.write_bool(False)
        self.write_byte(-1)
        self.write_float(0.0)
