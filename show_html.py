from weasyprint import HTML, CSS
from PIL import Image
import io
import markdown2

def sq(top = 0, left = 0, width = 6, height = 5 ):
     return f"""
<div style="width: 12px; height: 12px; border: 1px solid black;">
<div style="position: relative; top: {top}px; left: {left}px;width: {width}px; height: {height}px; background-color: black;"></div>
</div>
""".replace("\n","")
     
md = f"""
|Act  |Key  |
|:------:|:-----:|
|{sq(top = 0, width = 6, height = 6, left = 0)}      | ^⌥U |
|{sq(top = 0, width = 6, height = 6, left = 6)}      | ^⌥I |
|{sq(top = 6, width = 6, height = 6, left = 6)}      | ^⌥K |
|{sq(top = 6, width = 6, height = 6, left = 0)}      | ^⌥J |
|{sq(top = 0, width = 4, height = 12, left = 0)}      | ^⌥D |
|{sq(top = 0, width = 8, height = 12, left = 4)}      | ^⌥T |
|Clip | ⇧⌃⌘ 4 |

"""
print(md)
html = markdown2.markdown(md, extras = ['tables'])
css = """
@page {size: 400px 300px; margin:0;}
body {
   background-color: white;
}
table *
{
   font-size: 1em !important;
   color: #000 !important;
   font-family: "Arial Black", Gadget, sans-serif !important;
   font-weight: 900;
}
table {
    width: 33%;
    height: 100%;
    border: 1px solid black;
}
"""
html = HTML(string=html)
png = html.write_png(stylesheets = [CSS(string=css)])
image = Image.open(io.BytesIO(png)).convert('P')
#image = Image.open(io.BytesIO(png)).resize([400,300]).convert('P')
try:
   from inky import InkyWHAT
   inkywhat = InkyWHAT('red')
   inkywhat.set_image(image)
   inkywhat.show()
except:
   image.save("result.png")
