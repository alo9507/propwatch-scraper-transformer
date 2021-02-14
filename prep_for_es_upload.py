import json

def insert_index_id_line():
    f = open("final_result.txt", "r")
    contents = f.readlines()
    f.close()

    for index in range(0, len(contents)*2, 2):
        newline = { "index" : { "_index": "articles", "_id" : index } }
        y = json.dumps(newline)
        contents.insert(index, y)

    f = open("final_results_bulk_format.json", "w")
    contents = "\n".join(contents)
    f.write(contents)
    f.close()

if __name__ == '__main__':
    insert_index_id_line()