import webview

html = """
<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Messenger</title><style>
*{box-sizing:border-box;margin:0;padding:0;font-family:'Segoe UI',sans-serif}
body{background:#f0f2f5;height:100vh;display:flex;justify-content:center;align-items:center}
.app{width:900px;height:600px;background:#fff;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.1);display:flex;overflow:hidden}
.sidebar{width:300px;border-right:1px solid #e0e0e0;display:flex;flex-direction:column}
.search{padding:15px;background:#f7f7f7;border-bottom:1px solid #e0e0e0}
.search input{width:100%;padding:8px 12px;border-radius:20px;border:none;background:#e4e6eb}
.chats{flex:1;overflow-y:auto}.chat{display:flex;align-items:center;padding:15px;cursor:pointer;border-bottom:1px solid #f0f0f0}
.chat:hover{background:#f0f2f5}.chat.active{background:#e6f2ff}
.avatar{width:45px;height:45px;border-radius:50%;background:linear-gradient(45deg,#FF9A9E,#FECFEF);margin-right:15px}
.chat-info h4{font-size:15px;color:#333}.chat-info p{font-size:13px;color:#888}
.main{flex:1;display:flex;flex-direction:column}.header{padding:15px 20px;border-bottom:1px solid #e0e0e0;display:flex;align-items:center}
.dot{width:10px;height:10px;background:#4cd964;border-radius:50%;margin-left:10px}
.messages{flex:1;padding:20px;background:#fafafa;overflow-y:auto;display:flex;flex-direction:column;gap:10px}
.msg{max-width:70%;padding:10px 15px;border-radius:18px;font-size:14px}
.msg.in{align-self:flex-start;background:#e4e6eb}.msg.out{align-self:flex-end;background:#0084ff;color:#fff}
.input{padding:15px;border-top:1px solid #e0e0e0;display:flex;gap:10px}
.input input{flex:1;padding:10px 15px;border-radius:20px;border:1px solid #ddd}
.input button{background:#0084ff;color:#fff;border:none;padding:0 20px;border-radius:20px;cursor:pointer}
</style></head><body>
<div class='app'><div class='sidebar'><div class='search'><input placeholder='Поиск...'></div><div class='chats'>
<div class='chat active'><div class='avatar'></div><div class='chat-info'><h4>Максим</h4><p>Привет!</p></div></div>
<div class='chat'><div class='avatar' style='background:linear-gradient(45deg,#a18cd1,#fbc2eb)'></div><div class='chat-info'><h4>Анна</h4><p>Скинь файлы</p></div></div>
</div></div><div class='main'><div class='header'><div class='avatar'></div><div><h4>Максим</h4><span style='font-size:12px;color:#888'>в сети</span><span class='dot'></span></div></div>
<div class='messages' id='box'><div class='msg in'>Привет! Давно не виделись.</div></div>
<div class='input'><input id='inp' placeholder='Сообщение...'><button onclick='send()'>Отправить</button></div></div></div>
<script>
function send(){const t=document.getElementById('inp').value;if(!t.trim())return;
const b=document.getElementById('box'),m=document.createElement('div');
m.className='msg out';m.textContent=t;b.appendChild(m);b.scrollTop=b.scrollHeight;document.getElementById('inp').value='';
setTimeout(()=>{const r=document.createElement('div');r.className='msg in';r.textContent='Автоответ из EXE!';b.appendChild(r);b.scrollTop=b.scrollHeight;},1000)}
document.getElementById('inp').addEventListener('keypress',e=>{if(e.key==='Enter')send()});
</script></body></html>
"""

def main():
    window = webview.create_window('Messenger', html=html, width=900, height=600)
    webview.start()

if __name__ == '__main__':
    main()
