class BoardBase:
    """Base class that describes the structure for inheriting classes"""
    def __init__(self, protocol: str):
        self.protocol = protocol
        self.connected = False

    def __repr__(self):
        return f"Board with protocol: {self.protocol}"

    def connect(self):
        return

    def disconnect(self):
        return

    def send_weight(self, weight: float):
        return
