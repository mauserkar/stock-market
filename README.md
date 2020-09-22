## Send stock info to telegram channel

1 - Register to https://finnhub.io/ and create token
2 - Create telegram channel with bot 
3 - Build and run docker 

```bash
    docker build -t stock-market .
    docker run -d \
        --restart always \
        --name stock-market \
        -E STOCK=TSLA \ # tesla stock    
        -E FIN_TOKEN=my_finhub_token \
        -E BOT_TOKEN=my_telegram_token \
        -E BOT_CHAT_ID=my_telegram_channel_id \
        stock-market
```