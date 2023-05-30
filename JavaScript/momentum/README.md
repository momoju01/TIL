## 3.2 Searching For Element

### getElementById("")



### getElementByClassName("hello")



### getElementByTagName("h1")



### querySelector(".hello h1")

조건에 부합하는 하나의 element만 가져옴.

괄호 안에 css selector를 전달하면 됨

ex) `document.querySelector("div.hello:first-child h1")`

class hello를 가진 div 내부의 first-child인 h1을 찾아오는 것



### querySelectorAll(".hello h1")

조건에 부합하는 모든 element 가져오고 싶다면



## 3.3 Events

html에서 app.js를 import했기 때문에 javascript를 쓸 수 있는 것임

import 하지 않았다면 document는 존재하지 않음. 

### addEventListener()

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick() {
  title.style.color = "blue"
}

title.addEventListener("click", handleTitleClick);  // click 이벤트 일어나면 실행될 함수를 두 번째 인자로 넣어줌
```

함수 자체를 넘겨주어야 함. `handleTitleClick()` 이런 식으로 괄호 쓰면 안됨

## 3.4 Events 2

```javascript
title.addEventListener("click", handleTitleClick);
title.addEventListener("mouseenter", handleMouseEnter);
title.addEventListener("mouseleave", handleMouseLeave);
```





## 3.5 More Events

 ```javascript
 title.onclick = handleTitleClick;
 title.onmouseenter = handleMouseEnter;
 title.onmouseleave = handleMouseLeave;
 ```

이렇게 해도 동작함

```javascript
function handleWindowResize() {
  document.body.style.backgroundColor = "tomato";
}

function handleWindowCopy() {
  alert("copier!");
}

window.addEventListener("resize", handleWindowResize);
window.addEventListener("copy", handleWindowCopy);
```

`document.body` 이런 식으로 가져올 수 있음. `body`만 가능. `document.div`이런 식은 안 됨



## 3.6 CSS in JavaScript

```javascript
const h1 = document.querySelector("div.hello:first-child h1");

function handleTitleClick() {
  console.log(h1.style.color);
  if (h1.style.color === "blue") {
    h1.style.color = "tomato";
  } else {
    h1.style.color = "blue";
  }
}

h1.addEventListener("click", handleTitleClick);
```

아래처럼 변경해주기

```javascript
const h1 = document.querySelector("div.hello:first-child h1");

function handleTitleClick() {
  const currentColor = h1.style.color;
  let newColor;
  if (currentColor === "blue") {
    newColor = "tomato";
  } else {
    newColor = "blue";
  }
  h1.style.color = newColor;
}

h1.onclick = handleTitleClick;
```

### 전체 과정

1. find the element
2. listen for an event
3. react for the event



## 3.7 CSS in JavaScript 2

```javascript
const h1 = document.querySelector("div.hello:first-child h1");

function handleTitleClick() {
  if (h1.className === "clicked") {
    h1.className = "";
  } else {
    h1.className = "clicked";
  }
}

h1.addEventListener("click", handleTitleClick);
```

```css
body {
  background-color: beige;
}

h1 {
  color: cornflowerblue;
}

.clicked {
  color: tomato;
}
```



코드 옮길 때 실수할 수 있으니 javscript 코드 변수로 바꿔주기

```javascript
const h1 = document.querySelector("div.hello:first-child h1");

function handleTitleClick() {
  const clickedClass = "clicked";
  if (h1.className === clickedClass) {
    h1.className = "";
  } else {
    h1.className = clickedClass";
  }
}

h1.addEventListener("click", handleTitleClick);
```



### 여러개의 클래스를 적용하기

```html
  <div class="hello">
    <h1 class="sexy-font">Click me!</h1>
  </div>
```

```javascript
function handleTitleClick() {
  const clickedClass = "clicked";
  if (h1.className === clickedClass) {
    h1.className = "";
  } else {
    h1.className = clickedClass;
  }
}
```

이렇게 하면 두 번 클릭 했을 때 "sexy-font" 라는 class가 완전히 사라짐. clicked만 업데이트 하고 싶은 건데

```javascript
const clickedClass = "clicked sexy-font";
```

이렇게 하는 건 별로 안 좋아 보임



## 3.8 CSS in JavaScript 3

### classList

```javascript
function handleTitleClick() {
  const clickedClass = "clicked";
  if (h1.classList.contains(clickedClass)) {
    h1.classList.remove(clickedClass);
  } else {
    h1.classList.add(clickedClass);
  }
}
```

### toggle

```javascript
function handleTitleClick() {
  h1.classList.toggle("clicked");
}
```

이렇게 하면 한줄로 작성 가능. classList에서 한 것 그대로 !!