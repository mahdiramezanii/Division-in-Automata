#============================ import ============================
from create_string import division_operation
from Class_Function import String,reverse,division,Dictlist
#================================================================

# l1=input("enter l1: ")
# l2=input("enter l2: ")

# re=division_operation(l1,l2)

"""L1=re[0]
L2=re[1]"""

L1=["a","b","aa","bb","ab","ba","abbb","aaba","abaa"]
L2=["a","aa","b","bb","bbb"]



result_l1=Dictlist()


for L in L1:

    for item in L2:


        if len(L) == 1:

            if (item in L) or (item == L):


                result_l1[item]=L

        elif item in L:


            result_l1[item] = L



L1.clear()
L2.clear()

for k in result_l1.keys():

    L2.append(k)

for k,v in result_l1.items():

    L1.append(v)

print(f"L1: {L1}")
print(f"L2: {L2}")

final_result=[]
index=0

while len(L2)>index:

    for item in L1[index]:


        if L2[index] in reverse((item[-1:(-((len(L2[index]))+1)):-1])): #چک کردن اینکه رشته l1 پسوندی از l2 داشته باشد.

            if item == L2[index]:

                final_result.append("λ")

            else:
                final_result.append(division(item,L2[index]))

    index += 1


print(f"result___l1: {result_l1}")
# print(final_result)

final_result = list(dict.fromkeys(final_result)) #Remove duplicate strings
print(final_result)


