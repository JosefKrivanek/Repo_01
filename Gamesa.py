

choice = 0


input("Spoopy game \nPress Enter to continue\n ")

input("\033[91m. . .\nYou’re walking down the street as you notice someone else’s footsteps behind you.\n \033[0m")
input("You turn around, a figure in a black hoodie passes by you. You recognize the hoodie.\nIt’s the same person you have been strangely noticing near you for the past few weeks.\n ")
input("You don’t want to accuse anyone of anything but it is rather creepy.\n ")
input("You get home and try to open the door only to find out it’s unlocked. Did you forget to lock it?\n ")
input("You step in and turn on the light.")
print(".")
input("Nothing unusual or out of order. But you swear you locked the door when you left.\n ")
input("There’s an unsettling feeling, but you’re not sure if you should stay.")
print(".")

choice=int(input("0 - I should call someone\n1 - Stay \n "))
if choice == 0:
    choice = int(input("Who are you going to call?\n0 - Best friend\n1 - Your sister\n "))
    if choice == 0:
        input("You call your friend and ask if you can come over, they agree and you get on your way.\nYou walk through the dark as you notice familiar footsteps once again.\n  ")
        input("As you reach your friends building, you finally find to courage to turn around, only to find an empty street.\n ")
        input("Weird. Are you going insane?\n ")
        input("You spend the night at your friends house and tell them about your weird encounters with this mysterious figure.\n ")
        choice =int(input("Your friend seems worried, maybe you should go to the police station?\n0 - Yes\n1 - No\n "))
        if choice == 0:
           input("You agree to stop by the police station in the morning. \n ")
           input("When morning comes, you sit in the office as they tell you that unless an attack or harassment happens, there’s nothing they can do.\nRidiculous.\n ")
        elif choice == 1:
           input("Your probably just paranoid, going to the police station will make you look even more crazy.\n ")
           input("You go to sleep and try to forget about it. The morning comes and you have stuff to do so you head back\n ")
           choice = 0
    elif choice == 1:
        input("You call your sister and ask if you can come over, she agrees and you get on your way.\n ")
        input("You keep thinking about the weird person you keep seeing. \nYou feel unsafe.\n ")
        input("You spend the night at your sisters house and tell her about your weird encounters with this mysterious figure.\n ")
        input("She tells you that you’re probably just paranoid, \nI mean, how many people own a black hoodie? \nEveryone.\n ")
        input("Maybe she’s right?\n ")
        input("However, she tells you that if you ever see them again, to call her right away.\n ")
    input("You walk home. You enter your house, you’re not scared much anymore. \nEverything is less scary in daylight. \nDid you really just forget to lock the door and overreacted?\n ")
    input("It’s evening when everything starts making you paranoid again. \nYou walk home from work and every sound makes you turn around abruptly. \nYou get closer to your street when you see it. When you see him.\n ")
    input("Waiting by your home entrance, the person that has been following you for weeks. You change your mind about going home very quickly.\n ")
    input("Taking advantage of the fact that he hasn’t noticed you yet, you run in the opposite direction. \nYou’re going straight to your friends house, might as well move in there at this point. \nYou ring the doorbell on room 504 and step inside as soon as the door opens.\n ")
    input("Your friend seems rather surprised, so you tell them about another chilling situation. \nThey seems to have mixed feelings, they’re worried but what if it was just a random person.\n ")
    input("You get the feeling that they think you’re just making this up.\n ")
    input("They let you stay the night anyways and you calm down. \nSuddenly, you get a text from your sister asking if you got home safely. \nShe’s worried since you’ve been acting strange lately.\nYou text her back, saying you’re okay and will sleep over at your friends house.\n ")
    input("You and your friend ordered pizza for dinner and decide to do a movie night. \nUnfortunately, there’s no popcorn. Your friend suggests going to the nearby store to get some.\n ")
    input("You don’t like this idea, you don’t want to go outside. \nYour friend decides to go alone and promises to be back in a few minuets. \nThey tell you to call them if anything happens and they will come back immediately.\n ")
    input("You’re left alone for a while. At least you’re safe, right?\n ")
    input("The doorbell rings, apparently, the pizza you ordered is here. \nSeriously?? Right now?? \nBut picking it up is the least you could do.\n ")
    input("It’s just a short elevator ride and a few steps, you can do that. \nYou walk in front of the building and look around, it’s dark. \nWhere’s the delivery guy…?\n ")
    input("Oh, you see him. Why did he have to park so far away? you walk towards the car and he hands you your dinner. \nYou start heading back to the building when you notice that guy again, behind the building corner\n ")
    input("Your heart speeds up, did he follow you the entire day? How did he know you’re here?\n ")
    input("You pretend not to see him and fasten your pace. He follows right behind. \nYou panic, you drop the pizza box and start running.\n ")
    input("You run into the huge apartment complex and start making your way up.\n ")
    input("He’s following your every step, not caring if someone sees him or not. \nYou take the stairs but he seems to keep getting closer.\n ")
    choice = int(input("0 - Defend yourself \n1 - RUN FASTER \n "))
    if choice == 0:
        input("You know you can’t outrun him, so you turn around and kick him with all your strength.\n ")
        input("He falls down giving you more time to spare. \nAs you enter the 5th floor, it seems like you’re out of his sight even though you still hear his steps behind you.\n ")
        input("You struggle to unlock the door, breaking the key in half. \nYou succeed, leaving half of the key in the keyhole and slam the door behind you.\n ")
        input(" You can’t lock the door anymore but there is 10 apartments on this floor. Is he going to try to open every single one of them?\n ")
        input("As long as he doesn’t know where you are, you should be fine, right? \nJust in case though, you crouch behind the kitchen cabinet and pull out your phone.\n ")
        choice = int(input("0 - Call your sister \n1 - call your friend \n2 - call the police\n "))
        if choice == 0:
            input("You call your sister right away.\n ")
            input(" She picks up immediately and you panic, telling her you’re hiding away behind your friends kitchen cabinet and need help.\n ")
            input("Your sister sounds rather calm, she says she’ll be right there. \nShe asks where EXACTLY you are.\n ")
            choice = int(input("\'I’m in a room with nuber:\n0 - 503\n1 - 504\n2 - 505\n "))
            if choice == 0:
                input("Room 503.\n ")
                input("Your sister hangs up. You’re confused but hope she’ll come any minute. \nYou wait for a few minutes in silence.\n ")
                input("Nothing is happening. Where is… anyone, actually? \n ")
                input("The realization hits you now. You’re not in room 505, you gave her the wrong number. \nYou call your sister again but with no luck. \n ")
                input("The door flys open and you freeze. You stop breathing and feel like your world is falling apart. \nYou’re preparing for the worst, but in the door stands… your friend?\n ")
                input("They rush over to you, worried. They say how glad they are that you’re okay. \nPolice officers step into the room next and you’re more confused than ever.\n ")
                input("Your friend starts to explain. They saw your sister at the store. \nYou called your sister and told her where you are, she immediately hang up and called someone else, \ntelling them which room you’re in and to go get you.\n ")
                input("Your friend overheard the whole conversation and That’s when they realized your own sister was in on it the whole time and called the police. \nThey say they’re glad you told your sister the wrong room number which gave them enough time to get help. \n ")
                input("You’re horrified, how could your own sister try to kill you?\n ")
                input("Both your sister and the stalker get charged for their crimes. It makes you sick. \nYou’ll never trust anyone ever again.\n ")
            elif choice == 1:
                input("Room 504.\n ")
                input("Your sister hangs up and leaves you scared waiting. \nJust a minute passes by and the stalker bolts through the door.\n ")
                input("He doesn’t even look around, aiming straight for your hiding spot. \nIt’s like he knows exactly where to go…\n ")
                input("He pushes the cabinet to the side and you’re met with his cold hands as he strangles you.\n ")
                input("You feel dizzy and faint.\n ")
                input("Before you pass out, you recognize your sisters voice coming from a call on his phone.\n ")
                input("It’s the last thing you hear before your life cuts short.\n ")
            elif choice == 2:
                input("Room 505.\n ")
                input("Your sister hangs up. You’re confused but hope she’ll come any minute. \nYou wait for a few minutes in silence.\n ")
                input("Nothing is happening. Where is… anyone, actually? \n ")
                input("The realization hits you now. You’re not in room 505, you gave her the wrong number. \nYou call your sister again but with no luck. \n ")
                input("The door flys open and you freeze. You stop breathing and feel like your world is falling apart. \nYou’re preparing for the worst, but in the door stands… your friend?\n ")
                input("They rush over to you, worried. They say how glad they are that you’re okay. \nPolice officers step into the room next and you’re more confused than ever.\n ")
                input("Your friend starts to explain. They saw your sister at the store. \nYou called your sister and told her where you are, she immediately hang up and called someone else, \ntelling them which room you’re in and to go get you.\n ")
                input("Your friend overheard the whole conversation and That’s when they realized your own sister was in on it the whole time and called the police. \nThey say they’re glad you told your sister the wrong room number which gave them enough time to get help. \n ")
                input("You’re horrified, how could your own sister try to kill you?\n ")
                input("Both your sister and the stalker get charged for their crimes. It makes you sick. \nYou’ll never trust anyone ever again.\n ")
        elif choice == 1:
            input("You call your friend and they immediately pick up. \nThey don’t ask any questions and say they’ll be there in a second.\n ")
            input("Your friend rushes over to you. \nIf he didn’t know before, he definitely knows where you are now, since he probably saw your friend enter the apartment.\n ")
            input(" Your friend picks up the phone and calls for help while you block the door with anything useful you can find.\n ")
            input("Silence fills the room as you hear footsteps outside the door. \nThe door handle pushes down slowly, banging on the door follows shortly after. \nYou and your friend panic, praying that help will come any second.\n ")
            input("You keep pushing furniture onto the door keeping it shut. \nYou hear sirens in the distance and the banging stops.\n ")
            input("The police arrives and investigation starts. \nYou escaped death just barely and know that you’re not safe since the stalker ran away before he got caught. \nWho knows when will this repeat. \n ")
        elif choice == 2:
            input("You dial the number and wait in silence. The line puts you on hold. \nYour blood runs cold as you dial the number again and again and again.\n ")
            input("How can be an emergency line unavailable?? \nSomebody finally picks up on the 5th try and you start slurring words together.\n ")
            input("They tell you to calm down and tell them what happened. You whisper the address and tell them to come. \nApparently they can’t hear you, you need to speak up.\n ")
            input("You gather all your strength and start speaking clearly.\n ")
            input("You shouldn’t have.\n ")
            input("He heard you...\n ")
            input("The door flys open and you’re met with the person you barely escaped a few seconds ago. \nYou can’t do anything anymore.\n ")
            input("This is how it ends.\n ")
            input("Your dead body appears on the news the next day.\n ")
    elif choice == 1:
        input("You try to run faster but trip over your own feet.\n ")
        input("You land harshly on the ground and scream for the last time before he steps on your neck \nmaking you suffer a painful death on the poorly lit up stairs.\n ")
elif choice == 1:
    input("Whatever, it’s too late to go somewhere else.\n ")
    input("You just have too many things on your mind and forgot to lock the door.\n ")
    input("You get ready for bed and lay down. You’re about to fall asleep when you hear the door click.\n ")
    input("Shivers go down your spine, you get up and slowly open your bedroom door to investigate.\n ")
    input("You don’t see anything weird. You turn on the light and walk into the kitchen.\n ")
    input("You look around and see nothing. Are you hallucinating right now? Is this just a dream?\n ")
    input("You start to walk back to your bedroom when your head is suddenly met with a strong force and your body hits the ground.\n ")
    input("You can feel blood gushing out of your head as you hear footsteps walking towards you.\n ")
    input("Everything turns black and you never meet the light of tomorrow.\n \n \n ")
    print("Death speedrun")






