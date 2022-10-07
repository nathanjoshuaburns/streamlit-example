def get_icon(coords) -> str:
    icon_name = "cloud" # Default to cloud
    temperature = 0
    humidity = 0

    print(coords)

    # TEST
    if coords == [48.14244663381307, -2.8732976551510263]:
        temperature = 31

    if temperature >= 30 and humidity > 100:
        icon_name = "facloud-sun-rain"
    elif temperature >= 30:
        icon_name = "fasun"
    elif humidity > 100:
        icon_name = "facloud-rain"
    else:
        icon_name = "facloud"

    return icon_name