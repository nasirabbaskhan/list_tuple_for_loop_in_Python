
    
    
    
data_base:list[tuple[str,str]]= [("qasim","123"),
                                 ("nasir","345"),
                                 ("ikhlas","567"),
                                 ("nadeem","899")]
input_name:str = input("Enter Your Name:")
input_password:str = input("Enter Your password:")
for user in data_base:
    name,possward= user # unzip or destructure
    if input_name== name and input_password==possward:
        print(f"{input_name} is Valid user")
        break    
else:
    print(f"{input_name} is invalid user")

        
