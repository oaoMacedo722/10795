import requests
user=[]

id = 9500
while True:
    url = f"https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1747004400&end=1747609200&_=1747127402466"

    response = requests.get(url)

    print(f"\n A procura do ID:{id}")

    if "Rogélio Manuel Nascimento Palma Rodrigues" in response.text and "Sessão como Formador" in response.text:
        user.append(id)
        break

    else:
        print("O formador rogelio não foi encontrado como formador",id)
        id +=1

print("ID encontrado")
for id in user:
    print(">>ID Rogelio:",id)