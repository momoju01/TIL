import http from "http";
import SocketIO from "socket.io";
import express from "express";

const app = express();

app.set("view engine", "pug");
app.set("views", __dirname + "/views");
app.use("/public", express.static(__dirname + "/public"));
app.get("/", (req, res) => res.render("home"));
app.get("/*", (req, res) => res.redirect("/"));




const HttpServer = http.createServer(app);
const wsServer = SocketIO(HttpServer);

wsServer.on("connection", socket => {
  socket.onAny((event) => {
    console.log(`Socket Event: ${event}`)
  });
  socket.on("enter_room", (roomName, done) => {
    socket.join(roomName);
    done(); // frontend에서 보낸 showRoom 함수가 done에 들어옴
    socket.to(roomName).emit("welcome"); // "welcome" event를 roomName에 있는 모든 사람들에게 emit하기
  });
  socket.on("disconnecting", () => {
    socket.rooms.forEach(room => socket.to(room).emit("bye"));
  });
  socket.on("new_message", (msg, room, done) => {
    socket.to(room).emit("new_message", msg);
    done();
  })
})



// const wss = new WebSocket.Server({ server });
// wss.on("connection", (socket) => { 
//   sockets.push(socket); // 연결된 browser별 socket을 sockets에 넣어줌
//   socket["nickname"] = "Anon"; // 익명
//   console.log("Connected to Browser ✅");
//   socket.on("close", () => console.log("Disconnected from the Browser ❌"));  
//   socket.on("message", (msg) => {
//     const message = JSON.parse(msg);
//     switch(message.type){
//       case "new_message":
//         sockets.forEach((aSocket) => aSocket.send(`${socket.nickname}: ${message.payload}`));      
//       case "nickname":
//         socket["nickname"] = message.payload;
//     }
//   });
// });


const handleListen = () => console.log(`Listening on http://localhost:3000`)
HttpServer.listen(3000, handleListen);

