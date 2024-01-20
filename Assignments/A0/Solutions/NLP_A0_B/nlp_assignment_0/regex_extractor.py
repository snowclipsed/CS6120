# Group J
# Aishwarya Ravichandran
# Hardik Bishnoi
# B Dhanush Adhithya

# assignment 0
# importing pandas package to read .csv file
# importing re package to call functions of regular expression

# note -> install pandas in your virtual env for the program to run without roadblocks
 
import pandas as pd
import re

# part b
# read_book to read .txt files

def read_book(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# searchText() method to search the respective text
def searchText():

    # to read pm vol1 and store it in pm_vol1 attribute
    pm_vol1 = read_book('C:/Users/harry/OneDrive/Documents/Northeastern University/CS6120/Assignments/A0/Solutions/NLP_A0_B/nlp_assignment_0/practical_medicine_v1.txt')

    # to read pm vol2 and store it in pm_vol2 attribute
    pm_vol2 = read_book('C:/Users/harry/OneDrive/Documents/Northeastern University/CS6120/Assignments/A0/Solutions/NLP_A0_B/nlp_assignment_0/practical_medicine_v2.txt')

    # to read pm vol3 and store it in pm_vol3 attribute
    pm_vol3 = read_book('C:/Users/harry/OneDrive/Documents/Northeastern University/CS6120/Assignments/A0/Solutions/NLP_A0_B/nlp_assignment_0/practical_medicine_v3.txt')

    # to read pm vol4 and store it in pm_vol4 attribute
    pm_vol4 = read_book('C:/Users/harry/OneDrive/Documents/Northeastern University/CS6120/Assignments/A0/Solutions/NLP_A0_B/nlp_assignment_0/practical_medicine_v4.txt')

    # to read pm vol5 and store it in pm_vol5 attribute
    pm_vol5 = read_book('C:/Users/harry/OneDrive/Documents/Northeastern University/CS6120/Assignments/A0/Solutions/NLP_A0_B/nlp_assignment_0/practical_medicine_v5.txt')

    # list of disease that has to be searched 
    disease_list = ["Heart disease" , "Cancer" , "Stroke" , "Respiratory diseases" , "Alzheimer's disease" , "Diabetes" , "Influenza and Pneumonia" , "Kidney diseases" , 
                   "Septicemia" , "Liver disease" , "Hypertension" , "Parkinson's disease" , "Chronic lower respiratory disease" , "Accidents/injuries" , "Osteoporosis" , "Asthma" , 
                   "Depression" , "Oral health issues" , "HIV/AIDS" , "Tuberculosis" , "Malaria" , "Dengue fever" , "Hepatitis" , "Epilepsy" , "Multiple sclerosis"]

        
    diseases = set(["Heart disease" , "Cancer" , "Stroke" , "Respiratory diseases" , "Alzheimer's disease" , "Diabetes" , "Influenza and Pneumonia" , "Kidney diseases" ,
                        "Septicemia" , "Liver disease" , "Hypertension" , "Parkinson's disease" , "Chronic lower respiratory disease" , "Accidents/injuries" , 
                        "Osteoporosis" , "Asthma" ,
                        "Depression" , "Oral health issues" , "HIV/AIDS" , "Tuberculosis" , "Malaria" , "Dengue fever" , "Hepatitis" , 
                        "Epilepsy" , "Multiple sclerosis"])
    synonyms = {"Heart disease": ["cardiovascular disease", "coronary heart disease", "coronary artery disease", "coronary disease", "coronary heart disease", "coronary artery disease", "coronary disease", "heart attack"],
                "Cancer": ["malignancy", "neoplasm", "tumor", "malignant"] ,
                "Stroke":["myocardial infarction", "cerebral stroke", "brain attack", "brain stroke"],
                "Respiratory diseases":["lung disorders", "respiratory illnesses"],
                "Alzheimer's disease":["senile dementia", "dementia of the elderly"],
                "Diabetes":["hyperglycemia", "high blood sugar", "diabetic", "diabetes mellitus", "diabetes insipidus", "diabetes type 1", "diabetes type 2"],
                "Influenza and Pneumonia":["flu", "pneumonia", "lung infection"],
                "Kidney diseases":["renal diseases", "kidney problems"],
                "Septicemia":["sepsis", "blood infection"],
                "Liver disease":["hepatitis", "liver damage"],
                "Hypertension":["high blood pressure", "hypertensive disease"],
                "Parkinson's disease":["parkinsonsism", "paralysis of the face and body"],
                "Chronic lower respiratory disease":["chronic obstructive pulmonary disease", "lung cancer"],
                "Accidents/injuries":["trauma", "injury"], 
                "Osteoporosis":["brittle bone disease","osteomalacia"], 
                "Asthma":["asthma attacks", "lung constriction", "bronchial asthma", "bronchospasm", "bronchial hyperreactivity", "bronchial hyperresponsiveness"], 
                "Depression":["depressive disorder", "mood disorder", "mental illness", "mental disorder"],
                "Oral health issues":["oral infections", "dental problems", "dental caries"],
                "HIV/AIDS":["human immunodeficiency virus infection","acquired immune deficiency syndrome"], 
                "Tuberculosis":["TB", "mycobacterial infection"],
                "Malaria":["malaria fever", "malarial infection"],
                "Dengue fever":["dengue hemorrhagic fever", "dengue viral infection", "dengue"],
                "Hepatitis":["hepatitis A", "hepatitis B"],
                "Epilepsy":["seizures"],
                "Multiple sclerosis":["demyelinating disease"]}
        
    for disease in disease_list:

        # counting the occurrence of the disease ignoring case
        occurrence = re.findall(disease, pm_vol1, re.IGNORECASE) + re.findall(disease, pm_vol2, re.IGNORECASE) + re.findall(disease, pm_vol3, re.IGNORECASE) + re.findall(disease, pm_vol4 , re.IGNORECASE) + re.findall(disease, pm_vol5, re.IGNORECASE)
        
        for syn in synonyms[disease]:
            occurrence += re.findall(syn, pm_vol1, re.IGNORECASE) + re.findall(syn, pm_vol2, re.IGNORECASE) + re.findall(syn, pm_vol3, re.IGNORECASE) + re.findall(syn, pm_vol4 , re.IGNORECASE) + re.findall(syn, pm_vol5, re.IGNORECASE)

        # printing the disease name and the corresponding occurrence value
        print("Disease : " + disease + " | Occurrence : " + str(len(occurrence)))
   

# calling the searchText() method
searchText()