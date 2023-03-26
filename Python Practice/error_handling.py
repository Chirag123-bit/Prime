try:
    a = int(input('Enter a number'))
    print(10/a)
except ZeroDivisionError:
    print("Divided By Zero")
except ValueError:
    print("Enter NUMBERS only")
    
except:
    print("Some error Occured")

finally:
    print('Finally Executed')