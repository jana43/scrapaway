from bs4 import BeautifulSoup
import json
import os

import time 

htmls = os.listdir('htmls/')

main_list = []
for html in htmls:
    print(f'htmls/{html}')
    htm = open(f'htmls/{html}',"r")
    data = htm.read()
    soup = BeautifulSoup(data )

    table = soup.find_all('table' , {"id":"productDetails_techSpec_section_1"})
    about_table = soup.find_all('table',{"id":"productDetails_detailBullets_sections1"})


    th = table[0].find_all('th')
    td = table[0].find_all('td')
    
    ath = about_table[0].find_all('th')
    atd = about_table[0].find_all('td')
    
    tab_dic = {}
    for (head , data ) in zip(th,td):
        head = head.text.replace("\n","")
        head = head.replace("\u200e","")
        head=head.replace(" ","").lower()
        data = data.text.replace("\n","")
        data = data.replace("\u200e","")
        tab_dic[head]= data
      
    
    print("............................................................")
    for (head , data ) in zip(ath,atd):
        head = head.text.replace("\n","")
        head = head.replace("\u200e","")
        head=head.replace(" ","").lower()
        data = data.text.replace("\n","")
        data = data.replace("\u200e","")
        tab_dic[head]= data
      

    print(tab_dic)
    tab_dic["key"] = str(time.time()).replace(".", "")
    try:
        tab_dic["slug"] = tab_dic["genericname"].replace(" ", "_")+tab_dic["itemmodelnumber"].replace(" ", "_")+str(time.time()).replace(".", "")
    except:
        tab_dic["slug"] = " "
    print(tab_dic["asin"])
    ASIN = tab_dic["asin"]
    affliate1 = f'''<iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-in.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=IN&source=ac&ref=qf_sp_asin_til&ad_type=product_link&tracking_id=zcompariz-21&marketplace=amazon&region=IN&placement={ASIN}&asins={ASIN}&show_border=true&link_opens_in_new_window=true&price_color=eb2150&title_color=000000&bg_color=ffffff&linkId=870323cac8d2365ee6a35b0eb16d0cd7">
</iframe>'''

    affliate2 = f'''<a target="_blank"  href="https://www.amazon.in/gp/product/{ASIN}/ref=as_li_tl?ie=UTF8&camp=3638&creative=24630&creativeASIN={ASIN}&linkCode=as2&tag=zcompariz-21"><img border="0" src="//ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=IN&ASIN={ASIN}&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=zcompariz-21&linkId=870323cac8d2365ee6a35b0eb16d0cd7" ></a>'''

    affliate3 = f'''<a target="_blank" href="https://www.amazon.in/gp/product/{ASIN}/ref=as_li_tl?ie=UTF8&camp=3638&creative=24630&creativeASIN={ASIN}&linkCode=as2&tag=zcompariz-21&linkId=870323cac8d2365ee6a35b0eb16d0cd7">Check out</a>'''

    tab_dic["affliate1"] = affliate1
    tab_dic["affliate2"] = affliate2
    tab_dic["affliate3"] = affliate3
    if (len(tab_dic["slug"])>2):
        main_list.append(tab_dic)
    else:
        print("############### data is malformed")


with open('result.json', 'a') as fp:
    json.dump(main_list, fp)