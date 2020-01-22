import pandas as pd

# reading csv file
df = pd.read_csv("Aptitude_csv_text.csv")
row = df.shape
print("Size of fille : ", row)
first = df.loc[100:185, ['Question', 'Topic', 'Option 1']]
# print(first)

count = 0
file1 = open("aptitude.txt", "a+", encoding='utf-8')
# for i in range():
#     count += 1
#     print(i)
#     # print(df["Question"][i])
#     print("Question no ", count, " - ", str(df["Question"][i]).replace("\n", "").replace("\r", ""))

for i in range(1, 698):
    count += 1
    print(i)
    # print(df["Question"][i])
    print("Question no ", count, " - ", str(df["Question"][i]).replace("\n", "").replace("\r", ""))

    top = str(df["Topic"][i]).replace("\n", "").replace("\r", "")
    file1.write("Topic Name : " + top + "\n")
    ques = str(df["Question"][i]).replace("\n", "").replace("\r", "")
    file1.write("Question No-" + str(count) + "  " + ques + "\n")
    optA = str(df["Option 1"][i]).replace("\n", "").replace("\r", "")
    file1.write("A      " + optA + "\n")
    optB = str(df["Option 2"][i]).replace("\n", "").replace("\r", "")
    file1.write("B      " + optB + "\n")
    optC = str(df["Option 3"][i]).replace("\n", "").replace("\r", "")
    file1.write("C      " + optC + "\n")
    optD = str(df["Option 4"][i]).replace("\n", "").replace("\r", "")
    file1.write("D      " + optD + "\n")
    # optE = str(df["Option 5"][i]).replace("\n", "").replace("\r", "")
    # file1.write("E      " + optE + "\n")
    Ans = str(df["Answer"][i]).replace("\n", "").replace("\r", "")
    file1.write("Answer-- " + Ans + "\n")
    Exp = str(df["Explanation"][i]).replace("\n", "").replace("\r", "").replace('class="ga-tbl-answer" cellpadding="0" cellspacing="0"', "").replace('class="ga-tr-divident" align="center"',"").replace('class="ga-td-line-rpad" rowspan="2"', "").replace('class="ga-td-divident"', '').replace('class="ga-tr-divisor" align="center">', "").replace('class="ga-td-divisor"', '').replace(' <i class="ga-var">','').replace('class="ga-td-line" rowspan="2"', '').replace('class="ga-td-line-lrpad" rowspan="2"', '').replace('<i class="ga-var">', '').replace('<i class="ga-fhead">', '').replace('class="ga-td-normal-rpad"', '').replace('class="ga-td-normal"', '').replace('class="ga-tr-normal"','').replace('class="ga-pre-gen"', '').replace("/_files", "https://www.indiabix.com/_files").replace('align="center"', '').replace('align="left"', '')
    file1.write("Explanation-- " + Exp + "\n")
    # print("Topic Name - ", str(df["Topic"][i]).replace("\n", "").replace("\r", ""))
    # print("Option 1 ", " - ", str(df["Option 1"][i]).replace("\n", "").replace("\r", ""))
    # print("Option 2 ", " - ", str(df["Option 2"][i]).replace("\n", "").replace("\r", ""))
    # print("Option 3 ", " - ", str(df["Option 3"][i]).replace("\n", "").replace("\r", ""))
    # print("Option 4 ", " - ", str(df["Option 4"][i]).replace("\n", "").replace("\r", ""))
    # print("Option 5 ", " - ", str(df["Option 5"][i]).replace("\n", "").replace("\r", ""))
    # print("Answer ", " - ", str(df["Answer"][i]).replace("\n", "").replace("\r", ""))
    # print("Explanation ", " - ", str(df["Explanation"][i]).replace("\n", "").replace("\r", "").replace('class="ga-tbl-answer" cellpadding="0" cellspacing="0"', "").replace('class="ga-tr-divident" align="center"', "")
    #       .replace('class="ga-td-line-rpad" rowspan="2"', "").replace('class="ga-td-divident"', '').replace('class="ga-tr-divisor" align="center">', "").replace('class="ga-td-divisor"', '').replace(' <i class="ga-var">', '')
    #       .replace('class="ga-td-line" rowspan="2"', '').replace('class="ga-td-line-lrpad" rowspan="2"', '').replace('<i class="ga-var">','').replace('<i class="ga-fhead">', '')
    #       .replace('class="ga-td-normal-rpad"', '').replace('class="ga-td-normal"', '').replace('class="ga-tr-normal"', '').replace('class="ga-pre-gen"', '')
    #       .replace("/_files", "https://www.indiabix.com/_files").replace('align="center"', '').replace('align="left"', ''))