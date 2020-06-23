from typing import Any, Dict

import numpy as np


def generate_metrics(feat: str, cdf_variable) -> Dict[str, Any]:
    data = cdf_variable[:]
    valid_range = ""

    if hasattr(cdf_variable, "valid_range"):
        valid_range = str(cdf_variable.valid_range)
    

    feat_info = {
        "name": feat,
        "long_name": cdf_variable.long_name.decode("utf-8"),
        "units": cdf_variable.units.decode("utf-8"),
        "valid_range": valid_range, 
        "current_shape": str(data.shape),
        "mu": np.format_float_scientific(np.mean(data), precision=2),
        "std": np.format_float_scientific(np.std(data), precision=2),
        "max": np.format_float_scientific(np.amax(data), precision=2),
        "min": np.format_float_scientific(np.amin(data), precision=2),
    }

    return feat_info
