
class Requests:
    content_type = 'JSON'
    body = None

    def set_content_type(self, content_type: str): 
        self.content_type = content_type
        return self

    def set_body(self, body: any):
        self.body = body
        return self

    def post(url: str):
        pass


Requests().set_content_type('FORM_URLENCONDED').set_body({"name": "evans"}).post('url')
