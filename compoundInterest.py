def calculateCompoundInterest():
    
    # This first 3 lines are provided for yougetACompoundIntrest()
    # This first 3 lines are provided for you
    for i in range(1,4):
        principal = float(input("Principle (amount): "))
        time =      float(input("Time:               "))
        rate =      float(input("Rate:               "))

        Amount = principal * (1 + (rate/100))**time
        CompoundInterest = Amount - principal

        print("Compound Interest: "+str(CompoundInterest))
        if i < 3:
            print("---")

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

calculateCompoundInterest()
