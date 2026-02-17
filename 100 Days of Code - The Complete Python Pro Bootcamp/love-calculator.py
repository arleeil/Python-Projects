# name1= 'LEE'
# name2= 'CHRISTOPER'

def calculate_love_score(user_1,user_2):
    couple_name= user_1.upper() + user_2.upper()
    list(couple_name)

    print(couple_name)
    true=['T', 'R','U', 'E' ]
    love = ['L', 'O', 'v', 'E']
    true_num=0
    love_num=0

    for i in true:
        for x in couple_name:
            if i  in  x:
                true_num+=1

    for i in love:
        for x in couple_name:
             if i in x:
                 love_num+=1

    print(str(true_num)+str(love_num))



calculate_love_score('KANYE WEST', 'KIM KARDASHIAN')


