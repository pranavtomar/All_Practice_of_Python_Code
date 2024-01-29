def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    speciality_count = {speciality: 0 for speciality in medical_speciality.values()}

    for i in range(1,len(patient_medical_speciality_list),2):
        speciality_code = patient_medical_speciality_list[i]
        if speciality_code in medical_speciality:
            speciality = medical_speciality[speciality_code]
            speciality_count[speciality] += 1

    max_speciality = max(speciality_count, key=speciality_count.get)

    return max_speciality


#provide different values in the list and test your program
patient_medical_speciality_list=[101,'O',102, 'O' ,302, 'P' ,305, 'E' ,401, 'O',656, 'P']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)