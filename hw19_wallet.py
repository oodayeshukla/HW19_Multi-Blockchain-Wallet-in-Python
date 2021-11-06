#
#
# load in all the imports 

import subprocess
import json
from dotenv import load_dotenv
import os
from bit import wif_to_key
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from bit import PrivateKeyTestnet


os.chdir("/home/oem/Fintech_0/Crypto/Blockchain-Tools/wallet")

### load in the constants file
from constants import *

depth = 3
#%%
# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic1")

#%%  From class code --> https://upenn.bootcampcontent.com/upenn-bootcamp/upenn-phi-virt-fin-pt-05-2021-u-c/-/blob/master/01-Lesson-Plans/19-Blockchain-Python/1/Activities/04-Ins_Importing_Keystore/Solved/main.py
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

 #%%
 
# Create a function called `derive_wallets`
## need to escape the quotes to pass the mnemonic 
def derive_wallets(mnemonic, coin, derive_depth):
    command = f'./derive -g --mnemonic=\'{mnemonic}\' --coin={coin} --numderive={derive_depth} --format=json'
    
    ## print(command)

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

#%%
# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {
    BTC: derive_wallets(mnemonic, BTC, depth),
    ETH: derive_wallets(mnemonic, ETH, depth)
    }

print("Bitcoin Keys")
print(coins[BTC][0]['privkey'])
print(coins[BTC][1]['privkey'])
## KxDJua9xJWkQaAPGGAvWdU6KFVcy3UN4tgn9WWzTgPTAxrT1JPoC
## KxDJua9xJWkQaAPGGAvWdU6KFVcy3UN4tgn9WWzTgPTAxrT1JPoC
## KxxX2RTc4acNpAyWhmmz3nepjXbJ9AK2S6cAXqYboL8bFy6NN2v1

#%%
# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
## https://web3js.readthedocs.io/en/v1.2.0/web3-eth-accounts.html#privatekeytoaccount
## https://ofek.dev/bit/dev/api.html

def priv_key_to_account(coin, priv_key):
    if coin=='ETH':
        ## process ETH coin
        return Account.privateKeyToAccount(priv_key)
        
    if coin=='BTC':
        ## process BTC coin 
        return PrivateKeyTestnet(priv_key)
        

#%%
# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_raw_tx(coin, account, recipient, amount):
   ## coin -- the coin type (defined in constants.py).
   ## account -- the account object from priv_key_to_account.
   ## to -- the recipient address.
   ## amount -- the amount of the coin to send.
   ## https://medium.com/moonbeam-network/using-the-ethereum-web3-library-to-send-transactions-in-moonbeam-5b8593767904
   
    if coin=='ETH':   ## check the coin 
        ## return an object containing to, from, value, gas, gasPrice, nonce, and chainID.
        ## process ETH coin
        
        value = w3.toWei(amount, "ether")
        
        gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": value})

        return {
            "from": account.address,
            "to": to,
            "value": value,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
            "chainID": w3.net.chainId(),
            }

        
    if coin=='BTC': ## check the coin 
        ## process BTC coin 
        return PrivateKeyTestnet(priv_key)
        

#%%
# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, recipient, amount):
    if coin == 'ETH':   ### check the coin 
        raw_tx = create_raw_tx(coin, account, recipient, amount)
        signed = account.signTransaction(raw_tx)        ### sign the transaction 
        result = w3.eth.sendRawTransaction(signed.rawTransaction)
        return result.hex()
    
    if coin == 'BTC':  ### check the coin 
        raw_tx = create_raw_tx(coin, account, recipient, amount)
        signed = account.sign_transaction(raw_tx)       ### sign the transaction 
        return NetworkAPI.broadcast_tx_testnet(signed)

#%% get the account from the private key

kk = priv_key_to_account('BTC',"KxDJua9xJWkQaAPGGAvWdU6KFVcy3UN4tgn9WWzTgPTAxrT1JPoC")
kk1 = priv_key_to_account('BTC',"cTvq1is2fozhRHZqF89QxMhehADnKLHoPTDPeJnXwVKuP92swUo2")

eth_to = priv_key_to_account('ETH',"693646d7964e9a34525ab65ef8b6a5eb48979724fdcd14eb103be6ea332e8ffb")
eth_from =priv_key_to_account('ETH',"20c5853aac6dab19364ad30c7656513dbfe0755011d3c65a835160db312bf2c0")

#%% print addresses 

print("From -- ", eth_from.address)
print("To -- ", eth_to.address)


#%% send coins from one account to another 

res = send_tx('ETH', eth_from, eth_to, "20")

#%% test 
key = wif_to_key("KxxX2RTc4acNpAyWhmmz3nepjXbJ9AK2S6cAXqYboL8bFy6NN2v1")

print(key.get_balance())

print(key.get_transactions())

print(key.get_unspents())
      
print(key.get_transactions())


















