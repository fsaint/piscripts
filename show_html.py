from weasyprint import HTML, CSS
from PIL import Image
import io
from inky import InkyWHAT

html = """
<h1>   Felipe ... this is a test </h1>
<table>
<tr>
   <td>
       A1 ⌘ ⌥ ⌫ ⇧
   </td>
   <td>
       A2
   </td>
</tr>
</table>
"""

css = """
@page {size: 400px 300px; margin:0;}
table *
{
   font-size: 1em !important;
   color: #000 !important;
   font-family: Arial !important;
   font-weight: 900;
}
table {
    width: 100%;
    height: 100%;
    border: 1px solid black;
}
"""
inkywhat = InkyWHAT('red')
html = HTML(string=html)
png = html.write_png(stylesheets = [CSS(string=css)])
image = Image.open(io.BytesIO(png)).resize([400,300]).convert('P')
inkywhat.set_image(image)
inkywhat.show()
