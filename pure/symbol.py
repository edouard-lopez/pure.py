from pure import colors

SUCCESS = 0


def prompt(last_command_status=SUCCESS):
    symbol = colors.primary('❯') if last_command_status == SUCCESS else colors.danger('❯')
    return symbol
