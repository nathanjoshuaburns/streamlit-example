def get_icon(coords) -> str:
    icon_name = "cloud" # Default to cloud
    temperature = 0
    humidity = 0

    print(coords)

    # TEST
    if coords == [48.14244663381307, -2.8732976551510263]:
        temperature = 31
        humidity = 102

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