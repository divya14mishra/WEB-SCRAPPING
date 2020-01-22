import Gradeup.src.database_config as db_con
import pandas as pd

df = pd.read_csv("D:/Scrapping/Web-Scrapping/Gradeup/files/Banking.csv")

row = df.shape[0]


def upload_data():
    for i in range(row):
        try:
            sql = "INSERT INTO questions(question_id, group_id, institute_id, question_type, subject,topic, " \
                  "language, direction_to_solve, question, question_in_hindi, option_1, option_1_in_hindi, option_2, option_2_in_hindi," \
                  "option_3, option_3_in_hindi, option_4, option_4_in_hindi, option_5, option_5_in_hindi," \
                  "option_1_true_false, option_1_true_false_in_hindi, option_2_true_false, option_2_true_false_in_hindi," \
                  "correct_option, correct_answer_fib, correct_answer_fib_in_hindi, correct_answer_tf," \
                  "correct_answer_tf_in_hindi, correct_answer_sub, correct_answer_sub_in_hindi, explanation_answer," \
                  "explanation_answer_in_hindi, question_level, exam_name, tags, examvisor_bank, status, updated_at," \
                  "created_at) VALUES (NULL,NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                  "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,current_timestamp(),current_timestamp())"

            val = (0, "Objective", df['Subject'][i], df['Topic'][i], "English", df['Direction to solve'][i], df['Question'][i], "",
                   df['Option 1'][i], "", df['Option 2'][i], "", df['Option 3'][i], "", df['Option 4'][i], "", df['Option 5'][i], "",
                   "", "", "", "", str(df['Answer'][i]), "", "", "", "", "", "", str(df['Explanation'][i]).replace("&nbsp,", "&nbsp;")
                   , "", df['Difficulty Level'][i], df['Exam Type'][i], "Tag1", "yes", "0")

            # val = (0, "Objective", "Quantitative Aptitude", "Mathematics", "Hindi", "", "",df['Question'][i], "",
            #        df['Option 1'][i], "", df['Option 2'][i], "", df['Option 3'][i], "", df['Option 4'][i], "", "", "", "",
            #        "", "", str(df['Answer'][i]), "", "", "", "", "", "", "", "", "Easy", "RRB NTPC", "Tag1", "yes", "0")



            cursor = db_con.connection.cursor()
            cursor.execute(sql, val)
            db_con.connection.commit()
            print("Data Record inserted successfully")
        except db_con.Error as e:
            db_con.connection.rollback()
            print("Error while connecting to MySQL", e)
            pass