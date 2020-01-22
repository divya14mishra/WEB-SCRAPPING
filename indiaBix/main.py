import src.config as con
import sub_links.inner_links as inl
import aptitude.apt_ques as apt_q
import logical_ques.logi_ques as logi_q
import aptitude.verbal_reasoning_ques.nonverbal_ques as ver_q
import time

# Head  links
def links():
    link_list = []
    try:
        # count = 0
        # for i in range(2, 9):
        #     if i + 1 == 6:
        #         pass
        #     else:
        #         count += 1
        #         l = con.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/a[{}]'.format(i + 1))
        #         print(count, "--", l.text)
        #         print(l.get_attribute("href"))
        #         link_list.append(l.get_attribute("href"))
        count = 0
        for i in range(0, 7):
            var_li = con.driver.find_elements_by_class_name('ques-ans')[i]
            len_li = var_li.find_elements_by_tag_name("li")

            for j in len_li:
                links = j.find_element_by_tag_name("a").get_attribute("href")
                count += 1
                print(count, "------", links)
                link_list.append(links)
                # print(links)
        print("lenghth of links ------", len(link_list))

    except Exception as e:
        pass
    return link_list


# Inner links

if __name__ == "__main__":
    head_link = links()
    # print(head_link)
    try:
        for i in range(0, 1):  # len(head_link)):
            con.driver.get(head_link[i])
            time.sleep(2)
            # print("------loop 1-------")
            in_link, inner_link_name = inl.inner_link()
            print(len(in_link))
            # apt_q.pages(in_link)
            for j in range(20, 36):
                print("sub pages")
                logi_q.pages(in_link[j], inner_link_name[j])
    except Exception as e:
        pass
