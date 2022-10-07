def get_icon(coords) -> str:
    icon_name = "cloud" # Default to cloud
    temperature = 0
    humidity = 0

    if temperature > 30 and humidity > 100:
        icon_name = "cloud-sun-rain"
    elif temperature > 30:
        icon_name = "sun"
    elif humidity > 100:
        icon_name = "cloud-rain"
    else:
        icon_name = "cloud"

    return icon_name