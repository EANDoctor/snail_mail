email = input("Your email address: ")

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

    ok_message = "Valid email address :)"
    is_valid = True