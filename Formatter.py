# The dataset file should follow the format of ['Question'<TAB>'Answer'] in each line

# Change the directory of the input anfd the output of the file
# Open file to be formatted
f1 = open(r"C:\Users\MYPC\Documents\Courses\Visual Studio Code\python\2209 self work\AI Project\AI Q&A (original).txt", mode='r', encoding='utf-8')
# create a empty textfile to be written
f2 = open(r"C:\Users\MYPC\Documents\Courses\Visual Studio Code\python\2209 self work\AI Project\AI Q&A (formatted 3).txt", mode='w', encoding='utf-8')

# Split and write the formatted edition
for qna in f1:
	qna = qna.split('\t')
	q = qna[0]
	a = qna[1][:-1]
	f2.write('{\n\t"tag":"",\n\t"patterns":["' + q + '"],\n\t"responses":["' + a + '"],\n\t"context":[""]\n},\n')

print("----------end----------")

# Close the file
f1.close()
f2.close()