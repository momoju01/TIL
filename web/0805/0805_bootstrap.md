# 0805_bootstrap

### Bootstrap grid

##### offset

기본 형식 : `col-md-4 offset-md-4`

`md` 부분은 반응형으로 sm, md, lg, xl 순으로 있다.

```html
  <div class="row">
      <div class="item col-4 col-md-4">
        <p>item1</p>
      </div>
      <div class="item col-8 col-md-4 offset-md-4">
        <p>item2</p>
      </div>
    </div>
```





### nesting

Grid system> Nesting 문서 참조

중첩된 column이라고 생각하고 상위 column부터 분배해준다.

하위 column은 상위 column 기준으로 12column을 나눠 쓴다.

![image-20210805233601132](0805_bootstrap.assets/image-20210805233601132.png)





```html
<div class="row">
      <div class="item col-md-3 col-lg-3">
        item1
      </div>
      <div class="item col-md-9 col-lg-9">
        <div class="row">
          <div class="item col-6 col-lg-3">item2</div>
          <div class="item col-6 col-lg-3">item3</div>
          <div class="item col-6 col-lg-3">item4</div>
          <div class="item col-6 col-lg-3">item5</div>
        </div>
      </div>
    </div>

```





### bootstrap class

- Display :
  - d-flex

- Direction :
  - flex-row
  - flex-row-reverse
  - flex-column
  - flex-column-reverse
- flex-wrap :
  - flex-wrap
  - flex-nowrap
  - flex-wrap-reverse
- flex-flow :
  - 없나봄
- justify-content
  - justify-content-start
  - justify-content-end
  - justify-content-center
  - justify-content-between -> css에선 space-between
  - justify-content-around
  - justify-content-evenly

- align-items
  - align-items-start
  - align-items-end
  - align-items-center
  - align-items-baseline
  - align-items-stretch
- align-content
  - align-content-start
  - align-content-end
  - align-content-center
  - align-content-around
  - align-content-stretch
- align-self 
  - align-self-star
  - align-self-end
  - align-self-center
  - align-self-baselin
  - align-self-stretch

