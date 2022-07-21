def zigzag(word, numRows):
    matrix = []
    for i in range(numRows):
        matrix.append([])
    return(magic(matrix, word, 0))

def magic(matrix, word, rowIndex): 
    if(len(matrix) == 1):
        for letter in word:
            matrix[0].append(letter)
            print(type(matrix))
        return matrix
    
    goingUp = False
    
    for letter in word:
        
        if(goingUp == False):
            matrix[rowIndex].append(letter)
            rowIndex += 1
            if(rowIndex == len(matrix)):
                goingUp = True
                rowIndex -= 1
                continue

        if(goingUp == True):
            rowIndex -= 1
            for i in range(len(matrix)):
                if(i == rowIndex):
                    matrix[i].append(letter)
                else:
                    matrix[i].append(" ")
            if(rowIndex == 0):
                goingUp = False
    return matrix


answer = zigzag("ALGORITHMOFTHEDAY", 3)
for row in answer:
        print(" ")
        for letter in row:
            print(letter,end=" ")
    
