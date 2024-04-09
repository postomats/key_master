import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0
)


def connection():
    try:
        print(ser.is_open)
        ser.open()
    finally:
        yield ser
        ser.close()
