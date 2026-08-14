#Q1.Write a script that takes a number and prints whether it's positive, negative, or zero, and whether it's even or odd.
num=int(input('enter your number:'))
if num==0:
    print('number is zero and it is even')
elif num>0:
    if num%2==0:
        print('number is positive and it is even')
    else:
        print('number is positive and it is odd')
else:
    if num%2!=0:
        print('number is negative and it is odd')
    else:
        print('number is negative and it is odd')
#Q2.Write a function that takes a sentence and returns the count of vowels and the sentence reversed, using a loop.
sen=str(input('enter your sentence:'))
count=0
for i in sen:
    if i in 'aeiouAEIOU':
        count+=1
print('the count of vowels :',count)
newstr=''
for i in sen.split()[::-1]:
    newstr+=' ' +i

print('the  reversed sentence is ', newstr)

#Q3.Given a list of student names and marks, build a dictionary from them, then use a comprehension to get all students scoring above 50.
name=['ram','sham','karan','arjun','akshay']
marks=[78,37,49,55,95]
dict={}
for i in range(len(marks)):
    dict[name[i]]=marks[i]
print(dict)

for i,j in dict.items():
    if j>50:
        print(i)

#Q4.Write a script that reads a text file and prints its line count — handle the file-not-found case gracefully with try/except.
f=open(r'C:\Users\FCI\Desktop\PMS\Python\data.txt')
print(f.read())
#Q4.Write a script that reads a text file and prints its line count — handle the file-not-found case gracefully with try/except.
f=open(r'C:\Users\FCI\Desktop\PMS\Python\data.txt')
print(f.read())

#Q5Write a function with default arguments and *args that calculates the average of any number of values, with input validation.
def average(*num):
    s=len(list(*num))
    avg=sum(*num)/s
    return 'the average of all number ',avg 
values=[1,2,3,4,5,6,7,8,9]
print(average(values))