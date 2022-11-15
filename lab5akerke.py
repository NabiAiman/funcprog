resume = ["Myrzaly", "Akerke", "Sabitkyzy", "Almaty", "Satbayev University",]
print("Lastname:", resume[0], "\nName:", resume[1], "\nMiddleName:", resume[2], "\nCity:", resume[3], "\nUniversityty:", resume[4])

resume.append("020323601354") #ИИН қосу
print("\n", resume)

resumesecond = ["23.03.2002", "87078335178"] #екі листті біріктіру
resume.extend(resumesecond)
print("\n", resume)

x = "23.03.2002"
resume.insert(3, x) #x-тің мәнін индекс бойынша орналастыру
print("\n", resume)

resume.pop(5) #индекс бойынша элементті өшіру
print("\n", resume)

resume.reverse() # листті керісінше ауыстырып береді
print("\n", resume)

resume.clear() # листті тазалап береді
print("\n", resume)
