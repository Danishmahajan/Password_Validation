class ShortPass(Exception):
    pass
class NoSpecialCharacter(Exception):
    pass
class OneCapitalCase(Exception):
    pass
class LongerPass(Exception):
    pass
class  NoDigit(Exception):
    pass
class EmptyPassWord(Exception):
    pass


def isnumber(password):
            for i in password:
                if  i.isnumeric():
                    global val
                    val=1
                    break
  

while True:
#Try Block
    try:
        pwd = input("\nEnter Your Password : ")
        val=0
        isnumber(pwd)
        if len(pwd)<4:
            raise ShortPass
        elif len(pwd)>20:
            raise LongerPass
        elif len(pwd)==0:
            raise EmptyPassWord
        elif pwd.isalnum():
            raise NoSpecialCharacter
        elif pwd.islower():
            raise OneCapitalCase
        elif val == 0:
            raise NoDigit
        else:
            print("\nYour Password is Very Strong => ",pwd)
        
        
#Except Block
    except ShortPass:
        print("\nYour PasssWord  Is Too Short,Please Make Changes To Secure Your ID ......")
    except NoSpecialCharacter:
        print("\nMake sure Your Password Must Have Atleast 1 Special Character ......")
    except OneCapitalCase:
        print("\nMake Sure Your Password Must Contain 1 Capital Alphabet ......")
    except LongerPass:
        print("\nYour PAssword is Too Long ......")
    except  NoDigit:
        print("\nYour PassWord Not Containing any Digit ......")
    except EmptyPassWord:
        print("\nPlease Enter something ......")
    