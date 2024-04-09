from enum import Enum
from serial import Serial
import serial
import time


class COMMANDS(int, Enum):
    all_dors = 0x86


# Функция для отправки команды на RS485
def send_command(command, board_number=0x00, data_field=[]):
    ser = Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0
    )

    # Создание кадра данных
    start_character = [0x57, 0x4B, 0x4C, 0x59]  # Starter "WKLY"
    frame_length = 0x08 + len(data_field)
    #board_number = 0x00
    instruction_word = command
    
    checksum = 0
    for byte in start_character + [frame_length, board_number, instruction_word] + data_field:
        checksum ^= byte
    print(checksum)
    # Отправка кадра данных
    frame = start_character + [frame_length, board_number, instruction_word] + data_field + [checksum]
    print(frame)
    ser.write(bytearray(frame))
    response = ser.read(10)  # Ожидаем 7 байт ответа
    print("Response:", response)
    ser.close()

if __name__ == '__main__':
    # Открытие всех замков каналов
    send_command(0x87, [0x01])  # Instruction word для открытия всех замков каналов