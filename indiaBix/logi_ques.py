import src.config as con
import csv_write.write_csv as wc
from bs4 import BeautifulSoup
import time


def ques(in_link, inner_link_name):
    global o_i, dire
    ques = []
    option_id = []
    options = ["A", "B", "C", "D", "E"]  # options which are given in questions
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
    try:
        direction = soup.find("div", {"id": "divDirectionText"})
        dire = direction.text
        print(direction.text)
        print("--------direction----------")
    except Exception as e:
        dire = (" ")
        print(e)
        pass
    div = soup.find_all("div", {"class": "bix-div-container"})
    for j in div:
        q = j.find("td", {"class": "bix-td-qtxt"})
        ques.append(q.text)
        # print(ques)
        print("----------question loop----------------------")
        print(q.text)

    o = soup.find_all("table", {"class": "bix-tbl-options"})
    for o_i in o:
        option_id.append(o_i.get("id").strip("tblOption_"))
        # print(option_id)
    for o_i in range(len(option_id)):
        print("option id", o_i)
        print("-------------start loop of options-------------")
        for o_j in range(len(options)):
            print("total options", o_j)
            if options[o_j] == "A":
                try:
                    image_op = con.driver.find_element_by_xpath(
                        '//*[@id="tdOptionDt_{}_{}"]'.format(options[o_j], option_id[o_i]))
                    if image_op:
                        if "images" in image_op.get_attribute('innerHTML'):
                            optA.append(str(image_op.get_attribute('innerHTML')).replace("/_files",
                                                                                         "https://www.indiabix.com/_files"))
                            print(image_op.get_attribute('innerHTML'))
                            print("--------------------inner HTML----------------------------------------")
                        else:
                            try:
                                get_opt = soup.find("td",
                                                    {"id": "tdOptionDt_{}_{}".format(options[o_j], option_id[o_i])})
                                print(get_opt.text)
                                optA.append(get_opt.text)
                            except Exception as e:
                                # print("Cannot find options.")
                                optA.append(" ")
                                pass
                    else:
                        pass
                except Exception as e:
                    optA.append(" ")
                    print(e)
                    print("-------condition of A-------")


            elif options[o_j] == "B":
                try:
                    image_op = con.driver.find_element_by_xpath(
                        '//*[@id="tdOptionDt_{}_{}"]'.format(options[o_j], option_id[o_i]))
                    if image_op:
                        if "images" in image_op.get_attribute('innerHTML'):
                            optB.append(str(image_op.get_attribute('innerHTML')).replace("/_files",
                                                                                         "https://www.indiabix.com/_files"))
                            print(image_op.get_attribute('innerHTML'))
                            print("--------------------inner HTML----------------------------------------")
                        else:
                            try:
                                get_opt = soup.find("td",
                                                    {"id": "tdOptionDt_{}_{}".format(options[o_j], option_id[o_i])})
                                print(get_opt.text)
                                optB.append(get_opt.text)
                            except Exception as e:
                                # print("Cannot find options.")
                                optB.append(" ")
                                pass
                    else:
                        pass
                except Exception as e:
                    optB.append(" ")
                    print(e)
                    print("-------condition of B--------")

            elif options[o_j] == "C":
                try:
                    image_op = con.driver.find_element_by_xpath('//*[@id="tdOptionDt_{}_{}"]'.format(options[o_j], option_id[o_i]))
                    if image_op:
                        if "images" in image_op.get_attribute('innerHTML'):
                            optC.append(str(image_op.get_attribute('innerHTML')).replace("/_files", "https://www.indiabix.com/_files"))
                            print(image_op.get_attribute('innerHTML'))
                            print("--------------------inner HTML----------------------------------------")
                        else:
                            try:
                                get_opt = soup.find("td", {"id": "tdOptionDt_{}_{}".format(options[o_j], option_id[o_i])})
                                print(get_opt.text)
                                optC.append(get_opt.text)
                            except Exception as e:
                                # print("Cannot find options.")
                                optC.append(" ")
                                pass
                    else:
                        pass
                except Exception as e:
                    optC.append(" ")
                    print(e)
                    print("-------condition of C--------")

            elif options[o_j] == "D":
                try:
                    image_op = con.driver.find_element_by_xpath('//*[@id="tdOptionDt_{}_{}"]'.format(options[o_j], option_id[o_i]))
                    if image_op:
                        if "images" in image_op.get_attribute('innerHTML'):
                            optD.append(str(image_op.get_attribute('innerHTML')).replace("/_files",
                                                                                         "https://www.indiabix.com/_files"))
                            print(image_op.get_attribute('innerHTML'))
                            print("--------------------inner HTML----------------------------------------")
                        else:
                            try:
                                get_opt = soup.find("td",
                                                    {"id": "tdOptionDt_{}_{}".format(options[o_j], option_id[o_i])})
                                print(get_opt.text)
                                optD.append(get_opt.text)
                            except Exception as e:
                                # print("Cannot find options.")
                                optD.append(" ")
                                pass
                    else:
                        pass
                except Exception as e:
                    optD.append(" ")
                    print(e)
                    print("-------condition of D--------")

            elif options[o_j] == "E":
                print("in the e section", options[o_j])
                try:
                    image_op = con.driver.find_element_by_xpath(
                        '//*[@id="tdOptionDt_{}_{}"]'.format(options[o_j], option_id[o_i]))
                    if image_op:
                        if "images" in image_op.get_attribute('innerHTML'):
                            optE.append(str(image_op.get_attribute('innerHTML')).replace("/_files",
                                                                                         "https://www.indiabix.com/_files"))
                            print(image_op.get_attribute('innerHTML'))
                            print("--------------------inner HTML----------------------------------------")
                        else:
                            try:
                                get_opt = soup.find("td",{"id": "tdOptionDt_{}_{}".format(options[o_j], option_id[o_i])})
                                print(get_opt.text)
                                print("option E--------------")
                                optE.append(get_opt.text)
                            except Exception as e:
                                # print("Cannot find options.")
                                optE.append(" ")
                                pass
                    else:
                        pass
                except Exception as e:
                    optE.append(" ")
                    print("----condition of E---")
                    pass

        print("-------end of otions for 1 question-----")

        try:
            # print("entering explanation section")

            e = con.driver.find_element_by_xpath('//*[@id="divAnswer_{}"]/div'.format(option_id[o_i]))
            try:
                inner_html = e.get_attribute('innerHTML')
                if inner_html:
                    print(e.get_attribute('innerHTML'))
                    exp.append(e.get_attribute('innerHTML'))
                else:
                    exp.append(e.text)
                    print(e.text)
            except:
                exp.append(e.text)
                print(e.text)
                pass
            # print("----------------------------------------")
        except Exception as e:
            exp.append(" ")
            print(e)
            pass
    try:
        div2 = soup.find_all("span", {"class": "jq-hdnakqb mx-bold"})

        for k in div2:
            print(k.text)
            print("--------answer section------------------------")
            ans.append(k.text)
    except Exception as e:
        pass
    print("question - ", ques)
    print("direction - ", dire)
    print("Topics - ", inner_link_name)
    print("option 1 -", optA)
    print("option 2 -", optB)
    print("option 3 -", optC)
    print("option 4 -", optD)
    print("option 5 -", optE)
    print("answer - ", ans)
    print("explanation -", exp)
    wc.writecsv(inner_link_name, dire, ques, optA, optB, optC, optD, optE, ans, exp)
    return len(div)


def pages(in_link, inner_link_name):
    con.driver.get(in_link)
    time.sleep(2)

    html = con.driver.page_source
    s = BeautifulSoup(html, 'html.parser')

    n = s.find_all("span", {"class": "mx-pager-no"})
    print("link of pages", len(n))

    n_q = ques(in_link, inner_link_name)

    print(n_q)
    href_li = []

    for j in range(len(n)):
        try:
            l = con.driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[{}]/p/a[{}]'.format(n_q + 3, j + 1))
            # print("pages reading", l)
            # print('/html/body/div[1]/div/div[5]/div[{}]/p/a[{}]'.format(n_q + 3, j + 1))
        except:
            l = con.driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[{}]/p/a[{}]'.format(n_q + 4, j + 1))
            # print('/html/body/div[1]/div/div[5]/div[{}]/p/a[{}]'.format(n_q + 4, j + 1))

        href = l.get_attribute('href')
        href_li.append(href)

    for h in (href_li):
        print("link call", h)
        ques(h, inner_link_name)
