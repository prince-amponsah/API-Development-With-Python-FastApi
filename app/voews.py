def disemvowel(string_):
    vowes = "aeiou"
    string_ = input("Enter a string of text \n")
    for out in string_:
        if vowes in out:
            string_ = out.replace(vowes)
        print(string_)
    return string_


disemvowel(" kwame is from accra but livesin koforidua where he works. ")