class Memo:
    title = ''
    text = ''

    # constructor
    def __init__(self, title, text):
        self.title = title
        self.text = text

    # getter
    def get_memo(self):
        return {
            'title': self.title,
            'text': self.text
        }
