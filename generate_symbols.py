#!/usr/bin/env python3
"""
K1 SoC Symbol Generator
Generates SKiDL component definition and KiCad symbol file from soc_k1_pins.csv
"""

import csv
import re
from collections import defaultdict
from typing import Dict, List, Tuple

class PinInfo:
    def __init__(self, pin_id, name, type_, power_domain, function):
        self.pin_id = pin_id
        self.name = name
        self.type = type_
        self.power_domain = power_domain
        self.function = function
    
    def get_skidl_pin_type(self):
        """Map CSV type to SKiDL pin type"""
        type_map = {
            'G': 'Pin.types.PWRIN',  # Ground
            'P': 'Pin.types.PWRIN',  # Power Input
            'I': 'Pin.types.INPUT',
            'O': 'Pin.types.OUTPUT',
            'I/O': 'Pin.types.BIDIR',
            'AI': 'Pin.types.INPUT',  # Analog Input
            'AO': 'Pin.types.OUTPUT',  # Analog Output
            'AIO': 'Pin.types.PASSIVE',  # Analog Bidirectional
            'RO': 'Pin.types.PASSIVE',  # Passive (like capacitor connections)
        }
        return type_map.get(self.type, 'Pin.types.PASSIVE')
    
    def get_kicad_pin_type(self):
        """Map CSV type to KiCad electrical type"""
        type_map = {
            'G': 'power_in',
            'P': 'power_in',
            'I': 'input',
            'O': 'output',
            'I/O': 'bidirectional',
            'AI': 'input',
            'AO': 'output',
            'AIO': 'passive',
            'RO': 'passive',
        }
        return type_map.get(self.type, 'passive')

def classify_pin(pin: PinInfo) -> str:
    """Classify pin into functional groups"""
    name = pin.name
    func = pin.function.lower()
    
    # DDR/LPDDR Interface
    if any(x in name for x in ['DQ_', 'DQS', 'DMI', 'CA_', 'CK_', 'CS0_', 'CS1_', 'CKE', 'VDDQ', 'VSSQ', 'DDR']):
        return 'DDR_LPDDR'
    
    # GPIO
    if name.startswith('GPIO_'):
        return 'GPIO'
    
    # JTAG
    if any(x in name for x in ['PRI_TCK', 'PRI_TDO', 'PRI_TDI', 'PRI_TMS', 'PRI_TRST', 'JTAG_SEL']):
        return 'JTAG'
    
    # HDMI
    if 'HDMI' in name or 'HDMI' in func:
        return 'HDMI'
    
    # MIPI CSI (Camera)
    if 'MIPI_CSI' in name or 'CSI' in name:
        return 'MIPI_CSI'
    
    # MIPI DSI (Display)
    if 'MIPI_DSI' in name or 'DSI' in name:
        return 'MIPI_DSI'
    
    # PCIe
    if any(x in name for x in ['PCIEC_', 'PCIEB_', 'PCIEA_']):
        if 'PCIEC' in name:
            return 'PCIE_C'
        elif 'PCIEB' in name:
            return 'PCIE_B'
        elif 'PCIEA' in name:
            return 'PCIE_A'
    
    # USB
    if 'USB' in name:
        return 'USB'
    
    # SD/MMC
    if 'MMC1' in name or ('emmc' in func and 'MMC1' not in name):
        if 'MMC1' in name:
            return 'SD_MMC1'
        else:
            return 'EMMC'
    elif 'EMMC' in name:
        return 'EMMC'
    
    # QSPI
    if 'QSPI' in name:
        return 'QSPI'
    
    # Clock and Reference
    if any(x in name for x in ['XI_PAD', 'XO_PAD', 'EXT_32K', 'MPLL', 'BG_OUT']):
        return 'CLOCK_REF'
    
    # Power Management
    if any(x in name for x in ['PMIC', 'PWR_', 'RESET', 'SLEEP', 'DVL']):
        return 'POWER_MGMT'
    
    # Audio
    if 'AUD' in name:
        return 'AUDIO'
    
    # Power
    if name.startswith('VCC') or name.startswith('AVDD'):
        return 'POWER'
    
    # Ground
    if name.startswith('VSS') or name.startswith('AVSS'):
        return 'GROUND'
    
    # NC (Not Connected)
    if name == 'NC':
        return 'NC'
    
    return 'OTHER'

def parse_csv(filename: str) -> List[PinInfo]:
    """Parse the CSV file and return list of PinInfo objects"""
    pins = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Pin ID']:  # Skip empty rows
                pin = PinInfo(
                    row['Pin ID'],
                    row['Name'],
                    row['Type'],
                    row['Power Domain'],
                    row['Function']
                )
                pins.append(pin)
    return pins

def group_pins_by_category(pins: List[PinInfo]) -> Dict[str, List[PinInfo]]:
    """Group pins by their functional category"""
    groups = defaultdict(list)
    for pin in pins:
        category = classify_pin(pin)
        groups[category].append(pin)
    return dict(groups)

def generate_skidl_symbol(pins: List[PinInfo], output_file: str):
    """Generate SKiDL Python component definition"""
    
    groups = group_pins_by_category(pins)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('''"""
K1 SoC SKiDL Symbol Definition
Auto-generated from soc_k1_pins.csv

Usage:
    from k1_soc_symbol import K1_SoC
    
    # Create an instance
    k1 = K1_SoC()
    
    # Access pins by name
    k1['GPIO_00'] += net_gpio_00
    k1['VCC_M1'] += vcc_0v9
"""

from skidl import Pin, Part, SKIDL, TEMPLATE

def K1_SoC():
    """
    K1 SoC Component Definition
    676-pin BGA package
    
    Functional Groups:
    - DDR/LPDDR Interface: LPDDR4X/LPDDR3 memory interface
    - GPIO: General Purpose I/O (GPIO_00 to GPIO_127)
    - JTAG: Debug interface
    - HDMI: Video output
    - MIPI CSI: Camera serial interface
    - MIPI DSI: Display serial interface
    - PCIe: PCI Express interfaces (A, B, C)
    - USB: USB 2.0 interfaces
    - SD/eMMC: Storage interfaces
    - QSPI: Quad SPI flash interface
    - Clock/Reference: Crystal oscillator and reference signals
    - Power Management: PMIC interface, reset, sleep control
    - Audio: Audio codec interface
    - Power/Ground: Power supply and ground pins
    """
    
    k1_soc = Part(
        'K1_SoC',
        'K1_SoC',
        dest=TEMPLATE,
        footprint='BGA-676'
    )
    
''')
        
        # Generate pins by category
        category_order = [
            'DDR_LPDDR',
            'GPIO',
            'JTAG',
            'HDMI',
            'MIPI_CSI',
            'MIPI_DSI',
            'PCIE_A',
            'PCIE_B',
            'PCIE_C',
            'USB',
            'SD_MMC1',
            'EMMC',
            'QSPI',
            'CLOCK_REF',
            'POWER_MGMT',
            'AUDIO',
            'POWER',
            'GROUND',
            'NC',
            'OTHER'
        ]
        
        for category in category_order:
            if category not in groups:
                continue
            
            pins_in_cat = sorted(groups[category], key=lambda p: p.pin_id)
            
            # Write category header
            category_names = {
                'DDR_LPDDR': 'DDR/LPDDR Memory Interface',
                'GPIO': 'General Purpose I/O',
                'JTAG': 'JTAG Debug Interface',
                'HDMI': 'HDMI Video Output',
                'MIPI_CSI': 'MIPI CSI Camera Interface',
                'MIPI_DSI': 'MIPI DSI Display Interface',
                'PCIE_A': 'PCIe Interface A',
                'PCIE_B': 'PCIe Interface B',
                'PCIE_C': 'PCIe Interface C',
                'USB': 'USB 2.0 Interfaces',
                'SD_MMC1': 'SD Card Interface (MMC1)',
                'EMMC': 'eMMC Storage Interface',
                'QSPI': 'QSPI Flash Interface',
                'CLOCK_REF': 'Clock and Reference Signals',
                'POWER_MGMT': 'Power Management and Control',
                'AUDIO': 'Audio Interface',
                'POWER': 'Power Supply Pins',
                'GROUND': 'Ground Pins',
                'NC': 'Not Connected',
                'OTHER': 'Other Signals'
            }
            
            f.write(f"    # {category_names.get(category, category)}\n")
            
            for pin in pins_in_cat:
                pin_type = pin.get_skidl_pin_type()
                f.write(f"    Pin(name='{pin.name}', num='{pin.pin_id}', func={pin_type})\n")
            
            f.write("\n")
        
        f.write("    return k1_soc\n")
        f.write("\n\nif __name__ == '__main__':\n")
        f.write("    # Example usage\n")
        f.write("    k1 = K1_SoC()\n")
        f.write("    print(f'K1 SoC component created with {len(k1)} pins')\n")

def generate_kicad_symbol(pins: List[PinInfo], output_file: str):
    """Generate KiCad symbol file (.kicad_sym)"""
    
    groups = group_pins_by_category(pins)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # KiCad symbol file header
        f.write('(kicad_symbol_lib (version 20211014) (generator kicad_symbol_editor)\n')
        f.write('  (symbol "K1_SoC" (in_bom yes) (on_board yes)\n')
        f.write('    (property "Reference" "U" (id 0) (at 0 5.08 0)\n')
        f.write('      (effects (font (size 1.27 1.27)))\n')
        f.write('    )\n')
        f.write('    (property "Value" "K1_SoC" (id 1) (at 0 2.54 0)\n')
        f.write('      (effects (font (size 1.27 1.27)))\n')
        f.write('    )\n')
        f.write('    (property "Footprint" "BGA-676" (id 2) (at 0 0 0)\n')
        f.write('      (effects (font (size 1.27 1.27)) hide)\n')
        f.write('    )\n')
        f.write('    (property "Datasheet" "" (id 3) (at 0 0 0)\n')
        f.write('      (effects (font (size 1.27 1.27)) hide)\n')
        f.write('    )\n')
        f.write('    (property "ki_description" "K1 SoC - 676-pin BGA" (id 4) (at 0 0 0)\n')
        f.write('      (effects (font (size 1.27 1.27)) hide)\n')
        f.write('    )\n')
        f.write('    (symbol "K1_SoC_0_1"\n')
        f.write('      (rectangle (start -50.8 177.8) (end 50.8 -177.8)\n')
        f.write('        (stroke (width 0.254) (type default) (color 0 0 0 0))\n')
        f.write('        (fill (type background))\n')
        f.write('      )\n')
        f.write('    )\n')
        
        # Generate pin definitions organized by unit/group
        # We'll create multiple units for better organization
        unit_mapping = {
            'DDR_LPDDR': 1,
            'GPIO': 2,
            'JTAG': 3,
            'HDMI': 4,
            'MIPI_CSI': 5,
            'MIPI_DSI': 6,
            'PCIE_A': 7,
            'PCIE_B': 8,
            'PCIE_C': 9,
            'USB': 10,
            'SD_MMC1': 11,
            'EMMC': 12,
            'QSPI': 13,
            'CLOCK_REF': 14,
            'POWER_MGMT': 15,
            'AUDIO': 16,
            'POWER': 17,
            'GROUND': 18,
            'NC': 19,
            'OTHER': 20
        }
        
        # For simplicity, we'll put all pins in one unit (unit 1)
        # But organize them spatially by category
        pin_y_offset = 175.0
        pin_spacing = 2.54
        
        category_order = [
            'JTAG', 'CLOCK_REF', 'POWER_MGMT',  # Top
            'GPIO',  # Left side
            'DDR_LPDDR',  # Right side
            'USB', 'MIPI_CSI', 'MIPI_DSI',  # Bottom left
            'PCIE_A', 'PCIE_B', 'PCIE_C',  # Bottom middle
            'HDMI', 'SD_MMC1', 'EMMC', 'QSPI', 'AUDIO',  # Bottom right
            'POWER', 'GROUND', 'NC', 'OTHER'  # Bottom
        ]
        
        f.write('    (symbol "K1_SoC_1_1"\n')
        
        current_y = pin_y_offset
        for category in category_order:
            if category not in groups:
                continue
            
            pins_in_cat = sorted(groups[category], key=lambda p: p.pin_id)
            
            # Determine pin orientation based on category
            if category in ['GPIO', 'MIPI_CSI', 'USB']:
                # Left side pins
                x_pos = -53.34
                orientation = 'R'  # Right (into symbol)
                justify = 'left'
            elif category in ['DDR_LPDDR', 'PCIE_A', 'PCIE_B', 'PCIE_C']:
                # Right side pins
                x_pos = 53.34
                orientation = 'L'  # Left (into symbol)
                justify = 'right'
            elif category in ['POWER', 'GROUND']:
                # Bottom pins
                x_pos = 53.34
                orientation = 'L'
                justify = 'right'
            else:
                # Top/other pins
                x_pos = -53.34
                orientation = 'R'
                justify = 'left'
            
            for pin in pins_in_cat:
                pin_type = pin.get_kicad_pin_type()
                shape = 'line'  # default
                
                if pin.type == 'G':
                    shape = 'line'
                elif pin.type == 'P':
                    shape = 'line'
                
                f.write(f'      (pin {pin_type} {shape} (at {x_pos} {current_y:.2f} {orientation}) (length 2.54)\n')
                f.write(f'        (name "{pin.name}" (effects (font (size 1.27 1.27))))\n')
                f.write(f'        (number "{pin.pin_id}" (effects (font (size 1.27 1.27))))\n')
                f.write(f'      )\n')
                
                current_y -= pin_spacing
                
                # Reset position if we've gone too far
                if current_y < -175.0:
                    current_y = pin_y_offset
        
        f.write('    )\n')
        f.write('  )\n')
        f.write(')\n')

def generate_classification_report(pins: List[PinInfo], output_file: str):
    """Generate a classification report"""
    
    groups = group_pins_by_category(pins)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("K1 SoC Pin Classification Report\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total Pins: {len(pins)}\n\n")
        
        category_names = {
            'DDR_LPDDR': 'DDR/LPDDR Memory Interface',
            'GPIO': 'General Purpose I/O',
            'JTAG': 'JTAG Debug Interface',
            'HDMI': 'HDMI Video Output',
            'MIPI_CSI': 'MIPI CSI Camera Interface',
            'MIPI_DSI': 'MIPI DSI Display Interface',
            'PCIE_A': 'PCIe Interface A',
            'PCIE_B': 'PCIe Interface B',
            'PCIE_C': 'PCIe Interface C',
            'USB': 'USB 2.0 Interfaces',
            'SD_MMC1': 'SD Card Interface (MMC1)',
            'EMMC': 'eMMC Storage Interface',
            'QSPI': 'QSPI Flash Interface',
            'CLOCK_REF': 'Clock and Reference Signals',
            'POWER_MGMT': 'Power Management and Control',
            'AUDIO': 'Audio Interface',
            'POWER': 'Power Supply Pins',
            'GROUND': 'Ground Pins',
            'NC': 'Not Connected',
            'OTHER': 'Other Signals'
        }
        
        # Summary table
        f.write("Pin Count by Category:\n")
        f.write("-" * 80 + "\n")
        for category in sorted(groups.keys(), key=lambda c: -len(groups[c])):
            count = len(groups[category])
            cat_name = category_names.get(category, category)
            f.write(f"{cat_name:40s}: {count:4d} pins\n")
        
        f.write("\n" + "=" * 80 + "\n\n")
        
        # Detailed listing
        for category in sorted(groups.keys()):
            cat_name = category_names.get(category, category)
            pins_in_cat = sorted(groups[category], key=lambda p: p.pin_id)
            
            f.write(f"\n{cat_name}\n")
            f.write("-" * 80 + "\n")
            f.write(f"{'Pin ID':<8s} {'Name':<20s} {'Type':<6s} {'Power Domain':<25s} {'Function':<30s}\n")
            f.write("-" * 80 + "\n")
            
            for pin in pins_in_cat:
                f.write(f"{pin.pin_id:<8s} {pin.name:<20s} {pin.type:<6s} "
                       f"{pin.power_domain:<25s} {pin.function[:30]:<30s}\n")
            
            f.write("\n")

def main():
    """Main function"""
    print("K1 SoC Symbol Generator")
    print("=" * 60)
    
    # Parse CSV
    print("Reading soc_k1_pins.csv...")
    pins = parse_csv('soc_k1_pins.csv')
    print(f"Loaded {len(pins)} pins")
    
    # Generate SKiDL symbol
    print("\nGenerating SKiDL symbol (k1_soc_symbol.py)...")
    generate_skidl_symbol(pins, 'k1_soc_symbol.py')
    print("✓ Generated k1_soc_symbol.py")
    
    # Generate KiCad symbol
    print("\nGenerating KiCad symbol (k1_soc.kicad_sym)...")
    generate_kicad_symbol(pins, 'k1_soc.kicad_sym')
    print("✓ Generated k1_soc.kicad_sym")
    
    # Generate classification report
    print("\nGenerating classification report (pin_classification.txt)...")
    generate_classification_report(pins, 'pin_classification.txt')
    print("✓ Generated pin_classification.txt")
    
    # Verification
    print("\n" + "=" * 60)
    print("Verification:")
    groups = group_pins_by_category(pins)
    total_classified = sum(len(group) for group in groups.values())
    print(f"  Total pins: {len(pins)}")
    print(f"  Classified: {total_classified}")
    print(f"  Categories: {len(groups)}")
    
    if total_classified == len(pins):
        print("\n✓ All pins successfully classified!")
    else:
        print(f"\n⚠ Warning: {len(pins) - total_classified} pins not classified")
    
    print("\n" + "=" * 60)
    print("Generation complete!")
    print("\nGenerated files:")
    print("  - k1_soc_symbol.py      : SKiDL component definition")
    print("  - k1_soc.kicad_sym      : KiCad symbol library")
    print("  - pin_classification.txt: Detailed pin classification report")
    print("\nUsage:")
    print("  SKiDL: from k1_soc_symbol import K1_SoC")
    print("  KiCad: Add k1_soc.kicad_sym to your symbol libraries")

if __name__ == '__main__':
    main()
