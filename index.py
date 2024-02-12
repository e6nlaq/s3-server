# ライブラリ
import scratchattach as scratch3
from dotenv import load_dotenv
import os

project_id = "961035795"
load_dotenv()

# ログインや接続
session = scratch3.login(os.environ["user"], os.environ["pass"])
conn = session.connect_cloud(project_id)
events = scratch3.CloudEvents(project_id)


# クラウド変数が変更されたときの処理
@events.event
def on_set(event):
    if event.var != "server":
        return
    worldrec = int(scratch3.get_var(project_id, "world"))

    print(f"{event.user}がタイム{event.value}を記録!")
    if int(event.value) < worldrec:
        print("世界記録更新!")
        worldrec = int(event.value)
        conn.set_var("world", event.value)


@events.event
def on_ready():
    print("Server is ready!")


# 処理開始
events.start()
