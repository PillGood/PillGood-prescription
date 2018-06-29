import qrcode
import json
import urllib.request
import datetime
data = 0
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border=4,
)

now = datetime.datetime.now()

def init(vinsureType):
    global data
    data = {'insureType':vinsureType}


json_data = json.dumps(data)
qr.add_data(json_data)
qr.make(fit = True)

img = qr.make_image()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
imgname = "qrcode_"+nowDatetime+".jpg"
img.save(imgname)