from scapy.all import sniff

def process_packet(packet):

    protocol = packet.summary()

    print("Packet:", protocol)


def start_sniffing():

    sniff(prn=process_packet, count=10)