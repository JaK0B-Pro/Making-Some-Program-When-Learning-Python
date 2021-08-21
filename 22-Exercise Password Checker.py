# 22-Exercise Password Cheaker:

usern = input('Username: ')

passw = input('Password: ')

cryptpassw = len(passw) * '*'

# Turn the password to a secret

print(f'{usern}, your password {cryptpassw} is {len(passw)} letters long ')