from flask import Flask, request, jsonify


class Memo:
    __title = ''
    __text = ''

    def __init__(self, title, text):
        self.__title = title
        self.__text = text

    def get_memo(self):
        return {
            'title': self.__title,
            'text': self.__text
        }


memo_list = []

app = Flask(__name__)


@app.route('/memo', methods=['GET'])
def show_memo():
    response = []

    # iterate through memo objects
    for memo in memo_list:
        response.append(memo.get_memo())

    return jsonify(response)


@app.route('/memo', methods=['POST'])
def add_memo():
    data = request.get_json()
    response = {}

    # check if request is correct
    if 'title' not in data.keys() or 'text' not in data.keys():
        response['result'] = False
        return jsonify(response)

    title = data['title']
    text = data['text']

    # add memo to list
    memo = Memo(title, text)
    memo_list.append(memo)

    response['result'] = True
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
