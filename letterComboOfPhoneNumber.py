class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        numbers = {
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz" 
        }
        result = [""]
        for i in digits:
            letters = numbers[i]
            temp = []
            for combination in result:
                for letter in letters:
                    temp.append(combination + letter)
            result = temp
        return result
        
        