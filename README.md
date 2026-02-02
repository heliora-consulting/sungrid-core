# SunGrid Core Library

**Version:** 0.1.0-alpha  
**Status:** MVP Development  
**Maintainer:** Heliora Engineering Team

## Overview

`sungrid-core` is the standalone engineering engine for the SunGrid.ai platform. It contains the verified physics, mathematics, and validation logic for solar PV system design.

This library is architected to be **framework-agnostic**: it has no dependencies on web frameworks (FastAPI/React) or databases. This ensures that the core engineering logic remains a "Source of Truth" that can be rigorously tested against industry standards (NEC, IEC) and legacy Excel models.

## Module Structure

- `/pv`: Photovoltaic system algorithms (String Sizing, Energy Yield).
- `/electrical`: Cable sizing, voltage drop, and protection coordination.
- `/financial`: LCOE, NPV, and cash flow projection engines.

## Installation

To install this library in a local development environment (e.g., inside the backend service):

```bash
# From the parent directory containing the repo
pip install -e sungrid-core
```

## Usage Example

```python
from sungrid_core.pv.models import PanelSpecs, InverterSpecs
from sungrid_core.pv.sizing import StringSizer

# 1. Define Component Specifications
panel = PanelSpecs(
    model_name="Jinko Tiger Pro 540W",
    p_max=540,
    voc=49.5,
    isc=13.85,
    temp_coeff_voc=-0.29
)

inverter = InverterSpecs(
    model_name="Huawei SUN2000-100KTL",
    max_input_voltage=1100,
    mppt_voltage_min=200,
    mppt_voltage_max=1000
)

# 2. Initialize the Logic Engine
# (min_temp_c is the coldest ambient temperature recorded at site)
sizer = StringSizer(panel, inverter, min_temp_c=10)

# 3. Run Validation
result = sizer.validate(modules_per_string=20)

if result['valid']:
    print(f"Design Safe! Max Voltage: {result['max_string_voltage']}V")
else:
    print(f"CRITICAL ERROR: {result['status']}")
```

## Testing

We use `pytest` to validate engineering accuracy.

```bash
# Run all tests
pytest tests/
```