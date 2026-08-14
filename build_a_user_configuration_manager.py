def add_setting(settings, new_setting):
    new_key, new_value = new_setting
    new_key = new_key.lower()
    new_value = new_value.lower()

    for key in settings.keys():
        if key and key == new_key:
            exist_msg = f"Setting '{key}' already exists! Cannot add a new setting with this name."
            return exist_msg

    if len(settings) == 0 or new_key not in settings.keys():
        # settings.update(new_key=new_value)
        settings[new_key] = new_value
        success_msg = (
            f"Setting '{new_key}' added with value '{new_value}' successfully!"
        )
        return success_msg


def update_setting(settings, new_setting):
    new_key = new_setting[0].lower()
    new_value = new_setting[1].lower()
    for key in settings.keys():
        if key and key == new_key:
            settings[key] = new_value
            update_msg = f"Setting '{key}' updated to '{new_value}' successfully!"
            return update_msg
    if len(settings) == 0 or new_key not in settings.keys():
        settings.update(new_key=new_value)
        failure_msg = (
            f"Setting '{new_key}' does not exist! Cannot update a non-existing setting."
        )
        return failure_msg


def delete_setting(settings, del_setting):
    del_key = del_setting.lower()
    for key in settings.keys():
        if key and key == del_key:
            settings.pop(del_key)
            delete_msg = f"Setting '{del_key}' deleted successfully!"
            return delete_msg
    if len(settings) == 0 or del_key not in settings.keys():
        failed_msg = "Setting not found!"
        return failed_msg


def view_settings(settings):
    if len(settings) == 0:
        empty_msg = "No settings available."
        return empty_msg
    else:
        formatted_list = []

        for key, value in settings.items():
            x = f"{key.capitalize()}: {value}"
            formatted_list.append(x)

        formatted_text = "\n".join(formatted_list)
        return f"Current User Settings:\n{formatted_text}\n"


test_settings = {"developer": "forhad"}


print(add_setting(test_settings, ("Developer", "FORHAD")))
print(test_settings)
