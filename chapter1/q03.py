# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
    str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    pattern = re.compile('[.,]')
    print([len(pattern.sub('', word)) for word in str.split()])
