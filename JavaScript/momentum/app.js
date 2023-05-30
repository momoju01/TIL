const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");

const link = document.querySelector("a");
const greeting = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden"; // 변수명 대문자 : string만 포함된 변수, 중요한 변수 아닌 경우
const USERNAME_KEY = "username";

function onLoginSubmit(event) {
  // javascript는 event object를 넘겨줌
  // {information about the event that just happened}
  // all you have to do is to receive it.
  event.preventDefault(); // 기본 동작 막기
  loginForm.classList.add(HIDDEN_CLASSNAME);
  const username = loginInput.value;
  localStorage.setItem(USERNAME_KEY, username);
  paintGreetings(username);
}

function paintGreetings(username) {
  greeting.innerText = `Hello ${username}`;
  greeting.classList.remove(HIDDEN_CLASSNAME);
}

const savedUsername = localStorage.getItem(USERNAME_KEY);
if (savedUsername === null) {
  // show the form
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
} else {
  paintGreetings(savedUsername);
}
