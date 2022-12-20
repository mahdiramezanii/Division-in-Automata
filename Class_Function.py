class String(object):
    def __init__(self, string):
        self.string = string

    def __sub__(self, other):
        if self.string.startswith(other.string):
            return self.string[len(other.string):]

    def __str__(self):
        return self.string

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

def division(s_l_1,s_l_2):
    sub1 = String(s_l_1) - String(s_l_2)

    if sub1 == None:
        s1= reverse(s_l_1)

        sub1 = String(s1) - String(s_l_2)

        return reverse(sub1)
    else:

        return sub1


class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)