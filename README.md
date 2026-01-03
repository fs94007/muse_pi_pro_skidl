# K1 SoC SKiDL and KiCad Symbol Files

This repository contains automatically generated SKiDL component definitions and KiCad symbol files for the K1 System-on-Chip.

## Files Generated

- `k1_soc_symbol.py` - SKiDL Python component definition
- `k1_soc.kicad_sym` - KiCad symbol library file
- `pin_classification.txt` - Detailed pin classification information

## Usage

### SKiDL Usage

```python
from k1_soc_symbol import k1_soc

# Create K1 SoC component
k1 = k1_soc()

# Access pins by category
ddr_pins = k1.get_pins_by_category('DDR/LPDDR接口')
gpio_pins = k1.get_pins_by_category('GPIO')

# Use in your schematic
jtag_tck = k1['PRI_TCK']
jtag_tdo = k1['PRI_TDO']
```

### KiCad Usage

1. Copy `k1_soc.kicad_sym` to your KiCad symbol library directory
2. In KiCad Schematic Editor, add the symbol library
3. Place the K1_SoC symbol in your schematic

## Pin Classification

The K1 SoC has 676 pins organized into the following functional categories:

- **电源和地**: 205 pins
- **DDR/LPDDR接口**: 188 pins
- **JTAG**: 6 pins
- **HDMI接口**: 12 pins
- **GPIO**: 122 pins
- **SD/eMMC接口**: 22 pins
- **电源管理和控制**: 5 pins
- **时钟和参考**: 9 pins
- **QSPI接口**: 8 pins
- **MIPI CSI接口**: 24 pins
- **其他核心电源**: 6 pins
- **PCIe接口**: 38 pins
- **USB接口**: 11 pins
- **音频接口**: 8 pins
- **MIPI DSI接口**: 12 pins

## Pin Types

- **GND**: Ground pins
- **POWER_IN**: Power supply pins  
- **INPUT**: Digital input pins
- **OUTPUT**: Digital output pins
- **BIDIRECTIONAL**: Bidirectional I/O pins
- **ANALOG_IN**: Analog input pins
- **ANALOG_OUT**: Analog output pins
- **PASSIVE**: Analog bidirectional or passive pins
- **NC**: Not connected pins

## Generation Information

These files were automatically generated from the `soc_k1_pins.csv` file using the `parse_k1_pins.py` script.

## License

This work is derived from the original K1 SoC pin definitions and is provided for use with SKiDL and KiCad schematic design tools.
