def calculate_averages(variables):
    """
    Function: calculate_averages Calculates the average values of respiration, heart rate, blushing level,
    and pupillary dilation from a list of variables.

    Args:
    variables: a list of tuples, where each tuple contains four values (respiration, heart rate, blushing level,
    and pupillary dilation)

    Returns:
    A tuple containing four floats: the average respiration, average heart rate, average blushing level, and average
    pupillary dilation. If the input list is empty, all values will be zero.
    """

    respiration = sum([v[0] for v in variables]) / len(variables) if len(variables) > 0 else 0
    heart_rate = sum([v[1] for v in variables]) / len(variables) if len(variables) > 0 else 0
    blushing_level = sum([v[2] for v in variables]) / len(variables) if len(variables) > 0 else 0
    pupillary_dilation = sum([v[3] for v in variables]) / len(variables) if len(variables) > 0 else 0

    return respiration, heart_rate, blushing_level, pupillary_dilation
