import json
import os

def jsonl_convert(txt, jsonl):
    print('Converting txt to jsonl...')
    txt = 'multi_session\Training/01.원천데이터\TS_session3\K3-19961-CL24119-CP41665-14-05-S3.txt'

    with open(txt, 'r',encoding = 'utf-8') as f:
        data = json.load(f)
    print(data)
    print(data['FileInfo']['sessionLevel'])
    print(data['participantsInfo'])
    # with open(jsonl, 'w') as f:
        
    #     for item in data:
    #         f.write(json.dumps(item) + '\n')
            
jsonl_convert('multi_session\Training/01.원천데이터\TS_session3\K3-19961-CL24119-CP41665-14-05-S3.txt', 'multi_session\Training/01.원천데이터\TS_session3\K3-19961-CL24119-CP41665-14-05-S3.jsonl')