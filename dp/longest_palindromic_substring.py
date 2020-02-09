def longest_palindromic_substring(string):
    print('+++++here',string)

    if len(string) == 1:
        return {
            'is_palindrome': True,
            "string":string,
            "length":1
        }
    elif len(string)==2:
        if string[0]!=string[1]:
            return {
                'is_palindrome': False,
                "string":string,
                "length":2
            }
        else:
            return {
                'is_palindrome':"YES",
                "string":string,
                "length":2
            }


    if string[0] != string[-1]:

        
        str1 = longest_palindromic_substring(string[:-1])
        str2 = longest_palindromic_substring(string[1:])

        if str1['is_palindrome'] and not str2['is_palindrome']:
            return {
                'is_palindrome': True,
                "string":str1['string'],
                "length":len(str1['string'])
            }
        elif str2['is_palindrome'] and not str1['is_palindrome']:
            return {
                'is_palindrome': True,
                "string":str2['string'],
                "length":len(str2['string'])
            }
        elif str1['is_palindrome'] and str2['is_palindrome']:
            if str1['length']>=str2['length']:
                return {
                    'is_palindrome': True,
                    "string":str1['string'],
                    "length":len(str1['string'])
                }
            else:
                return {
                    'is_palindrome': True,
                    "string":str2['string'],
                    "length":len(str2['string'])
                }
        elif not str1['is_palindrome'] and not str2['is_palindrome']:
            return {
                    'is_palindrome': False,
                    "string":str1['string'],
                    "length":len(str1['string'])
                }

    else:
        new_str = longest_palindromic_substring(string[1:-1])
        data = {
            'is_palindrome': new_str['is_palindrome'],
            "string":string[0]+new_str['string']+string[-1],
            "length":len(new_str['string'])+2
        }
        return data


if __name__ == '__main__':
    print(longest_palindromic_substring("geeksforgeeks"))
    



