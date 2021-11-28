from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import pandas as pd

def scrape_UC_courses(path_to_save):
    
    req = Request("https://www.ucalgary.ca/pubs/calendar/current/course-desc-main.html")
    html_page = urlopen(req)
    
    soup = BeautifulSoup(html_page, "lxml")
    
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))
        
    
    base_url = 'https://www.ucalgary.ca/pubs/calendar/current/'
    
    links_filter = [x for x in links if 'course' not in x]
    links_filter = links_filter[42:]
    
    combine_df = pd.DataFrame()
    for l in range(0, len(links_filter)):
        url = base_url+links_filter[l]
        #print(url)
        scrape_raw = pd.read_html(url)
        df = scrape_raw[2]
        df['Course_Category'] = links_filter[l].replace('.html','')
        combine_df = pd.concat([combine_df, df], axis=0)
        
    return combine_df
    
#example usage
#from scrape_UC_courses import *
#scrape_UC_courses('./save_to_here/scraped_courses.csv')
