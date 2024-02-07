class Keywords:
    def __init__(self):
        self.keywords = {
            "keywords1": {"code": "", "contents": [], "keycode": [], "key_etc": [], "image_url": ""},
            "keywords2": {"code": "", "contents": [], "keycode": [], "key_etc": [], "image_url": ""}
        }

    def init_keywords(self):
        for key in self.keywords:
            self.keywords[key] = {"code": "", "contents": [], "keycode": [], "key_etc": [], "image_url": ""}
            
    def init_keyword(self, keyword):
        for key in self.keywords:
            self.keywords[keyword] = {"code": "", "contents": [], "keycode": [], "key_etc": [], "image_url": ""}

    def set_keyword(self, keyword, code, contents, keycode, key_etc, image_url):
        if keyword in self.keywords:
            self.keywords[keyword].update({
                "code": code,
                "contents": contents,
                "keycode": keycode,
                "key_etc": key_etc,
                "image_url": image_url
            })

    def get_keywords(self) -> dict:
        return self.keywords

    def get_keyword(self, keyword) -> dict:
        return self.keywords.get(keyword, {})