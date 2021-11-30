'''
    WAP to create a system to accept Patient Reservations from front-desk.
    The system should accept the patient's name and doctor he/she wishes to consult with.
    Sample:
        {
            "patient1":"doc1",
            "Patient2":"doc2",
            "Patient3":"doc1"
        }
'''
import os
res = dict()
while True:
    os.system('clear')
    print("--------------------------")
    print("    Reservation System")
    print("--------------------------")
    print("1. Show Reservation Charts")
    print("2. Add a Patient")
    print("3. Stop")
    option = int(input("Enter your option: "))
    if(option==1):
        for i in res:
            print("-------------------")
            print("Patient ID: ",i)
            print("Patient Name: ", res[i]["patient_name"])
            print("Doctor's Name: ", res[i]["doctor_name"])
            print("Age: ",res[i]["age"])
            print("--------------------")
        ch = input()
    elif(option==2):
        info = dict()
        pat_id = input("Enter the Patient ID: ")
        pat_name = input("Enter the patient name: ")
        doc_name = input("Enter the doctor's name: ")
        age = int(input("Enter the Age of the Patient: "))
        #Inner Dictionary
        info["patient_name"] = pat_name
        info["doctor_name"] = doc_name
        info["age"] = age
        #Adding the Inner Dictionary to the Main Dictionary
        res[pat_id] = info
    else:
        break