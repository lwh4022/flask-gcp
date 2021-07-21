import json

from google.cloud import vision
from enum import Enum
from parsers import separate_sentences


class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5


def get_text(content) -> str:
    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    block_data_set_list = []
    for page in document.pages:
        for block in page.blocks:
            block_data_set = {"vertices": [], "data": []}

            for index in range(len(block.bounding_box.vertices)):
                if index % 2 == 0:
                    block_data_set["vertices"].append([block.bounding_box.vertices[index].x, block.bounding_box.vertices[index].y])

            block_data = ""
            for paragraph in block.paragraphs:
                paragraph_data = ""
                for word in paragraph.words:

                    word_data = ""
                    for idx in range(len(word.symbols)):
                        word_data += word.symbols[idx].text
                    word_data += " "
                    paragraph_data += word_data


                block_data += str(paragraph_data)[:-1] + "\n"

            print(str(block_data)[:-1])
            block_data_set["data"].extend(separate_sentences(str(block_data)[:-1]))
            block_data_set_list.append(block_data_set)

    return json.dumps(block_data_set_list, ensure_ascii=False, indent=4)
