from PIL import Image
import pytesseract

class Languages:
    CHS = 'chi_sim'  # 识别汉字
    ENG = 'eng'  #　识别字母

def img_to_str(image_path, lang=Languages.ENG):
    return pytesseract.image_to_string(Image.open(image_path), lang)

# print(img_to_str('5374.png', lang=Languages.ENG))
text = img_to_str('zimu1.png', lang=Languages.ENG)
# print(type(text))
print(text)