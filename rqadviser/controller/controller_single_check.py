from rqadviser.nlp.cosine_processor import CosineProcessor


class ControllerSingleCheck:
    def __init__(self):
        pass

    def init_nlp_model(self, mode, df):
        if mode == 0:
            nlp_model = CosineProcessor(df)
            nlp_model.prepare()
        return nlp_model
