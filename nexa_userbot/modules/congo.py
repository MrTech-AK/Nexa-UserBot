import random 
from nexa_userbot.core.main_cmd import nexaub_on_cmd, e_or_r

RUNSREACTS = [ "Congratulations and BRAVO!", 
"You did it! So proud of you!", 
"This calls for celebrating! Congratulations",
"I knew it was only a matter of time. Well done!", 
"Congratulations on your well-deserved success.", 
"Heartfelt congratulations to you.", 
"Warmest congratulations on your achievement.", 
"Congratulations and best wishes for your next adventure!”", 
"So pleased to see you accomplishing great things.", 
"Feeling so much joy for you today. What an impressive achievement!",] 
@nexaub_on_cmd(command="congo")
async def _(event): 
if event.fwd_from: return bro = random.randint(0, len(RUNSREACTS) - 1) 
reply_text = RUNSREACTS[bro] 
await event.edit(reply_text)