
def account():
   
    import mysql.connector
    
    acdb = mysql.connector.connect(host="localhost",user="root",passwd=" ",database="test_py")
    accur = acdb.cursor()
    accur.execute("SELECT * FROM test_table3") #gets values from table
    acdata = accur.fetchall()
    

    while True:
     
        print("""What do you want to do?
            a) Deposit Cash
            b) Withdraw Cash
            c) Information :-
                    i) Loan  
            d) Exit""")
        print("")

        ch_in = input("Enter the option : ")

        if ch_in == "a": 
     
            or_depos = 0
            
            for i in acdata:
                if name in i:
                    or_depos = i[2]

            depos_amount = int(input("Enter amount to deposit : "))
            depos_update_query = """UPDATE test_table3
                            SET deposit=%s
                            WHERE name=%s"""
            depos_update_tup = (depos_amount+or_depos,name)
            
            accur.execute(depos_update_query,depos_update_tup)
            acdb.commit()

        if ch_in == "b":
 
            or_with = 0
            reduce_depos = 0

            for i in acdata:
                if name in i:
                    or_with = i[3]
                    reduce_depos = i[2]
            
            with_amount = int(input("Enter the amount to withdraw : "))
            with_update_query = """UPDATE test_table3
                                SET deposit=%s,withdraw=%s
                                WHERE name=%s """
            with_upadte_tup = (reduce_depos-with_amount,with_amount,name)
        
            accur.execute(with_update_query,with_upadte_tup)
            acdb.commit()

        if ch_in == "c":
 
            print("")
            print("Interest Rate per annum is 6%")
            print("According to Bank's Terms and Conditions your credit details have been changed")

            pri = int(input("The amount you would like to credit your acount with : "))
            rat = 6/100
            T = int(input("For how long do you want the loan[years] : "))
            am = pri*(1+rat)**T

            loan_am = am
            credit_depos = 0

            for i in acdata:
                if name in i:
                    credit_depos = i[2]
                
            loan_update_query = """UPDATE test_table3
                                SET deposit=%s,loan=%s
                                WHERE name=%s """
            loan_update_tup = (loan_am+credit_depos,loan_am)
            
            accur.execute(loan_update_query,loan_update_tup)
            acdb.commit()


        if ch_in == "d":
           
            print("")
            print("Hope you had nice day :)")
            input()
            exit()

    
    input()



def main():
    
    import mysql.connector
    
    global name
    name = input("Please enter your good name : ")

    db = mysql.connector.connect(host="localhost",user="root",passwd=" ",database="test_py")
    
    cur = db.cursor()
    cur.execute("SELECT * FROM test_table3")
    data = cur.fetchall()
    
    l = []
    
    for i in data:
        l.append(i[0])
    
    if name in l:
    
        pos = data.index(i)
        ch_pin = int(input("Please enter your PIN : "))
    
        if ch_pin == data[pos][1]:
     
            account()
           
        else:
     
            print("You entered wrong pin.")
            input()
            exit()

    else:
            
        print("You are not registered.")
        print("Please Register")
        print()
            
        reg_name = input("Enter Registration Name : ")
        reg_pin = int(input("Enter Registration PIN : "))
        reg_deposit = int(input("Enter the amount you would like to deposit : "))
        reg_with = 0
        reg_loan = 0

        insert_tup = (reg_name,reg_pin,reg_deposit,reg_with,reg_loan)
        insert_query = """INSERT INTO test_table3 (name, pin, deposit, withdraw, loan)
                        VALUES(%s,%s,%s,%s,%s)"""

        cur.execute(insert_query,insert_tup)
        db.commit()


pass_ch = "12345"

def  login():

    password = input("Enter Access-Password : ")
    print("")
    if password == pass_ch:
        main()

login()
