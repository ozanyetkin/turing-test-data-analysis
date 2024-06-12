import pandas as pd
import numpy as np

cardio_alco = pd.read_csv("./data/cardio_alco.csv", delimiter=";")
cardio_base = pd.read_csv("./data/cardio_base.csv")
covid_data = pd.read_csv("./data/covid_data.csv")

# print(cardio_alco)
# print(cardio_base)
# print(covid_data)

cardio_base["age"] = cardio_base["age"].div(365).round(0)
q1 = cardio_base.groupby(by="age", as_index=False)['weight'].mean()

q2a = cardio_base[cardio_base["age"] > 50]['cholesterol'].mean()
q2b = cardio_base[cardio_base["age"] < 50]['cholesterol'].mean()

q3a = cardio_base[cardio_base["gender"] == 1]['smoke'].sum()
q3b = cardio_base[cardio_base["gender"] == 2]['smoke'].sum()

q4 = cardio_base["height"].nlargest(int(cardio_base.shape[0]/100))

q5 = cardio_base.corr(method="spearman")

q6a = cardio_base["height"].mean()
q6b = cardio_base["height"].std()
q6c = cardio_base[cardio_base["height"] > q6a + 2 * q6b]

q7 = pd.merge(cardio_base, cardio_alco)
q7a = q7[(q7["age"] > 50) & (q7["alco"] == 1)]
q7b = q7[q7["age"] > 50]

q8a = cardio_base[cardio_base["smoke"] == 1]["ap_hi"]
q8b = cardio_base[cardio_base["smoke"] == 0]["ap_hi"]

q9 = covid_data[(covid_data["location"] == "Germany") | (covid_data["location"] == "Italy")]
q9a = q9.groupby(q9['date'])[['new_cases']].sum()

q10 = covid_data[covid_data["location"] == "Italy"]
q10 = q10[(q10['date'] >= "2020-02-28") & (q10['date'] <= "2020-03-20")]
q10a = q10.groupby(q10['date'])[['new_cases']].sum()
# q10b = np.polyfit(np.arange(20), q10a, deg=2)

q11a = covid_data.groupby([covid_data["location"]])[["new_deaths"]].sum()
q11b = covid_data.groupby([covid_data["location"]])[["population"]].mean()
q11b["ratio"] = q11a.values / q11b.values

q12a = covid_data.groupby([covid_data["location"]])[["hospital_beds_per_thousand"]].mean()
q12b = covid_data.groupby([covid_data["location"]])[["gdp_per_capita"]].mean()
q12c = q12a.join(q12b)
