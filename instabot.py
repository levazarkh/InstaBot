import time
from selenium import webdriver
import random


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver.exe')

    def closebrowser(self):
        self.driver.close()

    def login(self):
        self.driver.get('https://www.instagram.com')
        time.sleep(2)

        user_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        user_button.click()
        time.sleep(2)

        user_element = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(1)

        pass_element = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        pass_element.clear()
        pass_element.send_keys(self.password)
        time.sleep(1)

        login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
        login_button.click()
        time.sleep(5)

    def likemaking(self, hashtags):
        for hashtag in hashtags:
            self.driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
            time.sleep(3)

            #liking pictures
            first_pic = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')
            first_pic.click()
            time.sleep(2)
            like_button = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button[1]')
            like_button.click()

    def like_photos(self, hashtags, total_likes=0):
        self.hashtags = hashtags
        for hashtag in self.hashtags:
            like_count = 0
            self.driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
            time.sleep(2)
            #scrolling page
            for i in range(1, 5):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(2, 20, 1))
            #getting list of pictures
            href1s = self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div/div/a')
            for each in href1s:
                each.click()
                time.sleep(random.randrange(2, 20, 1))
                #liking pictures
                try:
                    time.sleep(5)
                    problem_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[1]')
                    problem_button.click()
                except:
                    try:
                        like_button = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                        like_button.click()
                        like_count += 1
                        total_likes += 1
                        time.sleep(random.randrange(2, 20, 1))
                        close_button = self.driver.find_element_by_xpath('/html/body/div/button')
                        close_button.click()
                    except:
                        close_button = self.driver.find_element_by_xpath('/html/body/div/button')
                        close_button.click()
                time.sleep(random.randrange(20, 200, 10))
            href2s = self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div/div/a')
            for each in href2s:
                each.click()
                time.sleep(random.randrange(2, 20, 1))
                try:
                    time.sleep(5)
                    problem_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[1]')
                    problem_button.click()
                except:
                    try:
                        like_button = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                        like_button.click()
                        like_count += 1
                        total_likes += 1
                        time.sleep(random.randrange(2, 20, 1))
                        close_button = self.driver.find_element_by_xpath('/html/body/div/button')
                        close_button.click()
                    except:
                        close_button = self.driver.find_element_by_xpath('/html/body/div/button')
                        close_button.click()
                time.sleep(random.randrange(20, 200, 10))
            print(hashtag + ": ", like_count)
            print(hashtag, ' ', time.ctime())
            print('=================================')
            time.sleep(random.randrange(900, 1200, 60))
        print('Total likes given: ', total_likes)


print('=================================')
print('Begin: ', time.ctime())
print('=================================')
levazarkh = InstagramBot("username", "password")
levazarkh.login()
levazarkh.like_photos(['mood', 'fashion', 'kiev', 'beautifulgirl', 'model', 'photography', 'beautiful', 'art', 'girl',
                       'inspire', 'portrait', 'lifeportraits', '35mm', 'videography',
                       'shotoncanon', 'photogear', 'dji', 'videoedits', 'modelukraine'
                       'dslr', 'cinema', 'camerasetup'])
print('=================================')
print('End: ', time.ctime())
print('=================================')

# this_amazing_art = InstagramBot("this.amazing.art", "Rkfdbfnehf&123")
# this_amazing_art.login()
# this_amazing_art.like_photos(['art'])
