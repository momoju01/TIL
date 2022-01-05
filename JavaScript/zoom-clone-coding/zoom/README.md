# Noom

Zoom Clone using NodeJS, WebRTC and Websockets.


## INTRODUCTION

### Setup
#### nodemon.json
```json
  "exec": "babel-node src/server.js"
```
  변경사항이 있을 시 서버를 재시작해주는 프로그램
  서버 재시작하는 대신 babel-node 실행하게 되는데 babel-node는 우리가 작성한 코드를 일반 NodeJS 코드로 컴파일 해주는데 그 작업을 src/server.js 파일에 해줌

#### server.js
  ```JS
  // server.js
    import express from "express";

    const app = express();

    app.set("view engine", "pug"); // Pug로 view engine 설정
    app.set("views", __dirname + "/views");  // express로 template이 어디있는지 지정해주고
    app.use("/public", express.static(__dirname + "/public")); // public url 생성해서 유저에게 파일을 공유해주고
    app.get("/", (req, res) => res.render("home")); //home.pug를 render해주는 router handler 만듦
    console.log("hello");

    app.listen(3000);
  ```
  server.js 파일에서는 express import 하고 express 어플리케이션을 구성하고 여기에 view engine을 Pug로 설정하고, views 디렉토리가 설정되고 public 파일들에 대해서도 똑같은 작업을 해주고 있음
  public 파일은 FrontEnd에서 구동되는 코드고 이건 아주 중요한 부분



## 1. CHAT WITH WEBSOCKETS

### HTTP vs WebSocket
#### Http 
- 유저가 request 보내면 server가 response로 반응
- **stateless** : backend가 유저를 기억하지 못함. 오직 request 받을 때만 답장(response)

#### WebSocket
- protocol
- wss://nomadcoders.co
- webSocket 연결이 일어날 때는 악수(handshake)처럼 작동함
- 브라우저가 서버로 webSocket request 보내면, 서버가 받거나 거절함
- 악수가 한 번 성립되면, 연결이 성립됨(establish). 브라우저와 서버가 서로 커뮤니케이션 할 수 있음. 
- 서버는 유저를 기억할 수 있고 원하면 유저에게 메시지 보낼 수 있음. (request를 기다리지 않아도 됨)
- real-time으로 소통하는 2 개의 서버 사이에서도 작동함. webSocket은 브라우저와 backend 사이에서만 발생할 수 있는 게 아님.


### WebSockets in Node.js
- a NodeJS WebSocket library
- protocol > implementation : 규칙을 따르는 코드
#### backend
```js
// server.js
import http from "http";
import WebSocket from "ws";
//... 
const server = http.createServer(app); // http server
const wss = new WebSocket.Server({ server }); // () 안에 꼭 뭐 안 넣어도 됨. 이렇게 하는 경우 http와 ws 둘 다 돌릴 수 있음


server.listen(3000, handleListen);
```
- createServer 하려면 requestListener 경로 있어야함 >> app
- 같은 서버에서 http, webSocket 둘 다 작동시키기
- () 안에 꼭 뭐 안 넣어도 됨. 이렇게 하는 경우 http와 ws 둘 다 돌릴 수 있음


### WebSocket Events
ws 사용해서 backend와 frontend 사이에 첫 번째 connection 만들기
frontend에서 브라우저가 이미 webSocket 클라이언트에 대한 implementation을 갖고 있음을 알아두기
webSocket을 이용해 backend와 연결하고 싶다면 JS가 해줄 것
#### backend
```JS
function handleConnection(socket) {
  console.log(socket); // socket 은 연결된 브라우저를 뜻함
}

wss.on("connection", handleConnection)

// 위 함수를 익명함수로 변경하면 아래와 같이 됨. 
wss.on("connection", (socket) => {
})
```

#### frontend
```JS
const socket = new WebSocket(`ws://${window.location.host}`)  // socket은 서버로의 연결을 뜻함
```


### WebSocket Message
#### backend
- wws 라는 web socket server 만듦
- .on으로 event listen하고 있음. 브라우저마다 연결된 socket에서 이벤트 listen가능.
- socket.on : 특정 socket에 eventlistener 등록한 것. wss(서버)에 등록한 것이 아님
```JS
const wss = new WebSocket.Server({ server });

wss.on("connection", (socket) => { 
  console.log("Connected to Browser ✅");
  socket.on("close", () => console.log("Disconnected from the Browser ❌"));  // Browser 닫는 경우
  socket.on("message", message => {
    console.log(message.toString('utf-8')); // terminal에 출력됨
  })
  // 메시지 브라우저로 전달
  socket.send("hello!!");
})
```

#### frontend
```JS
// backend와 connection 열어주고 있음
const socket = new WebSocket(`ws://${window.location.host}`)  // socket은 서버로의 연결을 뜻함

// eventListener 등록
socket.addEventListener("open", () => {
  console.log("Connected to Server ✅");
});

socket.addEventListener("message", (message) => {
  console.log("New message: ", message.data);
});

socket.addEventListener("close", () => {
  console.log("Disconnected from Server ❌");
});

// 메세지 보내기
setTimeout(() => {
  socket.send("hello from the browser!");
}, 10000);

```

### Chat completed
#### front end
- 
```JS
const messageList = document.querySelector("ul");
const messageForm = document.querySelector("form");
// (...)

function handleSubmit(event) {
  event.preventDefault();
  const input = messageForm.querySelector("input");
  socket.send(input.value);
  // console.log(input.value);
  input.value = "";
}
messageForm.addEventListener("submit", handleSubmit);
```

#### pug
```pug
    main 
      ul
      form
        input(type="text", placeholder="write a msg", required)
        button Send
```

#### backend
- socket.send(message.toString('utf-8')); // front로 message 보냄
- 하지만 chrome에서 보내면 chrome 밖에 응답 안 함. firefox에서도 응답하게 하려면?
- sockets라는 fake db 생성후 연결된 browser별 socket을 sockets에 push
```JS
const sockets = [];

wss.on("connection", (socket) => { 
  sockets.push(socket); 
  // (...)  
  socket.on("message", (message) => {
    // socket.send(message.toString('utf-8')); // front로 message 보냄  
    sockets.forEach((aSocket) => aSocket.send(message.toString('utf-8')));
  });
});
```


### Nicknames - part.1
#### frontend
- li tag 만들고 그 안에 message 넣어서 messageList에 append하기
```JS
socket.addEventListener("message", (message) => {
  const li = document.createElement("li");
  li.innerText = message.data;
  messageList.append(li);
});
```
- 닉네임 폼 사용시 form이 두 개 되므로 front 와 html(pug)에서 각각 코드 수정
```JS
// app.js
const nickForm = document.querySelector("#nick");
const messageForm = document.querySelector("#message");
//(...)

function handleNickSubmit(event) {
  event.preventDefault();
  const input = nickForm.querySelector("input");
  socket.send({
    type:"nickname",
    payload:input.value,
  })
}
messageForm.addEventListener("submit", handleSubmit);
nickForm.addEventListener("submit", handleNickSubmit);
```
```pug
    main
      form#nick
        input(type="text", placeholder="choose a nickname", required)
        button Save
      ul
      form#message
        input(type="text", placeholder="write a msg", required)
        button Send
```

- 하지만 이 경우 li에 추가되는 것은 [object Object]로 object이다(javascript).
데이터 가공 해주어야됨! front에서는 backend로 message를 보낼때 string으로 보내야 함. 그래서 JSON데이터를 string으로 만들어주는 makeMessage 함수 만들어 사용
- 결과 : {"type":"nickname","payload":"firefox"}
```JS
function makeMessage(type, payload) {
  const msg = {type, payload}
  return JSON.stringify(msg);
}

function handleSubmit(event) {
  //(...)
  // socket.send(input.value) >> 
  socket.send(makeMessage("new_message", input.value));
  //(...)
}

function handleNickSubmit(event) {
  //(...)
  socket.send(makeMessage("nickname", input.value));
  //(...)
}
```


### Nicknames - part.2
- Object를 backend로 보내면 안되는 이유:
  backend가 javascript인지 다른 programming 언어인지 알 수 없기 때문. 그래서 string으로 보낸 후 backend 에서 받아서 그 데이터로 무엇을 할지 결정해야 함
  `const wss = new WebSocket.Server({ server });` WebSocket이 브라우저에 있는 API이기 때문. 
- 우리는 backend에서 javascript 를 사용하므로, backend가 받은 string을 다시 object 로 변경해야 함.
#### backend
- `JSON.parse()`사용하여 string을 object로 변경.
- if / else if 대신 siwtch() / case 사용 (개인 선호도..)
- 닉네임 안 입력한 경우, 익명으로 글 작성할 수 있도록 socket에 nickname 저장
```JS
wss.on("connection", (socket) => { 
  sockets.push(socket);
  socket["nickname"] = "Anon"; // 익명
  //(...)
  socket.on("message", (msg) => {
    const message = JSON.parse(msg);
    switch(message.type){
      case "new_message":
        sockets.forEach((aSocket) => aSocket.send(`${socket.nickname}: ${message.payload}`));      
      case "nickname":
        socket["nickname"] = message.payload;
    }
  });
});
```

### Conclusion
나를 제외한 사람에게 메시지 보내기
=> framework 사용하기~

#### 전체 코드
#### frontend
```
const messageList = document.querySelector("ul");
const nickForm = document.querySelector("#nick");
const messageForm = document.querySelector("#message");
const socket = new WebSocket(`ws://${window.location.host}`);  // socket은 서버로의 연결을 뜻함

function makeMessage(type, payload) {
  const msg = {type, payload}
  return JSON.stringify(msg);
}

socket.addEventListener("open", () => {
  console.log("Connected to Server ✅");
});

socket.addEventListener("message", (message) => {
  const li = document.createElement("li");
  li.innerText = message.data;
  messageList.append(li);
});

socket.addEventListener("close", () => {
  console.log("Disconnected from Server ❌");
});

// ⭐메세지 보내기
// setTimeout(() => {
//   socket.send("hello from the browser!");
// }, 10000);

function handleSubmit(event) {
  event.preventDefault();
  const input = messageForm.querySelector("input");
  socket.send(makeMessage("new_message", input.value));
  input.value = "";
}

function handleNickSubmit(event) {
  event.preventDefault();
  const input = nickForm.querySelector("input");
  socket.send(makeMessage("nickname", input.value));
  input.value = "";
}
messageForm.addEventListener("submit", handleSubmit);
nickForm.addEventListener("submit", handleNickSubmit);
```

#### backend
```JS
import http from "http";
import WebSocket from "ws";
import express from "express";

const app = express();

app.set("view engine", "pug");
app.set("views", __dirname + "/views");
app.use("/public", express.static(__dirname + "/public"));
app.get("/", (req, res) => res.render("home"));
app.get("/*", (req, res) => res.redirect("/"));

const handleListen = () => console.log(`Listening on http://localhost:3000`)
// app.listen(3000);

const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

const sockets = [];

wss.on("connection", (socket) => { 
  sockets.push(socket); // 연결된 browser별 socket을 sockets에 넣어줌
  socket["nickname"] = "Anon"; // 익명
  console.log("Connected to Browser ✅");
  socket.on("close", () => console.log("Disconnected from the Browser ❌"));  
  socket.on("message", (msg) => {
    const message = JSON.parse(msg);
    switch(message.type){
      case "new_message":
        sockets.forEach((aSocket) => aSocket.send(`${socket.nickname}: ${message.payload}`));      
      case "nickname":
        socket["nickname"] = message.payload;
    }
  });
});
server.listen(3000, handleListen);
```

#### html(pug)
```JS
doctype html
html(lang="en")
  head
    meta(charset="UTF-8")
    meta(http-equiv="X-UA-Compatible", content="IE=edge")
    meta(name="viewport", content="width=device-width, initial-scale=1.0")
    title Noom
    link(rel="stylesheet", href="https://unpkg.com/mvp.css")
  body
    header
      h1 Noom
    main
      form#nick
        input(type="text", placeholder="choose a nickname", required)
        button Save
      ul
      form#message
        input(type="text", placeholder="write a msg", required)
        button Send
    script(src="/public/js/app.js")
```





