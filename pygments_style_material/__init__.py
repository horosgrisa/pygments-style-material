# -*- coding: utf-8 -*-
"""
    material
    ~~~~~~~~~~

    Material colorscheme.

    :copyright: Copyright 2019 Grigorii Horos
    :license: GPL3, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Generic, Keyword, Other, Whitespace, Literal, Name, Number, Operator, \
    Punctuation, String, Text


"""

BASE03 LIGHT_BLACK = "#1c1c1c"
BASE02 = "#262626"
BASE01 LIGHT_GREEN = "#4e4e4e"
BASE00 = "#585858"
BASE0 LIGHT_BLUE = "#808080"
BASE1 = "#8a8a8a"
BASE2 = "#d7d7af"
BASE3 = "#ffffd7"

YELLOW = "#af8700"
ORANGE = "#d75f00"
RED = "#af0000"
MAGENTA = "#af005f"
VIOLET = "#5f5faf"
BLUE = "#0087ff"
CYAN = "#00afaf"
GREEN = "#5f8700"


"""

BLACK = "#435B67"
RED = "#EF5350"
GREEN = "#66BB6A"
ORANGE = "#FFEE58"
BLUE = "#42A5F5"
PURPLE = "#AB47BC"
CYAN = "#26C6DA"
GREY = "#FAFAFA"

LIGHT_BLACK = "#A1B0B8"
LIGHT_RED = "#EF9A9A"
LIGHT_GREEN = "#A5D6A7"
LIGHT_ORANGE = "#FFF59D"
LIGHT_BLUE = "#90CAF9"
LIGHT_PURPLE = "#CE93D8"
LIGHT_CYAN = "#80DEEA"
LIGHT_GREY = "#FFFFFF"

BACKGROUND_COLOR = '#1c252a'
HIGHLIGHT_COLOR = '#435a66'


class MaterialStyle(Style):
  """
  Material colorscheme.
  """

  default_style = ''

  background_color = BACKGROUND_COLOR
  highlight_color = HIGHLIGHT_COLOR

  styles = {
      Text:                   LIGHT_BLUE,           # light_blue  ; class: ''
      Whitespace:             LIGHT_BLACK,          # light_black ; class: 'w'
      Error:                  RED,                  # red    ; class: 'err'
      Other:                  LIGHT_BLUE,           # light_blue  ; class: 'x'

      Comment:                'italic '+LIGHT_BLACK, # light_black ; class: 'c'
      Comment.Multiline:      'italic '+LIGHT_BLACK, # light_black ; class: 'cm'
      Comment.Preproc:        'italic '+LIGHT_BLACK, # light_black ; class: 'cp'
      Comment.Single:         'italic '+LIGHT_BLACK, # light_black ; class: 'c1'
      Comment.Special:        'italic '+LIGHT_BLACK, # light_black ; class: 'cs'

      Keyword:                GREEN,                 # green  ; class: 'k'
      Keyword.Constant:       GREEN,                 # green  ; class: 'kc'
      Keyword.Declaration:    GREEN,                 # green  ; class: 'kd'
      Keyword.Namespace:      ORANGE,                # orange ; class: 'kn'
      Keyword.Pseudo:         ORANGE,                # orange ; class: 'kp'
      Keyword.Reserved:       GREEN,                 # green  ; class: 'kr'
      Keyword.Type:           GREEN,                 # green  ; class: 'kt'

      Operator:               LIGHT_BLUE,            # light_blue  ; class: 'o'
      Operator.Word:          GREEN,                 # green  ; class: 'ow'

      Name:                   LIGHT_GREEN,           # light_green  ; class: 'n'
      Name.Attribute:         LIGHT_BLUE,            # light_blue  ; class: 'na'
      Name.Builtin:           BLUE,                  # blue   ; class: 'nb'
      Name.Builtin.Pseudo:    'bold '+BLUE,          # blue   ; class: 'bp'
      Name.Class:             BLUE,                  # blue   ; class: 'nc'
      Name.Constant:          PURPLE,                # purple ; class: 'no'
      Name.Decorator:         ORANGE,                # orange ; class: 'nd'
      Name.Entity:            ORANGE,                # orange ; class: 'ni'
      Name.Exception:         ORANGE,                # orange ; class: 'ne'
      Name.Function:          BLUE,                  # blue   ; class: 'nf'
      Name.Property:          BLUE,                  # blue   ; class: 'py'
      Name.Label:             LIGHT_BLUE,            # light_blue  ; class: 'nc'
      Name.Namespace:         PURPLE,                # purple ; class: 'nn'
      Name.Other:             LIGHT_BLUE,            # light_blue  ; class: 'nx'
      Name.Tag:               GREEN,                 # green  ; class: 'nt'
      Name.Variable:          ORANGE,                # orange ; class: 'nv'
      Name.Variable.Class:    BLUE,                  # blue   ; class: 'vc'
      Name.Variable.Global:   BLUE,                  # blue   ; class: 'vg'
      Name.Variable.Instance: BLUE,                  # blue   ; class: 'vi'

      Number:                 CYAN,                  # cyan   ; class: 'm'
      Number.Float:           CYAN,                  # cyan   ; class: 'mf'
      Number.Hex:             CYAN,                  # cyan   ; class: 'mh'
      Number.Integer:         CYAN,                  # cyan   ; class: 'mi'
      Number.Integer.Long:    CYAN,                  # cyan   ; class: 'il'
      Number.Oct:             CYAN,                  # cyan   ; class: 'mo'

      Literal:                LIGHT_BLUE,            # light_blue  ; class: 'l'
      Literal.Date:           LIGHT_BLUE,            # light_blue  ; class: 'ld'

      Punctuation:            LIGHT_BLUE,            # light_blue  ; class: 'p'

      String:                 CYAN,                  # cyan   ; class: 's'
      String.Backtick:        CYAN,                  # cyan   ; class: 'sb'
      String.Char:            CYAN,                  # cyan   ; class: 'sc'
      String.Doc:             CYAN,                  # cyan   ; class: 'sd'
      String.Double:          CYAN,                  # cyan   ; class: 's2'
      String.Escape:          ORANGE,                # orange ; class: 'se'
      String.Heredoc:         CYAN,                  # cyan   ; class: 'sh'
      String.Interpol:        ORANGE,                # orange ; class: 'si'
      String.Other:           CYAN,                  # cyan   ; class: 'sx'
      String.Regex:           CYAN,                  # cyan   ; class: 'sr'
      String.Single:          CYAN,                  # cyan   ; class: 's1'
      String.Symbol:          CYAN,                  # cyan   ; class: 'ss'

      Generic:                LIGHT_BLUE,            # light_blue  ; class: 'g'
      Generic.Deleted:        LIGHT_BLUE,            # light_blue  ; class: 'gd'
      Generic.Emph:           LIGHT_BLUE,            # light_blue  ; class: 'ge'
      Generic.Error:          LIGHT_BLUE,            # light_blue  ; class: 'gr'
      Generic.Heading:        LIGHT_BLUE,            # light_blue  ; class: 'gh'
      Generic.Inserted:       LIGHT_BLUE,            # light_blue  ; class: 'gi'
      Generic.Output:         LIGHT_BLUE,            # light_blue  ; class: 'go'
      Generic.Prompt:         LIGHT_BLUE,            # light_blue  ; class: 'gp'
      Generic.Strong:         LIGHT_BLUE,            # light_blue  ; class: 'gs'
      Generic.Subheading:     LIGHT_BLUE,            # light_blue  ; class: 'gu'
      Generic.Traceback:      LIGHT_BLUE,            # light_blue  ; class: 'gt'
  }
