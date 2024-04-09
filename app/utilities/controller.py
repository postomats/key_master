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
        if not ser.is_open:
            ser.open()
        yield ser
    finally:
        ser.close()
