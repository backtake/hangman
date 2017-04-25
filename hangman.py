import random
du[p
import time

capitol = ['AMSTERDAM',
'BERLIN',
'BUDAPEST',
'LONDON',
'MADRID',
'MOSCOW',
'OSLO',
'PARIS',
'ROME',
'WARSAW',
'VIENNA',
'HELSINKI',
'RIGA',
'LUXEMBURG',
'LISBON',
'BUKAREST',
'KYIV',
'VADUZ']

highscore = []

file = open('highscores.txt', "r+")
def new_game():

    start=time.time()
    stolica = random.choice(capitol).lower()
    #print(stolica)
    guess = None
    guessed_letters = []
    hp = 5
    word_guessed=[]
    for letter in stolica:
        word_guessed.append('_')
    print("><"*40,"\nWelcome in HANGMAN GAME!\nYou have to guess a capitol I am thinking of!\n",
    "\bTry yourself! Good luck!\n")

def game():
    joined_word = " ".join(word_guessed)
    print(joined_word)
    print('\nHP you have left: ', hp)
    guess = input('Wiec slucham: ').lower()
    if not guess.isalpha(): # check the input is a letter. Also checks an input has been made.
        print("That is not a letter. Please try again.")
        continue
    elif guess in guessed_letters: # check it letter hasn't been guessed already
        print("You have already guessed that letter. Please try again.")
        continue
    elif (len(guess) > 1 and len(guess) < len(stolica)): # check the input is only one letter
            print("That is more than one letter. Please try again.")
            continue
    if guess == stolica:
        print('Cool. You have won!')
        print('Congrats! The', stolica,'was the word!' )
        end=time.time()
        print('Time: ', int(end-start),'s')
        highscore.append(int(end-start))
        a = 0


    if guess in stolica:
        print(' ')
        guessed_letters.append(guess)
        print(guessed_letters)
        for letter in range(len(stolica)):
            if guess == stolica[letter]:
                word_guessed[letter] = guess
            if guess not in stolica:
                hp -= 1


    else:
        if len(guess) >= len(stolica) and hp > 1:
            print('Bardzo Źle!Tracisz 2 punkty życia!')
            guessed_letters.append(guess)
            print(guessed_letters)
            hp -= 2
        else:
            print('źle')
            guessed_letters.append(guess)
            print(guessed_letters)
            hp = hp - 1

    elif hp <= 0:
        print('Ilosc szans wykorzystana!')
        print('Szukana stolica jest: ', stolica)
        pytanie = input('Wanna play again? Y/N ')
        pytanie = pytanie.upper()
    if (pytanie == 'N'):
        i=i-1
        b=b-1
        break
    elif pytanie == 'Y':
        i=i-1
        hp = 5
        continue
if '_' not in word_guessed:
    print('Congrats! The', stolica,'was the word!' )
        a=a-1
    end=time.time()
    print('Time: ', int(end-start),'s')
    highscore.append(int(end-start))
if a == 0:
    pytanie = input('Wanna play again? Y/N ')
    pytanie = pytanie.upper()
    if (pytanie == 'N'):
        i=i-1
        b=b-1
        break
    elif pytanie == 'Y':
        i = i-1
        a=1
        hp = 5


print('Thanks for the game!')
file.write(str(highscore))
file.close()

def main():
    while True:
        new_game()

if __name__ == '__main__':
    main()
