# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
get_ipython().system('pip install line-bot-sdk ')


# %%
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage


# %%
file = open('info.json','r')
info = json.load(file)


# %%
info['CHANNEL_ACCESS_TOKEN']


# %%


# %%
CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN )


# %%
def main():
    USER_ID = info["USER_ID"]
    messages = TextSendMessage(text="おはよ〜　\n 朝だよ！起きてね♡")
    line_bot_api.push_message(USER_ID,messages=messages)
    
if __name__ == '__main__':   
    main()


# %%



# %%



# %%



