def colors(string, color, back=False):
    """Make things colorfull

    Arguments:
        string {str} -- String to apply colors on
        color {int} -- value of color to apply

    """
    if back:
        return("\033[7;%sm%s\033[0m" % (color, string))
    else:
        return("\033[%sm%s\033[0m" % (color, string))


# TODO: Use this kind of coloring maybe
# class Colors(object):

#     def __init__(self):
#         self.color = "\033[{}m{}\033[0m"

#     def green(self, arg):
#         return self.color.format(92, arg)
