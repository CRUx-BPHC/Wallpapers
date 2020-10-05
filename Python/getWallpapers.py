import requests
image_base_path="./Bing/"
markets=["EN-IN", "EN-US", "ZH-CN", "JA-JP", "EN-AU", "EN-UK", "DE-DE", "EN-NZ", "EN-CA"]
def bing():
    for mkt in markets:
        image_file_name="bing"
        r = requests.get('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt='+mkt)
        for img in r.json()['images']:
            image = requests.get('http://www.bing.com/'+img['url'])
            if image.status_code == 200:
                image_file_name=image_base_path+'bing_'+mkt+img['enddate']+'.jpg'
                with open(image_file_name, 'wb') as f:
                    f.write(image.content)
                return
bing()
