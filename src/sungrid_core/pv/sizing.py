from typing import Dict, Any
from .models import PanelSpecs, InverterSpecs

class StringSizer:
    """
    Validates PV string lengths against NEC 690.7 standards.
    """
    def __init__(self, panel: PanelSpecs, inverter: InverterSpecs, min_temp_c: float = -10.0):
        self.panel = panel
        self.inverter = inverter
        self.min_temp_c = min_temp_c

    def calculate_max_voltage(self, modules_per_string: int) -> float:
        """
        Calculates Voc_max based on coldest ambient temperature.
        Formula: Voc_max = Voc * (1 + (Temp_Coeff * (T_min - 25))) * N
        """
        # Convert percentage (e.g., -0.29) to decimal (-0.0029)
        coeff = self.panel.temp_coeff_voc / 100.0
        delta_t = self.min_temp_c - 25.0
        
        correction_factor = 1 + (coeff * delta_t)
        voc_corrected = self.panel.voc * correction_factor
        
        return round(voc_corrected * modules_per_string, 2)

    def validate(self, modules_per_string: int) -> Dict[str, Any]:
        max_v = self.calculate_max_voltage(modules_per_string)
        is_safe = max_v <= self.inverter.max_input_voltage
        
        return {
            "valid": is_safe,
            "max_string_voltage": max_v,
            "limit": self.inverter.max_input_voltage,
            "status": "SAFE" if is_safe else "CRITICAL: EXCEEDS INVERTER LIMIT"
        }
