#!/usr/bin/env python3
"""
Example: Using K1 SoC SKiDL Symbol
Demonstrates how to use the generated K1_SoC component in a SKiDL design

To run this example, first install SKiDL:
    pip install skidl

Then run:
    python3 example_usage.py
"""

from skidl import Net, Part, SKIDL, generate_netlist
from k1_soc_symbol import K1_SoC

def create_example_schematic():
    """
    Example schematic showing K1 SoC connections
    """
    
    # Create K1 SoC instance
    k1 = K1_SoC()
    
    # ============================================
    # Power Distribution
    # ============================================
    
    # Define power nets
    vcc_0v9 = Net('VCC_0V9')      # Core power
    vcc_1v8 = Net('VCC_1V8')      # 1.8V I/O
    vcc_3v3 = Net('VCC_3V3')      # 3.3V I/O
    gnd = Net('GND')              # Ground
    
    # Connect core power (0.9V)
    # Multiple VCC_M1 pins need to be connected
    for pin in k1.pins:
        if pin.name == 'VCC_M1':
            pin += vcc_0v9
    
    # Connect all ground pins
    for pin in k1.pins:
        if pin.name.startswith('VSS') or pin.name.startswith('AVSS'):
            pin += gnd
    
    # Connect GPIO power
    for pin in k1.pins:
        if 'VCC18_GPIO' in pin.name:
            pin += vcc_1v8
        elif 'VCC1833_GPIO' in pin.name:
            pin += vcc_1v8  # or vcc_3v3 depending on configuration
    
    # ============================================
    # Boot Flash (QSPI)
    # ============================================
    
    # Connect QSPI flash
    qspi_clk = Net('QSPI_CLK')
    qspi_cs = Net('QSPI_CS')
    qspi_data = [Net(f'QSPI_DAT{i}') for i in range(4)]
    
    k1['QSPI_CLK'] += qspi_clk
    k1['QSPI_CS1'] += qspi_cs
    for i in range(4):
        k1[f'QSPI_DAT{i}'] += qspi_data[i]
    
    # ============================================
    # UART Console (using GPIO)
    # ============================================
    
    uart_tx = Net('UART_TX')
    uart_rx = Net('UART_RX')
    k1['GPIO_00'] += uart_tx
    k1['GPIO_01'] += uart_rx
    
    # ============================================
    # Status LEDs (using GPIO)
    # ============================================
    
    led_nets = [Net(f'LED{i}') for i in range(4)]
    k1['GPIO_02'] += led_nets[0]
    k1['GPIO_03'] += led_nets[1]
    k1['GPIO_04'] += led_nets[2]
    k1['GPIO_05'] += led_nets[3]
    
    # ============================================
    # eMMC Storage
    # ============================================
    
    emmc_clk = Net('EMMC_CLK')
    emmc_cmd = Net('EMMC_CMD')
    emmc_ds = Net('EMMC_DS')
    emmc_data = [Net(f'EMMC_D{i}') for i in range(8)]
    
    k1['EMMC_CLK'] += emmc_clk
    k1['EMMC_CMD'] += emmc_cmd
    k1['EMMC_DS'] += emmc_ds
    for i in range(8):
        k1[f'EMMC_D{i}'] += emmc_data[i]
    
    # ============================================
    # SD Card Interface
    # ============================================
    
    mmc1_clk = Net('MMC1_CLK')
    mmc1_cmd = Net('MMC1_CMD')
    mmc1_data = [Net(f'MMC1_DAT{i}') for i in range(4)]
    
    k1['MMC1_CLK'] += mmc1_clk
    k1['MMC1_CMD'] += mmc1_cmd
    for i in range(4):
        k1[f'MMC1_DAT{i}'] += mmc1_data[i]
    
    # ============================================
    # USB Interfaces
    # ============================================
    
    # USB0
    usb0_dp = Net('USB0_DP')
    usb0_dm = Net('USB0_DN')
    k1['USB0_DP'] += usb0_dp
    k1['USB0_DN'] += usb0_dm
    
    # USB1
    usb1_dp = Net('USB1_DP')
    usb1_dm = Net('USB1_DN')
    k1['USB1_DP'] += usb1_dp
    k1['USB1_DN'] += usb1_dm
    
    # USB2
    usb2_dp = Net('USB2_DP')
    usb2_dm = Net('USB2_DN')
    k1['USB2_DP'] += usb2_dp
    k1['USB2_DN'] += usb2_dm
    
    # ============================================
    # JTAG Debug Interface
    # ============================================
    
    jtag_tck = Net('JTAG_TCK')
    jtag_tdo = Net('JTAG_TDO')
    jtag_tdi = Net('JTAG_TDI')
    jtag_tms = Net('JTAG_TMS')
    jtag_trst = Net('JTAG_TRST_N')
    
    k1['PRI_TCK'] += jtag_tck
    k1['PRI_TDO'] += jtag_tdo
    k1['PRI_TDI'] += jtag_tdi
    k1['PRI_TMS'] += jtag_tms
    k1['PRI_TRST_N'] += jtag_trst
    
    # ============================================
    # PMIC Interface
    # ============================================
    
    pmic_scl = Net('PMIC_SCL')
    pmic_sda = Net('PMIC_SDA')
    pmic_int = Net('PMIC_INT_N')
    
    k1['PWR_SCL'] += pmic_scl
    k1['PWR_SDA'] += pmic_sda
    k1['PMIC_INT_N'] += pmic_int
    
    # ============================================
    # Reset and Control
    # ============================================
    
    reset_in = Net('RESET_IN_N')
    sleep_out = Net('SLEEP_OUT')
    
    k1['RESET_IN_N'] += reset_in
    k1['SLEEP_OUT'] += sleep_out
    
    # ============================================
    # Crystal Oscillator
    # ============================================
    
    xtal_in = Net('XTAL_IN')
    xtal_out = Net('XTAL_OUT')
    clk_32k = Net('CLK_32K')
    
    k1['XI_PAD'] += xtal_in
    k1['XO_PAD'] += xtal_out
    k1['EXT_32K_IN'] += clk_32k
    
    print(f"✓ Example schematic created with K1 SoC")
    print(f"  Total pins in K1: {len(k1.pins)}")
    print(f"  Connected nets: {len(Net.get())}")
    
    return k1

def main():
    """Main function"""
    print("=" * 60)
    print("K1 SoC SKiDL Example")
    print("=" * 60)
    
    # Create schematic
    k1 = create_example_schematic()
    
    # Optionally generate netlist
    # generate_netlist(file_='k1_example.net')
    # print(f"✓ Netlist generated: k1_example.net")
    
    print("\nExample completed successfully!")
    print("\nThis example shows how to:")
    print("  1. Import the K1_SoC component")
    print("  2. Create power distribution networks")
    print("  3. Connect essential interfaces")
    print("  4. Use pin names to access K1 pins")
    print("\nFor a complete design, you would add:")
    print("  - DDR memory chips")
    print("  - Voltage regulators")
    print("  - Decoupling capacitors")
    print("  - Connectors for peripherals")
    print("  - PCIe, HDMI, MIPI CSI/DSI interfaces")
    print("=" * 60)

if __name__ == '__main__':
    main()
