import pandas as pd
import numpy  as np

df = pd.read_csv('Artjoms Kasperovičs - adult.data.csv')
print(df.info())

df_complete = df.dropna() 
adult = np.array(df_complete)
print("------------------------------------------------------------")
#Cik daudz cilvēku no katras rases ir pārstāvēti šajā datu kopā? (Rasu nosaukumi pieejami slejā `race`)
race = df["race"].value_counts()
print(race)
print("------------------------------------------------------------")
#Kāds ir vīriešu vidējais vecums?
print("visiem minimum:",np.amin(adult[:,0]),"gadi")
print("visiem maximum:",np.amax(adult[:,0]),"gadi")
videja = round(df.loc[df['sex'] == "Male",'age'].mean())
print(videja,"minimum gadi(tikai vīriešu)")
print("------------------------------------------------------------")
#Kāds ir to cilvēku īpatsvars(%), kuriem ir bakalaura grāds?
ed = df["education"].value_counts()
procent1=round(ed["Bachelors"])
procent2= procent1 / ed.sum() * 100
print(format(procent2,".1f"),"%" ,"cilvēku īpatsvars, kuriem ir bakalaura grāds")
print("------------------------------------------------------------")
#Kāds procentuālais daudzums cilvēku ar augstāko izglītību (`Bachelors`, `Masters`, or `Doctorate`) pelna vairāk nekā 50 tūkstošus?
yuy = df['education'].isin(["Bachelors","Masters","Doctorate"])
zarplata=df["salary"] == ">50K"
rich = round(df.loc[yuy & zarplata].shape[0] / df.loc[yuy].shape[0]*100)
print(rich, "cilvēku ar augstāko izglītību (`Bachelors`, `Masters`, or `Doctorate`) pelna vairāk nekā 50 tūkstošus")
print("------------------------------------------------------------")
poor = round(df.loc[~yuy & zarplata].shape[0] / df.loc[~yuy].shape[0]*100)
print(poor,"cilvēku bez augstākās izglītības pelna vairāk nekā 50 tūkstošus")

print("------------------------------------------------------------")
#Kāds ir minimālais stundu skaits, ko cilvēks strādā nedēļā?
minimus = df["hours-per-week"].min()
print(minimus ,"minimālais stundu skaits")
print("------------------------------------------------------------")
min2 = df[df["hours-per-week"] == minimus].shape[0]
procet_time = round(df[(df["hours-per-week"] == minimus) & (df["salary"] == ">50K")].shape[0] / min2 * 100)

print(procet_time,"%","procents cilvēku, kas strādā minimālo stundu skaitu nedēļā, saņem algu, kas pārsniedz 50 tūkstošus")
print("------------------------------------------------------------")
all = df.loc[df["salary"] == ">50K", "native-country"].value_counts(25) / df["native-country"].value_counts(25)
print(all)
big=all.idxmax()
print(big)


top_IN_occupation = df.loc[(df["native-country"] == "India") & (df["salary"] == ">50K"), "occupation"].value_counts()
print (top_IN_occupation)
