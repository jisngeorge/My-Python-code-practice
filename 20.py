'''
        WAP to create a reservation system for doctors.
        The system should store the name of Patients that are scheduled to each doctor.
        Sample:
        {
            "doctor1":["patient1","patient3"],
            "doctor2":["patient2"],
            "doctor3":["patient4"]
        }
'''

number = int(input("Enter the number of patients: "))
res    = dict()

while number:
    pat_name = input("Enter the patient name: ")
    doc_name = input("Enter the doctor name: ")

    if doc_name in res:
        res[doc_name].append(pat_name)
    else:
        res[doc_name] = [pat_name]

    number = number - 1

print(res)
