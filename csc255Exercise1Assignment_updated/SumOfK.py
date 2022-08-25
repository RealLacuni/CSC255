
count = 0

while count < 5:
    sumExists = False
    equation = ""
    # Ask user for file name #
    userInput = input("Enter file number: ")
    
    #Open, read, and save file name into a list
    fileName = "in" + userInput + ".txt"
    f = open(fileName, "r")
    contents = f.read()
    contentList = contents.strip().split("\n")

    #Prepare output file for writing
    outputFileName = "out" + userInput + ".txt"
    outputFile = open(outputFileName, "w")
    print(contentList)
    target = int(contentList[1])


    #Add list of numbers and target to output file
    outputFile.write(contentList[2] + "\n")
    outputFile.write(str(target) + "\n")


    numbers = contentList[2].split()
    print(numbers)
    index = 0
    while index < len(numbers) and not sumExists:
        print("checking index " + str(index))
        num = int(numbers[index])

        if numbers[index] * 2 == target:
            sumExists = True
            equation = f"{num} + {num} = {target}"
            break
        lookFor = int(target) - int(num)
        for j in range(index + 1, len(numbers)):
            print("comparing with " + numbers[j])
            if int(numbers[j]) == lookFor:
                print(numbers[j] + " is equal to " + str(lookFor))
                sumExists = True
                equation = f"{num} + {numbers[j]} = {target}"
                break
        
        index += 1
    
    outputFile.write("Yes" if sumExists else "no")

    if equation:
        outputFile.write("\n" + equation)
    outputFile.close()
    count += 1
    






    