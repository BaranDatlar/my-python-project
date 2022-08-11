import itertools

print("Çanta kapasitesini giriniz")
cap = int(input())
print("kaç adet eşya koymak istiyorsunuz")
item = int(input())
i = 0
weight = []
value = []
while item > 0 :
    i = i+1
    print(f"{i}. eşyanın ağırlığını ve değerini giriniz")
    weight.append(int(input()))
    value.append(int(input()))
    item -= 1


weightlist = []
valuelist = []
totalvalue = []
totalweight = []

def printTuple(tupple):
    toplam = 0
    for num in tupple:
        toplam +=num
    totalvalue.append(toplam)

def printTuple2(tupple):
    toplam = 0
    for num in tupple:
        toplam +=num
    totalweight.append(toplam)

def prinTuple(list,list2):
    i = 0
    for element in list :
        for tuple in element:
            print(f"ağırlıklar :{tuple} değerler : {list2[i]}")
            i += 1


j = 1
while j <= len(weight):
    weightlist.append(list(itertools.combinations(weight, j)))
    valuelist.append(list(itertools.combinations(value, j)))
    toplam = 0
    for element in valuelist[j-1] :
        if len(element) == 1:
            for num in element:
                totalvalue.append(num)

        if len(element) > 1:
            printTuple(element)

    for element in weightlist[j - 1]:
        if len(element) == 1:
            for num in element:
                totalweight.append(num)

        if len(element) > 1:
            printTuple2(element)

    j += 1


def knapsack(list1,list2,cap):
    sortedvalue = list2.copy()
    sortedvalue.sort()
    i = len(list2)
    while i > 0:
        if list1[list2.index(sortedvalue[i-1])] <= cap:
            print(f" taşınan ağırlık : {list1[list2.index(sortedvalue[i-1])]} \n en büyük değer :  {sortedvalue[i-1]}")
            break

        i -= 1

# print(weightlist)
# print(valuelist)
# print(totalweight)
# print(totalvalue)
knapsack(totalweight,totalvalue,cap)
prinTuple(weightlist,totalvalue)








