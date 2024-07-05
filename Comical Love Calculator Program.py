#lol this is just a fun program I learnt in a Python course based on some internet article.
#not to be taken seriously in any means :P
# also added a ascii art 

print('''
                        __,,,__
                ,-""-,-"       "-,-""-,
               /,-' , .-'-.7.-'-. , '-,\
               \(    /  _     _  \    )/
                '-,  { (0)   (0) }  ,-'
                 /    >  .---.  <    \
                |/ .-'   \___/   '-. \|
                {, /  ,_       _,  \ ,}
                \ {,    \     /    ,} /
                 ',\.    '---'    ./,'
             _.-""""""-._     _.-""""""-._
           .'            `._.`            '.
         _/_               _                \
      .'`   `\            | |                \
     /        |           | |                 ;
     |        /           |_|                 |
     \  ;'---'    _    ___  _  _  ___         ;
      '. ;       | |  /   \| || ||  _|     _ ;
        `-\      | |_ | | || |/ /|  _|   .' `,
           `\    |___|\___/ \__/ |___|  |     \
             \            _ _           \     |
         jgs  `\         | | |         /`   _/
    ,-""-.    .'`\       | | |       /`-,-'` .-""-,
   /      `\.'    `\     \___/     /`    './`      \
  ;  .--.   \       '\           /'       /   .--.  ;
  | (    \   |,       '\       /'        |   /    ) |
   \ ;    }             ;\   /;         `   {    ; /
    `;\   \         _.-'  \ /  `-._         /   /;`
      \ \__.'   _.-'       Y       `-._    '.__//
       '.___,.-'                       `-.,___.'
''')

print("The Love Calculator is calculating your score...")

name1 = input("What is your name? ")
name2 = input("What is their name? ")

added_name = name1 + name2
lower_name = added_name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e1 = lower_name.count("e")
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e2 = lower_name.count("e")

first_digit = t + r + u + e1
second_digit = l + o + v + e2
num_score = int(str(first_digit) + str(second_digit))

# now for calculation to be specified in the filters
if num_score < 10 or num_score > 90:
    print(f"Your score is {num_score}, damn, you go together like coke and mentos.")
elif 40 <= num_score <= 50:
    print(f"Your score is {num_score}, you are alright together lol.")
else:
    print(f"Your score is {num_score}.")
