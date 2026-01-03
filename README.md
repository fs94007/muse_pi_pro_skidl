# K1 SoC Symbol Definitions

Auto-generated SKiDL and KiCad symbol definitions for the K1 System-on-Chip (SoC).

## Overview

This repository contains automatically generated symbol definitions for the K1 SoC based on the pin configuration data in `soc_k1_pins.csv`. The K1 SoC features a 676-pin BGA package with comprehensive peripheral interfaces including DDR memory, GPIO, high-speed communication interfaces (PCIe, USB, MIPI), and multimedia interfaces (HDMI, CSI, DSI).

## Generated Files

### 1. `k1_soc_symbol.py` - SKiDL Symbol Definition

Python module containing the SKiDL component definition for the K1 SoC. This can be imported and used in SKiDL-based schematic designs.

**Usage:**
```python
from skidl import Net
from k1_soc_symbol import K1_SoC

# Create K1 SoC instance
k1 = K1_SoC()

# Create nets and connect to pins
vcc_0v9 = Net('VCC_0V9')
gnd = Net('GND')

# Connect power pins
k1['VCC_M1'] += vcc_0v9
k1['VSS'] += gnd

# Connect GPIO
gpio_net = Net('LED_CONTROL')
k1['GPIO_00'] += gpio_net

# Connect DDR interface
ddr_dq0 = Net('DDR_DQ0')
k1['DQ_A_0'] += ddr_dq0
```

### 2. `k1_soc.kicad_sym` - KiCad Symbol Library

KiCad symbol library file (compatible with KiCad 6.0+) containing the graphical symbol definition for the K1 SoC.

**Usage:**
1. Open KiCad's Preferences → Manage Symbol Libraries
2. Add `k1_soc.kicad_sym` as a new library
3. The K1_SoC symbol will be available in the symbol chooser

### 3. `pin_classification.txt` - Pin Classification Report

Detailed report showing all 676 pins organized by functional category with their electrical characteristics.

### 4. `generate_symbols.py` - Generator Script

Python script that parses `soc_k1_pins.csv` and generates all the symbol files. Can be re-run if the CSV is updated.

**Usage:**
```bash
python3 generate_symbols.py
```

## Pin Organization

The K1 SoC pins are organized into the following functional groups:

### Interface Categories

| Category | Pin Count | Description |
|----------|-----------|-------------|
| **DDR/LPDDR** | 141 | LPDDR4X/LPDDR3 memory interface (data, strobes, command/address, clocks) |
| **GPIO** | 107 | General Purpose I/O pins (GPIO_00 to GPIO_127) |
| **Ground** | 159 | Ground pins (VSS, AVSS, VSSU variants) |
| **Power** | 74 | Power supply pins (VCC, AVDD variants) |
| **MIPI CSI** | 33 | Camera Serial Interface (CSI1, CSI2, CSI3) |
| **MIPI DSI** | 21 | Display Serial Interface |
| **eMMC** | 24 | Embedded MMC storage interface |
| **USB** | 18 | USB 2.0 interfaces (USB0, USB1, USB2) |
| **Audio** | 13 | Audio codec interface |
| **PCIe C** | 10 | PCI Express interface C |
| **PCIe B** | 10 | PCI Express interface B |
| **PCIe A** | 7 | PCI Express interface A |
| **SD/MMC1** | 8 | SD card interface |
| **QSPI** | 8 | Quad SPI flash interface |
| **HDMI** | 15 | HDMI video output (within DDR group for classification) |
| **Power Mgmt** | 7 | PMIC interface, reset, sleep control |
| **JTAG** | 6 | Debug interface |
| **Clock/Ref** | 6 | Crystal oscillator and reference signals |
| **NC** | 22 | Not connected pins |
| **Other** | 2 | Miscellaneous signals |

### Major Pin Groups

#### 1. DDR/LPDDR Memory Interface
- **Data Lines:** DQ_A_[0:15], DQ_B_[0:15]
- **Data Strobes:** DQS0_T/C_A/B, DQS1_T/C_A/B
- **Command/Address:** CA_A_[0:5], CA_B_[0:5]
- **Clocks:** CK_T/C_A/B
- **Chip Select:** CS0_A/B, CS1_A/B
- **Clock Enable:** CKE0_A/B, CKE1_A/B
- **Data Mask:** DMI0_A/B, DMI1_A/B
- **Power:** VDDQ_V1P2, AVDD06_DDR, AVDD11_DDR, AVDD18_DDR
- **Control:** DDR_RESET_N, ZQ_DDR_PHY, DDR_LP23_VREFCA/DQ

#### 2. GPIO (General Purpose I/O)
- **Pins:** GPIO_00 through GPIO_127
- **Power Domains:** Configurable 1.8V or 1.8V/3.3V
- **Power:** VCC18_GPIO, VCC1833_GPIO[2,3]

#### 3. JTAG Debug Interface
- **PRI_TCK:** JTAG clock
- **PRI_TDO:** JTAG data output
- **PRI_TDI:** JTAG data input
- **PRI_TMS:** JTAG mode select
- **PRI_TRST_N:** JTAG reset (active low)
- **JTAG_SEL:** Primary JTAG selection

#### 4. HDMI Interface
- **Data Channels:** HDMI_TX0P/N, HDMI_TX1P/N, HDMI_TX2P/N
- **Clock:** HDMI_TXCP/N
- **Power:** AVDD18_HDMI, AVDD33_HDMI, AVDD09_HDMI

#### 5. MIPI CSI (Camera)
- **CSI1:** 4-lane (DATA0-3, CLK)
- **CSI2:** Clock lane for CSI3 dual configuration
- **CSI3:** 4-lane configurable as 4-lane or dual 2-lane
- **Power:** AVDD18_CSI, AVDD09_CSI

#### 6. MIPI DSI (Display)
- **DSI1:** 4-lane (DATA0-3, CLK)
- **Power:** AVDD18_DSI1, AVDD09_DSI1, AVDD12_DSI1

#### 7. PCIe Interfaces
- **PCIEA:** 1-lane (TX, RX, REFCLK)
- **PCIEB:** 2-lane (TX0/1, RX0/1, REFCLK)
- **PCIEC:** 2-lane (TX0/1, RX0/1, REFCLK)
- **Power:** AVDD18_PCIEx, AVDD09_PCIEx

#### 8. USB 2.0
- **USB0:** D+/D- differential pair
- **USB1:** D+/D- differential pair
- **USB2:** D+/D- differential pair
- **Power:** AVDD18_USB, AVDD09_USB, AVDD33_USB

#### 9. SD/eMMC Storage
- **MMC1 (SD):** DAT0-3, CLK, CMD
- **eMMC:** D0-7, CLK, CMD, DS (data strobe)
- **Power:** VCC1833_MMC1, AVDD18_EMMC, AVDD09_EMMC

#### 10. QSPI Flash
- **Data:** QSPI_DAT0-3
- **Control:** QSPI_CLK, QSPI_CS1
- **Power:** VCC1833_QSPI

#### 11. Clock and Reference
- **XI_PAD/XO_PAD:** Crystal oscillator pads
- **EXT_32K_IN:** External 32kHz clock input
- **BG_OUT:** Bandgap reference output
- **MPLL_TST_AD/CK:** MPLL test pins

#### 12. Power Management
- **PMIC_INT_N:** PMIC interrupt
- **PWR_SCL/SDA:** PMIC I²C interface
- **RESET_IN_N:** System reset input
- **SLEEP_OUT:** Sleep control output
- **DVL0/DVL1:** Dynamic voltage level control

#### 13. Audio Interface
- **Power:** AVDD18_AUD, AVDD3V3_AUD, AUD_VDDU09
- **Reference:** AUD_AUREF10, AUD_REFGND

## Pin Type Mapping

The following pin type mappings are used:

| CSV Type | SKiDL Type | KiCad Type | Description |
|----------|------------|------------|-------------|
| G | Pin.types.PWRIN | power_in | Ground |
| P | Pin.types.PWRIN | power_in | Power Input |
| I | Pin.types.INPUT | input | Digital Input |
| O | Pin.types.OUTPUT | output | Digital Output |
| I/O | Pin.types.BIDIR | bidirectional | Bidirectional |
| AI | Pin.types.INPUT | input | Analog Input |
| AO | Pin.types.OUTPUT | output | Analog Output |
| AIO | Pin.types.PASSIVE | passive | Analog Bidirectional |
| RO | Pin.types.PASSIVE | passive | Passive (e.g., capacitor) |

## Power Supply Requirements

The K1 SoC requires multiple power supply rails:

- **VCC_M1 (0.9V):** Digital core power
- **VCC18_GPIO (1.8V):** GPIO bank power
- **VCC1833_GPIO (1.8V/3.3V):** Configurable GPIO bank power
- **VCC1833_QSPI (1.8V/3.3V):** QSPI interface power
- **VCC1833_MMC1 (1.8V/3.3V):** SD card interface power
- **VDDQ_V1P2 (0.6V/1.2V):** DDR I/O power (LPDDR4X: 0.6V, LPDDR3: 1.2V)
- **AVDD06_DDR (0.6V):** DDR analog power (LPDDR4X)
- **AVDD11_DDR (1.1V):** DDR PHY power
- **AVDD18_* (1.8V):** Various 1.8V analog supplies
- **AVDD09_* (0.9V):** Various 0.9V digital supplies
- **AVDD33_* (3.3V):** Various 3.3V supplies

## Verification Checklist

✓ All 676 pins parsed from CSV  
✓ All pins classified into functional groups  
✓ No duplicate or missing pins  
✓ Pin types correctly mapped  
✓ SKiDL symbol generated  
✓ KiCad symbol generated  
✓ Classification report generated

## Example: Complete Design

```python
from skidl import Net, Part, generate_netlist
from k1_soc_symbol import K1_SoC

# Create K1 SoC
k1 = K1_SoC()

# Power supplies
vcc_0v9 = Net('VCC_0V9')
vcc_1v8 = Net('VCC_1V8')
vcc_3v3 = Net('VCC_3V3')
gnd = Net('GND')

# Connect all VCC_M1 pins (0.9V core)
k1['VCC_M1'] += vcc_0v9

# Connect all VSS pins (ground)
k1['VSS'] += gnd

# Connect GPIO power
k1['VCC18_GPIO'] += vcc_1v8

# Example: Connect UART on GPIO
uart_tx = Net('UART_TX')
uart_rx = Net('UART_RX')
k1['GPIO_00'] += uart_tx
k1['GPIO_01'] += uart_rx

# Example: Connect eMMC
emmc = Part('Memory', 'eMMC', footprint='BGA-153')
k1['EMMC_CLK'] += emmc['CLK']
k1['EMMC_CMD'] += emmc['CMD']
for i in range(8):
    k1[f'EMMC_D{i}'] += emmc[f'DAT{i}']

# Generate netlist
generate_netlist()
```

## Notes

- The K1 SoC supports both LPDDR4X (0.6V I/O) and LPDDR3 (1.2V I/O) memory configurations
- GPIO banks can operate at either 1.8V or 3.3V depending on the power supply configuration
- Multiple USB, PCIe, and camera interfaces provide flexibility for various applications
- NC (Not Connected) pins should be left unconnected on the PCB

## Regenerating Symbols

If the CSV file is updated, regenerate all symbol files:

```bash
python3 generate_symbols.py
```

This will recreate:
- `k1_soc_symbol.py`
- `k1_soc.kicad_sym`
- `pin_classification.txt`

## License

These symbol files are auto-generated from the K1 SoC pinout data and are provided as-is for schematic design purposes.

## Contact

For issues or questions regarding these symbol files, please refer to the K1 SoC documentation or create an issue in this repository.
