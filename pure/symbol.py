from pure import colors, constants


def raw():
    return '❯'


def segment(last_command_status=constants.SUCCESS):
    return {
        'text': raw(),
        'style': style(last_command_status)
    }


def style(last_command_status):
    return colors.primary if last_command_status == constants.SUCCESS else colors.danger
