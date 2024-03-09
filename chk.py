import pyfiglet
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
logo = pyfiglet.figlet_format('CODE_ZILLA')
print(Z+logo)

loo = pyfiglet.figlet_format('ScAM__eR')
print(F+loo)

k=("</>_</>_</>_</>_</>_</>_</>_</>_</>")
 
print(C+k)

lo=("Telegram User : @X_EG_VIP_</>_MY Channel : https://t.me/X_EG_VIP_X ")
print(X+lo)

i=("</>_</>_</>_</>_</>_</>_</>_</>_</>")
print(C+i)
o=("</>_</>_</>_</>_</>_</>_</>_</>_</></>_</>_</>_</>_</>_</>_</>_</>_</></>_</>_</>_</>_</>_</>_</>_</>_</></>_</>_</>_</>_</>_</>_</>_</>_</></>_</>_</>_</>_</>_</>_</>_</>_</></>_</>_</>_</>_</>_</>_</>_</>_</>_</>_")

print(B+o)




import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
print("</> Welcome to ᑕOᗪE_ᘔIᒪᒪᗩ worled </> ")
ch = '@SDBB_Bot'
api_id = '15372008'
api_hash = 'ed85c35370cffb1e2cf050e44e635d26'
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open("F4.txt").read().split("\n"):
    try:
        client.send_message(ch ,f"/chk {cc}")
        time.sleep(random.randint(120,115))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            t = str(mssag[0].message).split("again after ")[1]
            t = t.split("seconds")[0]
            t = int(t)
            print(f"Done Sleep : {t+2}")
            time.sleep(t+2)
        print(mssag[0].message)
        time.sleep(1)
    except:
        print(False)