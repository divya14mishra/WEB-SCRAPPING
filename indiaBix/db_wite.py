import pandas as pd
import database as db


df = pd.read_csv("Aptitude_format.csv")
row = df.shape[0]
print(row)
try:

    for i in range(row):

        sql = "INSERT INTO indiabix (`id`, `subject`, `topic`, `direction`, `questions`, `option 1`, `option 2`, `option 3`, `option 4`, " \
              "`option 5`, `answer`, `explanation`) VALUES (NULL,%s, %s, %s,%s, %s, %s, %s,%s, %s,%s, %s)"
        val = (df['Subject'][i], df['Topic'][i], df['Direction'][i], df['Question'][i], df['Option 1'][i], df['Option 2'][i], df['Option 3'][i],
               df['Option 4'][i], df['Option 5'][i], df['Answer'][i], df['Explanation'][i])

        cursor = db.connection.cursor()
        cursor.execute(sql, val)
        db.connection.commit()
        print("Writing to database.")
except Exception as e:
    print("Error in writing database ", e)