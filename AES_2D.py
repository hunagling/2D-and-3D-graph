import base64
from Crypto.Cipher import AES
import random
import matplotlib.pyplot as plt
'''
采用AES对称加密算法ECB
'''
# str不是32的倍数那就补足为16的倍数
def add_to_32(value):
    while len(value) % 32 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes
#加密方法
def encrypt_oracle(key):
    # 秘钥
    text = 'yun school of softwore'
    # 待加密文本
    # 初始化加密器
    aes = AES.new(add_to_32(key), AES.MODE_ECB)
    #先进行aes加密
    encrypt_aes = aes.encrypt(add_to_32(text))
    # print(set(encrypt_aes))  # 32位 <255
    #用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes   
    return encrypted_text
#解密方法
def decrypt_oralce(text):
    # 秘钥
    key = ''
    # 密文
    # 初始化加密器
    aes = AES.new(add_to_32(key), AES.MODE_ECB)
    #优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    #执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('\0','') 
    return decrypted_text

if __name__ == '__main__':

    count = 1
    Pmax = 0
    Qmax = 0
    Pmaxs = []
    Qmaxs = []
    m = []
    while count <=4000:  # m为2000一个单位

        key = random.randint(99999999999,1000000000000) #12位随机密钥
        key1 = str(key)
        encryptedtext = encrypt_oracle(key1)
        p = encryptedtext.count('1')
        Pmax = Pmax + p
        q = encryptedtext.count('0')
        Qmax = Qmax +q
        if count%25==0:         
            Pmaxs.append(Pmax)   
            Pmax = 0
            Qmaxs.append(Qmax)
            Qmax = 0
            m.append(count)
        count = count +1
     
    print('Pmax', Pmaxs)
    print('Qmax', Qmaxs)
    dictp = {}
    for key in Pmaxs:
        dictp[key] = dictp.get(key, 0) + 1
    Pmaxs = dictp.keys()
    m1 = dictp.values()
    dictq = {}
    for key in Qmaxs:
        dictq[key] = dictq.get(key, 0) + 1
    Qmaxs = dictq.keys()
    m2 = dictq.values()
    
    print('Pmax', Pmaxs)
    print('m1',m1)
    print('Qmax', Qmaxs)
    print('m2',m2)   
    print('success!!!')
    plt.bar(Pmaxs,m1, label='Pmaxs 1')
    #plt.bar(Qmaxs,m2, label='Qmaxs 0')

    plt.legend()
    plt.xlabel('number')
    plt.ylabel('value')
    plt.show()
