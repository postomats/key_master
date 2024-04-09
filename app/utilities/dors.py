from enum import Enum
from serial import Serial
import serial


class DoorCommands(int, Enum):
    UNLOCK = 0x82
    READ_SINGLE_DOOR_STATUS = 0x83
    READ_ALL_DOOR_STATES = 0x84
    OPEN_ALL_LOCKS = 0x86
    OPEN_MULTIPLE_LOCKS = 0x87
    LOCK_CHANNEL_CONTINUOUS = 0x88
    LOCK_CHANNEL_OUTPUT_OFF = 0x89
    


def send_single_door_status(ser, cell_id):
    return _send_command(ser, DoorCommands.READ_SINGLE_DOOR_STATUS, [cell_id])

def open_all_locks(ser, num_boards):
    return _send_command(ser, DoorCommands.OPEN_ALL_LOCKS, [num_boards])

def unlock(ser, cell_id):
    return _send_command(ser, DoorCommands.UNLOCK, [cell_id])

def _send_command(ser, command, data_field):
    # Создание кадра данных
    start_character = [0x57, 0x4B, 0x4C, 0x59]  # Starter "WKLY"
    
    # Если передано num_boards, то отправляем команду на все платы
    if command == DoorCommands.OPEN_ALL_LOCKS:
        num_boards = data_field[0]  # Предполагаем, что первый элемент в data_field содержит num_boards
        for i in range(num_boards):
            board_number = i
            return _send_command_frame(ser, start_character, board_number, command.value, data_field=[])
    else:
        cell_id = data_field[0]  # Предполагаем, что первый элемент в data_field содержит cell_id
        board_number = cell_id // 12
        cell_id %= 12
        return _send_command_frame(ser, start_character, board_number, command.value, [cell_id])
    
    ser.close()

def _send_command_frame(ser, start_character, board_number, instruction_word, data_field):
    # Вычисление длины кадра
    frame_length = 0x08 + len(data_field)
    
    # Вычисление проверочного байта XOR
    checksum = 0
    for byte in start_character + [frame_length, board_number, instruction_word] + data_field:
        checksum ^= byte
    
    # Отправка кадра данных
    frame = start_character + [frame_length, board_number, instruction_word] + data_field + [checksum]
    ser.write(bytearray(frame))
    return ser.read(10)  # Ожидаем 10 байт ответа