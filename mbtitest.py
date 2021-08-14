from telethon.sync import TelegramClient
from telethon import events,functions, types
from telethon.tl.custom import Button
from usersDB import UsersDatabase
from Analyser import Analyser
from TestQuesions import TestQuestions

# put your api_id & api_hash here:
# api_hash = ''
# api_id =
# put your bot_token here:
# bot_token = ''

usersDatabase = UsersDatabase()
usersDatabase.create()
analyser = Analyser()
testquesions = TestQuestions()
bot = TelegramClient('mbtiSession',api_id,api_hash).start(bot_token=bot_token)

def keyboardChanger(n):
    keyboard00 = [
        Button.inline('گزینه 1','{}.1'.format(n),),
        Button.inline('گزینه 2','{}.2'.format(n),),              
    ]
    return keyboard00

@bot.on(events.NewMessage(pattern='/start'))
async def starting(event):
    list2 = []
    user_in_the_channel2 = False
    senderId2 = await event.get_input_sender()
    keyboardMain = [
            [
                Button.inline("آغاز/ادامه آزمون", "s1"),
            ],
            [
                Button.inline("انصراف", "s0"),
            ]
    ]
    async for user2 in bot.iter_participants('etelaatomoomi7'):    
        list2.append(user2.id)

    for i in range(len(list2)):
        if list2[i] == senderId2.user_id:
            user_in_the_channel2 = True
            break
    if user_in_the_channel2 == True:
        await bot.send_message(senderId2.user_id, 'آیا می خواهید آزمون خود را آغاز کنید/ادامه دهید؟',buttons = keyboardMain)
        
    else:
     await event.reply("دوست من سلام👋 \nبرای اینکه ما بتونیم خدمات ربات رو روز به روز بهتر بکنیم و ربات بصورت کاملا رایگان قابل استفاده باشه لطفا عضو کانال زیر باشید🤩\n همچنین با عضویت در کانالمون به ما انگیزه ی زیادی میدین❤️\nt.me/etelaatomoomi7")
@bot.on(events.NewMessage(pattern='/analyse'))
async def analyseAnswer(event):
    list = []
    user_in_the_channel = False
    senderId3 = await event.get_input_sender()
    
    
    async for user in bot.iter_participants('etelaatomoomi7'):    
        list.append(user.id)

    for i in range(len(list)):
        if list[i] == senderId3.user_id:
            user_in_the_channel = True
            break
        
    if user_in_the_channel == True:
        await bot.send_message(senderId3.user_id, 'لطفا برای تحلیل، تیپ شخصیتی خود را انتخاب کنید',buttons = analyser.keyboard)
        
    else:
        await event.reply("دوست من سلام👋 \nبرای اینکه ما بتونیم خدمات ربات رو روز به روز بهتر بکنیم و ربات بصورت کاملا رایگان قابل استفاده باشه لطفا عضو کانال زیر باشید🤩\n همچنین با عضویت در کانالمون به ما انگیزه ی زیادی میدین❤️\nt.me/etelaatomoomi7")

@bot.on(events.CallbackQuery)
async def callback(event):
    senderId2 = await event.get_input_sender()
    #Keyboard Manager for Analyse
    if event.data.decode('ascii') in analyser.getAllKeys(analyser.analysesList):
        await event.delete()
        await bot.forward_messages(senderId2.user_id,analyser.analysesList[event.data.decode('ascii')]['id'],'bottttttest')
        nextId = analyser.analysesList[event.data.decode('ascii')]['id'] + 1
        await bot.forward_messages(senderId2.user_id,nextId,'bottttttest')
    #Keyboard Manager for Start the Test
    elif event.data.decode('ascii') == 's1':
        await event.delete()
        userison = usersDatabase.checkUser(senderId2.user_id)
        if userison == 1:
            userLevel = usersDatabase.levelById(senderId2.user_id)
            await bot.send_message(senderId2.user_id,
            'سوال {} \n گزینه1. {} \n گزینه2. {}'.format(userLevel, testquesions.mydict['{}.1'.format(userLevel)]['text'], testquesions.mydict['{}.2'.format(userLevel)]['text'])
            ,buttons=keyboardChanger('{}'.format(userLevel)))
        else:
            usersDatabase.insert(0,0,0,0,0,0,0,0,1,senderId2.user_id)
            await bot.send_message(senderId2.user_id,
            'سوال {} \n گزینه1. {} \n گزینه2. {}'.format(1, testquesions.mydict['{}.1'.format(1)]['text'], testquesions.mydict['{}.2'.format(1)]['text'])
            ,buttons=keyboardChanger('{}'.format(1)))
    #Keyboard Manager for Canceling the Test before Start
    elif event.data.decode('ascii') == 's0':
        await event.delete()
        await bot.send_message(senderId2.user_id ,"شما آزمون را لغو کردید")
    #Keyboard Manager for Answering Questions
    elif event.data.decode('ascii') in testquesions.getAllQuestionKeys(TestQuestions.mydict) and int(event.data.decode('ascii').split('.')[0]) != 60:
        await event.delete()
        if int(event.data.decode('ascii').split('.')[0])>9:
            questionNumber = int(event.data.decode('ascii')[:2])
        else:
            questionNumber = int(event.data.decode('ascii')[:1])
        usersDatabase.increaseLevel(senderId2.user_id,questionNumber+1)
        await bot.send_message(senderId2.user_id,
        'سوال {} \n گزینه1. {} \n گزینه2. {}'.format(questionNumber+1, testquesions.mydict['{}.1'.format(questionNumber+1)]['text'], testquesions.mydict['{}.2'.format(questionNumber+1)]['text'])
        ,buttons=keyboardChanger('{}'.format(questionNumber+1)))
        theScore = testquesions.mydict['{}.1'.format(questionNumber)]['score']
        if theScore == 'i' or theScore == 'e':           
            if event.data.decode('ascii')[2:] == '1':
                currentScore = usersDatabase.readScoreI(senderId2.user_id,)
                newScore = currentScore + 1
                usersDatabase.increaseI(senderId2.user_id,newScore)
            else:
                currentScore = usersDatabase.readScoreE(senderId2.user_id,)
                newScore = currentScore + 1
                usersDatabase.increaseE(senderId2.user_id,newScore)
        if theScore == 's' or theScore == 'n':           
            if event.data.decode('ascii')[2:] == '1':
                currentScore = usersDatabase.readScoreS(senderId2.user_id,)
                newScore = currentScore + 1
                usersDatabase.increaseS(senderId2.user_id,newScore)
            else:
                currentScore = usersDatabase.readScoreN(senderId2.user_id,)
                newScore = currentScore + 1
                usersDatabase.increaseN(senderId2.user_id,newScore)
        if theScore == 't' or theScore == 'f':           
            if event.data.decode('ascii')[2:] == '1':
                currentScore = usersDatabase.readScoreT(senderId2.user_id,)
                newScore = currentScore + 1
                usersDatabase.increaseT(senderId2.user_id,newScore)
            else:
                currentScore = usersDatabase.readScoreF(senderId2.user_id,)
                newScore = currentScore + 1
                usersDatabase.increaseF(senderId2.user_id,newScore)
        if theScore == 'p' or theScore == 'j':        
            if event.data.decode('ascii')[2:] == '1':
                currentScore = usersDatabase.readScoreP(senderId2.user_id,)
                newScore = currentScore + 1
                usersDatabase.increaseP(senderId2.user_id,newScore)
            else:
                currentScore = usersDatabase.readScoreJ(senderId2.user_id,)
                newScore = currentScore + 1
                usersDatabase.increaseJ(senderId2.user_id,newScore)
    elif event.data.decode('ascii') == '60.1':
        await event.delete()
        currentScore = usersDatabase.readScoreP(senderId2.user_id,)
        newScore = currentScore + 1
        usersDatabase.increaseP(senderId2.user_id,newScore)
        await bot.send_message(senderId2.user_id,'آزمون شما با موفقیت به پایان رسید')
        iS = usersDatabase.readScoreI(senderId2.user_id)
        eS = usersDatabase.readScoreE(senderId2.user_id)
        sS = usersDatabase.readScoreS(senderId2.user_id)
        nS = usersDatabase.readScoreN(senderId2.user_id)
        tS = usersDatabase.readScoreT(senderId2.user_id)
        fS = usersDatabase.readScoreF(senderId2.user_id)
        pS = usersDatabase.readScoreP(senderId2.user_id)
        jP = usersDatabase.readScoreJ(senderId2.user_id)
        usersDatabase.increaseLevel(senderId2.user_id,61)
        await bot.send_message(senderId2.user_id, 'شما در گروه شخصیتی {} قرار دارید'.format(finalType(
            iS,eS,sS,nS,tS,fS,pS,jP
        )))
        await analyseAnswer(event)
    elif event.data.decode('ascii') == '60.2':
        await event.delete()
        currentScore = usersDatabase.readScoreJ(senderId2.user_id,)
        newScore = currentScore + 1
        usersDatabase.increaseJ(senderId2.user_id,newScore)
        await bot.send_message(senderId2.user_id,'آزمون شما با موفقیت به پایان رسید')
        iS = usersDatabase.readScoreI(senderId2.user_id)
        eS = usersDatabase.readScoreE(senderId2.user_id)
        sS = usersDatabase.readScoreS(senderId2.user_id)
        nS = usersDatabase.readScoreN(senderId2.user_id)
        tS = usersDatabase.readScoreT(senderId2.user_id)
        fS = usersDatabase.readScoreF(senderId2.user_id)
        pS = usersDatabase.readScoreP(senderId2.user_id)
        jP = usersDatabase.readScoreJ(senderId2.user_id)
        usersDatabase.increaseLevel(senderId2.user_id,61)
        await bot.send_message(senderId2.user_id, 'شما در گروه شخصیتی {} قرار دارید'.format(finalType(
            iS,eS,sS,nS,tS,fS,pS,jP
        )))
        await analyseAnswer(event)

def finalType(i,e,s,n,t,f,p,j):
    finalTypeStr = ''
    if(i>e):
        finalTypeStr+='i'
    else:
        finalTypeStr+='e'
    
    if(s>n):
        finalTypeStr+='s'
    else:
        finalTypeStr+='n'
    
    if(t>f):
        finalTypeStr+='t'
    else:
        finalTypeStr+='f'
    
    if(p>j):
        finalTypeStr+='p'
    else:
        finalTypeStr+='j'
    return finalTypeStr

bot.start()
bot.run_until_disconnected()