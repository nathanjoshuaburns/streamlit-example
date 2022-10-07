import random

def get_icon(coords, selectedDate) -> str:
    icon_name = "cloud" # Default to cloud
    temperature = 0
    humidity = 0

    # Generate test data
    temperature = random.randint(16, 60)
    humidity = random.randint(50, 150)

    if temperature >= 30 and humidity > 100:
        icon_name = "sun-o"
    elif temperature >= 50:
        icon_name = "fire"
    elif temperature >= 30:
        icon_name = "sun-o"
    elif humidity > 100:
        icon_name = "tint"
    else:
        icon_name = "cloud"

    return icon_name