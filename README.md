# Operate flow

## ENV
- python >= 3.6

### Clone the Project
```angular2html
1. git clone git@github.com:andrewchang0910/BackpackAutoTrade.git
```

### Install the requires
```angular2html
2. pip install -r requirement.txt
```

### Copy the env file
```angular2html
3. copy .env.sample as .env
```

### Input the API KEY and SECRET
```angular2html
4. Get the API KEY from Backpack Website

#填入你的API KEY
API_KEY=''
#填入你的API SECRET
API_SECRET=''
#期望刷多少交易量
WISH_VOLUME='10000'
```

### Run the code
```angular2html
- python main.py
```

### Check the Volume and Fee
```angular2html
- python TotalVolCalc.py
```

