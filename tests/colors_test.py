import colorful

from pure import colors


def test_base_colors():
    assert str(colors.primary('foo')) == str(colorful.purple1('foo'))
    assert str(colors.info('foo')) == str(colorful.blue('foo'))
    assert str(colors.mute('foo')) == str(colorful.grey('foo'))
    assert str(colors.success('foo')) == str(colorful.green('foo'))
    assert str(colors.normal('foo')) == str(colorful.darkGray('foo'))
    assert str(colors.danger('foo')) == str(colorful.red3('foo'))
    assert str(colors.light('foo')) == str(colorful.white('foo'))
    assert str(colors.warning('foo')) == str(colorful.orange('foo'))
    assert str(colors.dark('foo')) == str(colorful.black('foo'))