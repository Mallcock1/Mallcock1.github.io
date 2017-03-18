# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1489869943.623
_enable_loop = True
_template_filename = u'c:/users/matthew/anaconda/lib/site-packages/nikola/data/themes/bootstrap3/templates/listing.tmpl'
_template_uri = u'listing.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'ui', context._clean_inheritance_tokens(), templateuri=u'crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def content():
            return render_content(context)
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(ui.bar(crumbs)))
        __M_writer(u'\n')
        if folders or files:
            __M_writer(u'<ul>\n')
            for name in folders:
                __M_writer(u'    <li><a href="')
                __M_writer(filters.url_escape(unicode(name)))
                __M_writer(u'"><i class="glyphicon glyphicon-folder-open"></i> ')
                __M_writer(filters.html_escape(unicode(name)))
                __M_writer(u'</a>\n')
            for name in files:
                __M_writer(u'    <li><a href="')
                __M_writer(filters.url_escape(unicode(name)))
                __M_writer(u'.html"><i class="glyphicon glyphicon-file"></i> ')
                __M_writer(filters.html_escape(unicode(name)))
                __M_writer(u'</a>\n')
            __M_writer(u'</ul>\n')
        if code:
            __M_writer(u'<h1>')
            __M_writer(unicode(title))
            __M_writer(u'\n')
            if source_link:
                __M_writer(u'        <small><a href="')
                __M_writer(unicode(source_link))
                __M_writer(u'">(')
                __M_writer(unicode(messages("Source")))
                __M_writer(u')</a></small>\n')
            __M_writer(u'    </h1>\n    ')
            __M_writer(unicode(code))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        def sourcelink():
            return render_sourcelink(context)
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if source_link:
            __M_writer(u'    <li>\n    <a href="')
            __M_writer(unicode(source_link))
            __M_writer(u'" id="sourcelink">')
            __M_writer(unicode(messages("Source")))
            __M_writer(u'</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 27, "129": 28, "130": 29, "131": 29, "132": 29, "133": 29, "139": 133, "23": 3, "29": 0, "48": 2, "49": 3, "54": 24, "59": 32, "65": 4, "81": 4, "82": 5, "83": 5, "84": 6, "85": 7, "86": 8, "87": 9, "88": 9, "89": 9, "90": 9, "91": 9, "92": 11, "93": 12, "94": 12, "95": 12, "96": 12, "97": 12, "98": 14, "99": 16, "100": 17, "101": 17, "102": 17, "103": 18, "104": 19, "105": 19, "106": 19, "107": 19, "108": 19, "109": 21, "110": 22, "111": 22, "117": 26, "127": 26}, "uri": "listing.tmpl", "filename": "c:/users/matthew/anaconda/lib/site-packages/nikola/data/themes/bootstrap3/templates/listing.tmpl"}
__M_END_METADATA
"""
