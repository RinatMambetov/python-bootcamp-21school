def calculate_averages(variables):
    respiration = sum([v[0] for v in variables]) / len(variables) if len(variables) > 0 else 0
    heart_rate = sum([v[1] for v in variables]) / len(variables) if len(variables) > 0 else 0
    blushing_level = sum([v[2] for v in variables]) / len(variables) if len(variables) > 0 else 0
    pupillary_dilation = sum([v[3] for v in variables]) / len(variables) if len(variables) > 0 else 0

    return respiration, heart_rate, blushing_level, pupillary_dilation
