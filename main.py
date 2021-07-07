import codecs
from hanspell import spell_checker


def remove_trailing_white_spaces_of_korean(text):
    scripts = text.split('\r\n')
    lines = [line.split(' ') for line in scripts]
    temp = ''
    with open('new_samplebook.txt', 'w', encoding='utf-8') as fw:
        # i가 2라고 가정
        for i in range(len(lines) - 1):
            if scripts[i] == '':  # line2가 빈 줄이라면
                fw.write('\n ')
                temp = ''
                continue
            temp += lines[i][0] if len(lines[i]) > 0 else ''  # lines[2][0] == line2시작단어
            if spell_checker.check(temp).errors > 0:  # temp(line1끝단어+line2시작단어) 맞춤법이 틀렸다면 그 사이 띄어쓰기
                fw.write(' ')
            fw.write(str(scripts[i]))  # line2 쓰기
            temp = lines[i][-1] if len(lines[i]) > 1 else ''  # lines[2][-1] == line2끝단어
            if len(scripts[i]) < 65:  # line2 글자수가 '한 줄 평균 글자수' 보다 작다면 의도한 개행으로 처리. 65 자리에 문서 한 줄 평균 글자수 입력
                fw.write('\n ')
                temp = ''


if __name__ == '__main__':
    textfile = 'samplebook.txt'
    with codecs.open(textfile, 'r', 'utf-8') as fr:
        text = fr.read()
    remove_trailing_white_spaces_of_korean(text)

