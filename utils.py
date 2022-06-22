def clean_name(name, delimiter=' '):
    return name.split(delimiter)[-1].lower()


def num_text(num, pos):
    if num >= 1e9:
        text = '{:1.1f}B'.format(num * 1e-9)
    elif num >= 1e6:
        text = '{:1.1f}M'.format(num * 1e-6)
    elif num >= 1e3:
        text = '{:1.1f}K'.format(num * 1e-3)
    else:
        text = '{:1.0f}'.format(num)
    return text


def num_curr(num, pos):
    if num >= 1e9:
        curr = '{:1.1f}B'.format(num * 1e-9)
    elif num >= 1e6:
        curr = '{:1.1f}M'.format(num * 1e-6)
    elif num >= 1e3:
        curr = '{:1.1f}K'.format(num * 1e-3)
    else:
        curr = '{:1.1f}'.format(num)
    return curr


def text_cap(text, pos):
    caps = text.capitalize()
    return caps


def num_cent(num, pos):
    cent = '{:1.1f}%'.format(num)
    return cent
