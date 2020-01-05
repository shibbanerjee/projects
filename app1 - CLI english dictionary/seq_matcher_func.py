#fucntion to recommend the best match for entered using the sequence matcher method
#written by me, but same thing can be done using get_close_matches method
# def seq_matcher(word1):
#     for i in data.keys():
#         #iterate through all the dict keys
#        seq = difflib.SequenceMatcher(None,word1,i)
#        d = seq.quick_ratio()*100
#         #check the sequence match and convert it to a ratio then a percentage
#        if d>80:
#            #check if percent match is more than 80
#         usr_inp = input("Did you mean {}, enter yes or no : ".format(i))
#         if usr_inp =='yes':
#             return data[i]
#             #return the value of the dict key i
#         else:
#             return "No problem, please check the spelling and enter again"