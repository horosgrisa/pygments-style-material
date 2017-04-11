Installation:
=============

Using PyPI and pip:

    pip install pygments-style-material

Manual installation:

    git clone git://github.com/horosgrisa/pygments-style-material.git
    cd pygments-style-material
    python setup.py install


Usage example:
==============

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='material').style
    <class 'pygments_style_material.MaterialStyle'>


Export the style as CSS:
========================

    pygmentize -S material -f html > material.css


Please read the [official documentation][pygments] for further information
on the usage of pygment styles.


[pygments]: http://pygments.org/docs/
