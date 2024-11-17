class ReportMixin:
    def process_instance(self, attr):
        print("Conteúdo do objeto:", attr)
        print("Tipo do objeto:", type(attr))
        try:
            title = attr.title
            text_body = self.attr.text_body
        except AttributeError:
            print("Erro: O objeto não possui os atributos 'title' ou 'text_body'.")
            return attr
        print("Olá, sou uma barata!")
        print(title, text_body)
        return attr
