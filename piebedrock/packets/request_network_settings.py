from piebedrock.packets.packet import BedrockPacket

# Packet Name: Request Network Settings
# Packet ID: 0xC1 (131)
# Bound to: Server
# Fields:
#
#  Protocol Version: Int (Big Endian).

class RequestNetworkSettings(BedrockPacket):
    packet_id = 0xc1
    packet_type = "request_network_settings"

    def decode_payload(self):
        self.protocol_version = seld.read_int_be()
