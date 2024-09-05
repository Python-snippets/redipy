import pickle

class Persistence:
    def __init__(self, db, persistence_file='db.pkl'):
        self.db = db
        self.persistence_file = persistence_file

    def save_data(self):
        """Persist data to disk"""
        with open(self.persistence_file, 'wb') as f:
            data = {
                'store': self.db.store,
                'expirations': self.db.expirations,
            }
            pickle.dump(data, f)
        return "OK"

    def load_data(self):
        """Load persisted data from disk"""
        try:
            with open(self.persistence_file, 'rb') as f:
                data = pickle.load(f)
                self.db.store = data.get('store', {})
                self.db.expirations = data.get('expirations', {})
        except FileNotFoundError:
            pass
