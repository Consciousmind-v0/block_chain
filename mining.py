from Hash import hash_generator
from BlockChain_update import DIFFICULTY,update
import time
import pandas as pd

df=pd.read_csv("BlockChain_data.csv")

def mine(text):
    nounce=0
    found=False
    while not found:
        text+=str(nounce)
        new_hash=hash_generator(text)
        if new_hash.startswith('0'*DIFFICULTY):
            print("Found hash at {} \nGenerated hash: {}".format(time.time(),new_hash))
            return new_hash
        nounce+=1

def get_data():
    miner_ID=input("Enter your ID: ")
    giver,taker,date_trxn,time_trxn,remark,prv_hash=df.iloc[-1].tolist()
    sep='->'
    text=giver+sep+taker+sep+date_trxn+sep+time_trxn+sep+remark+sep+prv_hash
    NEW_hash=mine(text)
    update(data=[giver,taker,date_trxn,time_trxn,remark],miner_ID=miner_ID,hash=NEW_hash)

if __name__=="__main__":
    get_data()


