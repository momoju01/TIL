# **2. 리액트 기초(THE BASICS OF REACT)**

## 2.1 Before React

기존 vanilaJS에서의 방식

```javascript
<!DOCTYPE html>
<html lang="en">
  <body>
    <button id="btn">Click me</button>
  </body>
  <script>
    const button = document.getElementById("btn");
    function handleClick() {
      console.log("i have been clicked");
    }
    button.addEventListener("click", handleClick);
  </script>
</html>

```

클릭시 html변경

```javascript
<!DOCTYPE html>
<html lang="en">
  <body>
    <span>Total clicks: 0</span>
    <button id="btn">Click me</button>
  </body>
  <script>
    let counter = 0;
    const button = document.getElementById("btn");
    const span = document.querySelector("span");
    function handleClick() {
      counter = counter + 1;
      span.innerText = `Total clicks: ${counter}`;
    }
    button.addEventListener("click", handleClick);
  </script>
</html>

```

지금은 간단해 보여도 나중에는 너무 복잡해질 수 있음.



## 2.2 **Our First React Element**

**React Js :** 어플리케이션이 interactive하게 만들어주는 library

**React-dom :** library or package 이고 모든 React element들을 html body에 둘 수 있도록 해줌.

Vanilla JS에서 했던 것을 그대로 React로 해보는 시간

단 React JS의 규칙 중 하나는 html을 이 페이지에 직접 작성하지 않음. 대신 javascript를 사용.



### 어려운 방식

To put a span on the page

1. React, React-dom cdn import

2. Root 생성하기

3. find root

4. **create element (react)  : start from javascript**

   `React.createElement("name_of_html_tag", {properties}, "content_of_tag")`

5. **render the element (react) : finishing on html**

   ```react
   <!DOCTYPE html>
   <html lang="en">
     <body>
       <div id="root"></div>
     </body>
     <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
     <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
     <script>
       const root = document.getElementById("root");
       // const span = React.createElement("span");
       const span = React.createElement(
         "span",
         { id: "sexy-span", style: { color: "red" } },
         "Hello I'm a Span"
       );
       ReactDOM.render(span, root)
     </script>
   </html>
   ```

   ​

## **2.3 Events in React**

vanilla javascript에서 element 선택 > addEventListener  등록하는 과정을 react에서는 property에서 한번에 event 등록할 수 있게 도와줌(하지만 아직 어려운방식임)

여러개를 rendering 하고싶으면 리스트 만들어서 보내주면 됨..!

```react
<script>
    const root = document.getElementById("root");
    const h3 = React.createElement(
      "h3",
      {
        onMouseEnter: () => console.log("mouse enter"),
      },
      "Hello I'm a Span"
    );
    const btn = React.createElement(
      "button", 
      {
        onClick: () => console.log("im clicked"),
      },
      "Click me"
    );
    const container = React.createElement("div", null, [h3, btn]);
    ReactDOM.render(container, root)
  </script>

```



## 2.4 Recap

## 2.5 **JSX**

**JSX** : a syntax extension to Javascript

1. import babel

2. script → `type="text/babel"`

3. html 작성하듯 작성하면 됨

   onMouseEnter쓸 때 `:` 에서 `=` 으로변경된 것 빼고는 변경사항 없음.

```react
  <script src="<https://unpkg.com/@babel/standalone/babel.min.js>"></script>
  <script type="text/babel">
    const root = document.getElementById("root");
    const Title = (
      <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
        Hello I'm a title
      </h3>
    );
    const Button = (
      <button 
        style={{
          backgroundColor: "tomato",
        }}
        onClick={() => console.log("im clicked")}
        >
        Click me
      </button>);
    const container = React.createElement("div", null, [Title, Button]);
    ReactDOM.render(container, root)
  </script>

```





`container` 도 수정해보기

container 안에서 내가 만든 Title과 Button 사용하려면

1. Title과 Button을 함수 형태로 만든다

   1. function으로 하면 return값 줘야함

      ```react
      function Title() {
            return (
              <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
                Hello I'm a title
              </h3>
            );
          };

      ```

   2. arrow function으로도 가능

      ```react
          const Button = () => (
            <button 
              style={{
                backgroundColor: "tomato",
              }}
              onClick={() => console.log("im clicked")}
              >
              Click me
            </button>);

      ```

2. Container 내부에 만든 태그를 대문자로 넣는다. (대문자 아니면 그냥 html태그 됨)

   Container도 함수 형태로 만들어서 render안에 tag형식으로 넣어준다.

   ```react
   const Container = () => (
         <div>
           <Title />
           <Button />
         </div>
       );
       ReactDOM.render(<Container />, root)
   ```







# 3. STATE

## **3.0 Understanding State**

버튼을 클릭했을 때 DOM을 바로 변경하기

1. Container 함수를 만들어 안에 바로 html요소를 rendering할 수 있음
2. Container를 처음 rendering한 후, countUp함수가 실행될 때도 re-rendering해주어야 interactive하게 반응함.
3. ReactJs는 container를 re-render해도 바뀐 부분만 re-render함!

```react
<script type="text/babel">
    const root = document.getElementById("root");
    let counter = 0;
    function countUp() {
      counter = counter + 1;
      render();
    }
    function render() {
      ReactDOM.render(<Container />, root);
    }
    const Container = () => (
      <div>
        <h3>Total clicks: {counter}</h3>
        <button onClick={countUp}>Click me</button>
      </div>
    );
    render();
  </script>

```

## **3.1 setState part One**

처음으로 다시 돌아가서 App 함수 안에 state를 정의

useState의 결과는 array로, 첫번째 요소는 데이터이고 두 번째 요소는 데이터를 수정하기 위한 함수.

console에 찍어보면 [undefined, f]를 얻음

useState()의 괄호 안의 값은 초기값을 나타냄 [0, f]을 얻음

```react
<script type="text/babel">
    const root = document.getElementById("root");
    function App() {
      const data = React.useState(0);
      console.log(data)
      return (
        <div>
          <h3>Total clicks: 0</h3>
          <button>Click me</button>
        </div>
      );
    } 
    ReactDOM.render(<App />, root)
  </script>

```

이 함수는 초기에 하던 방식과 동일. counter에 0넣고, counter를 변경하는 함수를 넣은.

```react
let counter = 0
    function countUp() {
      //code
    }

```

여기서 data에만 접근하려면, data[0] 이런식으로 index로 접근해야됨... not good

구조분해할당을 이용하면 더 깔끔하게 할 수 있음

```react
const food = ["tomato", "potato"]
const [myFavFood, secFavFood] = food
// console.log(myFavFood) -> "tomato"
// console.log(secFavFood) -> "potato"

```

```react
const [counter, modifier] = React.useState(0);

```

## 3.2 setState part Two

이어서

counter 를 let으로 바꾸고 onClick시 counter 값 변경되도록 함. 하지만 이것 역시 DOM을 바꾸려면 re-rendering해야하는데..

```react
<script type="text/babel">
    const root = document.getElementById("root");
    function App() {
      let [counter, modifier] = React.useState(0);
      const onClick = () => {
        counter = counter + 1;
        console.log(counter);
      };
      return (
        <div>
          <h3>Total clicks: {counter}</h3>
          <button onClick={onClick}>Click me</button>
        </div>
      );
    } 
    ReactDOM.render(<App />, root)
  </script>

```

modifier는 counter를 바꾸는 함수 자리

setCounter로 이름 바꾸고, counter에 들어갈 값을 매개변수로 넣어주면 자동으로 rendering 되는 함수 생성 완료!

modifier 함수를 가지고 state를 변경할 때 컴포넌트가 리랜더링됨

```react
<script type="text/babel">
    const root = document.getElementById("root");
    function App() {
      const [counter, setCounter] = React.useState(0);
      const onClick = () => {
        setCounter(counter + 1);
      };
			// console.log("rendered")
      // console.log(counter);
      return (
        <div>
          <h3>Total clicks: {counter}</h3>
          <button onClick={onClick}>Click me</button>
        </div>
      );
    } 
    ReactDOM.render(<App />, root)
  </script>

```

## 3.3 Recap

## 3.4 **State Functions**

counter 가 다른 곳에서 변경되었을 수도 있음.

state를 바꾸는 2가지 방법

1. setCounter() 안에서 counter value 바꿈

   `setCounter(counter + 1);`

2. **현재 state 바탕으로 다음 state를 계산해내고 싶다면** setCounter() 안에서 함수를 사용해서 바꿈 **(안전)**

   `setCounter((current) => current + 1);`

   ```react
   const onClick = () => {
           setCounter((current) => current + 1);
         };

   ```

## 3.5 Inputs and State

**JSX**

**for** : Javascript word 이라서 인식 못함..  for 사용 하지 말기...! class도.

```react
function App() {
      return (
        <div>
          <h3>Super Converter</h3>
          <label for="minutes">Minutes</label>
          <input id="minutes" placeholder="Minutes" type="number" />
          <label for="hours">Hours</label>
          <input id="hours" placeholder="Hours" type="number" />
        </div>
      );
    }

```

reactJS 는 javascript를 사용하기 때문에 event 보내는 것 가능

우리가 입력한 input의 value를 바탕으로 component를 업데이트 해주고 있음

```react
<script type="text/babel">
    const root = document.getElementById("root");
    function App() {
      const [minutes, setMinutes] = React.useState();
      const onChange = (event) => {
        setMinutes(event.target.value);
      }
      return (
        <div>
          <h3>Super Converter</h3>
          <label for="minutes">Minutes</label>
          <input 
            value={minutes}
            id="minutes"
            placeholder="Minutes"
            type="number"
            onChange={onChange}
          />
          <h4>You want to convert {minutes}</h4>
          <label for="hours">Hours</label>
          <input id="hours" placeholder="Hours" type="number" />
        </div>
      );
    } 
    ReactDOM.render(<App />, root)
  </script>

```



## 3.6 State Practice part One

**onChange** : 데이터 업데이트

React.useStore()의 매개변수를 0으로 놓고, input tage에서 onChange={onChange}를 삭제하면 Minutes의 input은 바꿀 수 없음.

왜냐하면 input의 value가 state(minutes) 이고, 이 state의 default 값이 0이기 때문

state를 setMinutes에서 바꿔주고 있기 때문에, 새로 업데이트 된 값을 가지고 return 안의 모든 코드가 다시 rendering 되는 것.

reset() 만들어서 0으로 초기화

```react
<script type="text/babel">
    const root = document.getElementById("root");
    function App() {
      const [minutes, setMinutes] = React.useState(0);
      const onChange = (event) => {
        setMinutes(event.target.value);
      }
      const reset = () => setMinutes(0)
      return (
        <div>
          <h3>Super Converter</h3>
          <div>
            <label for="minutes">Minutes</label>
            <input 
              value={minutes}
              id="minutes"
              placeholder="Minutes"
              type="number"
              onChange={onChange}
            />
          </div>
          <div>
            <label for="hours">Hours</label>
            <input
              value={minutes / 60}  // Math.round(minures/60)
              id="hours"
              placeholder="Hours"
              type="number"
            />
          </div>
          <button onClick={reset}>Reset</button>
        </div>
      );
    } 
    ReactDOM.render(<App />, root)
  </script>

```

input tag 안에 disabled 속성 넣어서 입력 막을 수 있음

```react
<input
  value={minutes / 60}
  id="hours"
  placeholder="Hours"
  type="number"
  disabled
/>

```

## 3.7 State Practice part Two

1. Flip button 만들어서 input할 값 제외하고 disabled 상태로 변경
2. minutes를 amout로 바꾸고 삼항연산자로 value 값을 직접 입력하는 상황일 때와 변환된 값을 반환할 때를 나눔.
3. flip버튼 클릭시 입력 값도 flip되는 문제 해결하기 위해 onFlip 함수 실행시 reset() 실행되도록 함.

```react
const root = document.getElementById("root");
    function App() {
      const [amount, setAmount] = React.useState(0);
      const [flipped, setFlipped] = React.useState(false);
      const onChange = (event) => {
        setAmount(event.target.value);
      }
      const reset = () => setAmount(0);
      const onFlip = () => {
        reset();
        setFlipped((current) => !current)
      };
      return (
        <div>
          <h3>Super Converter</h3>
          <div>
            <label for="minutes">Minutes</label>
            <input 
              value={flipped ? amount * 60 : amount}
              id="minutes"
              placeholder="Minutes"
              type="number"
              onChange={onChange}
              disabled={flipped}
            />
          </div>
          <div>
            <label for="hours">Hours</label>
            <input
              value={flipped ? amount : Math.round(amount/60)}  //minutes에 썼을때만 단위변환 일어나야 함
              id="hours"
              placeholder="Hours"
              type="number"
              onChange={onChange}
              disabled={!flipped}
            />
          </div>
          <button onClick={reset}>Reset</button>
          <button onClick={onFlip}>Flip</button>
        </div>
      );
    } 
    ReactDOM.render(<App />, root)

```

## 3.8 Recap

## 3.9 Final Practice and Recap

select 함수

**{ } 중괄호로 javascript 문법 사용 가능**

`const [index, setIndex] = React.useState("0");` 에는 0이 아니고 “0” 써줘야함.

```react
<script type="text/babel">
  const root = document.getElementById("root");
  function MinutesToHours(){
    const [amount, setAmount] = React.useState(0);
    const [flipped, setFlipped] = React.useState(false);
    const onChange = (event) => {
      setAmount(event.target.value);
    }
    const reset = () => setAmount(0);
    const onFlip = () => {
      reset();
      setFlipped((current) => !current)
      
    };
    return (
      <div>
        <div>
          <label for="minutes">Minutes</label>
          <input 
            value={flipped ? amount * 60 : amount}
            id="minutes"
            placeholder="Minutes"
            type="number"
            onChange={onChange}
            disabled={flipped}
          />
        </div>
        <div>
          <label for="hours">Hours</label>
          <input
            value={flipped ? amount : Math.round(amount/60)}  //minutes에 썼을때만 단위변환 일어나야 함
            id="hours"
            placeholder="Hours"
            type="number"
            onChange={onChange}
            disabled={!flipped}
          />
        </div>
        <button onClick={reset}>Reset</button>
        <button onClick={onFlip}>Flip</button>
      </div>
    );
  }
  function KmToMiles() {
    return <h3>KM 2 M</h3>;
  }
  function App() {
    const [index, setIndex] = React.useState("0");
    const onSelect = (event) => {
      setIndex(event.target.value)
    }
    return (
      <div>
        <h3>Super Converter</h3>
        <select value={index} onChange={onSelect}> // html
          <option value="0">Minutes & Hours</option> 
          <option value="1">Km & Miles</option>
        </select>
        <hr />
        {index === "0" ? <MinutesToHours /> : null}
        {index === "1" ? <KmToMiles /> : null}
      </div>
    );
  } 
  ReactDOM.render(<App />, root)
</script>

```