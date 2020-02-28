from urllib.request import urlopen

URL = 'ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt'
COMMENT_CHARS = '#:'

if __name__ == '__main__':
    lines = open('Predict.txt')
    data = []
    for line in lines:
        if not line.isspace() and not line[0] in COMMENT_CHARS:
            data.append( [float(item) for item in line.split(' ') if not item == ''])
    print(data)
