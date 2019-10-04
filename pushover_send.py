from pushover import Client
from weasyprint import HTML, CSS
import sys
user  = 'u88o975vp68jt3gaoyhfny9uq4cp4c'
token = 'ar3tggesdyxaaz7beq1wxwftscshsk'

from weasyprint.fonts import FontConfiguration


def genimage():
    #font_config = FontConfiguration()
    html = HTML(string='<h1>The title</h1>')
    #css = CSS(string="""@font-face {font-family: Gentium;src: url(http://example.com/fonts/Gentium.otf);}h1 { font-family: Gentium }""",font_config=font_config)
    return html.write_png()




def alert(text, **kwargs):
    """
    >>> alert("Doctest",title="Title", sound="magic",url="https://school4one.com/",attachment=genimage(),url_title="School 4 One Link")
    'OK'
    """
    client = Client(user, api_token=token)
    client.send_message(text, html=1 , **kwargs)
    return 'OK'

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    if len(sys.argv) == 1:
        lines = []
        for line in sys.stdin:
            lines.append(line)
        alert("".join(lines))
    else:
        lst = sys.argv[2:]
        args = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
        alert(sys.argv[1], **args)
