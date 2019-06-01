from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from promo_code_parser import Beautiful_Soup
from twilio.rest import Client

#Open chrome driver for dynamic web scraping
driver = webdriver.Chrome()
driver.get('https://twitter.com/ChipotleTweets')

#Enter twilio account info here
account_sid = 'ACCOUNT_SID'
auth_token = 'TOKEN'

#Check message execution
execute = False

#Connect to twilio api
client = Client(account_sid, auth_token)

#Instantiate custom class that utilizes BeautifulSoup library
code_parser = Beautiful_Soup()

#CTRL-C to exit program
try:
    while True:
        #Refresh the web browser to get updates
        driver.refresh()
        #Return webpage HTML after fully loaded
        res = driver.execute_script("return document.documentElement.outerHTML")
        #Parse HTML to get code
        code = code_parser.find_new_code(res)
        try:
            message = client.messages \
                        .create(
                            body=code,
                            from_='PHONE',
                            to='PHONE'
                        )
            print(message.sid)
        except Exception:
            if code:
                print(code)

except KeyboardInterrupt:
    #Close Chrome driver
    driver.quit()

