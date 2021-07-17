# TIL

<i>day1_2021.07.15_Thursday</i>





# 1. 마크다운 문법(Markdown Syntax)



## 제목(header) 

**`<h1>`**부터 **`<h6>`**까지 제목을 표현할 수 있습니다.

```
# 제목 1
## 제목 2
### 제목 3
#### 제목 4
##### 제목 5
###### 제목 6
```

제목1(h1)과 제목2(h2)는 다음과 같이 표현할 수 있습니다.

```
제목 1
======

제목 2
------
```



### 강조(Emphasis)

각각 **`<em>`**, **`<strong>`**, **`<del>`** 태그로 변환됩니다.

밑줄을 입력하고 싶다면 **`<u></u>`** 태그를 사용하세요.

```
이텔릭체는*별표(asterisks)* 혹은_언더바(underscore)_를 사용하세요.
두껍게는**별표(asterisks)** 혹은__언더바(underscore)__를 사용하세요.
**_이텔릭체_와 두껍게**를 같이 사용할 수 있습니다.
취소선은 ~~물결표시(tilde)~~를 사용하세요.
<u>밑줄</u>은 `<u></u>`를 사용하세요.
```



이탤릭체는 *별표(asterisks)* 혹은 _언더바(underscore)_를 사용하세요. 

두껍게는 **별표두개(asterisk)** 혹은 __언더바두줄(underscore)__를 사용하세요.

**_이탤릭체_와 두껍게**를 같이 사용할 수 있습니다. 취소선은 ~~물결표시(tilde)~~를 사용하세요. 

<u>밑줄</u>은 `<u></u>`를 사용하세요.







### 목록(List)

**`<ol>`**, **`<ul>`** 목록 태그로 변환됩니다.

```
1. 순서가 필요한 목록
1. 순서가 필요한 목록
  - 순서가 필요하지 않은 목록(서브)
  - 순서가 필요하지 않은 목록(서브)
1. 순서가 필요한 목록
  1. 순서가 필요한 목록(서브)
  1. 순서가 필요한 목록(서브)
1. 순서가 필요한 목록

- 순서가 필요하지 않은 목록에 사용 가능한 기호
  - 대쉬(hyphen)
  * 별표(asterisks)
  + 더하기(plus sign)
```

1. 순서가 필요한 목록
2. 순서가 필요한 목록
   - 순서가 필요하지 않은 목록(서브)
   - 순서가 필요하지 않은 목록(서브)
3. 순서가 필요한 목록
   1. 순서가 필요한 목록(서브)
   2. 순서가 필요한 목록(서브)
4. 순서가 필요한 목록

- 순서가 필요하지 않은 목록에 사용 가능한 기호
  - 대쉬(hyphen)
  - 별표(asterisks)
  - 더하기(plus sign)



### 링크(Links)

**`<a>`**로 변환됩니다.

```
[GOOGLE](<https://google.com>)

[NAVER](<https://naver.com> "링크 설명(title)을 작성하세요.")

[상대적 참조](../users/login)

[Dribbble][Dribbble link]

[GitHub][1]

문서 안에서 [참조 링크]를 그대로 사용할 수도 있습니다.

다음과 같이 문서 내 일반 URL이나 꺾쇠 괄호(`< >`, Angle Brackets)안의 URL은 자동으로 링크를 사용합니다.
구글 홈페이지:<https://google.com>
네이버 홈페이지: <https://naver.com>

[Dribbble link]:<https://dribbble.com>
[1]:<https://github.com>
[참조 링크]:<https://naver.com> "네이버로 이동합니다!"
```

[google](<http://google.com>)

[NAVER](<https://naver.com> "네이버로 이동합니다!")

[상대적 참조](https://heropy.blog/2017/09/30/users/login)

[Dribbble](https://dribbble.com/)

[GitHub](https://github.com/)

문서 안에서 [참조 링크](https://naver.com/)를 그대로 사용할 수도 있습니다.

다음과 같이 문서 내 일반 URL이나 꺾쇠 괄호(**`< >`**, Angle Brackets)안의 URL은 자동으로 링크를 사용합니다.

구글 홈페이지: https://google.com네이버 홈페이지: https://naver.com



### 이미지(Images)

**`<img>`**로 변환됩니다.링크과 비슷하지만 <u>**앞에 `!`가 붙습니다.**</u>

```
![대체 텍스트(alternative text)를 입력하세요!](<http://www.gstatic.com/webp/gallery/5.jpg> "링크 설명(title)을 작성하세요.")

![Kayak][logo]

![대체 텍스트 입력]이미지 복사 붙여넣기
```

![http://www.gstatic.com/webp/gallery/5.jpg](http://www.gstatic.com/webp/gallery/5.jpg)

![잭 로던 (Jack Lowden) - 많은 여성분들의 마음 속에 저장하신 분 나는 톰핡디가 전쟁했지 : 네이버 블로그](https://mblogthumb-phinf.pstatic.net/MjAxNzA4MzBfMjg1/MDAxNTA0MDkyNTA3NDM5.sKBDxJC3hV6ZJuKTwVR3P5oZSquQ4w4XkVxZRI32Swog.HBmbl38WZgDOQJG8ZCa1SNN6A4ngnB52AvWtuYu53ncg.JPEG.dusdubin114/j.jpg?type=w2)

### 이미지에 링크

마크다운 이미지 코드를 링크 코드로 묶어 줍니다.

```
[![Vue](/images/vue.png)](<https://kr.vuejs.org/>)
```

![https://heropy.blog/images/vue.png](https://heropy.blog/images/vue.png)

### 코드(Code) 강조

<pre>, **<code>**로 변환됩니다.숫자 1번 키 왼쪽에 있는 ```(Grave)를 입력하세요


### 인라인(inline) 코드 강조

```
`background`혹은 `background-image` 속성으로 요소에 배경 이미지를 삽입할 수 있습니다.
```

**`background`**혹은 **`background-image`** 속성으로 요소에 배경 이미지를 삽입할 수 있습니다.

### 블록(block) 코드 강조

**```**를 3번 이상 입력하고 코드 종류도 적습니다.

~~~text

```html
<a href="https://www.google.co.kr/" target="_blank">GOOGLE</a>
```

```css
.list > li {
  position: absolute;
  top: 40px;
}
```

```javascript
function func() {
  var a = 'AAA';
  return a;
}
```

```bash
$ vim ./~zshrc
```

```python
s = "Python syntax highlighting"
print s
```

```
No language indicated, so no syntax highlighting.
But let's throw in atag.
```
~~~

```html
<a href="https://www.google.co.kr/" target="_blank">GOOGLE</a>
```

```css
.list > li {
  position: absolute;
  top: 40px;
}
```

```python
s = "Python syntax highlighting"
print s
```

