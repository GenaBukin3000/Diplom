from bs4 import BeautifulSoup
def drom_parser():
    with open('drom.html') as file:
        drom_data = file.read()
    soup = BeautifulSoup(drom_data, 'lxml')
    drom_price = soup.find('span', class_='price-per-quantity__price')
    drom_price = drom_price.get_text()
    drom_price = drom_price.replace(' ', '')
    drom_price = drom_price.replace('₽', '')
    #print(drom_price)
    drom_ref = soup.find('a', class_='bulletinLink bull-item__self-link auto-shy')
    drom_ref = drom_ref.get('href')
    drom_ref = 'https://baza.drom.ru/' + drom_ref
    #print(drom_ref)
    return drom_ref

#def exist_perser():
    #with open ('exist.html', encoding='utf-8', newline='') as file:
        #exist_data = file.read()




























    #price_list = []
    #for price in drom_price:
        #current_price = price.get_text()
        #current_price = current_price.replace(' ', '')
        #current_price = current_price.replace('₽', '')
        #price_list.append(current_price)
        #print(current_price)
    #print(price_list)
    #best_price = min(price_list)
    #print(f'best_price = {best_price}')
    #index = price_list.index(best_price)
    #drom_ref = soup.find_all('a', class_='bulletinLink bull-item__self-link auto-shy')
    #i = 0

    #for ref in drom_ref:
        #if i == index + 1:
            #break
        #i = i + 1
        #link = ref.get('href')
        #link = 'https://baza.drom.ru/' + link
    #print(f'link = {link}')






