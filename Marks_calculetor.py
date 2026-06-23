print("\n=== MARKS CALCULATOR SHER EDITION ===")
while True:
    
    math = float(input("Marks of Maths: "))
    science = float(input("Marks of Science: "))  # spelling theek
    english = float(input("Marks of English: "))
    sst = float(input("Marks of SST: "))
    hindi = float(input("Marks of Hindi: "))

    # Sher wala Error Check 🔒
    if math < 0 or math > 100 or science < 0 or science > 100 or english < 0 or english > 100 or sst < 0 or sst > 100 or hindi < 0 or hindi > 100:
        print("Arre Sher! 0 se 100 ke beech me marks daalo! 😅 Dubara try kar")
        continue  # Wapas upar bhej dega, grade skip kar dega

    percentage = (math + science + sst + english + hindi) / 500 * 100
    print(f"\nPercentage: {percentage:.2f}% 🔥")

    # Grade wala system
    if percentage >= 90:
        grade = "A+ 👑 Topper Sher!"
    elif percentage >= 80:
        grade = "A 💪 Bahut Badhiya!"
    elif percentage >= 70:
        grade = "B 📚 Good!"
    elif percentage >= 60:
        grade = "C 😅 Pass!"
    else:
        grade = "Fail 😭 Agli Baar Pakka!"

    print(f"Grade: {grade}")
    
    chalu_rakho = input("Phir se check karna hai? haan/naa: ").lower()
    if chalu_rakho == "naa":
        print("Dhanyavaad Sher! Program band ho gaya 💪") 
        break
