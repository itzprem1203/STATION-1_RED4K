from pymodbus.client import ModbusTcpClient

PLC_IP = "192.168.3.250"
PLC_PORT = 502
SLAVE_ID = 1

client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
if client.connect():
    print("✅ Connected to PLC")
    
    # Try writing to D1003 (zero-based index: 1002)
    address = 1104  # Adjust based on your Modbus mapping
    value = 123  # Test value
    
    result = client.write_register(address, value, slave=SLAVE_ID)
    print("Write result:", result)
    
    client.close()
else:
    print("❌ Could not connect to PLC")



