from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from threading import Thread

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://www.autovit.ro/")
class Car():
    def AcceptCookies(self):
        button = driver.find_element(By.ID,"onetrust-accept-btn-handler")
        button.click()
    

    def CarSearching(self):
        pass

    def runall(self):
        if __name__ == '__main__':
            Thread(target=self.AcceptCookies).start()
            Thread(target=self.CarSearching).start()




run = Car()
run.runall()


#<button id="onetrust-accept-btn-handler">Accept</button>
