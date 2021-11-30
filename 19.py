'''
    WAP to create a system to accept Patient Reservations from front-desk of a clinic.
    The system should accept the patient's name and doctor he/she wishes to consult with.
    Hint:
    Accept the total number of patients first.
    Sample:
        {
            "patient1":"doc1",
            "Patient2":"doc2",
            "Patient3":"doc1"
        }
'''
'''
number_of_patients = int(input("Enter the number of patients: "))
dict_name = dict()

for i in range(number_of_patients):
    pat_name = input("Enter the patient name: ")
    doc_name = input("Enter the doctor name: ")
    dict_name[pat_name] = doc_name

for i in dict_name:
    print(i, dict_name[i])

OR
'''
r = dict()
while True:
    pat_name = input("Enter the patient name: ")
    doc_name = input("Enter the doctor name: ")
    r[pat_name] = doc_name

    choice = int(input("Continue (1/0) ?"))
    print(r)
    if choice == 0:
        break
