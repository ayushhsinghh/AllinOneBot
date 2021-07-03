import boto3
client = boto3.client('s3')
client.upload_file("/root/telegram-bot/cybergod/telegram.log" , "allinone-telegram-bot-log" , "telegram.log")
