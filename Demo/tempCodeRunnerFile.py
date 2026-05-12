# a = int(input())

# if(a == 0):
#     print("0")
# elif(a == 1):
#     print("$2000")
# elif(a == 2 or a == 3):
#     print("$5000")
# elif(a >= 4 and a <= 6):
#     print("$9000")
# elif(a == 9):
#     print("$12000")
# elif(a == 12):
#     print("$15000")
# else:
#     print("error")


def validate_transaction(transaction):
    seen = set()
    
    # Sort transactions based on time
    transaction.sort(key=lambda x: int(x[2]))
    
    prev_time = None
    
    for t in transaction:
        sender, receiver, time, amount = t
        time = int(time)

        # Rule 1: Duplicate check (full transaction)
        if (sender, receiver, time, amount) in seen:
            return "ERROR DUPLICATE TRANSACTION"
        seen.add((sender, receiver, time, amount))

        # Rule 2: Time difference check
        if prev_time is not None and (time - prev_time) > 60:
            return "FRAUD DETECTED"
        
        prev_time = time

    return "ALL TRANSACTIONS ARE VALID"