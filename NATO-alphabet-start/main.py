# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
# print(student_data_frame)
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
#
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas
nato=pandas.read_csv("nato_phonetic_alphabet.csv")

pairs={values.letter:values.code for (keys,values) in nato.iterrows() }
name=input("enter your name  : ").upper()
ans=[pairs[key] for key in name ]
answer={keys:pairs[keys] for keys in name }
print(ans)
print(answer)



