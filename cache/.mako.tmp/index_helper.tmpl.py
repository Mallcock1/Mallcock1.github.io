# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487772939.616
_enable_loop = True
_template_filename = u'c:/users/matt/anaconda2/lib/site-packages/nikola/data/themes/base/templates/index_helper.tmpl'
_template_uri = u'index_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['mathjax_script', 'html_pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        any = context.get('any', UNDEFINED)
        use_katex = context.get('use_katex', UNDEFINED)
        katex_auto_render = context.get('katex_auto_render', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if any(post.is_mathjax for post in posts):
            if use_katex:
                __M_writer(u'            <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.js"></script>\n            <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/contrib/auto-render.min.js"></script>\n')
                if katex_auto_render:
                    __M_writer(u'                <script>\n                    renderMathInElement(document.body,\n                        {\n                            ')
                    __M_writer(unicode(katex_auto_render))
                    __M_writer(u'\n                        }\n                    );\n                </script>\n')
                else:
                    __M_writer(u'                <script>\n                    renderMathInElement(document.body);\n                </script>\n')
            else:
                __M_writer(u'            <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>\n')
                if mathjax_config:
                    __M_writer(u'            ')
                    __M_writer(unicode(mathjax_config))
                    __M_writer(u'\n')
                else:
                    __M_writer(u'            <script type="text/x-mathjax-config">\n            MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n            </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        prevlink = context.get('prevlink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if prevlink or nextlink:
            __M_writer(u'        <nav class="postindexpager">\n        <ul class="pager">\n')
            if prevlink:
                __M_writer(u'            <li class="previous">\n                <a href="')
                __M_writer(unicode(prevlink))
                __M_writer(u'" rel="prev">')
                __M_writer(unicode(messages("Newer posts")))
                __M_writer(u'</a>\n            </li>\n')
            if nextlink:
                __M_writer(u'            <li class="next">\n                <a href="')
                __M_writer(unicode(nextlink))
                __M_writer(u'" rel="next">')
                __M_writer(unicode(messages("Older posts")))
                __M_writer(u'</a>\n            </li>\n')
            __M_writer(u'        </ul>\n        </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "21": 19, "22": 50, "28": 21, "36": 21, "37": 22, "38": 23, "39": 24, "40": 26, "41": 27, "42": 30, "43": 30, "44": 34, "45": 35, "46": 39, "47": 40, "48": 41, "49": 42, "50": 42, "51": 42, "52": 43, "53": 44, "59": 2, "66": 2, "67": 3, "68": 4, "69": 6, "70": 7, "71": 8, "72": 8, "73": 8, "74": 8, "75": 11, "76": 12, "77": 13, "78": 13, "79": 13, "80": 13, "81": 16, "87": 81}, "uri": "index_helper.tmpl", "filename": "c:/users/matt/anaconda2/lib/site-packages/nikola/data/themes/base/templates/index_helper.tmpl"}
__M_END_METADATA
"""
