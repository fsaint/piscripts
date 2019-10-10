from weasyprint import HTML, CSS
from PIL import Image
import io
from inky import InkyWHAT
import markdown2
md = """
#Felipe ... this is a test 

|Action  |Key  |
|:------:|:-----:|
|▛      | ^⌥K |
|▜      | ^⌥J |


"""
html = markdown2.markdown(md, extras = ['tables'])
css = """
@page {size: 400px 300px; margin:0;}
table *
{
   font-size: 1em !important;
   color: #000 !important;
   font-family: "Arial Black", Gadget, sans-serif !important;
   font-weight: 900;
}
table {
    width: 50%;
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
