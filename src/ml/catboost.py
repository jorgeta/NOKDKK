from catboost import Pool, CatBoostRegressor

class Catboost:
    
    def __init__(self):
        self.model = CatBoostClassifier(
            iterations=2, 
            depth=2, 
            learning_rate=1, 
            loss_function='RMSE')
    
    def fit(self):
        self.model.fit(self.train_pool)
    
    def predict(self):
        return self.model.predict(self.valid_pool)