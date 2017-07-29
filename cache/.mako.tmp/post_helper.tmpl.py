# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501361846.029
_enable_loop = True
_template_filename = u'c:/users/matthew/anaconda/lib/site-packages/nikola/data/themes/base/templates/post_helper.tmpl'
_template_uri = u'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_tags', 'html_pager', 'twitter_card_information', 'meta_translations', 'mathjax_script', 'open_graph_metadata']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.tags:
            __M_writer(u'        <ul itemprop="keywords" class="tags">\n')
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer(u'            <li><a class="tag p-category" href="')
                    __M_writer(unicode(_link('tag', tag)))
                    __M_writer(u'" rel="tag">')
                    __M_writer(filters.html_escape(unicode(tag)))
                    __M_writer(u'</a></li>\n')
            __M_writer(u'        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.prev_post or post.next_post:
            __M_writer(u'        <ul class="pager hidden-print">\n')
            if post.prev_post:
                __M_writer(u'            <li class="previous">\n                <a href="')
                __M_writer(unicode(post.prev_post.permalink()))
                __M_writer(u'" rel="prev" title="')
                __M_writer(filters.html_escape(unicode(post.prev_post.title())))
                __M_writer(u'">')
                __M_writer(unicode(messages("Previous post")))
                __M_writer(u'</a>\n            </li>\n')
            if post.next_post:
                __M_writer(u'            <li class="next">\n                <a href="')
                __M_writer(unicode(post.next_post.permalink()))
                __M_writer(u'" rel="next" title="')
                __M_writer(filters.html_escape(unicode(post.next_post.title())))
                __M_writer(u'">')
                __M_writer(unicode(messages("Next post")))
                __M_writer(u'</a>\n            </li>\n')
            __M_writer(u'        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer(u'    <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(unicode(twitter_card.get('card', 'summary'))))
            __M_writer(u'">\n')
            if 'site:id' in twitter_card:
                __M_writer(u'    <meta name="twitter:site:id" content="')
                __M_writer(unicode(twitter_card['site:id']))
                __M_writer(u'">\n')
            elif 'site' in twitter_card:
                __M_writer(u'    <meta name="twitter:site" content="')
                __M_writer(unicode(twitter_card['site']))
                __M_writer(u'">\n')
            if 'creator:id' in twitter_card:
                __M_writer(u'    <meta name="twitter:creator:id" content="')
                __M_writer(unicode(twitter_card['creator:id']))
                __M_writer(u'">\n')
            elif 'creator' in twitter_card:
                __M_writer(u'    <meta name="twitter:creator" content="')
                __M_writer(unicode(twitter_card['creator']))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            for langname in sorted(translations):
                if langname != lang and ((not post.skip_untranslated) or post.is_translation_available(langname)):
                    __M_writer(u'                <link rel="alternate" hreflang="')
                    __M_writer(unicode(langname))
                    __M_writer(u'" href="')
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        use_katex = context.get('use_katex', UNDEFINED)
        katex_auto_render = context.get('katex_auto_render', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.is_mathjax:
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


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_open_graph:
            __M_writer(u'    <meta property="og:site_name" content="')
            __M_writer(filters.html_escape(unicode(blog_title)))
            __M_writer(u'">\n    <meta property="og:title" content="')
            __M_writer(filters.html_escape(unicode(post.title()[:70])))
            __M_writer(u'">\n    <meta property="og:url" content="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
            if post.description():
                __M_writer(u'    <meta property="og:description" content="')
                __M_writer(filters.html_escape(unicode(post.description()[:200])))
                __M_writer(u'">\n')
            else:
                __M_writer(u'    <meta property="og:description" content="')
                __M_writer(filters.html_escape(unicode(post.text(strip_html=True)[:200])))
                __M_writer(u'">\n')
            if post.previewimage:
                __M_writer(u'    <meta property="og:image" content="')
                __M_writer(unicode(url_replacer(permalink, post.previewimage, lang, 'absolute')))
                __M_writer(u'">\n')
            __M_writer(u'    <meta property="og:type" content="article">\n')
            if post.date.isoformat():
                __M_writer(u'    <meta property="article:published_time" content="')
                __M_writer(unicode(post.formatted_date('webiso')))
                __M_writer(u'">\n')
            if post.tags:
                for tag in post.tags:
                    __M_writer(u'           <meta property="article:tag" content="')
                    __M_writer(filters.html_escape(unicode(tag)))
                    __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 11, "23": 23, "24": 40, "25": 69, "26": 85, "27": 116, "33": 13, "39": 13, "40": 14, "41": 15, "42": 16, "43": 17, "44": 18, "45": 18, "46": 18, "47": 18, "48": 18, "49": 21, "55": 25, "60": 25, "61": 26, "62": 27, "63": 28, "64": 29, "65": 30, "66": 30, "67": 30, "68": 30, "69": 30, "70": 30, "71": 33, "72": 34, "73": 35, "74": 35, "75": 35, "76": 35, "77": 35, "78": 35, "79": 38, "85": 71, "90": 71, "91": 72, "92": 73, "93": 73, "94": 73, "95": 74, "96": 75, "97": 75, "98": 75, "99": 76, "100": 77, "101": 77, "102": 77, "103": 79, "104": 80, "105": 80, "106": 80, "107": 81, "108": 82, "109": 82, "110": 82, "116": 3, "124": 3, "125": 4, "126": 5, "127": 6, "128": 7, "129": 7, "130": 7, "131": 7, "132": 7, "138": 87, "145": 87, "146": 88, "147": 89, "148": 90, "149": 92, "150": 93, "151": 96, "152": 96, "153": 100, "154": 101, "155": 105, "156": 106, "157": 107, "158": 108, "159": 108, "160": 108, "161": 109, "162": 110, "168": 42, "178": 42, "179": 43, "180": 44, "181": 44, "182": 44, "183": 45, "184": 45, "185": 46, "186": 46, "187": 47, "188": 48, "189": 48, "190": 48, "191": 49, "192": 50, "193": 50, "194": 50, "195": 52, "196": 53, "197": 53, "198": 53, "199": 55, "200": 60, "201": 61, "202": 61, "203": 61, "204": 63, "205": 64, "206": 65, "207": 65, "208": 65, "214": 208}, "uri": "post_helper.tmpl", "filename": "c:/users/matthew/anaconda/lib/site-packages/nikola/data/themes/base/templates/post_helper.tmpl"}
__M_END_METADATA
"""
