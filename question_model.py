import html
class Question:

    def __init__(self, q_text, q_answer):
        self.text = html.unescape(q_text)
        self.answer = html.unescape(q_answer)
