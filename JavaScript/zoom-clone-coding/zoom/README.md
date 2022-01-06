





# Noom

Zoom Clone using NodeJS, WebRTC and Websockets.




## INTRODUCTION

### Setup
**nodemon.json**

```json
  "exec": "babel-node src/server.js"
```
  변경사항이 있을 시 서버를 재시작해주는 프로그램
  서버 재시작하는 대신 babel-node 실행하게 되는데 babel-node는 우리가 작성한 코드를 일반 NodeJS 코드로 컴파일 해주는데 그 작업을 src/server.js 파일에 해줌

**server.js**

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
**Http** 

- 유저가 request 보내면 server가 response로 반응
- **stateless** : backend가 유저를 기억하지 못함. 오직 request 받을 때만 답장(response)

**WebSocket**

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

**backend**

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

**backend**

```JS
function handleConnection(socket) {
  console.log(socket); // socket 은 연결된 브라우저를 뜻함
}

wss.on("connection", handleConnection)

// 위 함수를 익명함수로 변경하면 아래와 같이 됨. 
wss.on("connection", (socket) => {
})
```

**frontend**

```JS
const socket = new WebSocket(`ws://${window.location.host}`)  // socket은 서버로의 연결을 뜻함
```

 

### WebSocket Message

**backend**

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

**frontend**

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

**frontend**

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

**pug**

```pug
    main 
      ul
      form
        input(type="text", placeholder="write a msg", required)
        button Send
```

**backend**

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

**frontend**

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
```html
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

**backend**

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

**전체 코드**

**frontend**

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

**backend**

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

**html(pug)**

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





## 2. SOCKETIO

### Socket.IO vs webSockets
- Socket.IO는 프론트와 백앤드 간 실시간 통신을 가능하게 해주는 프레임워크 또는 라이브러리
- 실시간/ 양방향/ event 기반 통신 
- websocket 보다 탄력성 있음: websocket이 동작하지 않으면 다른 방법으로 동작함
- 신뢰성과 빠른 속도 제공 : websocket보다는 살짝 무거움




### Installing socket IO

**backend**

- `$npm i socket.io`
- `import SocketIO from "socket.io";`
- http://localhost:3000/socket.io/socket.io.js 로 연결

- 서버에 socketIO 설치한 것처럼 client에도 socketIO 설치해야함. (socket IO는 webSocket의 부가 기능이 아님)
- 이전에는 브라우저가 주는 WebSocket API 이용하면 되었음. 하지만 webSocket API는 socket IO와 호환 안 됨.(socket IO가 더 많은 기능이 있기 때문)

**frontend**

- socket IO 설치
```pug
    main
    
    script(src="/socket.io/socket.io.js")
    script(src="/public/js/app.js") 
```
- http://localhost:3000 으로 연결 후 console창에 io 치면 function 나옴
- io() : 자동적으로 backend socket-io와 연결해주는 function
- frontend 전부 삭제하고 아래만 입력하고 새로고침 하면 터미널에 Socket 뜸 (이전에는 webSocket이었음)
- 이미 sockets: 가 적용됨 (이전에는 우리가 만들어주었음)
```JS
const socket = io();
```



### SocketIO is Amazing

**pug**

```pug

```
**frontend**

- `socket.emit("room", { payload: input.value });`
1. client는 어떤 event든 emit 해줄 수 있음. 이름 상관 x
2. 전송할 때 아무거나 전송할 수 있음. 이전엔 only text (numbers, Object, etx.. )
3. 원하는 만큼 backend로 전송 가능
```JS
const socket = io();

const welcome = document.getElementById("welcome");
const form = welcome.querySelector("form");


function handleRoomSubmit(event) {
  event.preventDefault();
  const input = form.querySelector("input")
  socket.emit("enter_room", { payload: input.value }, ); // 이전에는 message만 보냄
  input.value = "";
}
form.addEventListener("submit", handleRoomSubmit);
```

**backend**

1. custom event를 암거나 써도 됨 ! message 아니어도 됨.
2. frontend에서 object를 전송할 수 있음. 결과 : { payload: 'nicoroom' }
3. 여러개 받을 수 있음
```JS
wsServer.on("connection", socket => {
  socket.on("enter_room", (msg) => console.log(msg));
})
```
- **callback 함수 사용할수 있음!!!!** 
  
  **frontend**
  
  - 3번째 인자로 callback 함수 보내면
  ```JS
  socket.emit("enter_room", { payload: input.value }, () => {
    console.log("server is done!");
  });
  ```
  **backend**
  
  - 전달 받은 함수를 done이라는 이름으로 하고 실행시키면 frontend에서 실행됨
  ```JS
  wsServer.on("connection", socket => {
    socket.on("enter_room", (msg, done) => {
      console.log(msg);
      setTimeout(() => {
        done();
      }, 10000);
    });
  })
  ```



  ### recap

**backendDone() 함수**

  - FrontEnd에서 실행된 코드는 BackEnd가 실행시킨 것
  - 보통 http는 사람들이 request를 보내면 loading 후 http에 대한 결과를 보여줌. 이렇게 하면 오래 걸릴 수 있음.
  - 그런데 여기서는 backend를 실행시키는 코드를 만들 수 있음. 
  - backend에서 이 function에 argument를 보낼 수 있다는 것. (msg)
  - **다만 emit의 마지막 argument가 function이어야 함!!**

**frontend**

  ```JS  
  function backendDone(msg) {
    //console.log("backend done");
    console.log(`The backend says: `, msg);
  }

  function handleRoomSubmit(event) {
    event.preventDefault();
    const input = form.querySelector("input")
    socket.emit("enter_room", input.value, backendDone); 
    input.value = "";
  }
  form.addEventListener("submit", handleRoomSubmit);
  ```
**backend**

  ```JS
  wsServer.on("connection", socket => {
    socket.on("enter_room", (roomName, done) => {
      console.log(roomName);
      setTimeout(() => {
        // done();
        done("hello from the backend");
      }, 5000);
    });
  })
  ```



### Rooms
방에 참가하기

**backend**

`socket.join(roomName)`
```JS
wsServer.on("connection", socket => {
  socket.onAny((event) => {
    console.log(`Socket Event: ${event}`)
  });
  socket.on("enter_room", (roomName, done) => {
    socket.join(roomName);
    done(); // frontend에서 보낸 showRoom 함수가 done에 들어옴
  });
})
```
**frontend**

```JS
const room = document.getElementById("room");

room.hidden = true;

let roomName;

function showRoom() {
  welcome.hidden = true;
  room.hidden = false;
  const h3 = room.querySelector("h3");
  h3.innerText = `Room ${roomName}`;
}
function handleRoomSubmit(event) {
  //(...)
  socket.emit("enter_room", input.value, showRoom);
  roomName = input.value;
  //(...)
}
```
**pug**

```pug
      div#room
        h3
        ul
        form
          input(placeholder="message", required, type="text")
          button Send
```



### Room Message

방 안의 모든 사람들에게 메시지 보내기

**backend**

```JS
wsServer.on("connection", socket => {
  //(...)
  socket.on("enter_room", (roomName, done) => {
    //(...)
    socket.to(roomName).emit("welcome"); // "welcome" event를 roomName에 있는 모든 사람들에게 emit하기
  });
})
```
**frontend**

```JS
function addMessage(message) {
  const ul = room.querySelector("ul");
  const li = document.createElement("li");
  li.innerText = message;
  ul.appendChild(li);
}

socket.on("welcome", () => {  
  addMessage("someone joined");
})
```



### Room Notifications

**backend**
```JS
wsServer.on("connection", socket => {
  //(...)
  socket.on("disconnecting", () => {
    socket.rooms.forEach(room => socket.to(room).emit("bye"));
  });
  socket.on("new_message", (msg, room, done) => {
    socket.to(room).emit("new_message", msg);
    done();
  })
})
```

**frontend**
```JS
// html에 message 추가하는 함수
function addMessage(message) {
  const ul = room.querySelector("ul");
  const li = document.createElement("li");
  li.innerText = message;
  ul.appendChild(li);
}

// submit한 message를 backend에 보내는 함수 ("new_message")
function handleMessageSubmit(event) {
  event.preventDefault();
  const input = room.querySelector("input");
  const value = input.value;
  socket.emit("new_message", value, roomName, () => {
    addMessage(`You: ${value}`);
  });
  input.value = "";
}

// backend에서 보낸 것 frontend에서 실행
socket.on("bye", () => {  
  addMessage("someone left ㅠㅠ");
});
socket.on("new_message", (msg)=> {
  addMessage(msg);
});
```