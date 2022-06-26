import requests
headers = {
    'authority': 'baza.drom.ru',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': 'ring=c71ebe3WeYqPTsf7z7arJ9583%2BaBA0a2; cookie_cityid=3; cookie_regionid=54; apple-pay-available=0; google-pay-available=1; review_x_url=9f5bd25c22d58d294506c2975f1dcecc4d891387; my_geo=54; _ga=GA1.2.1345874365.1642410774; last_search_auto_compatibility=model%3D%25CB%25E0%25E4%25E0%2B2107%26autoPartsEngine%3D2107; last_search_disc_size=wheelPcd%255B0%255D%3D100.00x5; dr_df=1; PHPSESSID=0adbc02b76ca0885d12bac94e0251129; city=135',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

def my_request(location, partnumber):
    drom_url = 'https://baza.drom.ru/' + location+ '/sell_spare_parts/?query=' + partnumber + '&sortBy=pricea'
    emex_url = 'http://emex.ru/products/' + partnumber
    exist_url = 'https://www.exist.ru/Price/?pcode=' + partnumber
    drom_response = requests.get(drom_url, headers=headers)
    #emex_response = requests.get(emex_url, headers=emex_headers)
    print(drom_response.text)
    with open('drom.html', 'w') as file:
        file.write(drom_response.text)




