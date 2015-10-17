from django import http
from django.template.loader import get_template
from django.template import Context
import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
import cgi


def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(
        html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(),
                                 content_type='application/pdf')
    return http.HttpResponse('Gremlin\'s ate your pdf! % s' % cgi.escape(html))
