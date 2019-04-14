#homework2

#Input data
males=int(input("Enter number of males:"))
females=int(input("Enter number of females:"))

#Variables with sum of both int
total= males+females

#Variables
percentmale= males/total
percentfemale= females/total

#Data output/Print
print("Percent males:", end=" ")
print(format(percentmale,'.0%'))
print("Percent females:", end=" ")
print(format(percentfemale,'.0%'))
print("The total Women and men combined:", end=" ")

#Extra Data output added
print(format(total))

