# flan-t5-chat-bot-workshop-demo
Finetuning Flan T5 Chat Bot Workshop Demo.
Collab example: https://colab.research.google.com/drive/1y6hYbub89f0By9aXIyscqXWqHkWP5DbE#scrollTo=33b5785c

### Install dependencies
and change your hub token on .env 

```dotenv
pip install -r requirements.txt
scp -r .env.sample .env
```

### Run Chat Bot
```dotenv
streamlit run chatbotapp/main.py
```
