from scale_board.board.serial import BoardSerial


class MicrosimBoard(BoardSerial):
    """Класс для работы с табло фирмы Микро-Сим"""
    def send_weight(self, weight: int):
        self.serial.write(b'\x81\x20\x20' + str.encode(f"{int(weight):05}") + b'\x20\x20\x0d\x0A')
