import pandas as pd
import csv

def Calculate_enthu(ph, ps, bh, cm, rs):
    if rs == "Single_and_stud":
        r = 0.2
    elif rs == "Long_distance_lover":
        r = 0
    else:
        r = -0.2
    enthu = (ph/20)*(0.4) + (ps/10)*(0.2) + (bh/10)*(0.2) - (cm/8)*(0.2) + r
    return enthu


df = pd.read_csv("galaxy_data_sk.csv")


'''creating sub dataframes of all the halls'''
df_hall2 = df[df['Hall']==2]
df_hall3 = df[df['Hall']==3]
df_hall5 = df[df['Hall']==5]
df_hall6 = df[df['Hall']==6]
df_hall12 = df[df['Hall']==12]

'''Finding mean of Practice hours'''
ph_mean2 = df_hall2['Practice_hours'].mean(skipna = True)
ph_mean3 = df_hall3['Practice_hours'].mean(skipna = True)
ph_mean5 = df_hall5['Practice_hours'].mean(skipna = True)
ph_mean6 = df_hall6['Practice_hours'].mean(skipna = True)
ph_mean12 = df_hall12['Practice_hours'].mean(skipna = True)

'''Finding median of Posts shared'''
ps_median2 = df_hall2['Posts_shared'].median(skipna = True)
ps_median3 = df_hall3['Posts_shared'].median(skipna = True)
ps_median5 = df_hall5['Posts_shared'].median(skipna = True)
ps_median6 = df_hall6['Posts_shared'].median(skipna = True)
ps_median12 = df_hall12['Posts_shared'].median(skipna = True)

'''Finding median of Bulla hours'''
bh_median2 = df_hall2['Bulla_hours'].median(skipna = True)
bh_median3 = df_hall3['Bulla_hours'].median(skipna = True)
bh_median5 = df_hall5['Bulla_hours'].median(skipna = True)
bh_median6 = df_hall6['Bulla_hours'].median(skipna = True)
bh_median12 = df_hall12['Bulla_hours'].median(skipna = True)

'''Finding mean of Classes missed'''
cm_mean2 = df_hall2['Classes_missed'].mean(skipna = True)
cm_mean3 = df_hall3['Classes_missed'].mean(skipna = True)
cm_mean5 = df_hall5['Classes_missed'].mean(skipna = True)
cm_mean6 = df_hall6['Classes_missed'].mean(skipna = True)
cm_mean12 = df_hall12['Classes_missed'].mean(skipna = True)

'''Finding the number of hall residents'''
h2_num = len(df_hall2.axes[0])
h3_num = len(df_hall3.axes[0])
h5_num = len(df_hall3.axes[0])
h6_num = len(df_hall6.axes[0])
h12_num = len(df_hall12.axes[0])


'''To fill missing entries'''
for i in range(h2_num):
    if(pd.isna(df_hall2.iloc[i,5])):
        df_hall2.iloc[i,5] = "Single_and_stud"
for i in range(h3_num):
    if(pd.isna(df_hall3.iloc[i,5])):
        df_hall3.iloc[i,5] = "Single_and_stud"
for i in range(h5_num):
    if(pd.isna(df_hall5.iloc[i,5])):
        df_hall5.iloc[i,5] = "Committed_inside_campus"
for i in range(h6_num):
    if(pd.isna(df_hall6.iloc[i,5])):
        df_hall6.iloc[i,5] = "Single_and_stud"
for i in range(h12_num):
    if(pd.isna(df_hall12.iloc[i,5])):
        df_hall12.iloc[i,5] = "Single_and_stud"

for i in range(h2_num):
    if(pd.isna(df_hall2.iloc[i,1])):
        df_hall2.iloc[i,1] = ph_mean2
for i in range(h3_num):
    if(pd.isna(df_hall3.iloc[i,1])):
        df_hall3.iloc[i,1] = ph_mean3
for i in range(h5_num):
    if(pd.isna(df_hall5.iloc[i,1])):
        df_hall5.iloc[i,1] = ph_mean5
for i in range(h6_num):
    if(pd.isna(df_hall6.iloc[i,1])):
        df_hall6.iloc[i,1] = ph_mean6
for i in range(h12_num):
    if(pd.isna(df_hall12.iloc[i,1])):
        df_hall12.iloc[i,1] = ph_mean12

for i in range(h2_num):
    if(pd.isna(df_hall2.iloc[i,2])):
        df_hall2.iloc[i,2] = ps_median2
for i in range(h3_num):
    if(pd.isna(df_hall3.iloc[i,2])):
        df_hall3.iloc[i,2] = ps_median3
for i in range(h5_num):
    if(pd.isna(df_hall5.iloc[i,2])):
        df_hall5.iloc[i,2] = ps_median5
for i in range(h6_num):
    if(pd.isna(df_hall6.iloc[i,2])):
        df_hall6.iloc[i,2] = ps_median6
for i in range(h12_num):
    if(pd.isna(df_hall12.iloc[i,2])):
        df_hall12.iloc[i,2] = ps_median12

for i in range(h2_num):
    if(pd.isna(df_hall2.iloc[i,3])):
        df_hall2.iloc[i,3] = bh_median2
for i in range(h3_num):
    if(pd.isna(df_hall3.iloc[i,3])):
        df_hall3.iloc[i,3] = bh_median3
for i in range(h5_num):
    if(pd.isna(df_hall5.iloc[i,3])):
        df_hall5.iloc[i,3] = bh_median5
for i in range(h6_num):
    if(pd.isna(df_hall6.iloc[i,3])):
        df_hall6.iloc[i,3] = bh_median6
for i in range(h12_num):
    if(pd.isna(df_hall12.iloc[i,3])):
        df_hall12.iloc[i,3] = bh_median12


for i in range(h2_num):
    if(pd.isna(df_hall2.iloc[i,4])):
        df_hall2.iloc[i,4] = cm_mean2
for i in range(h3_num):
    if(pd.isna(df_hall3.iloc[i,4])):
        df_hall3.iloc[i,4] = cm_mean3
for i in range(h5_num):
    if(pd.isna(df_hall5.iloc[i,4])):
        df_hall5.iloc[i,4] = cm_mean5
for i in range(h6_num):
    if(pd.isna(df_hall6.iloc[i,4])):
        df_hall6.iloc[i,4] = cm_mean6
for i in range(h12_num):
    if(pd.isna(df_hall12.iloc[i,4])):
        df_hall12.iloc[i,4] = cm_mean12


'''To find average of each hall'''
avg = []

total = 0
for i in range(h2_num):
    
    df_hall2.iloc[i,5] = Calculate_enthu(
        df_hall2.iloc[i,1],
        df_hall2.iloc[i,2],
        df_hall2.iloc[i,3], 
        df_hall2.iloc[i,4],
        df_hall2.iloc[i,5])
    total += df_hall2.iloc[i, 5]
avg_h2 = total/h2_num
avg.append(avg_h2)


total = 0
for i in range(h3_num):
    
    df_hall3.iloc[i,5] = Calculate_enthu(
        df_hall3.iloc[i,1],
        df_hall3.iloc[i,2],
        df_hall3.iloc[i,3], 
        df_hall3.iloc[i,4],
        df_hall3.iloc[i,5])
    total += df_hall3.iloc[i, 5]
avg_h3 = total/h3_num
avg.append(avg_h3)


total = 0
for i in range(h5_num):
    
    df_hall5.iloc[i,5] = Calculate_enthu(
        df_hall5.iloc[i,1],
        df_hall5.iloc[i,2],
        df_hall5.iloc[i,3], 
        df_hall5.iloc[i,4],
        df_hall5.iloc[i,5])
    total += df_hall5.iloc[i, 5]
avg_h5 = total/h5_num
avg.append(total/h5_num)

total = 0
for i in range(h6_num):
    
    df_hall6.iloc[i,5] = Calculate_enthu(
        df_hall6.iloc[i,1],
        df_hall6.iloc[i,2],
        df_hall6.iloc[i,3], 
        df_hall6.iloc[i,4],
        df_hall6.iloc[i,5])
    total += df_hall6.iloc[i, 5]
avg_h6 = total/h6_num
avg.append(total/h6_num)

total = 0
for i in range(h12_num):
    
    df_hall12.iloc[i,5] = Calculate_enthu(
        df_hall12.iloc[i,1],
        df_hall12.iloc[i,2],
        df_hall12.iloc[i,3], 
        df_hall12.iloc[i,4],
        df_hall12.iloc[i,5])
    total += df_hall12.iloc[i, 5]
avg_h12 = total/h12_num
avg.append(total/h12_num)

win_val = max(avg)

if win_val == avg_h2:
    print("Winner of Galaxy is HALL-2")
elif win_val == avg_h3:
    print("Winner of Galaxy is HALL-3")
elif win_val == avg_h5:
    print("Winner of Galaxy is HALL-5")
elif win_val == avg_h6:
    print("Winner of Galaxy is HALL-6")
else:
    print("Winner of Galaxy is HALL-12")

with open('Solved.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Hall", "Practice_hours", "Posts_shared", "Bulla_hours", "Classes_missed", "Relationship_status", "Enthu"])
    for i in range(len(df.axes[0])):
        writer.writerow([df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4],df.iloc[i,5],df.iloc[i,6]])