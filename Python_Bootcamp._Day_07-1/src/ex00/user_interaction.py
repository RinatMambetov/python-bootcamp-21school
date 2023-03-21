def prompt_user(question, responses):
    print(question)
    for i, r in enumerate(responses):
        print(f"{i + 1}. {r}")
    response = int(input("Enter your response (1-4): "))
    respiration = int(input("Enter your respiration (0-30 BPM): "))
    heart_rate = int(input("Enter your heart rate (0-150 BPM): "))
    blushing_level = int(input("Enter your blushing level (1-6): "))
    pupillary_dilation = int(input("Enter your pupillary dilation (2-8 mm): "))

    return responses[response - 1], (respiration, heart_rate, blushing_level, pupillary_dilation)
