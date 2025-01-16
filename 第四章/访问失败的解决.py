import requests
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
resp=requests.get(url='https://v2.qstuvwx.com/202308/22/ijuDiFd8WR2/video/2000k_1080/hls/11218_3AspY.jpeg',headers=headers)
with open('error.ts',mode='wb') as f:
    f.write(resp.content)
resp.close()