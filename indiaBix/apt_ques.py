import src.config as con
import csv_write.write_csv as wc
from bs4 import BeautifulSoup
import time


def ques(in_link):
    global o_i, soup
    ques = []
    option_id = []
    options = ["A", "B", "C", "D", "E"] #options which are given in questions
    optA = []
    optB = []
    optC = []
    optD = []
    optE = []
    ans = []
    exp = []

    con.driver.get(in_link)
    time.sleep(2)

    html_content = con.driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    div = soup.find_all("div", {"class": "bix-div-container"})
    for j in div:
        q = j.find("td", {"class": "bix-td-qtxt"})
        ques.append(q.text)
        # print(q.text)
        # print("--------------------------------")
    o = soup.find_all("table", {"class": "bix-tbl-options"})
    for o_i in o:
        option_id.append(o_i.get("id").strip("tblOption_"))
    for o_i in range(len(option_id)):
        for o_j in range(len(options)):
            if options[o_j] == "A":
                try:
                    get_opt = soup.find("td", {"id": "tdOptionDt_{}_{}".format(options[o_j], option_id[o_i])})
                    # print(get_opt.text)
                    optA.append(get_opt.text)
                except Exception as e:
                    # print("Cannot find options.")
                    optA.append(" ")
                    pass
            elif options[o_j] == "B":
                try:
                    get_opt = soup.find("td", {"id": "tdOptionDt_{}_{}".format(options[o_j], option_id[o_i])})
                    # print(get_opt.text)
                    optB.append(get_opt.text)
                except Exception as e:
                    # print("Cannot find options.")
                    optB.append(" ")
                    pass
            elif options[o_j] == "C":
                try:
                    get_opt = soup.find("td", {"id": "tdOptionDt_{}_{}".format(options[o_j], option_id[o_i])})
                    # print(get_opt.text)
                    optC.append(get_opt.text)
                except Exception as e:
                    # print("Cannot find options.")
                    optC.append(" ")
                    pass
            elif options[o_j] == "D":
                try:
                    get_opt = soup.find("td", {"id": "tdOptionDt_{}_{}".format(options[o_j], option_id[o_i])})
                    # print(get_opt.text)
                    optD.append(get_opt.text)
                except Exception as e:
                    # print("Cannot find options.")
                    optD.append(" ")
                    pass
            elif options[o_j] == "E":
                try:
                    get_opt = soup.find("td", {"id": "tdOptionDt_{}_{}".format(options[o_j], option_id[o_i])})
                    # print(get_opt.text)
                    optE.append(get_opt.text)
                except Exception as e:
                    # print("Cannot find options.")
                    optE.append(" ")
                    pass
            else:
                pass

        try:
            e = con.driver.find_element_by_xpath('//*[@id="divAnswer_{}"]/div'.format(option_id[o_i]))
            # print(e.get_attribute('innerHTML'))
            exp.append(e.get_attribute('innerHTML'))
            # print("------------------------------------------------------------------------------------------------------------")
        except:
            pass

    div2 = soup.find_all("span", {"class": "jq-hdnakqb mx-bold"})
    for k in div2:
        # print(k.text)
        ans.append(k.text)
        # print("--------------------------------")

    wc.writecsv(ques, optA, optB, optC, optD, optE, ans, exp)
    return len(div)


def pages(in_link):
    for i in range(len(in_link)): #(0, 1)
        n_q = ques(in_link[i])
        con.driver.get(in_link[i])
        time.sleep(2)

        html = con.driver.page_source
        s = BeautifulSoup(html, 'html.parser')

        n = s.find_all("span", {"class": "mx-pager-no"})
        href_li=[]

        for j in range(len(n)):
            try:
                l = con.driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[{}]/p/a[{}]'.format(n_q + 3, j+1))
            except:
                l = con.driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[{}]/p/a[{}]'.format(n_q + 4, j + 1))
            href = l.get_attribute('href')
            href_li.append(href)
        # /html/body/div[1]/div/div[5]/div[9]/p/a[1]
        for h in (href_li):
            ques(h)
            # print("------loop--------")