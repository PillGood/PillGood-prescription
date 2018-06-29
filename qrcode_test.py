import qrcode
import json
import urllib.request
import datetime



def init(vinsureType,vfilledDate,vpName,vpidNum,vhName,vphone,vfax,vemail,vdiseaseNum,vdName,vlicType,vlicNum,vpillList,vuseBefore,vpharmName,vpharmacist,vpillQty,vpillDate):
    global data
    data = [{'insureType' : vinsureType,
            'filledDate' : vfilledDate,
            'patient' : {'pName' : vpName, 'pidNum' : vpidNum}
            'hospital' : {'hName' : vhName, 'phone' : vphone, 'fax':vfax, 'email':vemail}
            'diseaseNum' : vdiseaseNum
            'doctor' : {'dName' : vdName, 'licType' : vlicType, 'licNum' : vlicNum}
            'pill' : [vpillList],
            'useBefore' : vuseBefore,
            'pharmacy' : {'pharmName' : vpharmName, 'pharmcist' : vpharmacist, 'pillQty' : vpillQty, 'pillDate' : vpillDate }
            }]

if __name__ == '__main__':
    data = 0
    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border=4,
    )

    now = datetime.datetime.now()
    drug1 = {'pillname' : '설리드정', ''}
    init("의료보험","2018/06/29","헤롱이","960319-1075519","성심병원","02-000-0000","02-000-1111","st.s@hallym.or.kr","H208",
    "한예진","의사","155346",,"2018/07/06","약장수약국","약장수","30","2018/06/29")
    json_data = json.dumps(data)
    qr.add_data(json_data)
    qr.make(fit = True)

    img = qr.make_image()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    imgname = "qrcode_"+nowDatetime+".jpg"
    img.save(imgname)