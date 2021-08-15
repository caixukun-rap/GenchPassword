import execjs
def get_js():
    f = open('C:/Users/Administrator/Desktop/gench.js', 'r', encoding='utf-8')#导入js
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr
    
def GenchRsaEncrpyt(password):
    jsstr = get_js()
    js = execjs.compile(jsstr)
    return js.call('aaa',password)#aaa为函数名
    
if __name__ == "__main__":
    pass_ = GenchRsaEncrpyt('你的密码')
    print(pass_)
    


