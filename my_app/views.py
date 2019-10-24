from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
BASE_URL_CRAG="https://mumbai.craigslist.org/search/bbb?query={}&sort=rel"


def index(request):
    return render(request,'base.html',context=None)

def new_search(request):
    search = request.POST.get('search')
    minval = request.POST.get('min')
    
    maxval = request.POST.get('max')
    
    url=f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={quote_plus(search)}&_sacat=0&rt=nc&_udlo={minval}&_udhi={maxval}"
   
    data=requests.get(url)
    soup=BeautifulSoup(data.text,features='html.parser')
  
    final_list=[]
    
    title= soup.find_all(class_='s-item__title')
    title=[x.text for x in title]
    img_url= soup.find_all(class_='s-item__image-img')
    img_url=[y.get('src') for y in img_url]
    price= soup.find_all(class_='s-item__price')
    price=[y.text for y in price]
    item_url= soup.find_all(class_='s-item__link')
    item_url=[y.get('href') for y in item_url]
    for i in range(len(title)):
        final_list.append((title[i],img_url[i],price[i],item_url[i]))
    
    stuff={'search':search,"final_list":final_list}
    return render(request,'my_app/new_search.html',context=stuff)    









