# HW19 Multi-Blockchain-Wallet-in-Python

Initial set up

Running the following command: 
./derive --key=xprv9zbB6Xchu2zRkf6jSEnH9vuy7tpBuq2njDRr9efSGBXSYr1QtN8QHRur28QLQvKRqFThCxopdS1UD61a5q6jGyuJPGLDV9XfYHQto72DAE8 --cols=path,address --coin=ZEC --numderive=3 -g

We get the following result: 
![Initial Result](https://github.com/oodayeshukla/HW19_Multi-Blockchain-Wallet-in-Python/blob/main/1_Init_setup_transaction.png)


The derived keys are:
![Derived Keys](https://github.com/oodayeshukla/HW19_Multi-Blockchain-Wallet-in-Python/blob/main/2_Key_Tree.png) 

When using the send transaction for ETH I get the following error: 


runcell('send coins from one account to another', '/home/oem/Fintech_0/Crypto/Blockchain-Tools/wallet/hw19_wallet.py')
Traceback (most recent call last):

  File "/home/oem/Fintech_0/Crypto/Blockchain-Tools/wallet/hw19_wallet.py", line 138, in <module>
    res = send_tx('ETH', eth_from, eth_to, 20)

  File "/home/oem/Fintech_0/Crypto/Blockchain-Tools/wallet/hw19_wallet.py", line 112, in send_tx
    raw_tx = create_raw_tx(coin, account, recipient, amount)

  File "/home/oem/Fintech_0/Crypto/Blockchain-Tools/wallet/hw19_wallet.py", line 99, in create_raw_tx
    "chainID": w3.net.chainId(),

  File "/home/oem/apps/anaconda3/envs/eth/lib/python3.7/site-packages/web3/net.py", line 40, in chainId
    raise DeprecationWarning("This method has been deprecated in EIP 1474.")

DeprecationWarning: This method has been deprecated in EIP 1474.
  
  
