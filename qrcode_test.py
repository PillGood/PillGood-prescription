import qrcode
import json
import urllib.request
import datetime



def init(vinsureType,vfilledDate,vpName,vpidNum,vhName,vphone,vfax,vemail,vdiseaseName,vdName,vlicType,vlicNum,vpillList,vuseBefore,vpharmName,vpharmacist,vpillQty,vpillDate):
    global data
    data = [{'insureType' : vinsureType,
            'filledDate' : vfilledDate,
            'patient' : {'pName' : vpName, 'pidNum' : vpidNum},
            'hospital' : {'hName' : vhName, 'phone' : vphone, 'fax':vfax, 'email':vemail},
            'diseaseName' : vdiseaseName,
            'doctor' : {'dName' : vdName, 'licType' : vlicType, 'licNum' : vlicNum},
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
    t = datetime.datetime(2018, 6, 29)
    due = datetime.datetime(2018, 7, 3)
    pdate = datetime.datetime(2018, 7, 1)
    now = datetime.datetime.now()
    drug = list()
    drug.append({'pillname' : '슬로젠정', 'qty':'1', 'num':'3','days':'3','instruction':'식후 30분'})
    drug.append({'pillname' : '파모시드정', 'qty':'1', 'num':'3','days':'3','instruction':'식후 30분'})
    init("의료보험",(t-datetime.datetime.fromtimestamp(0)).total_seconds(),"헤롱이","960319-1075519","성심병원","02-000-0000","02-000-1111","st.s@hallym.or.kr","출혈이 있는 급성 위궤양",
    "한예진","의사","155346",drug,(due-datetime.datetime.fromtimestamp(0)).total_seconds(),"약장수약국","약장수","18",(pdate-datetime.datetime.fromtimestamp(0)).total_seconds())

   
    json_data = json.dumps(data,ensure_ascii=False)
   # k_data = json_data.decode('euc-kr')
    #print(json_data)
    qr.add_data(json_data)
    qr.make(fit = True)

    img = qr.make_image()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    imgname = "qrcode_"+nowDatetime+".jpg"
    img.save(imgname)