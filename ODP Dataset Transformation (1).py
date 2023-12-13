#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 

degree2yr = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Degrees_and_Certificates_Awarded.xlsx', sheet_name = '2yr.AwardsByLevel')
degree2yr = degree2yr.drop([0,1,2])
degree2yr = degree2yr.reset_index(drop=True)

columns = {
  'Degrees and Certificates Awarded by Level': 'Fice',
    'Unnamed: 1' : 'Institution_name', 
    'Unnamed: 2' : 'Cert20',
    'Unnamed: 3' : 'Ass20',
    'Unnamed: 4' : 'Bacc20',
    'Unnamed: 5' : 'Total20',
    'Unnamed: 6' : 'Cert21',
    'Unnamed: 7' : 'Ass21',
    'Unnamed: 8' : 'Bacc21',
    'Unnamed: 9' : 'Total21',
    'Unnamed: 10': 'Cert22',
    'Unnamed: 11': 'Ass22',
    'Unnamed: 12': 'Bacc22',
    'Unnamed: 13': 'Total22'
}
degree2yr = degree2yr.rename(columns=columns)
degree2yr = degree2yr.drop([0, 91, 92, 93])
degree2yr = degree2yr.reset_index(drop=True)

columns = ['Fice', 
           'Institution',
           'Certificates', 
           'Associates', 
           'Bacchelors', 
           'Total']

yr20 = degree2yr[['Fice', 
                  'Institution_name', 
                  'Cert20', 
                  'Ass20', 
                  'Bacc20',
                  'Total20']]
yr20.columns = columns
yr20.insert(0, 'Report Year', 2020)

yr21 = degree2yr[['Fice', 
                  'Institution_name', 
                  'Cert21', 
                  'Ass21', 
                  'Bacc21',
                  'Total21']]
yr21.columns = columns
yr21.insert(0, 'Report Year', 2021)

yr22 = degree2yr[['Fice', 
                  'Institution_name', 
                  'Cert22', 
                  'Ass22', 
                  'Bacc22',
                  'Total22']]
yr22.columns = columns
yr22.insert(0, 'Report Year', 2022)

df = pd.concat([yr20, yr21, yr22], ignore_index=True)

removed_values = [
'Alamo Community College District',
'Dallas College Brookhaven',
'Dallas College Cedar Valley',
'Dallas College Eastfield',
'Dallas College El Centro',
'Dallas College Mountain View',
'Dallas College North Lake',
'Dallas College Richland',
'Howard County Junior College\nDistrict',
'Lone Star College System',
'San Jacinto CCD-Central Campus',
'San Jacinto CCD-North Campus',
'San Jacinto CCD-South Campus',
'Tarrant CCD-Connect Campus',
'Tarrant CCD-Northeast Campus',
'Tarrant CCD-Northwest Campus',
'Tarrant CCD-South Campus',
'Tarrant CCD-Southeast Campus',
'Tarrant CCD-Trinity River Campus',
]

df = df[~df['Institution'].isin(removed_values)]

rename = {
'Alamo CCD-Northwest Vista\nCollege'                   : 'Alamo CCD-Northwest Vista College',
'Alamo CCD-Northeast Lakeview\nCollege'                : 'Alamo CCD-Northeast Lakeview College',
'Howard CJCD-SW College for the\nDeaf'                 : 'Howard CJCD-SW College for the Deaf',
'Texas State Technical College in\nWaco'               : 'Texas State Technical College in Waco' ,
'College of the Mainland\nCommunity College District'  : 'College of the Mainland Community College District',
'Texas State Technical College in\nHarlingen'          : 'Texas State Technical College in Harlingen',
'Texas State Technical College in\nWest Texas'         : 'Texas State Technical College in West Texas',
'El Paso Community College\nDistrict'                  : 'El Paso Community College District',
'Northeast Texas Community\nCollege'                   : 'Northeast Texas Community College',
'Collin County Community College\nDistrict'            : 'Collin County Community College District',
'Texas State Technical College in\nMarshall'           : 'Texas State Technical College in Marshall',
'Texas State Technical College\nConnect Campus'        : 'Texas State Technical College Connect Campus',
'Texas State Technical College in\nNorth Texas'        : 'Texas State Technical College in North Texas',
'Texas State Technical College in\nFt. Bend County'    : 'Texas State Technical College in Ft. Bend County',
'San Jacinto Community College\nDistrict'              : 'San Jacinto Community College District',
'Alamo CCD-St. Philip’s College'                       : 'Alamo CCD-St. Philip\'s College', 
'San Jacinto Community College District'               : 'San Jacinto College', 
'Southwest Texas Junior College'                       : 'Southwest Texas College', 
'Dallas College District'                              : 'Dallas College', 
'Tarrant County College District'                      : 'Tarrant County College'
}

df['Institution'] = df['Institution'].replace(rename)
df.replace(0, pd.NA, inplace=True)
df['Fice'] = df['Fice'].astype(str).apply(lambda x: x.replace('D', '0'))                               

df.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/Degrees and Certificates Awarded at Public 2-Year Institutions by Award Level.csv', index=False)


# In[5]:


degreehealth = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Degrees_and_Certificates_Awarded.xlsx', sheet_name = 'HRI.AwardsByLevel')
degreehealth = degreehealth.drop([0,1,2,3])
degreehealth = degreehealth.reset_index(drop=True)

columns = {
'Degrees and Certificates Awarded by Level': 'Fice', 
    'Unnamed: 1' : 'Institution', 
    'Unnamed: 2' : 'Cert20',
    'Unnamed: 3' : 'Bacc20',
    'Unnamed: 4' : 'Mast20', 
    'Unnamed: 5' : 'DocSch20', 
    'Unnamed: 6' : 'DocPro20', 
    'Unnamed: 7' : 'Total20',
    'Unnamed: 8' : 'Cert21', 
    'Unnamed: 9' : 'Bacc21', 
    'Unnamed: 10': 'Mast21', 
    'Unnamed: 11': 'DocSch21', 
    'Unnamed: 12': 'DocPro21',
    'Unnamed: 13': 'Total21', 
    'Unnamed: 14': 'Cert22', 
    'Unnamed: 15': 'Bacc22', 
    'Unnamed: 16': 'Mast22',
    'Unnamed: 17': 'DocSch22', 
    'Unnamed: 18': 'DocPro22', 
    'Unnamed: 19': 'Total22'
}

degreehealth = degreehealth.rename(columns=columns)
degreehealth = degreehealth.drop([12, 13, 14])
degreehealth = degreehealth.reset_index(drop=True)

columns = ['Fice', 
           'Institution', 
           'Certificate', 
           'Bachelors', 
           'Masters', 
           'DoctorResearchScholar', 
           'DoctoralProfPractice', 
           'Total']

yr20 = degreehealth[['Fice', 
                     'Institution', 
                     'Cert20', 
                     'Bacc20', 
                     'Mast20',
                     'DocSch20', 
                     'DocPro20', 
                     'Total20']]
yr20.columns = columns
yr20.insert(0, 'Report Year', 2020)

yr21 = degreehealth[['Fice', 
                     'Institution', 
                     'Cert21', 
                     'Bacc21', 
                     'Mast21',
                     'DocSch21', 
                     'DocPro21', 
                     'Total21']]
yr21.columns = columns
yr21.insert(0, 'Report Year', 2021)

yr22 = degreehealth[['Fice', 
                     'Institution', 
                     'Cert22', 
                     'Bacc22', 
                     'Mast22',
                     'DocSch22', 
                     'DocPro22', 
                     'Total22']]
yr22.columns = columns
yr22.insert(0, 'Report Year', 2022)

df = pd.concat([yr20, yr21, yr22], ignore_index=True)
df.replace(0, pd.NA, inplace=True)
df['Fice'] = df['Fice'].astype(str).apply(lambda x: x.replace('D', '0'))    

df.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/Degrees and Certificates Awarded at Public Health-Related Institutions by Award Level.csv', index=False)



# In[6]:


degreeuni = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Degrees_and_Certificates_Awarded.xlsx', sheet_name = 'Univ.AwardsByLevel')
degreeuni = degreeuni.drop([0,1,2,3])
degreeuni = degreeuni.reset_index(drop=True)

columns = {
    'Degrees and Certificates Awarded by Level': 'Fice',
    'Unnamed: 1' : 'Institution',
    'Unnamed: 2' : 'Ass20',
    'Unnamed: 3' : 'Bacc20', 
    'Unnamed: 4' : 'Mast20',
    'Unnamed: 5' : 'DocR20', 
    'Unnamed: 6' : 'DocP20', 
    'Unnamed: 7' : 'Tot20',
    'Unnamed: 8' : 'Ass21', 
    'Unnamed: 9' : 'Bacc21', 
    'Unnamed: 10': 'Mast21', 
    'Unnamed: 11': 'DocR21', 
    'Unnamed: 12': 'DocP21',
    'Unnamed: 13': 'Tot21', 
    'Unnamed: 14': 'Ass22', 
    'Unnamed: 15': 'Bacc22',
    'Unnamed: 16': 'Mast22',
    'Unnamed: 17': 'DocR22', 
    'Unnamed: 18': 'DocP22',
    'Unnamed: 19': 'Tot22'
}

degreeuni = degreeuni.rename(columns=columns)
degreeuni = degreeuni.drop([37, 38, 39])
degreeuni = degreeuni.reset_index(drop=True)

columns = ['Fice', 
           'Institution', 
           'Certificate', 
           'Bachelors', 
           'Masters', 
           'DoctorResearchScholar', 
           'DoctoralProfPractice', 
           'Total']

yr20 = degreeuni[['Fice', 
                     'Institution',
                     'Ass20',
                     'Bacc20',
                     'Mast20',
                     'DocR20',
                     'DocP20',
                     'Tot20']]
yr20.columns = columns
yr20.insert(0, 'Report Year', 2020)

yr21 = degreeuni[['Fice', 
                     'Institution',
                     'Ass21',
                     'Bacc21',
                     'Mast21',
                     'DocR21',
                     'DocP21',
                     'Tot21']]
yr21.columns = columns
yr21.insert(0, 'Report Year', 2021)

yr22 = degreeuni[['Fice', 
                     'Institution',
                     'Ass22',
                     'Bacc22',
                     'Mast22',
                     'DocR22',
                     'DocP22',
                     'Tot22']]
yr22.columns = columns
yr22.insert(0, 'Report Year', 2022)

df = pd.concat([yr20, yr21, yr22], ignore_index=True)
df.replace(0, pd.NA, inplace=True)
df['Fice'] = df['Fice'].astype(str).apply(lambda x: x.replace('D', '0')) 

df.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/Degrees and Certificates Awarded at Public Universities by Award level.csv', index=False)


# In[7]:


import pandas as pd
enrollgender = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Fall_Enrollment.xlsx', sheet_name = '2yr.EnrollbyGender')
enrollgender = enrollgender.drop([0,1,2,3])
enrollgender = enrollgender.reset_index(drop=True)
columns = {
    'Fall Enrollment by Gender': 'Fice',
    'Unnamed: 1' : 'Institution', 
    'Unnamed: 2' : 'M20', 
    'Unnamed: 3' : 'F20',
    'Unnamed: 4' : 'T20', 
    'Unnamed: 5' : 'M21', 
    'Unnamed: 6' : 'F21', 
    'Unnamed: 7' : 'T21', 
    'Unnamed: 8' : 'M22',
    'Unnamed: 9' : 'F22', 
    'Unnamed: 10': 'T22'
}

enrollgender = enrollgender.rename(columns=columns)
enrollgender = enrollgender.drop([81, 82, 83])
enrollgender = enrollgender.reset_index(drop=True)

columns = ['Fice', 
           'Institution', 
           'Male', 
           'Female', 
           'Total'
          ]

yr20 = enrollgender[['Fice', 
                     'Institution',
                     'M20',
                     'F20', 
                     'T20']]

yr20.columns = columns
yr20.insert(0, 'Report Year', 2020)

yr21 = enrollgender[['Fice', 
                     'Institution',
                     'M21',
                     'F21', 
                     'T21']]

yr21.columns = columns
yr21.insert(0, 'Report Year', 2021)

yr22 = enrollgender[['Fice', 
                     'Institution',
                     'M22',
                     'F22', 
                     'T22']]

yr22.columns = columns
yr22.insert(0, 'Report Year', 2022)

df = pd.concat([yr20, yr21, yr22], ignore_index=True)

drop = [
    'Alamo Community College District', 
    'Howard County Junior College District', 
    'Lone Star College System', 
    'Tarrant CCD-Connect Campus',
    'Tarrant CCD-Northeast Campus',
    'Tarrant CCD-Northwest Campus',
    'Tarrant CCD-South Campus',
    'Tarrant CCD-Southeast Campus',
    'Tarrant CCD-Trinity River Campus'
]

df = df[~df['Institution'].isin(drop)]

rename = {
    'College of the Mainland Community College\nDistrict' : 'College of the Mainland Community College District',
    'Texas State Technical College in Ft. Bend\nCounty'   : 'Texas State Technical College in Ft. Bend County', 
    'Dallas College District'                             : 'Dallas College', 
    'San Jacinto Community College District'              : 'San Jacinto College', 
    'Tarrant County College District'                     : 'Tarrant County College', 
    'Southwest Texas Junior College'                      : 'Southwest Texas College',
}

df['Institution'] = df['Institution'].replace(rename)
df.replace(0, pd.NA, inplace=True)
df['Fice'] = df['Fice'].astype(str).apply(lambda x: x.replace('D', '0')) 

df.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/Fall Enrollment at Public 2-Year Institutions by Gender.csv', index=False)


# In[36]:


enrollgenderU = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Fall_Enrollment.xlsx', sheet_name = 'Univ.EnrollbyGender')
enrollgenderU = enrollgenderU.drop([0,1,2,3])
enrollgenderU = enrollgenderU.reset_index(drop=True)

columns = {
    'Fall Enrollment by Gender': 'Fice',
    'Unnamed: 1' : 'Institution', 
    'Unnamed: 2' : 'M20', 
    'Unnamed: 3' : 'F20',
    'Unnamed: 4' : 'T20', 
    'Unnamed: 5' : 'M21', 
    'Unnamed: 6' : 'F21', 
    'Unnamed: 7' : 'T21', 
    'Unnamed: 8' : 'M22',
    'Unnamed: 9' : 'F22', 
    'Unnamed: 10': 'T22'
}

enrollgenderU = enrollgenderU.rename(columns=columns)
enrollgenderU = enrollgenderU.drop([37, 38, 39])
enrollgenderU = enrollgenderU.reset_index(drop=True)

columns = ['Fice', 
           'Institution', 
           'Male', 
           'Female', 
           'Total'
          ]

yr20 = enrollgenderU[['Fice', 
                     'Institution',
                     'M20',
                     'F20', 
                     'T20']]

yr20.columns = columns
yr20.insert(0, 'Report Year', 2020)

yr21 = enrollgenderU[['Fice', 
                     'Institution',
                     'M21',
                     'F21', 
                     'T21']]

yr21.columns = columns
yr21.insert(0, 'Report Year', 2021)

yr22 = enrollgenderU[['Fice', 
                     'Institution',
                     'M22',
                     'F22', 
                     'T22']]

yr22.columns = columns
yr22.insert(0, 'Report Year', 2022)

df = pd.concat([yr20, yr21, yr22], ignore_index=True)
df.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/Fall Enrollment at Public Universities by Gender.csv', index=False)


# In[9]:


enrollgenderHRI = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Fall_Enrollment.xlsx', sheet_name = 'HRI.EnrollbyGender')
enrollgenderHRI = enrollgenderHRI.drop([0,1,2,3])
enrollgenderHRI = enrollgenderHRI.reset_index(drop=True)

columns = {
    'Fall Enrollment by Gender': 'Fice',
    'Unnamed: 1' : 'Institution', 
    'Unnamed: 2' : 'M20', 
    'Unnamed: 3' : 'F20',
    'Unnamed: 4' : 'T20', 
    'Unnamed: 5' : 'M21', 
    'Unnamed: 6' : 'F21', 
    'Unnamed: 7' : 'T21', 
    'Unnamed: 8' : 'M22',
    'Unnamed: 9' : 'F22', 
    'Unnamed: 10': 'T22'
}

enrollgenderHRI = enrollgenderHRI.rename(columns=columns)
enrollgenderHRI = enrollgenderHRI.drop([14,15,16])
enrollgenderHRI = enrollgenderHRI.reset_index(drop=True)

columns = ['Fice', 
           'Institution', 
           'Male', 
           'Female', 
           'Total'
          ]

yr20 = enrollgenderHRI[['Fice', 
                     'Institution',
                     'M20',
                     'F20', 
                     'T20']]

yr20.columns = columns
yr20.insert(0, 'Report Year', 2020)

yr21 = enrollgenderHRI[['Fice', 
                     'Institution',
                     'M21',
                     'F21', 
                     'T21']]

yr21.columns = columns
yr21.insert(0, 'Report Year', 2021)

yr22 = enrollgenderHRI[['Fice', 
                     'Institution',
                     'M22',
                     'F22', 
                     'T22']]

yr22.columns = columns
yr22.insert(0, 'Report Year', 2022)

df = pd.concat([yr20, yr21, yr22], ignore_index=True)
df.replace(0, pd.NA, inplace=True)
df['Fice'] = df['Fice'].astype(str).apply(lambda x: x.replace('D', '0')) 

df.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/Fall Enrollment at Public Health-Related Institutions by Gender.csv', index=False)


# In[10]:


rate2yr_3 = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Graduation_Rates.xlsx', sheet_name = 'CTC3yrGradRates')
rate2yr_3 = rate2yr_3.drop([0,1,2,3,4])
rate2yr_3 = rate2yr_3.reset_index(drop=True)

columns = {
    'Three-Year Graduation Rates at Two-Year Colleges' : 'Fice', 
    'Unnamed: 1' : 'Institution',
    'Unnamed: 2' : 'Ethnicity', 
    'Unnamed: 3' : 'Category', 
    'Unnamed: 4' : 'Cohort17', 
    'Unnamed: 5' : 'Grad17', 
    'Unnamed: 6' : 'Rate17',
    'Unnamed: 7' : 'Cohort18', 
    'Unnamed: 8' : 'Grad18', 
    'Unnamed: 9' : 'Rate18', 
    'Unnamed: 10': 'Cohort19', 
    'Unnamed: 11': 'Grad19',
    'Unnamed: 12': 'Rate19'
}

rate2yr_3 = rate2yr_3.rename(columns=columns)
rate2yr_3 = rate2yr_3.drop([490, 491, 492, 493, 494, 495, 496, 497, 498])
rate2yr_3 = rate2yr_3.reset_index(drop=True)

rate2yr_3 = rate2yr_3[rate2yr_3['Category'] == 'Total']
rate2yr_3 = rate2yr_3.reset_index(drop=True)


columns = ['Fice', 
           'Institution', 
           'CohortCount3yr', 
           'GradRate3yr'
          ]

co17 = rate2yr_3[['Fice', 
                     'Institution',
                     'Cohort17', 
                     'Rate17']]

co17.columns = columns
co17.insert(2, 'CohortYear3yr', 2017)
co17.insert(0, 'ReportYear', 2020)

co18 = rate2yr_3[['Fice', 
                     'Institution',
                     'Cohort18', 
                     'Rate18']]

co18.columns = columns
co18.insert(2, 'CohortYear3yr', 2018)
co18.insert(0, 'ReportYear', 2021)

co19 = rate2yr_3[['Fice', 
                     'Institution',
                     'Cohort19', 
                     'Rate19']]

co19.columns = columns
co19.insert(2, 'CohortYear3yr', 2019)
co19.insert(0, 'ReportYear', 2022)

df1 = pd.concat([co17, co18, co19], ignore_index=True)

rename = {
    'Dallas College District'                             : 'Dallas College', 
    'San Jacinto Community College'                       : 'San Jacinto College', 
    'Tarrant County College District'                     : 'Tarrant County College', 
    'Southwest Texas Junior College'                      : 'Southwest Texas College',
    'Howard County Junior College District'               : 'Howard CJCD-Howard College'
}

df1['Institution'] = df1['Institution'].replace(rename)

drop = [
    'Howard CJCD-Howard College'
]

df1 = df1[~df1['Institution'].isin(drop)]
#df1.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/df1.csv', index=False)
#print(df1)


# In[11]:


rate2yr_4 = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Graduation_Rates.xlsx', sheet_name = 'CTC4yrGradRates')
rate2yr_4 = rate2yr_4.drop([0,1,2,3,4])
rate2yr_4 = rate2yr_4.reset_index(drop=True)

columns = {
    'Four-Year Graduation Rates at Two-Year Colleges' : 'Fice', 
    'Unnamed: 1' : 'Institution',
    'Unnamed: 2' : 'Ethnicity', 
    'Unnamed: 3' : 'Category', 
    'Unnamed: 4' : 'Cohort16', 
    'Unnamed: 5' : 'Grad16', 
    'Unnamed: 6' : 'Rate16',
    'Unnamed: 7' : 'Cohort17', 
    'Unnamed: 8' : 'Grad17', 
    'Unnamed: 9' : 'Rate17', 
    'Unnamed: 10': 'Cohort18', 
    'Unnamed: 11': 'Grad18',
    'Unnamed: 12': 'Rate18'
}

rate2yr_4 = rate2yr_4.rename(columns=columns)

rate2yr_4 = rate2yr_4.drop([482, 483, 484, 485, 486, 487, 488, 489, 490])

rate2yr_4 = rate2yr_4.reset_index(drop=True)

rate2yr_4 = rate2yr_4[rate2yr_4['Category'] == 'Total']
rate2yr_4 = rate2yr_4.reset_index(drop=True)

columns = ['Fice', 
           'Institution', 
           'CohortCount4yr', 
           'GradRate4yr'
          ]

co16 = rate2yr_4[['Fice', 
                     'Institution',
                     'Cohort16', 
                     'Rate16']]

co16.columns = columns
co16.insert(2, 'CohortYear4yr', 2016)
co16.insert(0, 'ReportYear', 2020)

co17 = rate2yr_4[['Fice', 
                     'Institution',
                     'Cohort17', 
                     'Rate17']]

co17.columns = columns
co17.insert(2, 'CohortYear4yr', 2017)
co17.insert(0, 'ReportYear', 2021)

co18 = rate2yr_4[['Fice', 
                     'Institution',
                     'Cohort18', 
                     'Rate18']]

co18.columns = columns
co18.insert(2, 'CohortYear4yr', 2018)
co18.insert(0, 'ReportYear', 2022)

df2 = pd.concat([co16, co17, co18], ignore_index=True)

drop = [
    'Howard County Junior College District'
]
df2 = df2[~df2['Institution'].isin(drop)]

#df2.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/df2.csv', index=False)
#print(df2)


# In[12]:


rate2yr_6 = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Graduation_Rates.xlsx', sheet_name = 'CTC6yrGradRates')
rate2yr_6 = rate2yr_6.drop([0,1,2,3,4])
rate2yr_6 = rate2yr_6.reset_index(drop=True)


columns = {
    'Six-Year Graduation Rates at Two-Year Colleges' : 'Fice', 
    'Unnamed: 1' : 'Institution',
    'Unnamed: 2' : 'Ethnicity', 
    'Unnamed: 3' : 'Category', 
    'Unnamed: 4' : 'Cohort14', 
    'Unnamed: 5' : 'Grad14', 
    'Unnamed: 6' : 'Rate14',
    'Unnamed: 7' : 'Cohort15', 
    'Unnamed: 8' : 'Grad15', 
    'Unnamed: 9' : 'Rate15', 
    'Unnamed: 10': 'Cohort16', 
    'Unnamed: 11': 'Grad16',
    'Unnamed: 12': 'Rate16'
}

rate2yr_6 = rate2yr_6.rename(columns=columns)
rate2yr_6 = rate2yr_6.drop([483, 484, 485, 486, 487, 488, 489, 490])
rate2yr_4 = rate2yr_4.reset_index(drop=True)

rate2yr_6 = rate2yr_6[rate2yr_6['Category'] == 'Total']
rate2yr_6 = rate2yr_6.reset_index(drop=True)

columns = ['Fice', 
           'Institution', 
           'CohortCount6yr', 
           'GradRate6yr'
          ]

co14 = rate2yr_6[['Fice', 
                     'Institution',
                     'Cohort14', 
                     'Rate14']]

co14.columns = columns
co14.insert(2, 'CohortYear6yr', 2014)
co14.insert(0, 'ReportYear', 2020)

co15 = rate2yr_6[['Fice', 
                     'Institution',
                     'Cohort15', 
                     'Rate15']]

co15.columns = columns
co15.insert(2, 'CohortYear6yr', 2015)
co15.insert(0, 'ReportYear', 2021)

co16 = rate2yr_6[['Fice', 
                     'Institution',
                     'Cohort16', 
                     'Rate16']]

co16.columns = columns
co16.insert(2, 'CohortYear6yr', 2016)
co16.insert(0, 'ReportYear', 2022)

df3 = pd.concat([co14, co15, co16], ignore_index=True)

drop = [
    'Howard County Junior College District'
]
df3 = df3[~df3['Institution'].isin(drop)]

#df3.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/df3.csv', index=False)
#print(df3)


# In[19]:


merged_df = pd.merge(df1, df2, on=['Fice', 'ReportYear'], how='left')
merged_df = pd.merge(merged_df, df3, on=['Fice', 'ReportYear'], how='left')

merged_df = merged_df.drop(columns=['Institution', 'Institution_y'])
merged_df = merged_df.rename(columns={'Institution_x': 'Institution'})

merged_df.replace(0, pd.NA, inplace=True)
merged_df['Fice'] = merged_df['Fice'].astype(str).apply(lambda x: x.replace('D', '0')) 

merged_df.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/Graduation Rates at Public 2-Year Institutions.csv', index=False)
#print(merged_df)


# In[30]:


rateuni_4 = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Graduation_Rates.xlsx', sheet_name = 'Univ4yrGradRates')
rateuni_4 = rateuni_4.drop([0,1,2,3])
rateuni_4 = rateuni_4.reset_index(drop=True)

columns = {
    'Four-Year Graduation Rates for Public Universities' : 'Fice', 
    'Unnamed: 1' : 'Institution',
    'Unnamed: 2' : 'Ethnicity', 
    'Unnamed: 3' : 'Category', 
    'Unnamed: 4' : 'Cohort16', 
    'Unnamed: 5' : 'Grad16', 
    'Unnamed: 6' : 'Rate16',
    'Unnamed: 7' : 'Cohort17', 
    'Unnamed: 8' : 'Grad17', 
    'Unnamed: 9' : 'Rate17', 
    'Unnamed: 10': 'Cohort18', 
    'Unnamed: 11': 'Grad18',
    'Unnamed: 12': 'Rate18'
}

rateuni_4 = rateuni_4.rename(columns=columns)

rateuni_4 = rateuni_4[rateuni_4['Category'] == 'Total']
rateuni_4 = rateuni_4.reset_index(drop=True)

rateuni_4 = rateuni_4.drop([35])
rateuni_4 = rateuni_4.reset_index(drop=True)
print(rateuni_4)

columns = ['Fice', 
           'Institution', 
           'CohortCount4yr', 
           'GradRate4yr'
          ]

co16 = rateuni_4[['Fice', 
                     'Institution',
                     'Cohort16', 
                     'Rate16']]

co16.columns = columns
co16.insert(2, 'CohortYear4yr', 2016)
co16.insert(0, 'ReportYear', 2020)

co17 = rateuni_4[['Fice', 
                     'Institution',
                     'Cohort17', 
                     'Rate17']]

co17.columns = columns
co17.insert(2, 'CohortYear4yr', 2017)
co17.insert(0, 'ReportYear', 2021)

co18 = rateuni_4[['Fice', 
                     'Institution',
                     'Cohort18', 
                     'Rate18']]

co18.columns = columns
co18.insert(2, 'CohortYear4yr', 2018)
co18.insert(0, 'ReportYear', 2022)

df1 = pd.concat([co16, co17, co18], ignore_index=True)

#df1.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/df1.csv', index=False)

#print(df1)


# In[31]:


rateuni_5 = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Graduation_Rates.xlsx', sheet_name = 'Univ5yrGradRates')
rateuni_5 = rateuni_5.drop([0,1,2,3])
rateuni_5 = rateuni_5.reset_index(drop=True)

columns = {
    'Five-Year Graduation Rates for Public Universities' : 'Fice', 
    'Unnamed: 1' : 'Institution',
    'Unnamed: 2' : 'Ethnicity', 
    'Unnamed: 3' : 'Category', 
    'Unnamed: 4' : 'Cohort15', 
    'Unnamed: 5' : 'Grad15', 
    'Unnamed: 6' : 'Rate15',
    'Unnamed: 7' : 'Cohort16', 
    'Unnamed: 8' : 'Grad16', 
    'Unnamed: 9' : 'Rate16', 
    'Unnamed: 10': 'Cohort17', 
    'Unnamed: 11': 'Grad17',
    'Unnamed: 12': 'Rate17'
}
rateuni_5 = rateuni_5.rename(columns=columns)
rateuni_5 = rateuni_5.reset_index(drop=True)
rateuni_5 = rateuni_5[rateuni_5['Category'] == 'Total']
rateuni_5 = rateuni_5.reset_index(drop=True)
#print(rateuni_5)

rateuni_5 = rateuni_5.drop([35])

columns = ['Fice', 
           'Institution', 
           'CohortCount5yr', 
           'GradRate5yr'
          ]

co15 = rateuni_5[['Fice', 
                     'Institution',
                     'Cohort15', 
                     'Rate15']]

co15.columns = columns
co15.insert(2, 'CohortYear5yr', 2015)
co15.insert(0, 'ReportYear', 2020)

co16 = rateuni_5[['Fice', 
                     'Institution',
                     'Cohort16', 
                     'Rate16']]

co16.columns = columns
co16.insert(2, 'CohortYear5yr', 2016)
co16.insert(0, 'ReportYear', 2021)

co17 = rateuni_5[['Fice', 
                     'Institution',
                     'Cohort17', 
                     'Rate17']]

co17.columns = columns
co17.insert(2, 'CohortYear5yr', 2017)
co17.insert(0, 'ReportYear', 2022)

df2 = pd.concat([co15, co16, co17], ignore_index=True)

#df2.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/df1.csv', index=False)
#print(df2)


# In[32]:


rateuni_6 = pd.read_excel('/Users/oliviaenriquez/Desktop/Fall_23/ODP/predefined/Graduation_Rates.xlsx', sheet_name = 'Univ6yrGradRates')
rateuni_6 = rateuni_6.drop([0,1,2,3])
rateuni_6 = rateuni_6.reset_index(drop=True)

columns = {
    'Six-Year Graduation Rates for Public Universities' : 'Fice', 
    'Unnamed: 1' : 'Institution',
    'Unnamed: 2' : 'Ethnicity', 
    'Unnamed: 3' : 'Category', 
    'Unnamed: 4' : 'Cohort14', 
    'Unnamed: 5' : 'Grad14', 
    'Unnamed: 6' : 'Rate14',
    'Unnamed: 7' : 'Cohort15', 
    'Unnamed: 8' : 'Grad15', 
    'Unnamed: 9' : 'Rate15', 
    'Unnamed: 10': 'Cohort16', 
    'Unnamed: 11': 'Grad16',
    'Unnamed: 12': 'Rate16'
}
rateuni_6 = rateuni_6.rename(columns=columns)
rateuni_6 = rateuni_6.drop([263,264,265,266,267])
rateuni_6 = rateuni_6.reset_index(drop=True)

rateuni_6 = rateuni_6[rateuni_6['Category'] == 'Total']
rateuni_6 = rateuni_6.reset_index(drop=True)

columns = ['Fice', 
           'Institution', 
           'CohortCount6yr', 
           'GradRate6yr'
          ]

co14 = rateuni_6[['Fice', 
                     'Institution',
                     'Cohort14', 
                     'Rate14']]

co14.columns = columns
co14.insert(2, 'CohortYear6yr', 2014)
co14.insert(0, 'ReportYear', 2020)

co15 = rateuni_6[['Fice', 
                     'Institution',
                     'Cohort15', 
                     'Rate15']]

co15.columns = columns
co15.insert(2, 'CohortYear6yr', 2015)
co15.insert(0, 'ReportYear', 2021)

co16 = rateuni_6[['Fice', 
                     'Institution',
                     'Cohort16', 
                     'Rate16']]

co16.columns = columns
co16.insert(2, 'CohortYear6yr', 2016)
co16.insert(0, 'ReportYear', 2022)

df3 = pd.concat([co14, co15, co16], ignore_index=True)

#df3.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/df1.csv', index=False)

#print(df3)


# In[35]:


merged_df = pd.merge(df3, df2, on=['Fice', 'ReportYear'], how='left')
merged_df = pd.merge(merged_df, df1, on=['Fice', 'ReportYear'], how='left')

merged_df = merged_df.drop(columns=['Institution', 'Institution_y'])
merged_df = merged_df.rename(columns={'Institution_x': 'Institution'})

merged_df.replace(0, pd.NA, inplace=True)
merged_df['Fice'] = merged_df['Fice'].astype(str).apply(lambda x: x.replace('D', '0')) 
merged_df = merged_df[['ReportYear', 'Fice', 'Institution', 'CohortYear4yr', 'CohortCount4yr', 'GradRate4yr', 'CohortYear5yr', 'CohortCount5yr', 'GradRate5yr', 'CohortYear6yr', 'CohortCount6yr', 'GradRate6yr']]

print(merged_df)
merged_df.to_csv('/Users/oliviaenriquez/Desktop/Fall_23/ODP/Graduation Rates at Public Universities.csv', index=False)


# In[ ]:





# In[ ]:




