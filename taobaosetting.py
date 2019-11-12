MONGO_URL = 'localhost' #在处理以mongodb为例，也可自己添加数据库api
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
ISToDB=False    #是否存储到数据库中
KEYWORD = 'ic卡' #你要搜索的关键词
MAX_PAGE = 100  #页数
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
weibo_user=''    #在此输入你的weibo账号（尽量输入手机号或者邮箱的形式
weibo_pawd=''    #weibo密码
login_url='https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
def extract_cookies(cookie):
    """从浏览器或者request headers中拿到cookie字符串，提取为字典格式的cookies"""
    cookies = dict([l.split("=", 1) for l in cookie.split("; ")])
    return cookies
headers = {
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
cookies=extract_cookies('thw=cn; v=0; t=968eebed1469c77695bc10096987b410; cookie2=1a51629b82aff3cf0c5afcc9c5ef0e32; _tb_token_=efb73784e9e7a; cna=QqQ8FqmuzmECAatcmlkjlnDK; unb=2139709278; uc3=vt3=F8dByuchWQq0cMCFqEE%3D&id2=UUkNbZ2u7JdL9g%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&nk2=sDIlKOXJDfAnBA%3D%3D; csg=e5bfc616; lgc=%5Cu786C%5Cu6C49%5Cu7A0B%5Cu4E0D%5Cu4E8C; cookie17=UUkNbZ2u7JdL9g%3D%3D; dnk=%5Cu786C%5Cu6C49%5Cu7A0B%5Cu4E0D%5Cu4E8C; skt=f1a561fd807e080c; existShop=MTU3MjE4OTc5Mg%3D%3D; uc4=nk4=0%40ssom%2F3RymDh%2FRYIpACUmgYuilZH4&id4=0%40U2uBZguz4RBVq632Dpam1QyLrStO; tracknick=%5Cu786C%5Cu6C49%5Cu7A0B%5Cu4E0D%5Cu4E8C; _cc_=VT5L2FSpdA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=%E4%BA%8C8f; _nk_=%5Cu786C%5Cu6C49%5Cu7A0B%5Cu4E0D%5Cu4E8C; cookie1=Vq8wncmIQ%2FA0hg%2Fne8k9cCOBxUyGktnxLhaPCtTFEmI%3D; enc=A5ZIoZWM%2BnXiKIEyG74Otk9%2B7m9clhwtZqpUxnQUt83KOllQU7kXv2UownayjXd9Ily6SEqmUfqgBL56UQarew%3D%3D; mt=ci=110_1; hng=CN%7Czh-CN%7CCNY%7C156; JSESSIONID=BE20216D1061BF5C5833A60E0588C978; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; l=dBOaczwVqGRgpfJbKOCMCZOSsab99IRAguWfVDWki_5CE6Y13z_OkaG26Fv6cjWftnYB4NSLztv9-etlmKa0mGt-g3fPrxDc.; isg=BG5utluev-zD5suIfua3_xNwv8Q642WngyWDzZg36HEsew7VAP4xeTk5N6cyoyqB; uc1=cookie14=UoTbnxk2wUDkcA%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3Dreferer: https://www.taobao.com/?spm=a230r.1.0.0.70d15268m34ADS')
