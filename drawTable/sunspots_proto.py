from urllib.request import urlopen

from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.shapes import Drawing, PolyLine, String
from reportlab.lib import colors

URL = 'ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt'
COMMENT_CHARS = '#:'
lines = open('Predict.txt')
data = []
for line in lines:
    if not line.isspace() and not line[0] in COMMENT_CHARS:
        data.append([float(item) for item in line.split(' ') if not item == ''])

drawing = Drawing(400, 200)
pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1] / 12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [list(zip(times, pred)),
           list(zip(times, high)),
           list(zip(times, low))]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green
drawing.add(lp)
drawing.add(String(250, 150, 'Sunspots', fontSize=14, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')
if __name__ == '__main__':
    pass
# data =[]
# for line in urlopen(URL).readlines():
#     line = line.decode()
#     if not line.isspace() and not line[0] in COMMENT_CHARS:
#         print(line)
