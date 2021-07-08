<br>

# trailing_white_spaces_remover_korean

자동 줄바꿈된 문장들을 이어 붙이고 단락을 구분하는 프로그램입니다. 

한글 맞춤법에 의거하여 제작하였습니다. 

<br>

## 설치

1. clone
``` bash
$ git clone https://github.com/jiwoo-jus/trailing_white_spaces_remover_korean.git
```

2. 서브모듈 가져오기
```
$ git submodule init
$ git submodule udpate
```

3. py-hanspell 폴더로 이동 및 설치
```
$ cd py-hanspell
$ python setup.py install
```
<br>

## 텍스트 파일 넣기

1. 프로젝트 폴더 내부에 대상 텍스트파일을 넣습니다. (.txt 확장자)

2. 코드 수정

    [main.py](https://github.com/jiwoo-jus/trailing_white_spaces_remover_korean/blob/master/main.py) **line 27**
    
    ```
    textfile = '대상 텍스트파일명'
    ```

    [main.py](https://github.com/jiwoo-jus/trailing_white_spaces_remover_korean/blob/master/main.py) **line 9**

    ```
    with open('결과로 반환할 텍스트파일명.txt', 'w', encoding='utf-8') as fw:
    ```

    [main.py](https://github.com/jiwoo-jus/trailing_white_spaces_remover_korean/blob/master/main.py) **line 21**

    ```
    if len(scripts[i]) < 대상 텍스트의 한 행 평균 글자수:
    ```


<br>

## 실행

``` bash
$ python main.py
```

