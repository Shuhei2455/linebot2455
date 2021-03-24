import requests,datetime,webbrowser
from bs4 import BeautifulSoup

what_day_url = 'https://kids.yahoo.co.jp/today/'
wr = requests.get(what_day_url)
wbs = BeautifulSoup(wr.content, 'html.parser')

tenki_url = 'https://tenki.jp/forecast/7/37/6710/34212/'
tr = requests.get(tenki_url)
tbs = BeautifulSoup(tr.content, 'html.parser')

oushi_url = 'https://service.smt.docomo.ne.jp/portal/fortune/src/fortune_02.html'
mizugame_url = 'https://service.smt.docomo.ne.jp/portal/fortune/src/fortune_11.html'
r = requests.get(oushi_url)
r1 = requests.get(mizugame_url)
bs = BeautifulSoup(r.content, 'html.parser')
bs1 = BeautifulSoup(r1.content, 'html.parser')

#交際
cupple_day = datetime.date(2019,4,9)
today = datetime.date.today()
days = str(today - cupple_day).strip(', 0:00:00')

#日にち
day = wbs.find('h2').contents[1].string
date = wbs.find('h2').contents[3].string

#今日は何の日
whats_day = wbs.find('dt').contents[0].string
whats_day_detail = wbs.find('dd').string

#場所
place = tbs.find('h2').contents[0]

#天気
today = tbs.find(class_='today-weather') 
weather = today.p.string

#気温
temp =today.div.find(class_='date-value-wrap')
temp=temp.find_all("dd")
temp_max = temp[0].contents[0].string #最高気温
temp_max_diff=temp[1].string #最高気温の前日比
temp_min = temp[2].contents[0].string #最低気温
temp_min_diff=temp[3].string #最低気温の前日比

#星座
oushi_number = bs.find(class_='val').find('p').text
od = bs.find(class_='all box').find_all('p')
oushi_detail = od[2].text
mizugame_number = bs1.find(class_='val').find('p').text
md = bs1.find(class_='all box').find_all('p')
mizugame_detail = md[2].text


message = '\n♡ {} ♡\n'.format(days) + '\n今日は{}'.format(day) + '{}\n'.format(date) + '{}です。\n'.format(whats_day)+'{}\n'.format(whats_day_detail) + '\n\n今日の{}は、\n'.format(place) + "  {}\n".format(weather)+"最高気温は{}℃{} \n".format(temp_max,temp_max_diff)+"最低気温は{}℃{}\nです。".format(temp_min,temp_min_diff) + '\n\n\n今日の牡牛座は{}です。\n'.format(oushi_number)+'{}\n\n'.format(oushi_detail) + '今日の水瓶座は{}です。\n'.format(mizugame_number) + '{}\n'.format(mizugame_detail)


print(message)
access_token ='CPlnLOtXl8bJOrRe1d6qaLmwD5YhiBHdpjQ0YGlUeCe'
headers = {'Authorization': 'Bearer ' + access_token}

url = "https://notify-api.line.me/api/notify"
payload = {'message': message}
requests.post(url, headers=headers, params=payload)

webbrowser.open('shortcuts://')

