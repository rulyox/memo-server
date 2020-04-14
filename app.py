from data import Memo


# instead of a database
memo_list = []


def add_memo(data):
    response = {}

    # check if request is correct
    if 'title' not in data.keys() or 'text' not in data.keys():
        response['result'] = False
        return response

    title = data['title']
    text = data['text']

    # add memo to list
    memo = Memo(title, text)
    memo_list.append(memo)

    response['result'] = True
    return response


def show_memo():
    response = []

    # iterate through memo objects
    for memo in memo_list:
        response.append(memo.get_memo())

    return response


def main():
    print('----- add memo without text -----')
    data = {
        'title': 'hello world'
    }
    print(add_memo(data))
    print()

    print('----- add 2 memos -----')
    data = {
        'title': 'hello world',
        'text': 'good day'
    }
    print(add_memo(data))
    data = {
        'title': 'second memo',
        'text': '222'
    }
    print(add_memo(data))
    print()

    print('----- show memos -----')
    print(show_memo())
    print()


if __name__ == "__main__":
    main()
