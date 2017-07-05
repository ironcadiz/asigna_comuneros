from random import choice,randint

class Comunero:

    def __init__(self,name,sex,activities):
        self.name  = name
        self.sex = sex # 1 for male 0 for Female
        self.done = {x:False for x in activities}
        self.partners = []
        self.count = 0

    def __repr__(self):
        return self.name

#gets array of comuneros from stdin
def get_comuneros(sex,activities):
    question_string = "Nombre de un comunero (enter si no quedan mas) " if sex else "Nombre de una comunera (enter si no quedan mas) "
    a = input(question_string).strip()
    comuneros = []
    while a != "":
        comuneros.append(Comunero(a,sex,activities))
        a = input(question_string).strip()
    return comuneros

def assign_activity(men,women,activity):
    w_min_count = min(women, key=lambda  x: x.count).count
    w_valid = list(filter(lambda x: x.count == w_min_count and not x.done[activity], women))
    if w_valid == []:
        w_valid = list(filter(lambda x: x.count == w_min_count, women))

    woman = choice(w_valid)
    woman.count += 1
    man = valid_pair(woman,men,women,activity)
    man.count +=1
    woman.done[activity] = True
    man.done[activity] = False
    return (man,woman)

def valid_pair(woman,men,women,activity):
    valid_men = list(filter(lambda x: woman in x.partners,men))
    if valid_men == []:
        valid_men = men
    m_min_count = min(men, key=lambda  x: x.count).count
    valid_men = list(filter(lambda x: x.count == m_min_count,valid_men))
    if valid_men == []:
        valid_men = men

    valid_men = list(filter(lambda x: not x.done[activity]  ,valid_men))
    if valid_men == []:
        valid_men = men

    return choice(valid_men)

def pretty_print(result,days,activities,file):
    f = open(file,"w")
    headers = ["| {} |".format(d.center(20," ")) for d in days]
    headers = "".join(headers)
    headers = " " * 10 + "|" + headers
    print(headers)
    f.write(headers + "\n")
    for a in activities:
        row = ["| {} |".format(str(result[d][a]).center(20, " ")) for d in days]
        row = a.center(10," ") + "|" + "".join(row)
        print(row)
        f.write(row + "\n")
    f.close()




if __name__ == '__main__':

    ACTIVITIES = ["Desayuno","Aseo","Almuerzo","Cena"]
    DAYS = ["Viernes","Sábado","Domingo","Lunes","Martes"]
    result = {d:{a:(None,None) for a in ACTIVITIES} for d in DAYS}
    men = get_comuneros(1,ACTIVITIES)
    women = get_comuneros(0,ACTIVITIES)
    for d in DAYS:
        for a in ACTIVITIES:
            result[d][a] = tuple(assign_activity(men,women,a))
    pretty_print(result,DAYS,ACTIVITIES,"asignacion.txt" )

