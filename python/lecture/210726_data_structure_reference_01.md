### 공통 시퀀스 연산

다음 표의 연산들은 대부분의 가변과 불변 시퀀스에서 지원됩니다. 사용자 정의 시퀀스에서 이 연산들을 올바르게 구현하기 쉽게 하려고 [`collections.abc.Sequence`](https://docs.python.org/ko/3/library/collections.abc.html#collections.abc.Sequence) ABC가 제공됩니다.

이 표는 우선순위에 따라 오름차순으로 시퀀스 연산들을 나열합니다. 표에서, *s* 와 *t* 는 같은 형의 시퀀스고, *n*, *i*, *j*, *k* 는 정수이고, *x* 는 *s* 가 요구하는 형과 값 제한을 만족하는 임의의 객체입니다.

`in` 과 `not in` 연산은 비교 연산과 우선순위가 같습니다. `+` (이어 붙이기)와 `*` (반복) 연산은 대응하는 숫자 연산과 같은 우선순위를 갖습니다. [3](https://docs.python.org/ko/3/library/stdtypes.html#id14)

| 연산                   | 결과                                                         | 노트   |
| :--------------------- | :----------------------------------------------------------- | :----- |
| `x in s`               | *s* 의 항목 중 하나가 *x* 와 같으면 `True`, 그렇지 않으면 `False` | (1)    |
| `x not in s`           | *s* 의 항목 중 하나가 *x* 와 같으면 `False`, 그렇지 않으면 `True` | (1)    |
| `s + t`                | *s* 와 *t* 의 이어 붙이기                                    | (6)(7) |
| `s * n` 또는 `n * s`   | *s* 를 그 자신에 *n* 번 더하는 것과 같습니다                 | (2)(7) |
| `s[i]`                 | *s* 의 *i* 번째 항목, 0에서 시작합니다                       | (3)    |
| `s[i:j]`               | *s* 의 *i* 에서 *j* 까지의 슬라이스                          | (3)(4) |
| `s[i:j:k]`             | *s* 의 *i* 에서 *j* 까지 스텝 *k* 의 슬라이스                | (3)(5) |
| `len(s)`               | *s* 의 길이                                                  |        |
| `min(s)`               | *s* 의 가장 작은 항목                                        |        |
| `max(s)`               | *s* 의 가장 큰 항목                                          |        |
| `s.index(x[, i[, j]])` | (인덱스 *i* 또는 그 이후에, 인덱스 *j* 전에 등장하는) *s* 의 첫 번째 *x* 의 인덱스 | (8)    |
| `s.count(x)`           | *s* 등장하는 *x* 의 총수                                     |        |

같은 형의 시퀀스는 비교를 지원합니다. 특히, 튜플과 리스트는 대응하는 항목들을 사전적으로 비교합니다. 이것은 같다고 비교되기 위해서는, 모든 항목이 같다고 비교되고, 두 시퀀스의 형과 길이가 같아야 함을 의미합니다. (자세한 내용은 언어 레퍼런스의 [비교](https://docs.python.org/ko/3/reference/expressions.html#comparisons)를 참조하십시오.)

노트:

1. `in` 과 `not in` 연산은 일반적으로 단순한 포함 검사를 위해서만 사용되지만, 몇몇 특수한 시퀀스 ([`str`](https://docs.python.org/ko/3/library/stdtypes.html#str), [`bytes`](https://docs.python.org/ko/3/library/stdtypes.html#bytes), [`bytearray`](https://docs.python.org/ko/3/library/stdtypes.html#bytearray) 같은) 들은 서브 시퀀스 검사에 사용하기도 합니다:

   \>>>

   ```
   >>> "gg" in "eggs"
   True
   ```

2. *n* 의 값이 `0` 보다 작으면 `0` 으로 처리됩니다 (*s* 와 같은 형의 빈 시퀀스가 됩니다). 시퀀스 *s* 의 항목들이 복사되지 않음에 주의해야 합니다; 그들은 여러 번 참조됩니다. 이것은 종종 새 파이썬 프로그래머들을 괴롭힙니다; 이 코드를 살펴보세요:

   \>>>

   ```
   >>> lists = [[]] * 3
   >>> lists
   [[], [], []]
   >>> lists[0].append(3)
   >>> lists
   [[3], [3], [3]]
   ```

   무슨 일이 일어났는가 하면, `[[]]` 는 빈 리스트를 포함하는 길이 1인 리스트인데, `[[]] * 3` 의 세 항목은 모두 같은 빈 리스트를 참조합니다. `lists` 의 어느 항목을 수정하더라도 이 하나의 리스트를 수정하게 됩니다. 서로 다른 리스트들을 포함하는 리스트는 이런 식으로 만들 수 있습니다:

   \>>>

   ```
   >>> lists = [[] for i in range(3)]
   >>> lists[0].append(3)
   >>> lists[1].append(5)
   >>> lists[2].append(7)
   >>> lists
   [[3], [5], [7]]
   ```

   더 자세한 설명은 FAQ 항목 [다차원 리스트를 어떻게 만듭니까?](https://docs.python.org/ko/3/faq/programming.html#faq-multidimensional-list)에서 얻을 수 있습니다.

3. *i* 또는 *j* 가 음수인 경우, 인덱스는 시퀀스 *s* 의 끝에 상대적입니다: `len(s) + i` 이나 `len(s) + j` 로 치환됩니다. 하지만 `-0` 은 여전히 `0` 입니다.

4. *i* 에서 *j* 까지의 *s* 의 슬라이스는 `i <= k < j` 를 만족하는 인덱스 *k* 의 항목들로 구성된 시퀀스로 정의됩니다. *i* 또는 *j* 가 `len(s)` 보다 크면 `len(s)` 을 사용합니다. *i* 가 생략되거나 `None` 이라면 `0` 을 사용합니다. *j* 가 생략되거나 `None` 이면 `len(s)` 을 사용합니다. *i* 가 *j* 보다 크거나 같으면 빈 슬라이스가 됩니다.

5. 스텝 *k* 가 있는 *i* 에서 *j* 까지의 슬라이스는 `0 <= n < (j-i)/k` 를 만족하는 인덱스 `x = i + n*k` 의 항목들로 구성된 시퀀스로 정의됩니다. 다시 말하면, 인덱스는 `i`, `i+k`, `i+2*k`, `i+3*k` 등이며 *j* 에 도달할 때 멈춥니다 (하지만 절대 *j* 를 포함하지는 않습니다). *k* 가 양수면 *i* 와 *j* 는 더 큰 경우 `len(s)` 로 줄어듭니다. *k* 가 음수면, *i* 와 *j* 는 더 큰 경우 `len(s) - 1` 로 줄어듭니다. *i* 또는 *j* 가 생략되거나 `None` 이면, 그것들은 《끝》 값이 됩니다 (끝은 *k* 의 부호에 따라 달라집니다). *k* 는 0일 수 없음에 주의하세요. *k* 가 `None` 이면 `1` 로 취급됩니다.

6. 불변 시퀀스를 이어 붙이면 항상 새로운 객체가 생성됩니다. 이것은 반복적으로 이어붙이기를 해서 시퀀스를 만들 때 실행 시간이 시퀀스의 총 길이의 제곱에 비례한다는 뜻입니다. 선형 실행 시간 비용을 얻으려면 아래 대안 중 하나로 전환해야 합니다:

   - [str](<https://docs.python.org/ko/3/library/stdtypes.html#str>) 객체를 이어붙이기를 한다면, 리스트를 만들고 마지막에 [str.join()](https://docs.python.org/ko/3/library/stdtypes.html#str.join) 을 사용하거나 [io.StringIO](https://docs.python.org/ko/3/library/io.html#io.StringIO) 인스턴스에 쓰고 완료될 때 값을 꺼낼 수 있습니다
   - [bytes](https://docs.python.org/ko/3/library/stdtypes.html#bytes) 객체를 연결하는 경우 비슷하게 [bytes.join()](https://docs.python.org/ko/3/library/stdtypes.html#bytes.join) 또는 [io.BytesIO](https://docs.python.org/ko/3/library/io.html#io.BytesIO) 를 사용하거나, [bytearray](https://docs.python.org/ko/3/library/stdtypes.html#bytearray) 객체를 사용하여 제자리에서 이어붙이기를 할 수 있습니다. [bytearray](https://docs.python.org/ko/3/library/stdtypes.html#bytearray) 객체는 가변이고 효율적인 과할당(overallocation) 메커니즘을 가지고 있습니다.
   - [tuple](https://docs.python.org/ko/3/library/stdtypes.html#tuple) 객체를 이어붙이기를 한다면, 대신 [list](https://docs.python.org/ko/3/library/stdtypes.html#list)를 extend 하십시오.
   - 다른 형의 경우 관련 클래스 문서를 조사하십시오.

7. 일부 시퀀스 형 (예를 들어 [range](https://docs.python.org/ko/3/library/stdtypes.html#range))은 특정 패턴을 따르는 항목 시퀀스 만 지원하기 때문에 시퀀스 이어붙이기나 반복을 지원하지 않습니다.

8. *s* 에 *x* 가 없을 때 `index` 는 [ValueError](https://docs.python.org/ko/3/library/exceptions.html#ValueError) 를 일으킵니다. 모든 구현이 추가 인자 *i* 및 *j* 전달을 지원하지는 않습니다. 이러한 인자를 사용하면 시퀀스의 부분을 효율적으로 검색할 수 있습니다. 추가 인자를 전달하는 것은 대략 `s[i:j].index(x)` 를 사용하는 것과 비슷한데, 데이터를 복사하지 않고 반환된 인덱스가 슬라이스의 시작이 아닌 시퀀스의 시작을 기준으로 삼습니다.