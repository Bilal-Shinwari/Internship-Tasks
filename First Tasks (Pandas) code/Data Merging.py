import pandas as pd
import numpy as np

#Reading .xlsx files
case_textual_df=pd.read_excel("D:\Internship Red Buffer\Tasks\First Tasks (Pandas) code\case_textual_details.xlsx")
cases_df=pd.read_excel("cases.xlsx")
#reading .csv files
case_dollar_df=pd.read_csv("case_dollar_stats.csv")

#Convert Function
def convertToint(x):
    if x==np.nan:
        return np.nan
    else:
        return int(x)

#Data Cleaning 
cases_df['age'] =pd.to_numeric(cases_df['age'],errors='coerce')
cases_df['trial_length'] =pd.to_numeric(cases_df['trial_length'],errors='coerce')
cases_df['trial_length_days'] =pd.to_numeric(cases_df['trial_length_days'],errors='coerce')

#Filling Nan value with Zero
cases_df.fillna(0,inplace=True)

#converting it to int
cases_df['age']=cases_df['age'].apply(convertToint)
cases_df['trial_length']=cases_df['trial_length'].apply(convertToint)
cases_df['trial_length_days']=cases_df['trial_length_days'].apply(convertToint)


#Data Merged
merged_data=pd.merge(case_textual_df,cases_df,how="inner",on="case_text_id")
merged_data=pd.merge(merged_data,case_dollar_df,how="inner",on="case_dollar_stats_id")

#Adding Two columns
merged_data["total_money_case"] = merged_data["award_total"] + merged_data["award_actual"] + merged_data["final_demand"] +merged_data["case_specials"] + merged_data["cum_total_special"] + merged_data["cum_general_special"]
merged_data["ratio_case_general_to_specials"] =merged_data["case_generals"]/merged_data["case_specials"]

#Filter DataFrames
filtered_df1=merged_data[merged_data['award_total'] > merged_data['award_actual']*1/2]
filtered_df2=merged_data[(merged_data['report_type_desc'] =="Settlement") & (merged_data["case_end_data"].apply(lambda x:x.year <2010))]

#saving merged .csv and .xlsx
merged_data.to_csv("merged_data.csv",index=False)
merged_data.to_excel("merged_data.xlsx",index=False)

#printing Data
print(merged_data.info())
print(filtered_df1.head())
print(filtered_df2)





