class Observer:
    def __init__(self) -> None:
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class UserLimitObserver:
    def __init__(self, user) -> None:
        self.user = user

    def update(self, message):
        print(f"Notification for {self.user.name}: {message}")
