def solution(A, D):
    transaction_per_month = dict() #dictionary to map the total transactions per month
    no_of_transactions = dict()  #number of payments made in a paticular month
    payments_per_month = dict() # sum of paymments made in a month
    #dates = dict(zip(D, A))

    transaction_Dict = (zip(D, A)) #zips the date with the corresponding amount using zip() function
    total =  -60
    for date, amount in transaction_Dict:
        year, month, _ = date.split("-") #splits the date into year and month discarding the date part
        if (year, month) not in transaction_per_month:
            transaction_per_month[(year, month)] = amount #add the month to the dict with initial amount
        else:
            transaction_per_month[(year, month)] += amount #accumulate amount per month
        if (amount < 0): #for the payments(ie -transactions)
            if (year, month) not in no_of_transactions and (year, month) not in payments_per_month:
                no_of_transactions[(year, month)] = 1
                payments_per_month[(year, month)] = amount # increase payment count and amount
            else:
                no_of_transactions[(year, month)] += 1
                payments_per_month[(year, month)] += amount
    for (year, month), amount in transaction_per_month.items(): #loop to determine card deduction
        if (year, month) in no_of_transactions and (year, month) in payments_per_month:
            if no_of_transactions[(year, month)] < 3 and payments_per_month[(year, month)] <= -100:
                total += 5
        total += amount

        
    print(transaction_per_month)
    print(no_of_transactions)
    print((payments_per_month))
    print(total)
    #print(dates)
tra = solution([100, 100, -10, 200, -30], ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"])
#print(tra)
