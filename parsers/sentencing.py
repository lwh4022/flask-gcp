from konlpy.tag import Kkma
from typing import List


def separate_sentences(sentence) -> List[str]:
    kkma = Kkma()
    return kkma.sentences(sentence)
