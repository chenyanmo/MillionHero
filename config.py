# -*- coding:utf-8 -*-


data_directory = "screenshots"

default_answer_number = 2

### 1代表灰度处理， 2代表二值化处理，如果需要使用二值化，需要将2放到前面, 0不使用
image_compress_level = (0, 1, 2)

### ocr config
# hanwan_appcode = "***"
hanwan_appcode = "***"

### baidu orc
app_id = "10661627"
app_key = "h5xcL0m4TB8fiiFWoysn7uxt"
app_secret = " HGA1cgXzz80douKQUpII7K77TYWSGcfW"

### 0 表示普通识别，配合compress_level 1使用
### 1 标识精确识别，精确识别建议配合image_compress_level 2使用
api_version = (0, 1)

### 如果你想要使用汉王的话，将汉王移动到前面，默认使用百度，每天封顶500次
prefer = ("hanwang")

text_summary = True
summary_sentence_count = 3

