import requests
url='https://www.pearvideo.com/video_1797662'
contid=url.split('_')[1]
videoStatus='https://www.pearvideo.com/videoStatus.jsp?contId=1797662&mrd=0.7330931394105344'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'referer':url
}

resp=requests.get(videoStatus,headers=headers)
text=resp.json()
srcurl=text['videoInfo']['videos']['srcUrl']
systemTime=text['systemTime']
srcurl=srcurl.replace(systemTime,'cont-'+contid)
print(srcurl)
with open('good.mp4',mode='wb') as v:
    v.write(requests.get(srcurl).content)
resp.close()