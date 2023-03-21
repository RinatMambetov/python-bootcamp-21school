def calculate_averages(variables):
    respiration = sum([v[0] for v in variables]) / len(variables)
    heart_rate = sum([v[1] for v in variables]) / len(variables)
    blushing_level = sum([v[2] for v in variables]) / len(variables)
    pupillary_dilation = sum([v[3] for v in variables]) / len(variables)

    return respiration, heart_rate, blushing_level, pupillary_dilation
