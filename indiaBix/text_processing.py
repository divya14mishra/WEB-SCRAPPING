import pandas as pd
import csv
# reading csv file
df = pd.read_csv("GK_text.csv", encoding="ISO-8859-1")
r = df.shape[0]
# print("Size of fille : ", row)
# first = df.loc[100:185, ['Question', 'Topic', 'Option 1']]
# print(first)

count = 0
# file1 = open("aptitude.txt", "a+", encoding='utf-8')
# # for i in range():
#     count += 1
#     print(i)
#     # print(df["Question"][i])
#     print("Question no ", count, " - ", str(df["Question"][i]).replace("\n", "").replace("\r", ""))
row = ["Direction", "Question", "Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Answer", "Explanation"]
file_object1 = open("GK_format.csv", 'a', encoding="utf-8")
writer = csv.DictWriter(file_object1, fieldnames=row)
if file_object1.tell() == 0:
    writer.writeheader()
for i in range(r):
    count += 1
    # print(i)
    # print(df["Question"][i])

    # topic =  str(df["Topic"][i]).replace("\n", "").replace("\r", "")
    # top.append(topic)
    direction = str(df["Direction"][i]).replace("\n", "").replace("\r", "")
    # dire.append(direction)
    print("Question no ", count, " - ", str(df["Question"][i]).replace("\n", "").replace("\r", ""))
    # top = str(df["Topic"][i]).replace("\n", "").replace("\r", "")
    # file1.write("Topic Name : " + top + "\n")
    question = str(df["Question"][i]).replace("\n", "").replace("\r", "")
    # ques.append(question)
    # file1.write("Question No-" + str(count) + "  " + ques + "\n")
    optionA = str(df["Option 1"][i]).replace("\n", "").replace("\r", "")
    # optA.append(optionA)
    # file1.write("A      " + optA + "\n")
    optionB = str(df["Option 2"][i]).replace("\n", "").replace("\r", "")
    # optB.append(optionB)
    # file1.write("B      " + optB + "\n")
    optionC = str(df["Option 3"][i]).replace("\n", "").replace("\r", "")
    # optC.append(optionC)
    # file1.write("C      " + optC + "\n")
    optionD = str(df["Option 4"][i]).replace("\n", "").replace("\r", "")
    # optD.append(optionD)
    # file1.write("D      " + optD + "\n")
    optionE = str(df["Option 5"][i]).replace("\n", "").replace("\r", "")
    # optE.append(optionE)
    # # file1.write("E      " + optE + "\n")
    Answer = str(df["Answer"][i]).replace("\n", "").replace("\r", "")
    # ans.append(Answer)
    # file1.write("Answer-- " + Ans + "\n")
    Explanation = str(df["Explanation"][i]).replace("\n", "").replace("\r", "").replace('class="ga-tbl-answer" cellpadding="0" cellspacing="0"', "").replace('class="ga-tr-divident" align="center"',"").replace('class="ga-td-line-rpad" rowspan="2"', "").replace('class="ga-td-divident"', '').replace('class="ga-tr-divisor" align="center">', "").replace('class="ga-td-divisor"', '').replace(' <i class="ga-var">','').replace('class="ga-td-line" rowspan="2"', '').replace('class="ga-td-line-lrpad" rowspan="2"', '').replace('<i class="ga-var">', '').replace('<i class="ga-fhead">', '').replace('class="ga-td-normal-rpad"', '').replace('class="ga-td-normal"', '').replace('class="ga-tr-normal"','').replace('class="ga-pre-gen"', '').replace("/_files", "https://www.indiabix.com/_files").replace('align="center"', '').replace('align="left"', '')
    # file1.write("Explanation-- " + Exp + "\n")
    # exp.append(Explanation)

    # print("Topic Name - ", str(df["Topic"][i]).replace("\n", "").replace("\r", ""))
    print("Option 1 ", " - ", str(df["Option 1"][i]).replace("\n", "").replace("\r", ""))
    print("Option 2 ", " - ", str(df["Option 2"][i]).replace("\n", "").replace("\r", ""))
    print("Option 3 ", " - ", str(df["Option 3"][i]).replace("\n", "").replace("\r", ""))
    print("Option 4 ", " - ", str(df["Option 4"][i]).replace("\n", "").replace("\r", ""))
    print("Option 5 ", " - ", str(df["Option 5"][i]).replace("\n", "").replace("\r", ""))
    print("Answer ", " - ", str(df["Answer"][i]).replace("\n", "").replace("\r", ""))
    print("Explanation ", " - ", str(df["Explanation"][i]).replace("\n", "").replace("\r", "").replace('class="ga-tbl-answer" cellpadding="0" cellspacing="0"', "").replace('class="ga-tr-divident" align="center"', "")
          .replace('class="ga-td-line-rpad" rowspan="2"', "").replace('class="ga-td-divident"', '').replace('class="ga-tr-divisor" align="center">', "").replace('class="ga-td-divisor"', '').replace(' <i class="ga-var">', '')
          .replace('class="ga-td-line" rowspan="2"', '').replace('class="ga-td-line-lrpad" rowspan="2"', '').replace('<i class="ga-var">','').replace('<i class="ga-fhead">', '')
          .replace('class="ga-td-normal-rpad"', '').replace('class="ga-td-normal"', '').replace('class="ga-tr-normal"', '').replace('class="ga-pre-gen"', '')
          .replace("/_files", "https://www.indiabix.com/_files").replace('align="center"', '').replace('align="left"', ''))
    # result = re.sub("<.*?>", "", Exp)
    # print("Explanation-- ", result)
    #
    # print("questions ---- ", ques)
    # print("option a ---- ", optA)
    # print("option b ---- ", optB)
    # print("option c ---- ", optC)
    # print("option d ---- ", optD)
    # print("option e ---- ", optE)
    # print("answers ---- ", ans)
    # print("explanation ---- ", exp)
    # print("topics ---- ", top)
    # print("direction ----- ", dire)
    writer.writerow({'Direction': direction, 'Question': question,
                     'Option 1': optionA, 'Option 2': optionB,
                     'Option 3': optionC, 'Option 4': optionD,
                     'Option 5': optionE, 'Answer': Answer,
                     'Explanation': Explanation})



file_object1.close()
