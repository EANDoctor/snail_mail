# "hello.worldcom"    => An email address has to contain a '@' character!
# "he@llo@world.com"  => An email address cannot contain more than one '@' characters!
# "@world.com"        => The username before the '@' character cannot be empty!
# "hello@"            => The domain after the '@' character cannot be empty!
# "hello@worldcom"    => An email address has to contain at least one '.' character!
# "hell.o@worldcom"   => The domain has to contain at least one '.' character!
# "he.llo@worldcom."  => The top-level domain cannot be empty!
# "he.llo@worldco.m"  => The top-level domain has to be at least two characters long!
# ".hello@world.com"  => The username cannot start with a '.' character!
# "he.llo@.world.com" => The domain cannot start with a '.' character!
# "hello@world.com"   => Valid email address :)

def validate_email(email: str):
	
    length_of_email = len(email)
    number_of_at_characters = email.count("@") #számolja a "@" mennyiségét.
    number_of_dot_characters = email.count(".") #számolja a "." menyiségét. 
    position_of_at = email.find("@") #megkeresi a "@" helyét a címben.

    position_of_first_dot = email.find(".") #megkeresi a "." karaktert a címben.
    position_of_last_dot = email.rfind(".") #megkeresi az utolsó "." karaktert a címben.
    position_of_first_dot_after_the_at = -1 #kezdeti értéke -1 az első "." karakternek a "@" karakter után.
    if position_of_at != -1: #ha van "@" karakter, akkor:
      position_of_first_dot_after_the_at = email.find(".", position_of_at) #megkeresi az első "." karaktert a "@" karakter után.
		
    error_message_no_at = "An email address has to contain a '@' character!"
    error_message_too_many_at = "An email address cannot contain more than one '@' characters!"
    error_message_no_dot = "An email address has to contain at least one '.' character!"
    error_message_no_username = "The username before the '@' character cannot be empty!"
    error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!"
    error_message_no_server_name = "The domain cannot start with a '.' character!"
    error_message_no_tld = "The top-level domain cannot be empty!"
    error_message_short_tld = "The top-level domain has to be at least two characters long!"
    error_message_no_domain = "The domain after the '@' character cannot be empty!"
    error_message_invalid_username = "The username cannot start with a '.' character!"

    ok_message = "Valid email address :D"

	#1 Minimum egy "@" karakter kell legyen az email címben.
    if number_of_at_characters == 0:
      print(error_message_no_at)
      return

    #2 csak egy "@" karakter lehet az email címben.
    if number_of_at_characters > 1:
      print(error_message_too_many_at)
      return
    
    #3 felhasználónév nem lehet üres.
    if position_of_at == 0:
      print(error_message_no_username)
      return

    #4 a domain nem lehet üres.
    if position_of_at == length_of_email - 1:
      print(error_message_no_domain)
      return

    #5 Minimum egy "." karakter kell hogy legyen az email címben.
    if number_of_dot_characters == 0:
      print(error_message_no_dot)
      return

    #6 a domainban kell hogy legyen legalább egy "." karakter a "@" karakter után.
    if position_of_first_dot_after_the_at == -1:
      print(error_message_no_dot_in_domain)
      return

    #7 A "top level domain" nem lehet üres (PL nem lehet "random@gmail.)
    if position_of_last_dot == length_of_email - 1:
      print(error_message_no_tld)
      return

    #8 A "top level domain" legalább 2 karakternek kell lennie.(pl: .hu)
    tld_length = length_of_email - position_of_last_dot - 1
    if tld_length < 2:
      print(error_message_short_tld)
      return

    #9 Érvényes felhasználónév. Az első karakter nem lehet "."
    if email[0] == ".":
      print(error_message_invalid_username)
      return

    #10 Érvényes domain név. A "@" karakter után az első karakter nem lehet "."
    if email[position_of_at + 1] == ".":
      print(error_message_no_server_name)
      return

    # Ha minden szabályos akkor kiírhatja az e-mail címet.
    print(ok_message)


#ezt kivülről vettük szóval nem igazán tudom elmagyarázni.
if __name__ == "__main__":
	email = input("Your email address: ")
	validate_email(email)

#Lényegében az "input" lekerült a kód végére a "validate_email" felé közvetlenül.
#Így a felhasználó be tudja írni az email címét és aztán a program csak ellenőrzi. 