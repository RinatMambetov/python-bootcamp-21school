def make_decision(averages):
    respiration_min = 12
    respiration_max = 16
    heart_rate_min = 60
    heart_rate_max = 100
    blushing_level_min = 3
    blushing_level_max = 4
    pupillary_dilation_min = 4
    pupillary_dilation_max = 4

    is_replicant = (averages[0] < respiration_min or averages[0] > respiration_max
                    or averages[1] < heart_rate_min or averages[1] > heart_rate_max
                    or averages[2] < blushing_level_min or averages[2] > blushing_level_max
                    or averages[3] < pupillary_dilation_min or averages[3] > pupillary_dilation_max)

    if is_replicant:
        return "replicant"
    else:
        return "human"
