'''
Password should have:
* at least one digit
* at least one lower case character
* at least one upper case character
* no empty character space
* six or more characters totally

Assume that special characters are [!,@,#,$,%,^,&,*,(,),_]
'''

import unittest
import re

def solution(password):

    special_chars = ["!","@","#","$","%","^","&","*","(",")","_"]

    # check if password has at least 6 characters
    min_char_required= 6

    # check password criteria
    has_special_char = False
    has_digit= False
    has_lower= False
    has_upper=False
    has_space= False

    # assume pass is wrong
    result = False

    # count password characters
    count_char=0

    for char in password:

        count_char+=1

        if char in special_chars:
            has_special_char = True

        if re.search('[0-9]',str(password)) is not None:
            has_digit = True
        
        if re.search('[A-Z]', str(password)) is not None: 
            has_upper = True

        if any(char.islower() for char in password) == True:
            has_lower = True 

        if " " in password:
            has_space= True
    
        if (has_special_char == True and has_digit== True and has_lower== True and has_upper== True and (count_char>=min_char_required) and has_space==False):
            result= True
        else:
            result= False

    if result == True:
        result= "Valid"
    else:
        result= "Not_valid"

    return result


class Test_solution(unittest.TestCase):
    
    def test_case_valid(self):
        self.assertEqual(solution(["FooBar123!"]), "Valid")
        
    def test_case_no_special(self):
        self.assertEqual(solution(["FooBar123"]), "Not_valid")

    def test_case_no_capital(self):
        self.assertEqual(solution(["foobar123"]), "Not_valid")

    def test_case_has_spaces(self):
        self.assertEqual(solution(["foob ar123!!!"]), "Not_valid")

if __name__ == "__main__":
    unittest.main()