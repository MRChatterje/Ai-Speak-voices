from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import warnings
from time import sleep
import pathlib

warnings.simplefilter('ignore')

try:
    url = 'https://ttsmp3.com/'
    chrome_opt = Options()
    scriptDirectory = pathlib.Path().absolute()
    chrome_opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_opt.add_argument("--headless=new")
    #chrome_opt.add_experimental_option("detach", True) #leave that commented for backgroud use
    chrome_opt.add_argument('--log-level=3')
    chrome_opt.add_argument("--disable-features=NetworkService")
    chrome_opt.add_argument("--use-fake-ui-for-media-stream")  
    chrome_opt.add_argument("--use-fake-device-for-media-stream")
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    chrome_opt.add_argument(f'user-agent={user_agent}')
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    browser = webdriver.Chrome(service=service, options=chrome_opt)
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(url)


    def voiceSelect():
        xpath = '//*[@id="sprachwahl"]'        
        select_element = browser.find_element(by=By.XPATH, value=xpath)
        select = Select(select_element)
        select.select_by_visible_text('British English / Brian')       



    def speak(text):
        voiceSelect()

        xpath1 = '//*[@id="voicetext"]'
        textbox = browser.find_element(by=By.XPATH, value=xpath1)
        textbox.send_keys(str(text))

        xpath2 = '/html/body/div[3]/div[2]/form/input[1]'
        button = browser.find_element(by=By.XPATH , value=xpath2)
        browser.execute_script("arguments[0].click();", button)

        xpath3 = '//*[@id="voicetext"]'
        textboxcl =  browser.find_element(by=By.XPATH, value=xpath3)
        textboxcl.clear()


        print(f'AI : {text}')


    # speak('hey mr chatterjee')
    # sleep(2)
    # speak('how are you doin')
    # sleep(2)
    # speak('hows you day')
   



except Exception as e:
    print(e)