import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json
url='https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
#真实data
data={
    'csrf_token': "",
'cursor': "-1",
'offset': "0",
'orderType': "1",
'pageNo': "1",
'pageSize': "20",
'rid': "R_SO_4_487434788",
'threadId': "R_SO_4_487434788"
}
#处理加密过程
f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
e='010001'
g='0CoJUm6Qyw8W8jud'
i="hvAbR0YGWTYhcNqr"
encseckey="b1f668bb79b4fcde1e07443a4827edc372e9f20ea7e56f71946d9d06ac0395d1de8581bd414cc6e1771bde01a07c8c45c97730a2f9440639c5442838464fe4b6fbfa1b01f1cfc92f1f78509394ac3684359a802d4f3b71d8a169c0d5d838eef343ec20dec9bfe118369d2f330549e26f75a1b7807894559ec0c257847a56508e"
def get_params(data):#默认data是字符串
    first=enc_params(data,g)
    second=enc_params(first,i)
    return second
def to_16(data):
    pad=16-len(data)%16
    data+=chr(pad)*pad
    return data
def enc_params(data,key):
    iv="0102030405060708"
    aes=AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)#创造加密器(key(byte),IV偏移量)
    bs=aes.encrypt(to_16(data).encode('utf-8'))
    return str(b64encode(bs),'utf-8')#转化成字符串
resp=requests.post(url,data={
    'params':get_params(json.dumps(data)),
    'encSecKey':encseckey
})
print(resp.text)
print(get_params(json.dumps(data)))
resp.close()
"""
!function() {
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,#随机数
            e = Math.floor(e),#取整
            c += b.charAt(e);#随机取b中一个字母
        return c
    }
    function b(a, b) {#a要加密的内容，data
        var c = CryptoJS.enc.Utf8.parse(b)#转换成c，密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)#data的转换
          , f = CryptoJS.AES.encrypt(e, c#是密钥, {
            iv: d,#偏移量
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {d是数据，e是010001，
    f是'00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g是'0CoJUm6Qyw8W8jud'
        var h = {}
          , i = a(16);#i是16位随机值
顶死i="88YsEG5OXqNYO0Ki"
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),#返回paramas,两次加密，g，i均是密钥
        h.encSecKey = c(i, e, f),#返回encseckey，又c里面不产生随机数，把i设成定值，则该值不变
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e
}();
"""
