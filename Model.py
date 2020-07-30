class Model:
    __instance = None
    score = 0.8

    @staticmethod
    def instance():
        if Model.__instance == None:
            Model()
        else:
            return Model.__instance

    def __init__(self):
        if Model.__instance != None:
            raise Exception("Error")
        else:
            Model.__instance = self

    @staticmethod
    def predict():
        # model = Model.loadModel()
        return Model.score

    @staticmethod
    def loadModel():
        return "Loaded Model"

