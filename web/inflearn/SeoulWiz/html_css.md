# CSS

### 6-1 선택자란?

특정 태그<div> 를 선택하여 해당 태그의 속성을 변경하는 목적으로 사용됨

```html
<style>
div{
    background:#ffd800;
}
</style>
```





### 6-2  tag 선택자

```html
<style>
li{
    color:#ffd800;
}
</style>
```



### 7-1 id(#)와 class(.)

tag 에 고유한 id 값 쓸 수 있음

```html
<div id="wrap">
    <div id="content">
        <h1>content</h1>
        <ul>
            <li>list1</li>
            <li>list2</li>
            <li>list3</li>
        </ul>
    </div>
</div>
```



### 7-4 후손 및 자손 선택자

후손 선택자 : div 태그의 li 전체/ 자손 선택자 : div 태그의 바로 밑에 있는 태그 p

```html
div > p {
    color : red;
}
```



### 7-5 동위 선택자

- ~ : 자신과 동등한 위치에 있는 태그 전부 선택

- +: 자신과 동등한 위치에 있는 태그 바로 아래  하나 선택



