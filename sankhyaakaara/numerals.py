import csv
import re

num2word_dict3={}
num2word_dict2={}

with open('other_num.csv','r') as f:
    red = csv.DictReader(f)
    for d in red:
            k = d['num']
            v = d['word']
            num2word_dict3.update({k:v})

with open('ekam.csv','r') as f:
    red = csv.DictReader(f)
    for d in red:
            k = d['num']
            v = d['word']
            num2word_dict2.update({k:v})

# -----Taking inp            
inp_num = input("Enter a number without commas: ")
# inp_num = 133456789 #current limit = 10 crore
inp_type = input("Visheshana (enter 'v') or samkhya (enter 's') ?")

num = str(inp_num) #[::-1]#reversing

output_wr = ""
#-------------- Starts with 0? then remove 0s -----------
def zero(num):
    if re.search(r"^0*",num ):
      num = re.sub(r"^0*","", num) 
    return num

num = zero(num)
num_len = len(num)     

if re.search(r"^0*",num ):
      num = re.sub(r"^0*","", num) 
num_len = len(num)
num1 = num       
# print(num)
#--------------------- For 1 and 2 digit num and 1 with 0s number ----------- 

key_12num = num2word_dict2.keys() 

if num in key_12num:
    output_wr = num2word_dict2[num]
    num = ""

#---------------------- For number more than 2 digits -------
#abja
if len(num) == 10:
    output_wr = num2word_dict3[num[:1]] + "-अब्ज\n"+ output_wr
    num = num[1:]
    num = zero(num)
    # print("o-num",num, output_wr)
#arbuxa
if len(num) == 9:
    output_wr = num2word_dict3[num[:1]] + "-अर्बुद\n" + output_wr
    num = num[1:]
    num = zero(num)

# #koti
if len(num) == 8:
    output_wr = num2word_dict3[num[:1]] + "-कोटि\n"+ output_wr
    num = num[1:]
    num = zero(num)

# #laksh 

if len(num) == 7:
    output_wr = num2word_dict3[num[:1]] + "-प्रयुत\n"+ output_wr
    num = num[1:]
    num = zero(num)

#  print(output_wr)

if len(num) == 6:
    output_wr = num2word_dict3[num[:1]] + "-लक्ष\n"+  output_wr
    num = num[1:]
    num = zero(num)
# #sahasra
if len(num) == 5:
    output_wr = num2word_dict3[num[:1]] + "-अयुत\n" + output_wr
    num = num[1:]
    num = zero(num)
if len(num) == 4:
    output_wr = num2word_dict3[num[:1]] + "-सहस्र\n" + output_wr
    num = num[1:]
    num = zero(num)
# #shatam
if len(num) == 3:
    output_wr = num2word_dict3[num[:1]] + "-शत\n" + output_wr
    num = num[1:] 
    num = zero(num)
if len(num) == 2:
    output_wr = num2word_dict2[num[:2]] + "\n" + output_wr
    num = num[2:]
if len(num) == 1:
    output_wr = num2word_dict2[num[:1]] + "\n" + output_wr
    num = ""

with_uttara = output_wr.split()
len_with_uttara = len(with_uttara)

for i in range(len(with_uttara)-1):
    with_uttara[i] = with_uttara[i]+"-उत्तर-"

# print(with_uttara, "num len", num_len)
with_uttara = "".join(with_uttara)    

######## ------------- if visherana -> 3 outputs for last value with three genders 
# ---------------------else print the samkhya in napum singular

output = {}
if num_len != 8 and num_len >= 3: # exept for koti and one or two digit num.
    if inp_type == "v":# v for visheshana
        output = {"stri":with_uttara+"म्", "pum":with_uttara+"म्", "napum":with_uttara+"म्"}
    elif inp_type == "s":#s for sankhya
         output = {"s":with_uttara+"म्"}

elif num_len == 8:#for kotiH
    if inp_type == "v":# v for visheshana
        output = {"stri":with_uttara+"ः", "pum":with_uttara+"ः", "napum":with_uttara+"ः"}
    elif inp_type == "s":#s for sankhya
         output = {"s":with_uttara+"ः"}

elif num_len == 1:
    if num1 == "1": #or num1 == 2 or num == 3:
        if inp_type == "v":# v for visheshana
            output = {"stri":with_uttara[:-1]+"ा", "pum":with_uttara[:-1]+"ः", "napum":with_uttara}
        elif inp_type == "s":#s for sankhya
             output = {"s":with_uttara}
    elif num1 == "2": #or num1 == 2 or num == 3:
        if inp_type == "v":# v for visheshana
            output = {"stri":with_uttara[:-1]+"े", "pum":with_uttara[:-1]+"ौ", "napum":with_uttara[:-1]+"े"}
        elif inp_type == "s":#s for sankhya
            output = {"s":with_uttara}
    elif num1 == "3": #or num1 == 2 or num == 3:
        if inp_type == "v":# v for visheshana
            output = {"stri":"तिस्रः", "pum":"त्रयः", "napum":"त्रिणि"}
        elif inp_type == "s":#s for sankhya
            output = {"s":with_uttara}     
    elif num1 == "4": #or num1 == 2 or num == 3:
        if inp_type == "v":# v for visheshana
            output = {"stri":"चतस्रः", "pum":"चत्वारः", "napum":with_uttara}
        elif inp_type == "s":#s for sankhya
            output = {"s":with_uttara}                     
else:# for 2 digit
    if inp_type == "v":# v for visheshana
        output = {"stri":with_uttara, "pum":with_uttara, "napum":with_uttara}
    elif inp_type == "s":#s for sankhya
        output = {"s":with_uttara}
  

print(inp_num)#prints the input
print(output)#prints the output

