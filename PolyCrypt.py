
# the characters being used
alphs = r'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~ '      #raw string to avoid python string formatting

#the function for calculating the shift number
def f(i,l):
    return int((905*i**-16+439*l**-16+76*i**-15+-805*l**-15+-35*i**-14+-488*l**-14+834*i**-13+-114*l**-13+-576*i**-12+657*l**-12+-628*i**-11+536*l**-11+-314*i**-10+-7*l**-10+221*i**-9+-215*l**-9+1021*i**-8+-932*l**-8+-789*i**-7+970*l**-7+865*i**-6+874*l**-6+458*i**-5+-842*l**-5+-277*i**-4+51*l**-4+-478*i**-3+739*l**-3+140*i**-2+-768*l**-2+-160*i**-1+-826*l**-1+-829*i**1+219*l**1+-338*i**2+331*l**2+-723*i**3+-640*l**3+-773*i**4+957*l**4+1023*i**5+-465*l**5+-284*i**6+-12*l**6+-983*i**7+797*l**7+450*i**8+-128*l**8+-482*i**9+426*l**9+-723*i**10+854*l**10+355*i**11+-232*l**11+577*i**12+414*l**12+-543*i**13+73*l**13+513*i**14+103*l**14+689*i**15+-499*l**15+-823*i**16+-525*l**16)%3381317950)

#the encrypt and decrypt functions follow
#both functions follow roughly the exact same process

#due to the internal functioning of the methods, the first and last characters are not encrypted by default(mathematical errors such as division by 0 and raising 0 to a negative power)
#hence, the string is temporarily modified to have empty spaces before and after the original string
#the ciphertext does not contain any empty spaces

def encrypt(inp:str):
    s = [' ']+[_ for _ in inp]+[' ']      #converting the string to a list as lists are easier to assign and modify items to
    length = len(s)

    for i in range(length):                 #a loop which runs for each character
        if s[i] not in alphs or i==0 or i==length-1:        #avoid mathematical errors and invalid characters
            continue

        char = s[i]                                                    #This is where the shift number is calculated
        shifted_char = alphs[(alphs.find(char)+f(i,length-i))%len(alphs)]            #and applied to the character list
        s[i] = shifted_char                                                
    
    cipher_text = ''
    for i in s:                                                     #The ciphertext is converted to string for returning
        cipher_text+=i                                              #After conversion, the ciphertext is returned
    return cipher_text[1:-1]


def decrypt(inp:str):
    s = [' ']+[_ for _ in inp]+[' ']      #converting the string to a list as lists are easier to assign and modify items to
    length = len(s)

    for i in range(length):                 #a loop which runs for each character
        if s[i] not in alphs or i==0 or i==length-1:        #avoid mathematical errors and invalid characters
            continue

        char = s[i]                                                    #This is where the shift number is calculated
        shifted_char = alphs[(alphs.find(char)-f(i,length-i))%len(alphs)]            #and applied to the character list
        s[i] = shifted_char                                                
    
    cipher_text = ''
    for i in s:                                                     #The ciphertext is converted to string for returning
        cipher_text+=i                                              #After conversion, the ciphertext is returned
    return cipher_text[1:-1]
