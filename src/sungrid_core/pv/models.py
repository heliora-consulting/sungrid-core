from dataclasses import dataclass

@dataclass
class PanelSpecs:
    """Standard STC specifications for a Solar Module."""
    model_name: str
    p_max: float        # Wattage (W)
    voc: float          # Open Circuit Voltage (V)
    isc: float          # Short Circuit Current (A)
    temp_coeff_voc: float # % per Degree C (e.g., -0.29)

@dataclass
class InverterSpecs:
    """Specifications for a String Inverter."""
    model_name: str
    max_input_voltage: float # V
    mppt_voltage_min: float  # V
    mppt_voltage_max: float  # V
