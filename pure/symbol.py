from pure import colors, constants


def prompt(last_command_status=constants.SUCCESS):
    symbol = colors.primary('❯') if last_command_status == constants.SUCCESS else colors.danger('❯')
    return symbol
