
import tweepy
import random

#API の設定
consumer_key = '32Jd96ccUuJwfAfjtzCghcA44'
consumer_secret = 'MVWk9PO7EPQ5qhA4H6clP0C0PAis2FDeLlpBl7tqRrKRsoTLUA'
access_token_key = '1240606785762775040-fLPaRMytqOHFmC2thD4TDkGSOhnVRQ'
access_token_secret = 'Zbcd8vHeiH5fhWOz63u6TkB6lrG4AqbUY7heTifV6dbCi'

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

#To make txt file.

# data.txtファイルを"読み込みモード"で開く
file_data = open("kafka_prose.txt", "r", encoding="utf-8_sig")
# それぞれの行をまとめて取得する
lines = file_data.readlines()
# 取得した行(要素)数をカウント
count = len(lines)
# 要素数の範囲内でランダムの数を設定
number = random.randrange(count)
# 開いたファイルを閉じる
file_data.close()

# ツイートする
api.update_status(lines[number])