def prompt_user(question, responses):
    """
    Function: prompt_user
    This function prompts the user with a question and a set of responses and collects the user's responses
    to the questions.

    Args:
    question (str): The question to ask the user.
    responses (list): A list of strings representing the possible responses to the question.

    Returns: tuple: A tuple containing the user's selected response as a string and a tuple of the user's
    physiological measurements (respiration rate, heart rate, blushing level, pupillary dilation).

    Raises:
    ValueError: If the user enters an invalid response or an invalid physiological measurement value.
    """
    
    print(question)
    for i, r in enumerate(responses):
        print(f"{i + 1}. {r}")

    response = None
    while response is None:
        try:
            response = int(input("Enter your response (1-4): "))
            if response < 1 or response > 4:
                print("Invalid response. Please enter a number between 1 and 4.")
                response = None
        except ValueError:
            print("Invalid input. Please enter a number.")

    respiration = None
    while respiration is None:
        try:
            respiration = int(input("Enter your respiration (0-30 BPM): "))
            if respiration < 0 or respiration > 30:
                print("Invalid respiration measurement. Please enter a number between 0 and 30.")
                respiration = None
        except ValueError:
            print("Invalid input. Please enter a number.")

    heart_rate = None
    while heart_rate is None:
        try:
            heart_rate = int(input("Enter your heart rate (0-150 BPM): "))
            if heart_rate < 0 or heart_rate > 150:
                print("Invalid heart rate measurement. Please enter a number between 0 and 150.")
                heart_rate = None
        except ValueError:
            print("Invalid input. Please enter a number.")

    blushing_level = None
    while blushing_level is None:
        try:
            blushing_level = int(input("Enter your blushing level (1-6): "))
            if blushing_level < 1 or blushing_level > 6:
                print("Invalid blushing level. Please enter a number between 1 and 6.")
                blushing_level = None
        except ValueError:
            print("Invalid input. Please enter a number.")

    pupillary_dilation = None
    while pupillary_dilation is None:
        try:
            pupillary_dilation = int(input("Enter your pupillary dilation (2-8 mm): "))
            if pupillary_dilation < 2 or pupillary_dilation > 8:
                print("Invalid pupillary dilation measurement. Please enter a number between 2 and 8.")
                pupillary_dilation = None
        except ValueError:
            print("Invalid input. Please enter a number.")

    return responses[response - 1], (respiration, heart_rate, blushing_level, pupillary_dilation)
