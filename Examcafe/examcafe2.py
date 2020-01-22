import config_file as con
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


def login():
    url = "http://www.examcafe.in/"
    con.driver.get(url)
    time.sleep(3)
    con.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]').click()
    time.sleep(2)
    id = "mishra_divya"
    password = "divya14mishra"
    a = con.driver.find_element_by_name('login')
    a.send_keys(id)
    print("username entered...")
    b = con.driver.find_element_by_id('password')
    b.send_keys(password)
    print("Password entered...")
    b.send_keys(Keys.ENTER)
    time.sleep(2)
    con.driver.switch_to.alert.accept()


def links():
    con.driver.find_element_by_xpath('//*[@id="ot"]').click()
    time.sleep(2)
    html_content = con.driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    div = soup.find_all("div", {"class": "test_box1"})
    # print(soup)
    count = 0
    top_link = []
    try:
        for i in div:
            # print(i)
            a = i.find_all("div", {"class": "test_cattopic2"})
            # print(len(a))
            try:
                for j in a:
                    a_tag = j.find("a")
                    count += 1
                    href = a_tag.get('href')
                    # print(count)    #, " :  "+ "http://www.examcafe.in/" + href)
                    li = "http://www.examcafe.in/" + href
                    # print(li)
                    top_link.append(li)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
    return top_link


def start_button():
    click = []

    for i in pg:
        con.driver.get(i)
        time.sleep(2)

        html_content = con.driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        try:
            div1 = soup.find_all("div", {'class': 'test_button1'})
            # print(len(div1))
            try:
                for j in div1:
                    button = j.find("a")
                    hf = button.get('href')
                    li = "http://www.examcafe.in/" + hf
                    # print(li)
                    click.append(li)
            except Exception as e:
                print(e)
                pass
        except Exception as e:
            div1 = soup.find("div", {'class': 'test_button1'})
            button = div1.find("a")
            hf = button.get('href')
            li = "http://www.examcafe.in/" + hf
            # print(li)
            click.append(li)
    return click


if __name__ == "__main__":

    login()
    pg = links()
    page = start_button()
    qu = []
    ans = []
    o1 = []
    o2 = []
    o3 = []
    o4 = []
    for i in range(len(page)):
        if "&lan=h" in page[i]:
            print("----")
            con.driver.get(page[i])
            time.sleep(2)

            html_content = con.driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            print("current url : ", i)

            try:
                block = soup.find("div", {"class": "test_question_box1"})
                q = block.find_all("div", {"class": "test_question_box3q"})
                o = block.find_all("div", {"class": "test_question_box3"})
                print("length of test_question_box3 ", len(o))

                # -------question block-------

                try:
                    for ques in q:
                        print(ques.text)
                        qu.append(ques.text)
                except Exception as e:
                    print("error in question block", e)

                # ------option block-----------
                try:
                    for opt in o:

                        opt1 = opt.find_all("div", {"class": "test_option"})
                        # print("length of test_option", len(opt1))
                        # print("outside condition ", opt1.text)
                        for a in range(len(opt1)):
                            # print(opt1.text)
                            if a == 0:
                                print(opt1[a].text.replace("A.", ""))
                                o1.append(opt1[a].text.replace("A.", ""))
                            elif a == 1:
                                print(opt1[a].text.replace("B.", ""))
                                o2.append(opt1[a].text.replace("B.", ""))
                            elif a == 2:
                                print(opt1[a].text.replace("C.", ""))
                                o3.append(opt1[a].text.replace("C.", ""))
                            elif a == 3:
                                print(opt1[a].text.replace("D.", ""))
                                o4.append(opt1[a].text.replace("D.", ""))

                            else:
                                pass
                except Exception as e:
                    print(e)
                    print("Sorry!!")

            except Exception as e:
                print(e)
                pass

        else:
            pass


