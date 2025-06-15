import json
import re
import pandas as pd
import requests
import time
import hashlib
import urllib.parse

from Inquire import get_product_by_id

target = input("请输入想要的商品:")
target_encoded = urllib.parse.quote(target)

url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'
em_token = "9f9663534b3bb38c877ae73965b3921d"
eT = int(time.time()*1000)
# eT = 1746679149587
eC = "12574478"
ep_data = '{"appId":"34385","params":"{\\"device\\":\\"HMA-AL00\\",\\"isBeta\\":\\"false\\",\\"grayHair\\":\\"false\\",\\"from\\":\\"nt_history\\",\\"brand\\":\\"HUAWEI\\",\\"info\\":\\"wifi\\",\\"index\\":\\"4\\",\\"rainbow\\":\\"\\",\\"schemaType\\":\\"auction\\",\\"elderHome\\":\\"false\\",\\"isEnterSrpSearch\\":\\"true\\",\\"newSearch\\":\\"false\\",\\"network\\":\\"wifi\\",\\"subtype\\":\\"\\",\\"hasPreposeFilter\\":\\"false\\",\\"prepositionVersion\\":\\"v2\\",\\"client_os\\":\\"Android\\",\\"gpsEnabled\\":\\"false\\",\\"searchDoorFrom\\":\\"srp\\",\\"debug_rerankNewOpenCard\\":\\"false\\",\\"homePageVersion\\":\\"v7\\",\\"searchElderHomeOpen\\":\\"false\\",\\"search_action\\":\\"initiative\\",\\"sugg\\":\\"_4_1\\",\\"sversion\\":\\"13.6\\",\\"style\\":\\"list\\",\\"ttid\\":\\"600000@taobao_pc_10.7.0\\",\\"needTabs\\":\\"true\\",\\"areaCode\\":\\"CN\\",\\"vm\\":\\"nw\\",\\"countryNum\\":\\"156\\",\\"m\\":\\"pc\\",\\"page\\":1,\\"n\\":48,\\"q\\":\\"' + target_encoded + '\\",\\"qSource\\":\\"url\\",\\"pageSource\\":\\"a21bo.jianhua/a.search_history.d1\\",\\"tab\\":\\"all\\",\\"pageSize\\":48,\\"totalPage\\":100,\\"totalResults\\":4800,\\"sourceS\\":\\"0\\",\\"sort\\":\\"_coefp\\",\\"bcoffset\\":\\"\\",\\"ntoffset\\":\\"\\",\\"filterTag\\":\\"\\",\\"service\\":\\"\\",\\"prop\\":\\"\\",\\"loc\\":\\"\\",\\"start_price\\":null,\\"end_price\\":null,\\"startPrice\\":null,\\"endPrice\\":null,\\"itemIds\\":null,\\"p4pIds\\":null,\\"p4pS\\":null,\\"categoryp\\":\\"\\",\\"ha3Kvpairs\\":null,\\"myCNA\\":\\"\\",\\"screenResolution\\":\\"1536x864\\",\\"userAgent\\":\\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36\\",\\"couponUnikey\\":\\"\\"}"}'
string = em_token + "&" + str(eT) + "&" + eC + "&" + ep_data
MD5 = hashlib.md5()
MD5.update(string.encode('utf-8'))
sign = MD5.hexdigest()
headers = {
    "cookie": 'cookie2=1b127d8797526a018911669c88186a98; t=6f7bc56dd2418124446b619be3cf92af; thw=cn; 3PcFlag=1746612668892; unb=2201510739868; uc1=cookie14=UoYaje%2F4vIfPXQ%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjA%2Bl&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&pas=0&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D; sn=; uc3=id2=UUphy%2FeEAKGD%2FLIDtQ%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&vt3=F8dD2EXa0BMJWesurFI%3D&nk2=F5RDKJg2jIE28Vc%3D; csg=03a59aec; lgc=tb642647044; cancelledSubSites=empty; cookie17=UUphy%2FeEAKGD%2FLIDtQ%3D%3D; dnk=tb642647044; skt=7be409c6127d176f; existShop=MTc0NjYxMjcxNw%3D%3D; uc4=id4=0%40U2grEJAXozmILrxFZI4pzucjhBpfP19W&nk4=0%40FY4I65JrgQLdUcUeBSU%2FMfKzDVdekA%3D%3D; tracknick=tb642647044; _cc_=WqG3DMC9EA%3D%3D; _l_g_=Ug%3D%3D; sg=482; _nk_=tb642647044; cookie1=U7UxYbCCpV9Ly%2BjPrHfpXQ7HToE2uVFJ2JLwyujuGvo%3D; wk_cookie2=1b163e3a67d31a7f0e07189f134f0160; wk_unb=UUphy%2FeEAKGD%2FLIDtQ%3D%3D; sgcookie=E100XZTiFw%2B8eDwtJTpDgv4UKcXCfSwAZ2TXQaYN4H%2FWrQznazoSKunStYE2%2FAjrjZpqgrLGnfe0vT4Ff886PpMhx2q%2FXDssX343fzwg6NjJU7w%3D; aui=2201510739868; _tb_token_=3d6b5fb5e34d; _samesite_flag_=true; mtop_partitioned_detect=1; _m_h5_tk=9f9663534b3bb38c877ae73965b3921d_1746784667842; _m_h5_tk_enc=2ed406ce048a34bb75e8178c7618f08c; sca=ccfa09a7; bxuab=0; tfstk=g2oSCbf1H_f5osZddzv4C5LrCoZIyK-NN9wKIvIPpuE89qMiO7JHruubOjhbwgJkryFIZuUnzWPzOkMn1KRwbhkoEk4p_C-Nl97XOlwdy6PLMu2UrIJVghkoEkX59duvb9iyUk4dJWhLDreaFkeLJMEvhJw_9kF8JsQYBSELvJI8MSeuIwI8vXHvhJVY9kU-9rpbKjFpG-Y7wY9oBj5bILqSeSsdv0K3P5iG8MsIc8aSbYFjLvobFzN_JJ6hM0hqp0ouoU_8xxusO2h9gaP-5RGb74O1VfGupvwKNhX_M0MIcz0Vwae_V7at2PKFAYaKlmZr2Bbi3xN85ou2oQzUVbggszLDiXMbaXn7k_O4TVkq2rG9giG3R2nzD0dvfgldb59saw6bSMwb_K9f-wAWccnAMCqGQze03cJXh__3y-2b_K9f-w48n-zwhK15-; isg=BENDk7ESL7e4bOPFVAjXnbwM0gftuNf6oP5iRHUh16IZNGZW-YxmSnrirsR6ki_y',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

params = {
    'jsv': '2.7.2',
    'appKey': eC,
    't': eT,
    'sign': sign,
    'api': 'mtop.relationrecommend.wirelessrecommend.recommend',
    'v': '2.0',
    'type': 'jsonp',
    'dataType': 'jsonp',
    'callback': 'mtopjsonp11',
    'data': ep_data
}


res = requests.get(url, headers=headers, params=params)

text = res.text
json_str = re.findall(r'mtopjsonp\d+\((.*)', text)[0][:-1]
json_data = json.loads(json_str)

# 提取商品信息所在列
itemsArray = json_data['data']['itemsArray']
# 循环提取列表元素
records = []
for item in itemsArray:
    record = {
        '商品ID': item.get('item_id', ''),
        '标题': item.get('title', ''),
        '价格（元）': item.get('price', ''),
        '成交量': item.get('realSales', ''),
        '商品折扣信息': item.get('shopDiscountInfo', ''),
        '所在城市': item.get('procity', ''),
        '是否付费推广': item.get('isP4p', ''),
        '主图URL': item.get('pic_path', ''),
    }

    # 完善商品链接
    url = item.get('auctionURL', '')
    if url.startswith('//'):
        url = 'https:' + url
    record['商品链接'] = url

    # 拆分 extraParams 中的 key/value，并为它们设定中文列名
    for param in item.get('extraParams', []):
        key = param.get('key')
        val = param.get('value')
        if key == 'skuId':
            record['SKU 编号'] = val
    # 补充价格信息
    price_desc = item.get('priceShow', {})
    record['价格（元）'] += price_desc.get('priceDesc', '')
    # shopInfo 中提取店铺信息
    shop = item.get('shopInfo', {})
    record['店铺名称'] = shop.get('title', '')
    record['店铺链接'] = shop.get('url', '')

    records.append(record)

# 转为 DataFrame
df = pd.DataFrame(records)


df.to_csv(f'{target}商品.csv', index=False, encoding='utf-8-sig')
print("已成功导出：")
print(f" - {target}商品信息.csv")

while True:
    print("\n\n可以开始查询,输入商品ID即可查询,输入ccc退出\n")
    itemId = input('请输入商品ID:')
    if itemId == 'ccc':
        break
    res = get_product_by_id(f'{target}商品.csv', itemId)
    if res:
        print('查询成功\n\n')
        print(res)
    else:
        print('没有查到该商品信息\n')



