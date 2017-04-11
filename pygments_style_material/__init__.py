# -*- coding: utf-8 -*-
"""
    material
    ~~~~~~~~~~

    Material colorscheme.

    :copyright: Copyright 2017 Grigorii Horos
    :license: GPL3, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, \
                           Punctuation, String, Text


class MaterialStyle(Style):
    """
    Material colorscheme.
    """

    default_style = ''

    background_color = '#1c252a'
    highlight_color = '#435a66'

    styles = {
        Comment:                'italic #435a66',

        Error:                  '#fb3841',

        Keyword:                '#fed032',
        Keyword.Reserved:       '#fee16c',
        Keyword.Type:           '#36b6fe',

        Name:                   '#fffefe',
        Name.Attribute:         '#fb216e',
        Name.Builtin:           '#36b6fe',
        Name.Builtin.Pseudo:    '#fffefe',
        Name.Class:             '#fed032',
        Name.Constant:          '#fb216e',
        Name.Decorator:         '#fc736d',
        Name.Function:          '#fed032',
        Name.Tag:               '#fc736d',

        Number:                 '#5cf09e',

        Operator:               '#6fcefe',
        Operator.Word:          '#6fcefe',

        Punctuation:            '#6fcefe',

        String:                 '#5cf09e',
        String.Escape:          '#5cf09e',

        Text:                   '#fffefe',
    }
