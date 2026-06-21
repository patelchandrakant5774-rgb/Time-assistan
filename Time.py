# Project: Time Assistant
# Banaya: Chandrakant Patel - Class 9
##Kaam: Time ke hisaab se kaam batata hai
print("yeh tumhe sam
ke 5 se 11 baje tak batayega ki tumhe kis time pe kya karna chahiye")

while True:  # loop yahin se shuru
    time = float(input("time:"))
    if time == 5:
        print("bhai meko pata he teko cricket pasand he to thoda khel ke aja")
    elif time == 6:
        print("bas- bas bahut khel liya ghar ja bhai")
    elif time == 7:
        print("ab thoda padh bhi le ")
    elif time == 8:
        print("ab vo chij kar le jo tum kabhi bhul nahi sakte khana kha le")
    elif time == 9:
        print("ab thoda mummy papa ke sath Beth kar unake sath bat bhi ka le")
    elif time == 10:
        print("ab Tu free he tujhe jo karna he kar")
    elif time == 11:
        print("bhai mujhe pata he Tu kya kar rah tha ab thoda mobile ko rakh de so ja ")
    else:
        print("yah 5 se 11 tak ka time nahi he")

    aage = input("aage or karna he kya yes/no :")  # yahan 'aage' 
    if aage == "no":
        print("thik he phir by ")
        break  # loop tod dega
    # "yes" likhega to loop apne aap wapas chala jayega
