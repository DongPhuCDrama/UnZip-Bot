import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6443004679:AAEYqctJm8b4di4wWjTjqchau00M_IaXAeU")
    API_ID = int(os.environ.get("API_ID", "23407106"))
    API_HASH = os.environ.get("API_HASH", "34817fe096f567f55ce37750b8a5ff1b")
    
    
