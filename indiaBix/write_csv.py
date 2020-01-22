import csv

def writecsv(question, opt1, opt2, opt3, opt4, ans, exp):
    try:
        row = ["Question", "Option 1", "Option 2", "Option 3", "Option 4", "Answer", "Explanation"]
        file_object1 = open("Dristhi_IAS_text.csv", 'a', encoding="utf-8")
        print("-----------csv-----------")
        writer = csv.DictWriter(file_object1, fieldnames=row)
        if file_object1.tell()==0:
            writer.writeheader()
            # print("------csv---------")
        print(len(question))
        for p_i in range(len(question)):

            print("number of loop :", p_i)
            print("--------------------CSV WRITTEN--------------")
            # print('Topic - ', topic)
            # print('Direction - ', dire.replace(";", ","))
            # print('Question - ', ques[p_i].replace(";", ","))
            # print('Option 1 - ', optA[p_i].replace(";", ","))
            # print('Option 2 - ', optB[p_i].replace(";", ","))
            # print('Option 3 - ', optC[p_i].replace(";", ","))
            # print('Option 4 - ', optD[p_i].replace(";", ","))
            # print('Option 5 - ', optE[p_i].replace(";", ","))
            # print('Answer - ',  ans[p_i])
            # print('Explanation - ', exp[p_i].replace(";", ","))
            # print("--------------------CSV END------------------")
            writer.writerow({'Question': question[p_i].replace(";", ","),
                             'Option 1': opt1[p_i].replace(";", ","), 'Option 2': opt2[p_i].replace(";", ","),
                             'Option 3': opt3[p_i].replace(";", ","), 'Option 4': opt4[p_i].replace(";", ","),
                             'Answer': ans[p_i],
                             'Explanation': exp[p_i].replace(";", ",")})

        file_object1.close()
    except Exception as e:
        print(e)
        pass
