import config_file as con
import time
import csv
import  pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import src.database_config as db
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
                    li =  "http://www.examcafe.in/" + href
                    # print(li)
                    top_link.append(li)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
    return top_link

def start_button() :

    click = []

    for i in pg:
        con.driver.get(i)
        time.sleep(2)
        # try:
        #     con.driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[3]/div/div[4]/a').click()
        # except Exception as e:
        #     try:
        #         con.driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[3]/div/div[3]/a').click()
        #     except Exception as e:
        #         print(e)
        #         print(i)
        #         pass
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

def writecsv(qu, o1, o2, o3, o4, ans):
    try:
        row = ["Question", "Option 1", "Option 2", "Option 3", "Option 4", "Answer"]
        file_object1 = open("Examcafe_text.csv", 'a', encoding="utf-8")
        # print("-----------csv-----------")
        writer = csv.DictWriter(file_object1, fieldnames=row)
        if file_object1.tell() == 0:
            writer.writeheader()
            # print("------csv---------")
        print(len(qu))
        for p_i in range(len(qu)):
            print("number of loop :", p_i)
            print("--------------------CSV WRITTEN--------------")

            writer.writerow({'Question': qu[p_i].replace(";", ","),
                             'Option 1': o1[p_i].replace(";", ","), 'Option 2': o2[p_i].replace(";", ","),
                             'Option 3': o3[p_i].replace(";", ","), 'Option 4': o4[p_i].replace(";", ","),
                             'Answer': ans[p_i]})

        file_object1.close()
    except Exception as e:
        print(e)
        pass


def upload_data():
    df = pd.read_csv("Examcafe_text.csv",encoding='utf-8')
    row = df.shape[0]
    print(row)

    for i in range(row):
        try:
            sql = "INSERT INTO `exam_cafe`(`id`, `topic`, `question`, `option A`, `option B`, `option C`, `option D`, `answer`) " \
                  "VALUES (NULL,%s,%s,%s,%s,%s,%s,%s)"
            q = df['Question'][i].split()
            qt = str(df['Question'][i]).replace('{}'.format(q[0]), '')
            print(df['Topic'][i])
            print(qt)
            print(df['Option 1'][i])
            print(df['Option 2'][i])
            print(df['Option 3'][i])
            print(df['Option 4'][i])
            print(df['Answer'][i])
            val = df['Topic'][i], qt, df['Option 1'][i], df['Option 2'][i], df['Option 3'][i], df['Option 4'][i], df['Answer'][i],


            cursor = db.connection.cursor()
            cursor.execute(sql, val)
            db.connection.commit()
            print("Data Record inserted successfully")
        except db.Error as e:
            db.connection.rollback()
            print("Error while connecting to MySQL", e)
            pass

if __name__ == "__main__":
     upload_data()

    # login()
    # pg = links()
    # page = start_button()
    # qu = []
    # ans = []
    # o1 = []
    # o2 = []
    # o3 = []
    # o4 = []
    # c_o = []
    # for i in range(len(page)):
    #     if "&lan=h" in page[i]:
    #         print("----")
    #         con.driver.get(page[i])
    #         time.sleep(2)
    #
    #         html_content = con.driver.page_source
    #         soup = BeautifulSoup(html_content, 'html.parser')
    #         print("current url : ", i)
    #
    #         try:
    #             block = soup.find("div", {"class": "test_question_box1"})
    #             q = block.find_all("div", {"class": "test_question_box3q"})
    #             o = block.find_all("div", {"class": "test_question_box3"})
    #             print("length of test_question_box3 ", len(o))
    #
    #
    #         #-------question block-------
    #
    #             try:
    #                 for ques in q:
    #                     # Q = ques.text
    #                     print(ques.text)
    #                     qu.append(ques.text)
    #             except Exception as e:
    #                 print("error in question block", e)
    #
    #
    #         # ------option block-----------
    #             try:
    #                 for opt in o:
    #
    #                     opt1 = opt.find_all("div", {"class": "test_option"})
    #                     # print("length of test_option", len(opt1))
    #                     # print("outside condition ", opt1.text)
    #                     for a in range(len(opt1)):
    #                         # print(opt1.text)
    #                         if a == 0:
    #                             print(opt1[a].text)
    #                             o1.append(opt1[a].text.replace("A.", ""))
    #                         elif a == 1:
    #                             print(opt1[a].text)
    #                             o2.append(opt1[a].text.replace("B.", ""))
    #                         elif a == 2:
    #                             print(opt1[a].text)
    #                             o3.append(opt1[a].text.replace("C.", ""))
    #                         elif a == 3:
    #                             print(opt1[a].text)
    #                             o4.append(opt1[a].text.replace("D.", ""))
    #                         else:
    #                             pass
    #             except Exception as e:
    #                 print(e)
    #                 print("Sorry!!")
    #
    #             #---------answer block------------
    #             try:
    #                 con.driver.find_element_by_xpath('//*[@id="test_question"]/div/div[21]/div/a').click()
    #                 con.driver.switch_to.alert.accept()
    #                 time.sleep(2)
    #                 html_con = con.driver.page_source
    #                 sp = BeautifulSoup(html_con, 'html.parser')
    #                 try:
    #                     c = sp.find("div", {"class":"test_historybox3"})
    #                     d = c.find_all("div", {"class": "test_historybox8"})
    #                     print("length of test history box 8", len(d))
    #
    #                     for indx, k in enumerate(d, 1):
    #                         # f = np.array(o, len(d) , step=1)
    #                         if indx % 2 == 0:
    #                             print("check condition")
    #                             pass
    #                         else:
    #                             e = k.find_all("div", {"class": "test_historybox9"})
    #                             print("length of test_historybox9", len(e))
    #                             options = e[0].text.replace(" Correct Answer : ", "").replace(" Marks : ", "")
    #                             # if options == "0":
    #                             #     pass
    #                             # else:
    #                             print("Answer : ", options)
    #                             ans.append(options)
    #                             # c_o.append(options)
    #                             # print("c_o list : ", options)
    #                             # c_o = [x for x in c_o if x != 0]
    #                             # print(c_o)
    #
    #                 except Exception as e:
    #                     print(e)
    #                     pass
    #
    #             except Exception as e:
    #                 print(e)
    #                 pass
    #
    #         except Exception as e:
    #             print(e)
    #             pass
    #


        #
        # else:
        #     pass

    # writecsv(qu, o1, o2, o3, o4, ans)



