class ReportMixin:
    def process_instance(self, instance):
        title = getattr(instance, 'title')
        text_body = getattr(instance, 'text_body')
        
        return instance