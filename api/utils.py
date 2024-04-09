import serial
from api.models import DoorCommands


def send_command(command, data_field):
    ser = serial.Serial(
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
    board_number = 0x00
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

# Открытие всех замков каналов
send_command(DoorCommands.OPEN_ALL_LOCKS, [0x01])  # Instruction word для открытия всех замков каналов