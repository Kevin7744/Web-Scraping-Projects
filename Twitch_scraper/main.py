from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from parsel import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pprint

# launch the chrome browser
driver = webdriver.Chrome()
options = Options()
options.headless = False # hide GUI
options.add_argument("--window-size=1920, 1080") #set window size to native gui size
options.add_argument("start-maximized") #ensure window is full screen

# configure chrome browser to not load images and javascript
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option (
    # Disable image loading
    "prefs", {"profile.managed_default_content_settings.images" : 2}
)
driver = webdriver.Chrome(options=options)
driver.get("https://www.twitch.tv/directory/game/Art")
# find last item and scroll to it
driver.execute_script("""
let items=document.querySelectorAll('.tw-tower>div');
items[items.length-1].scrollIntoView();
""")

# Wait for page to load
element = WebDriverWait(driver=driver, timeout=5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-target=directory-first-item]'))
)
driver.page_source

sel = Selector(text=driver.page_source)
parsed = []
for item in sel.xpath("//div[contains(@class,'tw-tower')]/div[@data-target]"):
    parsed.append({
        'title': item.css('h3::text').get(),
        'url': item.css('.tw-link::attr(href)').get(),
        'username': item.css('.tw-link::text').get(),
        'tags': item.css('.tw-tag ::text').getall(),
        'viewers': ''.join(item.css('.tw-media-card-stat::text').re(r'(\d+)')),  
    })
pprint.pprint(parsed)
