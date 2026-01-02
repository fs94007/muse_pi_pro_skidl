#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
K1 SoC SKiDL Component Definition

This module provides a SKiDL component definition for the K1 SoC
with all pins categorized by function.
"""

from skidl import *

class K1_SoC(Component):
    """
    K1 SoC Component with all pins organized by functional groups.

    This component provides access to all 678 pins of the K1 SoC,
    categorized into functional groups for easier schematic design.
    """

    def __init__(self, **kwargs):
        super().__init__('K1_SoC', **kwargs)

        # Add pins organized by functional groups
        self._add_pins_by_category()

    def _add_pins_by_category(self):
        """Add pins organized by functional categories"""

        # 电源和地
        self += Pin(num='A1', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='A26', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='AA11', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AA12', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AA17', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AA18', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AA26', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AA3', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AA4', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AA5', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AA6', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AB10', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AB11', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AB12', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AB19', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AB20', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AB24', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AB3', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AC16', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AC19', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AC25', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AD16', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AD3', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AD4', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AD5', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AD6', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AD7', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AE1', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AE13', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AE24', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AE26', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AE3', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AF1', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AF10', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AF15', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AF2', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AF20', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AF25', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AF26', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='AF5', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='B1', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='B26', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='C23', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='D22', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='D25', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='E4', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='E6', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='F1', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='F2', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='F7', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='G25', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='G26', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='G3', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='G6', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='G7', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='G8', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='G9', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='H10', name='VSSU_DDR', func=PinTypes.GND, \
                     desc='system DDR Ground')
        self += Pin(num='H11', name='VSSU_DDR', func=PinTypes.GND, \
                     desc='system DDR Ground')
        self += Pin(num='H16', name='VSSU_DDR', func=PinTypes.GND, \
                     desc='System DDR Ground')
        self += Pin(num='H17', name='VSSU_DDR', func=PinTypes.GND, \
                     desc='System DDR Ground')
        self += Pin(num='H3', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='H9', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='J10', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='J16', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='J17', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='K10', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='K15', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='K16', name='VSS', func=PinTypes.GND, \
                     desc='Digital core Ground')
        self += Pin(num='K17', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='K9', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='L10', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='L14', name='VSSU_PLL', func=PinTypes.GND, \
                     desc='System PLL Ground')
        self += Pin(num='L15', name='VSS', func=PinTypes.GND, \
                     desc='Digital core Ground')
        self += Pin(num='L16', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='M10', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='M12', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='M13', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='M14', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='M15', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='M16', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='M3', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='M4', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='N10', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='N11', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='N12', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='N13', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='N14', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='N15', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='N16', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='N21', name='NC', func=PinTypes.POWER_IN, \
                     desc='NC')
        self += Pin(num='N22', name='NC', func=PinTypes.POWER_IN, \
                     desc='NC')
        self += Pin(num='N23', name='NC', func=PinTypes.ANALOG_OUT, \
                     desc='NC')
        self += Pin(num='N24', name='NC', func=PinTypes.ANALOG_OUT, \
                     desc='NC')
        self += Pin(num='N25', name='NC', func=PinTypes.ANALOG_OUT, \
                     desc='NC')
        self += Pin(num='N26', name='NC', func=PinTypes.ANALOG_OUT, \
                     desc='NC')
        self += Pin(num='P10', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='P11', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='P12', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='P13', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='P14', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='P15', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='P16', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='P20', name='NC', func=PinTypes.ANALOG_OUT, \
                     desc='NC')
        self += Pin(num='P21', name='NC', func=PinTypes.ANALOG_OUT, \
                     desc='NC')
        self += Pin(num='P22', name='NC', func=PinTypes.ANALOG_OUT, \
                     desc='NC')
        self += Pin(num='P23', name='NC', func=PinTypes.ANALOG_IN, \
                     desc='NC')
        self += Pin(num='P24', name='NC', func=PinTypes.ANALOG_IN, \
                     desc='NC')
        self += Pin(num='P25', name='NC', func=PinTypes.ANALOG_IN, \
                     desc='NC')
        self += Pin(num='P26', name='NC', func=PinTypes.ANALOG_IN, \
                     desc='NC')
        self += Pin(num='R10', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='R11', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='R12', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='R13', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='R14', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='R15', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='R16', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='R20', name='NC', func=PinTypes.ANALOG_OUT, \
                     desc='NC')
        self += Pin(num='R22', name='NC', func=PinTypes.ANALOG_IN, \
                     desc='NC')
        self += Pin(num='R23', name='NC', func=PinTypes.ANALOG_IN, \
                     desc='NC')
        self += Pin(num='R24', name='VSS', func=PinTypes.GND, \
                     desc='Digital core ground')
        self += Pin(num='R25', name='NC', func=PinTypes.ANALOG_IN, \
                     desc='NC')
        self += Pin(num='R26', name='NC', func=PinTypes.ANALOG_IN, \
                     desc='NC')
        self += Pin(num='R3', name='VSS', func=PinTypes.GND, \
                     desc='Digital core Ground')
        self += Pin(num='R8', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='R9', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core Ground')
        self += Pin(num='T10', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='T11', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='T12', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='T13', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='T14', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='T15', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='T16', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='T17', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='T18', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='T19', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='T20', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='T23', name='NC', func=PinTypes.ANALOG_IN, \
                     desc='NC')
        self += Pin(num='T24', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='T25', name='NC', func=PinTypes.ANALOG_OUT, \
                     desc='NC')
        self += Pin(num='T26', name='VSS', func=PinTypes.GND, \
                     desc='Digital core ground')
        self += Pin(num='T3', name='VSS', func=PinTypes.GND, \
                     desc='Digital core ground')
        self += Pin(num='T6', name='VSS', func=PinTypes.GND, \
                     desc='Digital core ground')
        self += Pin(num='T9', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='U10', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='U11', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='U12', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='U13', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='U14', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='U15', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='U16', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='U17', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='U18', name='VCC_M1_FB', func=PinTypes.POWER_IN, \
                     desc='Digital Core power FeedBack')
        self += Pin(num='U19', name='VSS_FB', func=PinTypes.GND, \
                     desc='Digital Core ground FeedBack')
        self += Pin(num='U20', name='VSS', func=PinTypes.GND, \
                     desc='Digital core ground')
        self += Pin(num='U23', name='NC', func=PinTypes.ANALOG_IN, \
                     desc='NC')
        self += Pin(num='U24', name='NC', func=PinTypes.ANALOG_OUT, \
                     desc='NC')
        self += Pin(num='U6', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='U8', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='U9', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='V10', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='V11', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='V12', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='V13', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='V14', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='V15', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='V16', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='V17', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='V18', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='V19', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='V20', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='V22', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='V25', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='V7', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='V8', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='V9', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='W1', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='W10', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='W11', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='W12', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='W14', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='W15', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='W16', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='W17', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='W18', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='W19', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='W2', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='W20', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='W24', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='W3', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='W6', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='W7', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='W8', name='VCC_M1', func=PinTypes.POWER_IN, \
                     desc='Digital Core power')
        self += Pin(num='W9', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='Y11', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='Y12', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='Y13', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='Y16', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='Y17', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='Y18', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='Y19', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='Y20', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='Y24', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='Y3', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')
        self += Pin(num='Y6', name='VSS', func=PinTypes.GND, \
                     desc='Digital Core ground')

        # DDR/LPDDR接口
        self += Pin(num='A10', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='A11', name='DQ_B_9', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ9; LPDDR3: DQ8')
        self += Pin(num='A12', name='DQ_B_12', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ12; LPDDR3: DQ10')
        self += Pin(num='A13', name='DQ_B_11', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ11; LPDDR3: DQ11')
        self += Pin(num='A14', name='DQS1_C_B', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Negative of CHB DQS1; LPDDR3: Negtive of DQS1')
        self += Pin(num='A15', name='DQS1_C_A', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Negative of CHA DQS1; LPDDR3: Negtive of DQS0')
        self += Pin(num='A16', name='DQ_A_12', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ12; LPDDR3: DQM0')
        self += Pin(num='A17', name='DQ_A_9', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ9; LPDDR3: DQ7')
        self += Pin(num='A18', name='DQ_A_8', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ8; LPDDR3: DQ5')
        self += Pin(num='A19', name='DQ_A_15', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ15; LPDDR3: DQ3')
        self += Pin(num='A2', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='A20', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='A21', name='DQ_A_5', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ5; LPDDR3: DQ21')
        self += Pin(num='A22', name='DQ_A_7', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ7; LPDDR3: DQ17')
        self += Pin(num='A23', name='DMI0_A', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Channel A DM0; LPDDR3: DQ22')
        self += Pin(num='A24', name='DQ_A_1', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ1; LPDDR3: DQ16')
        self += Pin(num='A25', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='A3', name='DQ_B_2', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ2; LPDDR3: DQ28')
        self += Pin(num='A4', name='DMI0_B', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Channel B DM0; LPDDR3: DQ25')
        self += Pin(num='A5', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='A6', name='DQ_B_6', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ6; LPDDR3: DQ24')
        self += Pin(num='A7', name='DQ_B_4', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ4; LPDDR3: DQ30')
        self += Pin(num='A8', name='DQ_B_13', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ13; LPDDR3: DQ15')
        self += Pin(num='A9', name='DQ_B_15', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ15; LPDDR3: DQ12')
        self += Pin(num='AA7', name='AVSS_HDMI', func=PinTypes.GND, \
                     desc='HDMI Ground')
        self += Pin(num='AB6', name='AVSS_HDMI', func=PinTypes.GND, \
                     desc='HDMI Ground')
        self += Pin(num='AB9', name='AVSS_HDMI', func=PinTypes.GND, \
                     desc='HDMI Ground')
        self += Pin(num='AC6', name='AVSS_HDMI', func=PinTypes.GND, \
                     desc='HDMI Ground')
        self += Pin(num='AC8', name='AVSS_HDMI', func=PinTypes.GND, \
                     desc='HDMI Ground')
        self += Pin(num='AC9', name='AVSS_HDMI', func=PinTypes.GND, \
                     desc='HDMI Ground')
        self += Pin(num='B10', name='DMI1_B', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Channel B DM1; LPDDR3: DQ14')
        self += Pin(num='B11', name='DQ_B_8', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ12; LPDDR3: DQM1')
        self += Pin(num='B12', name='DQ_B_10', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ10; LPDDR3: DQ9')
        self += Pin(num='B13', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='B14', name='DQS1_T_B', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Positive of CHB DQS1; LPDDR3: Positive of DQS1')
        self += Pin(num='B15', name='DQS1_T_A', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Positive of CHA DQS1; LPDDR3: Positive of DQS0')
        self += Pin(num='B16', name='DQ_A_11', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ11; LPDDR3: DQ4')
        self += Pin(num='B17', name='DQ_A_10', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ10; LPDDR3: DQ6')
        self += Pin(num='B18', name='DMI1_A', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Channel A DM1; LPDDR3: DQ2')
        self += Pin(num='B19', name='DQ_A_14', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ14; LPDDR3: DQ1')
        self += Pin(num='B2', name='DQ_B_3', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ3; LPDDR3: DQM3')
        self += Pin(num='B20', name='DQ_A_13', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ13; LPDDR3: DQ0')
        self += Pin(num='B21', name='DQ_A_4', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ4; LPDDR3: DQ18')
        self += Pin(num='B22', name='DQ_A_6', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ6; LPDDR3: DQ23')
        self += Pin(num='B23', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='B24', name='DQ_A_2', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ2; LPDDR3: DQ19')
        self += Pin(num='B25', name='DQ_A_3', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ3; LPDDR3: DQM2')
        self += Pin(num='B3', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='B4', name='DQ_B_1', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ1; LPDDR3: DQ27')
        self += Pin(num='B5', name='DQ_B_0', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ0; LPDDR3: DQ31')
        self += Pin(num='B6', name='DQ_B_7', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ7; LPDDR3: DQ29')
        self += Pin(num='B7', name='DQ_B_5', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ5; LPDDR3: DQ26')
        self += Pin(num='B8', name='VDDQ_V1P2', func=PinTypes.POWER_IN, \
                     desc='LPDDR3 IO power')
        self += Pin(num='B9', name='DQ_B_14', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHB DQ14; LPDDR3: DQ13')
        self += Pin(num='C10', name='CKE0_B', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: clock enabling 0 of CHB; LPDDR3: N/A')
        self += Pin(num='C11', name='CKE1_B', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: clock enabling 1 of CHB; LPDDR3: N/A')
        self += Pin(num='C12', name='VDDQ_V1P2', func=PinTypes.POWER_IN, \
                     desc='LPDDR3 IO power')
        self += Pin(num='C13', name='CA_B_5', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHB CA5; LPDDR3: CA8')
        self += Pin(num='C14', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='C15', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='C16', name='CA_A_4', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHA CA4; LPDDR3: CA3')
        self += Pin(num='C17', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='C18', name='CKE1_A', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: clock enabling 1 of CHA; LPDDR3: clock enabling 1')
        self += Pin(num='C19', name='CA_A_1', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHA CA1; LPDDR3: CA2')
        self += Pin(num='C20', name='CS1_A', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: Active-low chip select 1 of CHA; LPDDR3: Active-low chip select 1')
        self += Pin(num='C21', name='AVDD06_DDR', func=PinTypes.POWER_IN, \
                     desc='LPDDR4X IO power')
        self += Pin(num='C22', name='DQ_A_0', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: CHA DQ0; LPDDR3: DQ20')
        self += Pin(num='C6', name='DQS0_T_B', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Positive of CHB DQS0; LPDDR3: Positive of DQS3')
        self += Pin(num='C7', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='C8', name='CS1_B', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: Active-low chip select 1 of CHB; LPDDR3: N/A')
        self += Pin(num='C9', name='CA_B_1', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHB CA1; LPDDR3: CA5')
        self += Pin(num='D10', name='DDR_lp4x_SEL', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: connect to 1.8V; LP234: connect to Ground')
        self += Pin(num='D11', name='CK_C_B', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: negative LPDDR differential clock of CHB; LPDDR3: negative LPDDR differential clock')
        self += Pin(num='D12', name='CA_B_2', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHB CA2; LPDDR3: CA9')
        self += Pin(num='D13', name='CA_B_4', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHA CA4; LPDDR3: CA7')
        self += Pin(num='D14', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='D15', name='AVDD06_DDR', func=PinTypes.POWER_IN, \
                     desc='LPDDR4X IO power')
        self += Pin(num='D16', name='CA_A_2', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHA CA2')
        self += Pin(num='D17', name='CK_C_A', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: negative LPDDR differential clock of CHA; LPDDR3: N/A')
        self += Pin(num='D18', name='CKE0_A', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: clock enabling 0 of CHA; LPDDR3: clock enabling 0')
        self += Pin(num='D19', name='CA_A_0', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHA CA0; LPDDR3: CA4')
        self += Pin(num='D20', name='DQS0_T_A', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Positive of CHA DQS0; LPDDR3: Positive of DQS2')
        self += Pin(num='D21', name='DQS0_C_A', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Negative of CHA DQS0; LPDDR3: Negative of DQS2')
        self += Pin(num='D6', name='DQS0_C_B', func=PinTypes.PASSIVE, \
                     desc='LPDDR4X: Negative of CHB DQS0; LPDDR3: Negtive of DQS3')
        self += Pin(num='D7', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='D8', name='CA_B_0', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHB CA0')
        self += Pin(num='D9', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='E10', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='E11', name='CK_T_B', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: positive LPDDR differential clock of CHB; LPDDR3: positive LPDDR differential clock')
        self += Pin(num='E12', name='CA_B_3', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHB CA3; LPDDR3: CA6')
        self += Pin(num='E13', name='AVSS18_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='E14', name='AVDD18_DDR', func=PinTypes.POWER_IN, \
                     desc='LPDDR PHY PLL 1.8V power')
        self += Pin(num='E15', name='CA_A_5', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHA CA5; LPDDR3: CA1')
        self += Pin(num='E16', name='CS0_A', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: Active-low chip select 0 of CHA; LPDDR3: Active-low chip select 0')
        self += Pin(num='E17', name='CK_T_A', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: positive LPDDR differential clock of CHA; LPDDR3: N/A')
        self += Pin(num='E18', name='AVDD06_DDR', func=PinTypes.POWER_IN, \
                     desc='LPDDR4X IO power')
        self += Pin(num='E19', name='AVDD06_DDR', func=PinTypes.POWER_IN, \
                     desc='LPDDR4X IO power')
        self += Pin(num='E20', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='E21', name='AVSS_EMMC', func=PinTypes.GND, \
                     desc='eMMC Ground')
        self += Pin(num='E23', name='AVSS_EMMC', func=PinTypes.GND, \
                     desc='eMMC Ground')
        self += Pin(num='E7', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='E8', name='VDDQ_V1P2', func=PinTypes.POWER_IN, \
                     desc='LPDDR3 IO power')
        self += Pin(num='E9', name='DDR_LP23_VREFDQ', func=PinTypes.POWER_IN, \
                     desc='DQ VREF for lpddr23 , LP4/4x; Keep the pin NC')
        self += Pin(num='F10', name='VDDQ_V1P2', func=PinTypes.POWER_IN, \
                     desc='LPDDR3 IO power')
        self += Pin(num='F11', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='F12', name='CS0_B', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: clock enabling 1 of CHB; LPDDR3: N/A')
        self += Pin(num='F13', name='DDR_RESET_N', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR SDRAM reset')
        self += Pin(num='F14', name='ZQ_DDR_PHY', func=PinTypes.PASSIVE, \
                     desc='DDR ZQ calibration')
        self += Pin(num='F15', name='CA_A_3', func=PinTypes.ANALOG_OUT, \
                     desc='LPDDR4X: CHA CA3; LPDDR3: CA0')
        self += Pin(num='F16', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='F17', name='DDR_LDO_CAP', func=PinTypes.NC, \
                     desc='External LDO output ball;; Connect to a 100nF capacitor on PCB board')
        self += Pin(num='F18', name='AVDD06_DDR', func=PinTypes.POWER_IN, \
                     desc='LPDDR4X IO power')
        self += Pin(num='F19', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='F20', name='AVSS_EMMC', func=PinTypes.GND, \
                     desc='eMMC Ground')
        self += Pin(num='F21', name='AVSS_EMMC', func=PinTypes.GND, \
                     desc='eMMC Ground')
        self += Pin(num='F22', name='AVSS_EMMC', func=PinTypes.GND, \
                     desc='eMMC Ground')
        self += Pin(num='F8', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='F9', name='VDDQ_V1P2', func=PinTypes.POWER_IN, \
                     desc='LPDDR3 IO power')
        self += Pin(num='G10', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='G11', name='VDDQ_V1P2', func=PinTypes.POWER_IN, \
                     desc='LPDDR3 IO power')
        self += Pin(num='G12', name='AVDD11_DDR', func=PinTypes.POWER_IN, \
                     desc='LPDDR PHY power supply')
        self += Pin(num='G13', name='VDDQ_V1P2', func=PinTypes.POWER_IN, \
                     desc='LPDDR3 IO power')
        self += Pin(num='G14', name='DDR_LP23_VREFCA', func=PinTypes.POWER_IN, \
                     desc='CA VREF for lpddr23, LP4/4x; Keep the pin NC')
        self += Pin(num='G15', name='AVDD11_DDR', func=PinTypes.POWER_IN, \
                     desc='LPDDR PHY power supply')
        self += Pin(num='G16', name='AVDD06_DDR', func=PinTypes.POWER_IN, \
                     desc='LPDDR4X IO power')
        self += Pin(num='G17', name='VSSQ_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='G19', name='AVSS_EMMC', func=PinTypes.GND, \
                     desc='eMMC Ground')
        self += Pin(num='G20', name='AVSS_EMMC', func=PinTypes.GND, \
                     desc='eMMC Ground')
        self += Pin(num='G21', name='AVSS_EMMC', func=PinTypes.GND, \
                     desc='eMMC Ground')
        self += Pin(num='H12', name='AVDD18_PHY', func=PinTypes.POWER_IN, \
                     desc='Analog 1.8V power')
        self += Pin(num='H13', name='AVDDU_DDR', func=PinTypes.POWER_IN, \
                     desc='LPDDR PHY PLL logical power')
        self += Pin(num='H14', name='AVSSU_DDR', func=PinTypes.GND, \
                     desc='DDR Ground')
        self += Pin(num='H15', name='AVDD18_PHY', func=PinTypes.POWER_IN, \
                     desc='Analog 1.8V power')
        self += Pin(num='H20', name='AVDD09_EMMC', func=PinTypes.POWER_IN, \
                     desc='eMMC digtial power')
        self += Pin(num='H24', name='AVSS_PCIEC', func=PinTypes.GND, \
                     desc='PCIEC Ground')
        self += Pin(num='H6', name='AVSS18_AFEAP', func=PinTypes.GND, \
                     desc='DCXO Ground')
        self += Pin(num='H8', name='AVSS18_AFEAP', func=PinTypes.GND, \
                     desc='DCXO Ground')
        self += Pin(num='J20', name='AVDD09_EMMC', func=PinTypes.POWER_IN, \
                     desc='eMMC digtial power')
        self += Pin(num='J21', name='AVSS_PCIEC', func=PinTypes.GND, \
                     desc='PCIEC Ground')
        self += Pin(num='J24', name='AVSS_PCIEC', func=PinTypes.GND, \
                     desc='PCIEC Ground')
        self += Pin(num='J3', name='AVSS_CSI', func=PinTypes.GND, \
                     desc='MIPI_CSI Ground')
        self += Pin(num='J6', name='AVSS_CSI', func=PinTypes.GND, \
                     desc='MIPI_CSI Ground')
        self += Pin(num='J8', name='AVSS18_AFEAP', func=PinTypes.GND, \
                     desc='DCXO Ground')
        self += Pin(num='J9', name='AVSS18_AFEAP', func=PinTypes.GND, \
                     desc='DCXO Ground')
        self += Pin(num='K20', name='AVDD09_PCIEC', func=PinTypes.POWER_IN, \
                     desc='PCIEC digital power')
        self += Pin(num='K21', name='AVSS_PCIEC', func=PinTypes.GND, \
                     desc='PCIEC Ground')
        self += Pin(num='K24', name='AVSS_PCIEC', func=PinTypes.GND, \
                     desc='PCIEC Ground')
        self += Pin(num='K3', name='AVSS_CSI', func=PinTypes.GND, \
                     desc='MIPI_CSI Ground')
        self += Pin(num='K7', name='AVDD09_CSI', func=PinTypes.POWER_IN, \
                     desc='MIPI_CSI digtial power')
        self += Pin(num='K8', name='AVSS_CSI', func=PinTypes.GND, \
                     desc='MIPI_CSI Ground')
        self += Pin(num='L11', name='AVDD09_AFEAP', func=PinTypes.POWER_IN, \
                     desc='0.9V power for DCXO')
        self += Pin(num='L13', name='AVSS_PLL', func=PinTypes.GND, \
                     desc='Analog Core Ground')
        self += Pin(num='L20', name='AVDD09_PCIEB', func=PinTypes.POWER_IN, \
                     desc='PCIEB digital power')
        self += Pin(num='L21', name='AVDD09_PCIEB', func=PinTypes.POWER_IN, \
                     desc='PCIEB digital power')
        self += Pin(num='L24', name='AVSS_PCIEB', func=PinTypes.GND, \
                     desc='PCIEB Ground')
        self += Pin(num='L3', name='AVSS_CSI', func=PinTypes.GND, \
                     desc='MIPI_CSI Ground')
        self += Pin(num='L7', name='AVDD09_CSI', func=PinTypes.POWER_IN, \
                     desc='MIPI_CSI digtial power')
        self += Pin(num='L8', name='AVSS_CSI', func=PinTypes.GND, \
                     desc='MIPI_CSI Ground')
        self += Pin(num='L9', name='AVSS_CSI', func=PinTypes.GND, \
                     desc='MIPI_CSI Ground')
        self += Pin(num='M11', name='AVDD09_PLL', func=PinTypes.POWER_IN, \
                     desc='System PLL power supply')
        self += Pin(num='M20', name='AVSS_PCIEB', func=PinTypes.GND, \
                     desc='PCIEB Ground')
        self += Pin(num='M21', name='AVSS_PCIEB', func=PinTypes.GND, \
                     desc='PCIEB Ground')
        self += Pin(num='M24', name='AVSS_PCIEB', func=PinTypes.GND, \
                     desc='PCIEB Ground')
        self += Pin(num='M7', name='AVDD09_USB', func=PinTypes.POWER_IN, \
                     desc='USB2.0 digital power')
        self += Pin(num='N17', name='AVSS18_AUD', func=PinTypes.GND, \
                     desc='Audio Ground')
        self += Pin(num='N19', name='AVSS18_AUD', func=PinTypes.GND, \
                     desc='Audio Ground')
        self += Pin(num='N20', name='AVSS18_AUD', func=PinTypes.GND, \
                     desc='Audio Ground')
        self += Pin(num='N3', name='AVSS_USB', func=PinTypes.GND, \
                     desc='USB2.0 Ground')
        self += Pin(num='N7', name='AVDD09_PCIEA', func=PinTypes.POWER_IN, \
                     desc='PCIEA digital power')
        self += Pin(num='N8', name='AVSS_PCIEA', func=PinTypes.GND, \
                     desc='PCIEA Ground')
        self += Pin(num='P3', name='AVSS_USB', func=PinTypes.GND, \
                     desc='USB2.0 Ground')
        self += Pin(num='P5', name='AVSS_USB', func=PinTypes.GND, \
                     desc='USB2.0 Ground')
        self += Pin(num='P7', name='AVDD09_USB', func=PinTypes.POWER_IN, \
                     desc='USB2.0 digital power')
        self += Pin(num='P8', name='AVDD09_USB', func=PinTypes.POWER_IN, \
                     desc='USB2.0 digital power')
        self += Pin(num='R7', name='AVSS_USB', func=PinTypes.GND, \
                     desc='USB2.0 Ground')
        self += Pin(num='T21', name='AVSS18_AUD', func=PinTypes.GND, \
                     desc='Audio Ground')
        self += Pin(num='T22', name='AVSS18_AUD', func=PinTypes.GND, \
                     desc='Audio Ground')
        self += Pin(num='T7', name='AVDD09_DSI1', func=PinTypes.POWER_IN, \
                     desc='DSI digital power')
        self += Pin(num='U3', name='AVSS_DSI1', func=PinTypes.GND, \
                     desc='DSI Ground')
        self += Pin(num='U4', name='AVSS_DSI1', func=PinTypes.GND, \
                     desc='DSI Ground')
        self += Pin(num='U5', name='AVSS_DSI1', func=PinTypes.GND, \
                     desc='DSI Ground')
        self += Pin(num='U7', name='AVSS_DSI1', func=PinTypes.GND, \
                     desc='DSI Ground')
        self += Pin(num='V3', name='AVSS_DSI1', func=PinTypes.GND, \
                     desc='DSI Ground')
        self += Pin(num='V4', name='AVSS_DSI1', func=PinTypes.GND, \
                     desc='DSI Ground')
        self += Pin(num='V5', name='AVSS_DSI1', func=PinTypes.GND, \
                     desc='DSI Ground')
        self += Pin(num='V6', name='AVSS_DSI1', func=PinTypes.GND, \
                     desc='DSI Ground')
        self += Pin(num='Y10', name='AVDD09_HDMI', func=PinTypes.POWER_IN, \
                     desc='HDMI digtial power')
        self += Pin(num='Y9', name='AVDD09_HDMI', func=PinTypes.POWER_IN, \
                     desc='HDMI digtial power')

        # JTAG
        self += Pin(num='AA1', name='PRI_TCK', func=PinTypes.BIDIRECTIONAL, \
                     desc='JTAG clock')
        self += Pin(num='AA2', name='PRI_TDO', func=PinTypes.BIDIRECTIONAL, \
                     desc='JTAG output data')
        self += Pin(num='AB1', name='PRI_TDI', func=PinTypes.BIDIRECTIONAL, \
                     desc='JTAG input data')
        self += Pin(num='AB2', name='PRI_TMS', func=PinTypes.BIDIRECTIONAL, \
                     desc='JTAG mode selection')
        self += Pin(num='AF4', name='JTAG_SEL', func=PinTypes.BIDIRECTIONAL, \
                     desc='Primary JTAG selection')
        self += Pin(num='Y1', name='PRI_TRST_N', func=PinTypes.BIDIRECTIONAL, \
                     desc='JTAG reset')

        # HDMI接口
        self += Pin(num='AA10', name='AVDD18_HDMI', func=PinTypes.POWER_IN, \
                     desc='HDMI 1.8V power')
        self += Pin(num='AA8', name='HDMI_TX2N', func=PinTypes.ANALOG_OUT, \
                     desc='HDMI data2n')
        self += Pin(num='AA9', name='AVDD18_HDMI', func=PinTypes.POWER_IN, \
                     desc='HDMI 1.8V power')
        self += Pin(num='AB4', name='HDMI_TXCN', func=PinTypes.ANALOG_OUT, \
                     desc='HDMI clkn')
        self += Pin(num='AB5', name='HDMI_TX0N', func=PinTypes.ANALOG_OUT, \
                     desc='HDMI data0n')
        self += Pin(num='AB7', name='HDMI_TX1N', func=PinTypes.ANALOG_OUT, \
                     desc='HDMI data1n')
        self += Pin(num='AB8', name='HDMI_TX2P', func=PinTypes.ANALOG_OUT, \
                     desc='HDMI data2p')
        self += Pin(num='AC4', name='HDMI_TXCP', func=PinTypes.ANALOG_OUT, \
                     desc='HDMI clkp')
        self += Pin(num='AC5', name='HDMI_TX0P', func=PinTypes.ANALOG_OUT, \
                     desc='HDMI data0p')
        self += Pin(num='AC7', name='HDMI_TX1P', func=PinTypes.ANALOG_OUT, \
                     desc='HDMI data1p')
        self += Pin(num='Y7', name='AVDD33_HDMI', func=PinTypes.POWER_IN, \
                     desc='HDMI 3.3V power')
        self += Pin(num='Y8', name='AVDD33_HDMI', func=PinTypes.POWER_IN, \
                     desc='HDMI 3.3V power')

        # GPIO
        self += Pin(num='AA13', name='VCC1833_GPIO3', func=PinTypes.POWER_IN, \
                     desc='GPIO3 IO power')
        self += Pin(num='AA15', name='VCC1833_GPIO2', func=PinTypes.POWER_IN, \
                     desc='GPIO2 IO power')
        self += Pin(num='AA19', name='GPIO_32', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 32')
        self += Pin(num='AA20', name='GPIO_29', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 29')
        self += Pin(num='AA21', name='VCC18_GPIO', func=PinTypes.POWER_IN, \
                     desc='GPIO1/4/5/PMIC I/O power')
        self += Pin(num='AA22', name='GPIO_21', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 21')
        self += Pin(num='AA23', name='GPIO_24', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 24')
        self += Pin(num='AA24', name='GPIO_23', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 23')
        self += Pin(num='AA25', name='GPIO_25', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 25')
        self += Pin(num='AB13', name='GPIO_51', func=PinTypes.BIDIRECTIONAL, \
                     desc='General purpose I/O 51')
        self += Pin(num='AB15', name='GPIO_78', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 78')
        self += Pin(num='AB16', name='GPIO_77', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 77')
        self += Pin(num='AB17', name='GPIO_02', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 02')
        self += Pin(num='AB18', name='GPIO_03', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 03')
        self += Pin(num='AB21', name='GPIO_41', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 41')
        self += Pin(num='AB22', name='GPIO_44', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 44')
        self += Pin(num='AB23', name='GPIO_19', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 19')
        self += Pin(num='AB25', name='GPIO_20', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 20')
        self += Pin(num='AB26', name='GPIO_22', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 22')
        self += Pin(num='AC1', name='GPIO_61', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 61')
        self += Pin(num='AC10', name='GPIO_86', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 86')
        self += Pin(num='AC11', name='VCC18_GPIO', func=PinTypes.POWER_IN, \
                     desc='GPIO1/4/5/PMIC I/O power')
        self += Pin(num='AC12', name='GPIO_52', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 52')
        self += Pin(num='AC13', name='GPIO_47', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 47')
        self += Pin(num='AC14', name='VCC18_GPIO', func=PinTypes.POWER_IN, \
                     desc='GPIO1/4/5/PMIC I/O power')
        self += Pin(num='AC15', name='GPIO_79', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 79')
        self += Pin(num='AC17', name='GPIO_05', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 05')
        self += Pin(num='AC18', name='GPIO_00', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 00')
        self += Pin(num='AC2', name='GPIO_62', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 62')
        self += Pin(num='AC20', name='GPIO_31', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 31')
        self += Pin(num='AC21', name='GPIO_34', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 34')
        self += Pin(num='AC22', name='GPIO_42', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 42')
        self += Pin(num='AC23', name='GPIO_43', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 43')
        self += Pin(num='AC24', name='GPIO_17', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 17')
        self += Pin(num='AC26', name='GPIO_18', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 18')
        self += Pin(num='AC3', name='VCC18_GPIO', func=PinTypes.POWER_IN, \
                     desc='GPIO1/4/5/PMIC I/O power')
        self += Pin(num='AD1', name='GPIO_59', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 59')
        self += Pin(num='AD11', name='VCC18_GPIO', func=PinTypes.POWER_IN, \
                     desc='GPIO1/4/5/PMIC I/O power')
        self += Pin(num='AD12', name='GPIO_50', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 50')
        self += Pin(num='AD13', name='GPIO_48', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 48')
        self += Pin(num='AD15', name='GPIO_76', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 76')
        self += Pin(num='AD17', name='GPIO_04', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 04')
        self += Pin(num='AD18', name='GPIO_01', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 01')
        self += Pin(num='AD19', name='GPIO_30', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 30')
        self += Pin(num='AD2', name='GPIO_60', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 60')
        self += Pin(num='AD20', name='GPIO_33', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 33')
        self += Pin(num='AD21', name='VCC18_GPIO', func=PinTypes.POWER_IN, \
                     desc='GPIO1/4/5/PMIC I/O power')
        self += Pin(num='AD22', name='VCC18_GPIO', func=PinTypes.POWER_IN, \
                     desc='GPIO1/4/5/PMIC I/O power')
        self += Pin(num='AD23', name='GPIO_14', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 14')
        self += Pin(num='AD24', name='GPIO_12', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 12')
        self += Pin(num='AD25', name='GPIO_16', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 16')
        self += Pin(num='AD26', name='GPIO_15', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 15')
        self += Pin(num='AD8', name='GPIO_87', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 87')
        self += Pin(num='AD9', name='GPIO_85', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 85')
        self += Pin(num='AE11', name='PWR_SCL', func=PinTypes.BIDIRECTIONAL, \
                     desc='PMIC I2C bus clock')
        self += Pin(num='AE16', name='GPIO_75', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 75')
        self += Pin(num='AE17', name='GPIO_11', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 11')
        self += Pin(num='AE18', name='GPIO_07', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 07')
        self += Pin(num='AE19', name='GPIO_10', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 10')
        self += Pin(num='AE20', name='GPIO_37', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 37')
        self += Pin(num='AE21', name='GPIO_35', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 35')
        self += Pin(num='AE22', name='GPIO_38', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 38')
        self += Pin(num='AE23', name='GPIO_46', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 46')
        self += Pin(num='AE25', name='GPIO_13', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 13')
        self += Pin(num='AE4', name='GPIO_92', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 92')
        self += Pin(num='AE5', name='GPIO_90', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 90')
        self += Pin(num='AE6', name='GPIO_91', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 91')
        self += Pin(num='AE7', name='GPIO_89', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 89')
        self += Pin(num='AE8', name='GPIO_84', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 84')
        self += Pin(num='AE9', name='GPIO_81', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 81')
        self += Pin(num='AF12', name='PWR_SDA', func=PinTypes.BIDIRECTIONAL, \
                     desc='PMIC I2C bus data/address')
        self += Pin(num='AF13', name='GPIO_49', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 49')
        self += Pin(num='AF16', name='GPIO_80', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 80')
        self += Pin(num='AF17', name='GPIO_08', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 08')
        self += Pin(num='AF18', name='GPIO_06', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 06')
        self += Pin(num='AF19', name='GPIO_09', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 09')
        self += Pin(num='AF21', name='GPIO_40', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 40')
        self += Pin(num='AF22', name='GPIO_36', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 36')
        self += Pin(num='AF23', name='GPIO_39', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 39')
        self += Pin(num='AF24', name='GPIO_45', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 45')
        self += Pin(num='AF6', name='GPIO_88', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 88')
        self += Pin(num='AF7', name='GPIO_82', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 82')
        self += Pin(num='AF8', name='GPIO_83', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 83')
        self += Pin(num='C1', name='GPIO_58', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 58')
        self += Pin(num='C2', name='GPIO_57', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 57')
        self += Pin(num='C3', name='GPIO_56', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 56')
        self += Pin(num='C4', name='GPIO_55', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 55')
        self += Pin(num='C5', name='GPIO_54', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 54')
        self += Pin(num='D1', name='GPIO_114', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 114')
        self += Pin(num='D2', name='GPIO_113', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 113')
        self += Pin(num='D3', name='GPIO_112', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 112')
        self += Pin(num='D4', name='GPIO_111', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 111')
        self += Pin(num='D5', name='GPIO_53', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 53')
        self += Pin(num='E1', name='GPIO_67', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 67')
        self += Pin(num='E2', name='GPIO_65', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 65')
        self += Pin(num='E3', name='GPIO_64', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 64')
        self += Pin(num='E5', name='GPIO_63', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 63')
        self += Pin(num='F3', name='GPIO_69', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 69')
        self += Pin(num='F4', name='GPIO_68', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 68')
        self += Pin(num='F5', name='GPIO_66', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 66')
        self += Pin(num='F6', name='VCC18_GPIO', func=PinTypes.POWER_IN, \
                     desc='GPIO1/4/5/PMIC I/O power')
        self += Pin(num='U21', name='GPIO_123', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 123')
        self += Pin(num='U22', name='GPIO_125', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 125')
        self += Pin(num='U25', name='GPIO_126', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 126')
        self += Pin(num='U26', name='GPIO_127', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 127')
        self += Pin(num='V21', name='GPIO_121', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 121')
        self += Pin(num='V23', name='GPIO_124', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 124')
        self += Pin(num='V24', name='GPIO_120', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 120')
        self += Pin(num='V26', name='GPIO_122', func=PinTypes.BIDIRECTIONAL, \
                     desc='General purpose I/O 122')
        self += Pin(num='W13', name='GPIO3_VCC_CAP', func=PinTypes.NC, \
                     desc='GPIO3 1.8V LDO cap')
        self += Pin(num='W21', name='GPIO_110', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 110')
        self += Pin(num='W22', name='GPIO_117', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 117')
        self += Pin(num='W23', name='GPIO_116', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 116')
        self += Pin(num='W25', name='GPIO_119', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 119')
        self += Pin(num='W26', name='GPIO_118', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 118')
        self += Pin(num='Y15', name='GPIO2_VCC_CAP', func=PinTypes.NC, \
                     desc='GPIO2 1.8V LDO cap')
        self += Pin(num='Y2', name='GPIO_74', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 74')
        self += Pin(num='Y21', name='VCC18_GPIO', func=PinTypes.POWER_IN, \
                     desc='GPIO1/4/5/PMIC I/O power')
        self += Pin(num='Y22', name='GPIO_26', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 26')
        self += Pin(num='Y23', name='GPIO_27', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 27')
        self += Pin(num='Y25', name='GPIO_28', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 28')
        self += Pin(num='Y26', name='GPIO_115', func=PinTypes.BIDIRECTIONAL, \
                     desc='General Purpose I/O 115')

        # SD/eMMC接口
        self += Pin(num='AA14', name='VCC1833_MMC1', func=PinTypes.POWER_IN, \
                     desc='SD card IO power')
        self += Pin(num='AA16', name='MMC1_DAT2', func=PinTypes.BIDIRECTIONAL, \
                     desc='SD card data 2')
        self += Pin(num='AB14', name='MMC1_DAT0', func=PinTypes.BIDIRECTIONAL, \
                     desc='SD card data 0')
        self += Pin(num='AD14', name='MMC1_CMD', func=PinTypes.BIDIRECTIONAL, \
                     desc='SD card command')
        self += Pin(num='AE14', name='MMC1_CLK', func=PinTypes.BIDIRECTIONAL, \
                     desc='SD card clock')
        self += Pin(num='AE15', name='MMC1_DAT3', func=PinTypes.BIDIRECTIONAL, \
                     desc='SD card data 3')
        self += Pin(num='AF14', name='MMC1_DAT1', func=PinTypes.BIDIRECTIONAL, \
                     desc='SD card data 1')
        self += Pin(num='C24', name='EMMC_DS', func=PinTypes.BIDIRECTIONAL, \
                     desc='eMMC data strobe')
        self += Pin(num='C25', name='EMMC_D7', func=PinTypes.BIDIRECTIONAL, \
                     desc='eMMC data7')
        self += Pin(num='C26', name='EMMC_D2', func=PinTypes.BIDIRECTIONAL, \
                     desc='eMMC data2')
        self += Pin(num='D23', name='EMMC_D4', func=PinTypes.BIDIRECTIONAL, \
                     desc='eMMC data4')
        self += Pin(num='D24', name='EMMC_D1', func=PinTypes.BIDIRECTIONAL, \
                     desc='eMMC data1')
        self += Pin(num='D26', name='EMMC_D0', func=PinTypes.BIDIRECTIONAL, \
                     desc='eMMC data0')
        self += Pin(num='E22', name='EMMC_D6', func=PinTypes.BIDIRECTIONAL, \
                     desc='eMMC data6')
        self += Pin(num='E24', name='EMMC_CLK', func=PinTypes.BIDIRECTIONAL, \
                     desc='eMMC Clock')
        self += Pin(num='E25', name='EMMC_D3', func=PinTypes.BIDIRECTIONAL, \
                     desc='eMMC data3')
        self += Pin(num='E26', name='EMMC_D5', func=PinTypes.BIDIRECTIONAL, \
                     desc='eMMC data5')
        self += Pin(num='F25', name='EMMC_CMD', func=PinTypes.BIDIRECTIONAL, \
                     desc='eMMC command')
        self += Pin(num='H18', name='VSSU_EMMC', func=PinTypes.GND, \
                     desc='eMMC Ground')
        self += Pin(num='H19', name='AVDD18_EMMC', func=PinTypes.POWER_IN, \
                     desc='eMMC analog power')
        self += Pin(num='J18', name='VSSU_EMMC', func=PinTypes.GND, \
                     desc='eMMC Ground')
        self += Pin(num='Y14', name='MMC1_VCC_CAP', func=PinTypes.NC, \
                     desc='SD card 1.8V LDO cap')

        # 电源管理和控制
        self += Pin(num='AD10', name='PMIC_INT_N', func=PinTypes.BIDIRECTIONAL, \
                     desc='PMIC interrupt')
        self += Pin(num='AE10', name='DVL0', func=PinTypes.BIDIRECTIONAL, \
                     desc='Hardware dynamic voltage regulation signal0')
        self += Pin(num='AF11', name='SLEEP_OUT', func=PinTypes.BIDIRECTIONAL, \
                     desc='VCXO enabling')
        self += Pin(num='AF3', name='RESET_IN_N', func=PinTypes.BIDIRECTIONAL, \
                     desc='Reset input')
        self += Pin(num='AF9', name='DVL1', func=PinTypes.BIDIRECTIONAL, \
                     desc='Hardware dynamic voltage regulation signal1')

        # 时钟和参考
        self += Pin(num='AE12', name='EXT_32K_IN', func=PinTypes.BIDIRECTIONAL, \
                     desc='32K clock input')
        self += Pin(num='AE2', name='MPLL_TST_AD', func=PinTypes.PASSIVE, \
                     desc='Analog testpin')
        self += Pin(num='H7', name='XI_PAD', func=PinTypes.ANALOG_IN, \
                     desc='DCXO crystal input')
        self += Pin(num='J7', name='XO_PAD', func=PinTypes.ANALOG_OUT, \
                     desc='DCXO crystal output')
        self += Pin(num='K11', name='BG_OUT', func=PinTypes.ANALOG_OUT, \
                     desc='Bandgap output')
        self += Pin(num='K12', name='AVDD18_AFEAP', func=PinTypes.POWER_IN, \
                     desc='1.8V power for DCXO')
        self += Pin(num='K13', name='MPLL_TST_CK', func=PinTypes.PASSIVE, \
                     desc='Analog testpin')
        self += Pin(num='K14', name='AVDD18_PLL', func=PinTypes.POWER_IN, \
                     desc='System PLL power supply')
        self += Pin(num='L12', name='VSSU_AFEAP', func=PinTypes.GND, \
                     desc='DCXO Ground')

        # QSPI接口
        self += Pin(num='F23', name='QSPI_DAT2', func=PinTypes.BIDIRECTIONAL, \
                     desc='QSPI data2')
        self += Pin(num='F24', name='QSPI_DAT1', func=PinTypes.BIDIRECTIONAL, \
                     desc='QSPI data1')
        self += Pin(num='F26', name='QSPI_DAT0', func=PinTypes.BIDIRECTIONAL, \
                     desc='QSPI data0')
        self += Pin(num='G22', name='QSPI_DAT3', func=PinTypes.BIDIRECTIONAL, \
                     desc='QSPI data3')
        self += Pin(num='G23', name='QSPI_CLK', func=PinTypes.BIDIRECTIONAL, \
                     desc='QSPI CLK')
        self += Pin(num='G24', name='QSPI_CS1', func=PinTypes.BIDIRECTIONAL, \
                     desc='QSPI CS')
        self += Pin(num='H21', name='VCC1833_QSPI', func=PinTypes.POWER_IN, \
                     desc='QSPI IO power')
        self += Pin(num='J19', name='QSPI_VCC_CAP', func=PinTypes.NC, \
                     desc='QSPI 1.8V LDO cap')

        # MIPI CSI接口
        self += Pin(num='G1', name='MIPI_CSI1_D1N', func=PinTypes.ANALOG_IN, \
                     desc='CSI1 DATA1LANEN')
        self += Pin(num='G2', name='MIPI_CSI1_D1P', func=PinTypes.ANALOG_IN, \
                     desc='CSI1 DATA1LANEP')
        self += Pin(num='G4', name='MIPI_CSI1_D0N', func=PinTypes.ANALOG_IN, \
                     desc='CSI1 DATA0LANEN')
        self += Pin(num='G5', name='MIPI_CSI1_D0P', func=PinTypes.ANALOG_IN, \
                     desc='CSI1 DATA0LANEP')
        self += Pin(num='H1', name='MIPI_CSI1_D2N', func=PinTypes.ANALOG_IN, \
                     desc='CSI1 DATA2LANEN')
        self += Pin(num='H2', name='MIPI_CSI1_D2P', func=PinTypes.ANALOG_IN, \
                     desc='CSI1 DATA2LANEP')
        self += Pin(num='H4', name='MIPI_CSI1_CLKN', func=PinTypes.ANALOG_OUT, \
                     desc='CSI1 CKLANEN')
        self += Pin(num='H5', name='MIPI_CSI1_CLKP', func=PinTypes.ANALOG_OUT, \
                     desc='CSI1 CKLANEP')
        self += Pin(num='J1', name='MIPI_CSI3_D0N', func=PinTypes.ANALOG_IN, \
                     desc='CSI3 DATA0LANEN')
        self += Pin(num='J2', name='MIPI_CSI3_D0P', func=PinTypes.ANALOG_IN, \
                     desc='CSI3 DATA0LANEP')
        self += Pin(num='J4', name='MIPI_CSI1_D3N', func=PinTypes.ANALOG_IN, \
                     desc='CSI1 DATA3LANEN')
        self += Pin(num='J5', name='MIPI_CSI1_D3P', func=PinTypes.ANALOG_IN, \
                     desc='CSI1 DATA3LANEP')
        self += Pin(num='K1', name='MIPI_CSI3_CLKN', func=PinTypes.ANALOG_OUT, \
                     desc='CSI3 CKLANEN for CSI3 DATALANE0/1 when CSI3 is configured as two 2ch CSI;; CSI3 CKLANEN for CSI3 DATALANE0/1/2/3 when CSI3 is configured as 4ch CSI')
        self += Pin(num='K2', name='MIPI_CSI3_CLKP', func=PinTypes.ANALOG_OUT, \
                     desc='CSI3 CKLANEP for CSI3 DATALANE0/1 when CSI3 is configured as two 2ch CSI;; CSI3 CKLANEP for CSI3 DATALANE0/1/2/3 when CSI3 is configured as 4ch CSI')
        self += Pin(num='K4', name='MIPI_CSI3_D1N', func=PinTypes.ANALOG_IN, \
                     desc='CSI3 DATA1LANEN')
        self += Pin(num='K5', name='MIPI_CSI3_D1P', func=PinTypes.ANALOG_IN, \
                     desc='CSI3 DATA1LANEP')
        self += Pin(num='K6', name='AVDD18_CSI', func=PinTypes.POWER_IN, \
                     desc='MIPI_CSI analog power')
        self += Pin(num='L1', name='MIPI_CSI3_D2N', func=PinTypes.ANALOG_IN, \
                     desc='CSI3 DATA2LANEN')
        self += Pin(num='L2', name='MIPI_CSI3_D2P', func=PinTypes.ANALOG_IN, \
                     desc='CSI3 DATA2LANEP')
        self += Pin(num='L4', name='MIPI_CSI2_CLKN', func=PinTypes.ANALOG_OUT, \
                     desc='CKLANEN for CSI3 DATALANE2/3 when CSI3 is configured as two 2ch CSI;; Disabled when CSI3 is configured as 4ch CSI')
        self += Pin(num='L5', name='MIPI_CSI2_CLKP', func=PinTypes.ANALOG_OUT, \
                     desc='CKLANEP for CSI3 DATALANE2/3 when CSI3 is configured as two 2ch CSI;; Disabled when CSI3 is configured as 4ch CSI')
        self += Pin(num='L6', name='AVDD18_CSI', func=PinTypes.POWER_IN, \
                     desc='MIPI_CSI analog power')
        self += Pin(num='M1', name='MIPI_CSI3_D3N', func=PinTypes.ANALOG_IN, \
                     desc='CSI3 DATA3LANEN')
        self += Pin(num='M2', name='MIPI_CSI3_D3P', func=PinTypes.ANALOG_IN, \
                     desc='CSI3 DATA3LANEP')

        # 其他核心电源
        self += Pin(num='G18', name='AVDD18_EFUSE', func=PinTypes.POWER_IN, \
                     desc='ANAGRP')
        self += Pin(num='J11', name='AVDDU_PHY', func=PinTypes.POWER_IN, \
                     desc='LPDDR PHY core logical power')
        self += Pin(num='J12', name='AVDDU_PHY', func=PinTypes.POWER_IN, \
                     desc='LPDDR PHY core logical power')
        self += Pin(num='J13', name='AVDDU_PHY', func=PinTypes.POWER_IN, \
                     desc='LPDDR PHY core logical power')
        self += Pin(num='J14', name='AVDDU_PHY', func=PinTypes.POWER_IN, \
                     desc='LPDDR PHY core logical power')
        self += Pin(num='J15', name='AVDDU_PHY', func=PinTypes.POWER_IN, \
                     desc='LPDDR PHY core logical power')

        # PCIe接口
        self += Pin(num='H22', name='PCIEC_TX0P', func=PinTypes.ANALOG_OUT, \
                     desc='PCIEC TX0LANEP')
        self += Pin(num='H23', name='PCIEC_TX0N', func=PinTypes.ANALOG_OUT, \
                     desc='PCIEC TX0LANEN')
        self += Pin(num='H25', name='PCIEC_RX0P', func=PinTypes.ANALOG_IN, \
                     desc='PCIEC RX0LANEP')
        self += Pin(num='H26', name='PCIEC_RX0N', func=PinTypes.ANALOG_IN, \
                     desc='PCIEC RX0LANEN')
        self += Pin(num='J22', name='PCIEC_REFCLK_P', func=PinTypes.PASSIVE, \
                     desc='PCIEC CKLANEP')
        self += Pin(num='J23', name='PCIEC_REFCLK_N', func=PinTypes.PASSIVE, \
                     desc='PCIEC CKLANEN')
        self += Pin(num='J25', name='PCIEC_RX1P', func=PinTypes.ANALOG_IN, \
                     desc='PCIEC RX1LANEP')
        self += Pin(num='J26', name='PCIEC_RX1N', func=PinTypes.ANALOG_IN, \
                     desc='PCIEC RX1LANEN')
        self += Pin(num='K18', name='VSSU_PCIEC', func=PinTypes.GND, \
                     desc='PCIEC Ground')
        self += Pin(num='K19', name='VSSU_PCIEC', func=PinTypes.GND, \
                     desc='PCIEC Ground')
        self += Pin(num='K22', name='PCIEC_TX1P', func=PinTypes.ANALOG_OUT, \
                     desc='PCIEC TX1LANEP')
        self += Pin(num='K23', name='PCIEC_TX1N', func=PinTypes.ANALOG_OUT, \
                     desc='PCIEC TX1LANEN')
        self += Pin(num='K25', name='PCIEB_RX0P', func=PinTypes.ANALOG_IN, \
                     desc='PCIEB RX0LANEP')
        self += Pin(num='K26', name='PCIEB_RX0N', func=PinTypes.ANALOG_IN, \
                     desc='PCIEB RX0LANEN')
        self += Pin(num='L17', name='VSSU_PCIEC', func=PinTypes.GND, \
                     desc='PCIEC Ground')
        self += Pin(num='L18', name='VSSU_PCIEC', func=PinTypes.GND, \
                     desc='PCIEC Ground')
        self += Pin(num='L19', name='AVDD18_PCIEC', func=PinTypes.POWER_IN, \
                     desc='PCIEC analog power')
        self += Pin(num='L22', name='PCIEB_TX0P', func=PinTypes.ANALOG_OUT, \
                     desc='PCIEB TX0LANEP')
        self += Pin(num='L23', name='PCIEB_TX0N', func=PinTypes.ANALOG_OUT, \
                     desc='PCIEB TX0LANEN')
        self += Pin(num='L25', name='PCIEB_REFCLK_P', func=PinTypes.PASSIVE, \
                     desc='PCIEB CKLANEP')
        self += Pin(num='L26', name='PCIEB_REFCLK_N', func=PinTypes.PASSIVE, \
                     desc='PCIEB CKLANEN')
        self += Pin(num='M17', name='VSSU_PCIEB', func=PinTypes.GND, \
                     desc='PCIEB Ground')
        self += Pin(num='M18', name='VSSU_PCIEB', func=PinTypes.GND, \
                     desc='PCIEB Ground')
        self += Pin(num='M19', name='AVDD18_PCIEB', func=PinTypes.POWER_IN, \
                     desc='PCIEB analog power')
        self += Pin(num='M22', name='PCIEB_TX1P', func=PinTypes.ANALOG_OUT, \
                     desc='PCIEB TX1LANEP')
        self += Pin(num='M23', name='PCIEB_TX1N', func=PinTypes.ANALOG_OUT, \
                     desc='PCIEB TX1LANEN')
        self += Pin(num='M25', name='PCIEB_RX1P', func=PinTypes.ANALOG_IN, \
                     desc='PCIEB RX1LANEP')
        self += Pin(num='M26', name='PCIEB_RX1N', func=PinTypes.ANALOG_IN, \
                     desc='PCIEB RX1LANEN')
        self += Pin(num='M5', name='VSSU_PCIEA', func=PinTypes.GND, \
                     desc='PCIEA Ground')
        self += Pin(num='M8', name='VSSU_PCIEA', func=PinTypes.GND, \
                     desc='PCIEA Ground')
        self += Pin(num='N4', name='PCIEA_TXN', func=PinTypes.ANALOG_OUT, \
                     desc='PCIEA TXLANEN')
        self += Pin(num='N5', name='PCIEA_TXP', func=PinTypes.ANALOG_OUT, \
                     desc='PCIEA TXLANEP')
        self += Pin(num='N6', name='AVDD18_PCIEA', func=PinTypes.POWER_IN, \
                     desc='PCIEA analog power')
        self += Pin(num='P1', name='PCIEA_RXN', func=PinTypes.ANALOG_IN, \
                     desc='PCIEA RXLANEN')
        self += Pin(num='P2', name='PCIEA_RXP', func=PinTypes.ANALOG_IN, \
                     desc='PCIEA RXLANEP')
        self += Pin(num='P4', name='PCIEA_R_EXT', func=PinTypes.ANALOG_OUT, \
                     desc='PCIEA External calibration resistor')
        self += Pin(num='R1', name='PCIEA_REFCLK_N', func=PinTypes.PASSIVE, \
                     desc='PCIEA CKLANEN')
        self += Pin(num='R2', name='PCIEA_REFCLK_P', func=PinTypes.PASSIVE, \
                     desc='PCIEA CKLANEP')

        # USB接口
        self += Pin(num='M6', name='AVDD18_USB', func=PinTypes.POWER_IN, \
                     desc='USB2.0 1.8V power')
        self += Pin(num='M9', name='AVDD33_USB', func=PinTypes.POWER_IN, \
                     desc='USB2.0 3.3V power')
        self += Pin(num='N1', name='USB2_DN', func=PinTypes.PASSIVE, \
                     desc='USB2.0_2 D- differential data line')
        self += Pin(num='N2', name='USB2_DP', func=PinTypes.PASSIVE, \
                     desc='USB2.0_2 D+ differential data line')
        self += Pin(num='N9', name='AVDD33_USB', func=PinTypes.POWER_IN, \
                     desc='USB2.0 3.3V power')
        self += Pin(num='P6', name='AVDD18_USB', func=PinTypes.POWER_IN, \
                     desc='USB2.0 1.8V power')
        self += Pin(num='P9', name='AVDD33_USB', func=PinTypes.POWER_IN, \
                     desc='USB2.0 3.3V power')
        self += Pin(num='R4', name='USB1_DN', func=PinTypes.PASSIVE, \
                     desc='USB2.0_1 D- differential data line')
        self += Pin(num='R5', name='USB1_DP', func=PinTypes.PASSIVE, \
                     desc='USB2.0_1 D+ differential data line')
        self += Pin(num='T4', name='USB0_DN', func=PinTypes.PASSIVE, \
                     desc='USB2.0_0 D- differential data line')
        self += Pin(num='T5', name='USB0_DP', func=PinTypes.PASSIVE, \
                     desc='USB2.0_0 D+ differential data line')

        # 音频接口
        self += Pin(num='N18', name='AVDD3V3_AUD', func=PinTypes.POWER_IN, \
                     desc='3.3V power for earphone driver')
        self += Pin(num='P17', name='AUD_GNDSNS', func=PinTypes.GND, \
                     desc='Headphone sense_Ground')
        self += Pin(num='P18', name='AVDD18_AUD', func=PinTypes.POWER_IN, \
                     desc='1.8V power for audio')
        self += Pin(num='P19', name='AVDD18_AUD', func=PinTypes.POWER_IN, \
                     desc='1.8V power for audio')
        self += Pin(num='R17', name='AUD_VSSU', func=PinTypes.GND, \
                     desc='Audio Ground')
        self += Pin(num='R18', name='AUD_VDDU09', func=PinTypes.POWER_IN, \
                     desc='0.9V power for audio')
        self += Pin(num='R19', name='AUD_REFGND', func=PinTypes.GND, \
                     desc='Audio Reference Ground')
        self += Pin(num='R21', name='AUD_AUREF10', func=PinTypes.NC, \
                     desc='Audio reference voltage')

        # MIPI DSI接口
        self += Pin(num='R6', name='AVDD18_DSI1', func=PinTypes.POWER_IN, \
                     desc='DSI analog power')
        self += Pin(num='T1', name='MIPI_DSI1_D3N', func=PinTypes.ANALOG_OUT, \
                     desc='DSI DATA3LANEN')
        self += Pin(num='T2', name='MIPI_DSI1_D3P', func=PinTypes.ANALOG_OUT, \
                     desc='DSI DATA3LANEP')
        self += Pin(num='T8', name='AVDD12_DSI1', func=PinTypes.POWER_IN, \
                     desc='DSI driver power')
        self += Pin(num='U1', name='MIPI_DSI1_D2N', func=PinTypes.ANALOG_OUT, \
                     desc='DSI DATA2LANEN')
        self += Pin(num='U2', name='MIPI_DSI1_D2P', func=PinTypes.ANALOG_OUT, \
                     desc='DSI DATA2LANEP')
        self += Pin(num='V1', name='MIPI_DSI1_CLKN', func=PinTypes.ANALOG_OUT, \
                     desc='DSI CKLANEN')
        self += Pin(num='V2', name='MIPI_DSI1_CLKP', func=PinTypes.ANALOG_OUT, \
                     desc='DSI CKLANEP')
        self += Pin(num='W4', name='MIPI_DSI1_D1N', func=PinTypes.ANALOG_OUT, \
                     desc='DSI DATA1LANEN')
        self += Pin(num='W5', name='MIPI_DSI1_D1P', func=PinTypes.ANALOG_OUT, \
                     desc='DSI DATA1LANEP')
        self += Pin(num='Y4', name='MIPI_DSI1_D0N', func=PinTypes.ANALOG_OUT, \
                     desc='DSI DATA0LANEN')
        self += Pin(num='Y5', name='MIPI_DSI1_D0P', func=PinTypes.ANALOG_OUT, \
                     desc='DSI DATA0LANEP')

    def get_pins_by_category(self, category):
        """
        Get all pins belonging to a specific functional category.

        Args:
            category (str): Functional category name

        Returns:
            list: List of Pin objects in the specified category
        """
        category_pins = {
            '电源和地': ['VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSSU_DDR', 'VSSU_DDR', 'VSSU_DDR', 'VSSU_DDR', 'VSS', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VCC_M1', 'VCC_M1', 'VSSU_PLL', 'VSS', 'VCC_M1', 'VSS', 'VSS', 'VSS', 'VSS', 'VCC_M1', 'VSS', 'VSS', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'NC', 'NC', 'NC', 'NC', 'NC', 'NC', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'NC', 'NC', 'NC', 'NC', 'NC', 'NC', 'NC', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'NC', 'NC', 'NC', 'VSS', 'NC', 'NC', 'VSS', 'VSS', 'VSS', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VSS', 'VSS', 'NC', 'VSS', 'NC', 'VSS', 'VSS', 'VSS', 'VCC_M1', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1_FB', 'VSS_FB', 'VSS', 'NC', 'NC', 'VCC_M1', 'VCC_M1', 'VSS', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VCC_M1', 'VSS', 'VCC_M1', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS', 'VSS'],
            'DDR/LPDDR接口': ['VSSQ_DDR', 'DQ_B_9', 'DQ_B_12', 'DQ_B_11', 'DQS1_C_B', 'DQS1_C_A', 'DQ_A_12', 'DQ_A_9', 'DQ_A_8', 'DQ_A_15', 'VSSQ_DDR', 'VSSQ_DDR', 'DQ_A_5', 'DQ_A_7', 'DMI0_A', 'DQ_A_1', 'VSSQ_DDR', 'DQ_B_2', 'DMI0_B', 'VSSQ_DDR', 'DQ_B_6', 'DQ_B_4', 'DQ_B_13', 'DQ_B_15', 'AVSS_HDMI', 'AVSS_HDMI', 'AVSS_HDMI', 'AVSS_HDMI', 'AVSS_HDMI', 'AVSS_HDMI', 'DMI1_B', 'DQ_B_8', 'DQ_B_10', 'VSSQ_DDR', 'DQS1_T_B', 'DQS1_T_A', 'DQ_A_11', 'DQ_A_10', 'DMI1_A', 'DQ_A_14', 'DQ_B_3', 'DQ_A_13', 'DQ_A_4', 'DQ_A_6', 'VSSQ_DDR', 'DQ_A_2', 'DQ_A_3', 'VSSQ_DDR', 'DQ_B_1', 'DQ_B_0', 'DQ_B_7', 'DQ_B_5', 'VDDQ_V1P2', 'DQ_B_14', 'CKE0_B', 'CKE1_B', 'VDDQ_V1P2', 'CA_B_5', 'VSSQ_DDR', 'VSSQ_DDR', 'CA_A_4', 'VSSQ_DDR', 'CKE1_A', 'CA_A_1', 'CS1_A', 'AVDD06_DDR', 'DQ_A_0', 'DQS0_T_B', 'VSSQ_DDR', 'CS1_B', 'CA_B_1', 'DDR_lp4x_SEL', 'CK_C_B', 'CA_B_2', 'CA_B_4', 'VSSQ_DDR', 'AVDD06_DDR', 'CA_A_2', 'CK_C_A', 'CKE0_A', 'CA_A_0', 'DQS0_T_A', 'DQS0_C_A', 'DQS0_C_B', 'VSSQ_DDR', 'CA_B_0', 'VSSQ_DDR', 'VSSQ_DDR', 'CK_T_B', 'CA_B_3', 'AVSS18_DDR', 'AVDD18_DDR', 'CA_A_5', 'CS0_A', 'CK_T_A', 'AVDD06_DDR', 'AVDD06_DDR', 'VSSQ_DDR', 'AVSS_EMMC', 'AVSS_EMMC', 'VSSQ_DDR', 'VDDQ_V1P2', 'DDR_LP23_VREFDQ', 'VDDQ_V1P2', 'VSSQ_DDR', 'CS0_B', 'DDR_RESET_N', 'ZQ_DDR_PHY', 'CA_A_3', 'VSSQ_DDR', 'DDR_LDO_CAP', 'AVDD06_DDR', 'VSSQ_DDR', 'AVSS_EMMC', 'AVSS_EMMC', 'AVSS_EMMC', 'VSSQ_DDR', 'VDDQ_V1P2', 'VSSQ_DDR', 'VDDQ_V1P2', 'AVDD11_DDR', 'VDDQ_V1P2', 'DDR_LP23_VREFCA', 'AVDD11_DDR', 'AVDD06_DDR', 'VSSQ_DDR', 'AVSS_EMMC', 'AVSS_EMMC', 'AVSS_EMMC', 'AVDD18_PHY', 'AVDDU_DDR', 'AVSSU_DDR', 'AVDD18_PHY', 'AVDD09_EMMC', 'AVSS_PCIEC', 'AVSS18_AFEAP', 'AVSS18_AFEAP', 'AVDD09_EMMC', 'AVSS_PCIEC', 'AVSS_PCIEC', 'AVSS_CSI', 'AVSS_CSI', 'AVSS18_AFEAP', 'AVSS18_AFEAP', 'AVDD09_PCIEC', 'AVSS_PCIEC', 'AVSS_PCIEC', 'AVSS_CSI', 'AVDD09_CSI', 'AVSS_CSI', 'AVDD09_AFEAP', 'AVSS_PLL', 'AVDD09_PCIEB', 'AVDD09_PCIEB', 'AVSS_PCIEB', 'AVSS_CSI', 'AVDD09_CSI', 'AVSS_CSI', 'AVSS_CSI', 'AVDD09_PLL', 'AVSS_PCIEB', 'AVSS_PCIEB', 'AVSS_PCIEB', 'AVDD09_USB', 'AVSS18_AUD', 'AVSS18_AUD', 'AVSS18_AUD', 'AVSS_USB', 'AVDD09_PCIEA', 'AVSS_PCIEA', 'AVSS_USB', 'AVSS_USB', 'AVDD09_USB', 'AVDD09_USB', 'AVSS_USB', 'AVSS18_AUD', 'AVSS18_AUD', 'AVDD09_DSI1', 'AVSS_DSI1', 'AVSS_DSI1', 'AVSS_DSI1', 'AVSS_DSI1', 'AVSS_DSI1', 'AVSS_DSI1', 'AVSS_DSI1', 'AVSS_DSI1', 'AVDD09_HDMI', 'AVDD09_HDMI'],
            'JTAG': ['PRI_TCK', 'PRI_TDO', 'PRI_TDI', 'PRI_TMS', 'JTAG_SEL', 'PRI_TRST_N'],
            'HDMI接口': ['AVDD18_HDMI', 'HDMI_TX2N', 'AVDD18_HDMI', 'HDMI_TXCN', 'HDMI_TX0N', 'HDMI_TX1N', 'HDMI_TX2P', 'HDMI_TXCP', 'HDMI_TX0P', 'HDMI_TX1P', 'AVDD33_HDMI', 'AVDD33_HDMI'],
            'GPIO': ['VCC1833_GPIO3', 'VCC1833_GPIO2', 'GPIO_32', 'GPIO_29', 'VCC18_GPIO', 'GPIO_21', 'GPIO_24', 'GPIO_23', 'GPIO_25', 'GPIO_51', 'GPIO_78', 'GPIO_77', 'GPIO_02', 'GPIO_03', 'GPIO_41', 'GPIO_44', 'GPIO_19', 'GPIO_20', 'GPIO_22', 'GPIO_61', 'GPIO_86', 'VCC18_GPIO', 'GPIO_52', 'GPIO_47', 'VCC18_GPIO', 'GPIO_79', 'GPIO_05', 'GPIO_00', 'GPIO_62', 'GPIO_31', 'GPIO_34', 'GPIO_42', 'GPIO_43', 'GPIO_17', 'GPIO_18', 'VCC18_GPIO', 'GPIO_59', 'VCC18_GPIO', 'GPIO_50', 'GPIO_48', 'GPIO_76', 'GPIO_04', 'GPIO_01', 'GPIO_30', 'GPIO_60', 'GPIO_33', 'VCC18_GPIO', 'VCC18_GPIO', 'GPIO_14', 'GPIO_12', 'GPIO_16', 'GPIO_15', 'GPIO_87', 'GPIO_85', 'PWR_SCL', 'GPIO_75', 'GPIO_11', 'GPIO_07', 'GPIO_10', 'GPIO_37', 'GPIO_35', 'GPIO_38', 'GPIO_46', 'GPIO_13', 'GPIO_92', 'GPIO_90', 'GPIO_91', 'GPIO_89', 'GPIO_84', 'GPIO_81', 'PWR_SDA', 'GPIO_49', 'GPIO_80', 'GPIO_08', 'GPIO_06', 'GPIO_09', 'GPIO_40', 'GPIO_36', 'GPIO_39', 'GPIO_45', 'GPIO_88', 'GPIO_82', 'GPIO_83', 'GPIO_58', 'GPIO_57', 'GPIO_56', 'GPIO_55', 'GPIO_54', 'GPIO_114', 'GPIO_113', 'GPIO_112', 'GPIO_111', 'GPIO_53', 'GPIO_67', 'GPIO_65', 'GPIO_64', 'GPIO_63', 'GPIO_69', 'GPIO_68', 'GPIO_66', 'VCC18_GPIO', 'GPIO_123', 'GPIO_125', 'GPIO_126', 'GPIO_127', 'GPIO_121', 'GPIO_124', 'GPIO_120', 'GPIO_122', 'GPIO3_VCC_CAP', 'GPIO_110', 'GPIO_117', 'GPIO_116', 'GPIO_119', 'GPIO_118', 'GPIO2_VCC_CAP', 'GPIO_74', 'VCC18_GPIO', 'GPIO_26', 'GPIO_27', 'GPIO_28', 'GPIO_115'],
            'SD/eMMC接口': ['VCC1833_MMC1', 'MMC1_DAT2', 'MMC1_DAT0', 'MMC1_CMD', 'MMC1_CLK', 'MMC1_DAT3', 'MMC1_DAT1', 'EMMC_DS', 'EMMC_D7', 'EMMC_D2', 'EMMC_D4', 'EMMC_D1', 'EMMC_D0', 'EMMC_D6', 'EMMC_CLK', 'EMMC_D3', 'EMMC_D5', 'EMMC_CMD', 'VSSU_EMMC', 'AVDD18_EMMC', 'VSSU_EMMC', 'MMC1_VCC_CAP'],
            '电源管理和控制': ['PMIC_INT_N', 'DVL0', 'SLEEP_OUT', 'RESET_IN_N', 'DVL1'],
            '时钟和参考': ['EXT_32K_IN', 'MPLL_TST_AD', 'XI_PAD', 'XO_PAD', 'BG_OUT', 'AVDD18_AFEAP', 'MPLL_TST_CK', 'AVDD18_PLL', 'VSSU_AFEAP'],
            'QSPI接口': ['QSPI_DAT2', 'QSPI_DAT1', 'QSPI_DAT0', 'QSPI_DAT3', 'QSPI_CLK', 'QSPI_CS1', 'VCC1833_QSPI', 'QSPI_VCC_CAP'],
            'MIPI CSI接口': ['MIPI_CSI1_D1N', 'MIPI_CSI1_D1P', 'MIPI_CSI1_D0N', 'MIPI_CSI1_D0P', 'MIPI_CSI1_D2N', 'MIPI_CSI1_D2P', 'MIPI_CSI1_CLKN', 'MIPI_CSI1_CLKP', 'MIPI_CSI3_D0N', 'MIPI_CSI3_D0P', 'MIPI_CSI1_D3N', 'MIPI_CSI1_D3P', 'MIPI_CSI3_CLKN', 'MIPI_CSI3_CLKP', 'MIPI_CSI3_D1N', 'MIPI_CSI3_D1P', 'AVDD18_CSI', 'MIPI_CSI3_D2N', 'MIPI_CSI3_D2P', 'MIPI_CSI2_CLKN', 'MIPI_CSI2_CLKP', 'AVDD18_CSI', 'MIPI_CSI3_D3N', 'MIPI_CSI3_D3P'],
            '其他核心电源': ['AVDD18_EFUSE', 'AVDDU_PHY', 'AVDDU_PHY', 'AVDDU_PHY', 'AVDDU_PHY', 'AVDDU_PHY'],
            'PCIe接口': ['PCIEC_TX0P', 'PCIEC_TX0N', 'PCIEC_RX0P', 'PCIEC_RX0N', 'PCIEC_REFCLK_P', 'PCIEC_REFCLK_N', 'PCIEC_RX1P', 'PCIEC_RX1N', 'VSSU_PCIEC', 'VSSU_PCIEC', 'PCIEC_TX1P', 'PCIEC_TX1N', 'PCIEB_RX0P', 'PCIEB_RX0N', 'VSSU_PCIEC', 'VSSU_PCIEC', 'AVDD18_PCIEC', 'PCIEB_TX0P', 'PCIEB_TX0N', 'PCIEB_REFCLK_P', 'PCIEB_REFCLK_N', 'VSSU_PCIEB', 'VSSU_PCIEB', 'AVDD18_PCIEB', 'PCIEB_TX1P', 'PCIEB_TX1N', 'PCIEB_RX1P', 'PCIEB_RX1N', 'VSSU_PCIEA', 'VSSU_PCIEA', 'PCIEA_TXN', 'PCIEA_TXP', 'AVDD18_PCIEA', 'PCIEA_RXN', 'PCIEA_RXP', 'PCIEA_R_EXT', 'PCIEA_REFCLK_N', 'PCIEA_REFCLK_P'],
            'USB接口': ['AVDD18_USB', 'AVDD33_USB', 'USB2_DN', 'USB2_DP', 'AVDD33_USB', 'AVDD18_USB', 'AVDD33_USB', 'USB1_DN', 'USB1_DP', 'USB0_DN', 'USB0_DP'],
            '音频接口': ['AVDD3V3_AUD', 'AUD_GNDSNS', 'AVDD18_AUD', 'AVDD18_AUD', 'AUD_VSSU', 'AUD_VDDU09', 'AUD_REFGND', 'AUD_AUREF10'],
            'MIPI DSI接口': ['AVDD18_DSI1', 'MIPI_DSI1_D3N', 'MIPI_DSI1_D3P', 'AVDD12_DSI1', 'MIPI_DSI1_D2N', 'MIPI_DSI1_D2P', 'MIPI_DSI1_CLKN', 'MIPI_DSI1_CLKP', 'MIPI_DSI1_D1N', 'MIPI_DSI1_D1P', 'MIPI_DSI1_D0N', 'MIPI_DSI1_D0P'],
        }

        return [pin for pin in self.pins if pin.name in category_pins.get(category, [])]

# Convenience function to create K1_SoC instance

def k1_soc(**kwargs):
    """
    Create and return a K1_SoC component instance.

    Args:
        **kwargs: Additional arguments to pass to Component constructor

    Returns:
        K1_SoC: Instance of K1_SoC component
    """
    return K1_SoC(**kwargs)

if __name__ == '__main__':
    # Example usage
    k1 = k1_soc()
    print(f"Created K1_SoC with {len(k1.pins)} pins")

    # List all categories
    categories = ['DDR/LPDDR接口', 'GPIO', 'JTAG', 'HDMI接口', 'MIPI CSI接口', 
                  'PCIe接口', 'USB接口', 'SD/eMMC接口', 'QSPI接口', 
                  '时钟和参考', '电源管理和控制', '音频接口', '电源和地']

    for category in categories:
        pins = k1.get_pins_by_category(category)
        print(f"{category}: {len(pins)} pins")
