from weasyprint import HTML, CSS
from PIL import Image
import io
from inky import InkyWHAT

inkywhat = InkyWHAT('red')

html = HTML(string='<h1>The title</h1>')
png = html.write_png()
image = Image.open(io.BytesIO(png)).resize([400,300]).convert('1')

inkywhat.set_image(image)
inkywhat.show()
