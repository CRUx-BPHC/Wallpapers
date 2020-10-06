import requests
from datetime import date
today = date.today()
dt=today.strftime("%d%m%Y")
def bing(image_base_path):
    markets=["EN-IN", "EN-US", "ZH-CN", "JA-JP", "EN-AU", "EN-UK", "DE-DE", "EN-NZ", "EN-CA"]
    for mkt in markets:
        image_file_name="bing"
        r = requests.get('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt='+mkt)
        for img in r.json()['images']:
            image = requests.get('http://www.bing.com/'+img['url'])
            if image.status_code == 200:
                image_file_name=image_base_path+'bing_'+dt+'.jpg'
                with open(image_file_name, 'wb') as f:
                    f.write(image.content)
                return

def nasa(image_base_path):
    r = requests.get('http://apod.nasa.gov/apod/astropix.html')
    i=r.text.find("IMG SRC=")+len("IMG SRC=")+1
    j=r.text.find(".jpg",i)+len(".jpg")
    nasa_image_url='http://apod.nasa.gov/apod/'+r.text[i:j]
    image = requests.get(nasa_image_url)
    if image.status_code == 200:
        image_file_name=image_base_path+'nasa_'+dt+'.jpg'
        with open(image_file_name, 'wb') as f:
            f.write(image.content)
        return

def ngc(image_base_path):
    r = requests.get('http://photography.nationalgeographic.com/photography/photo-of-the-day/')
    i=r.text.find('https://www.nationalgeographic.com/content/dam/photography/photo-of-the-day/')
    j=r.text.find('.jpg',i)+len('.jpg')
    ngc_image_url=r.text[i:j]
    image = requests.get(ngc_image_url)
    if image.status_code == 200:
        image_file_name=image_base_path+'ngc_'+dt+'.jpg'
        with open(image_file_name, 'wb') as f:
            f.write(image.content)
        return

bing("./Images/")
nasa("./Images/")
ngc("./Images/")