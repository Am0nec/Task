class Dessert:
    def __init__(self, name = None, calories = None):
        self.name = name
        self.calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = value

    def is_healthy(self):
        if (isinstance(self.__calories, (int, float)) and self.__calories < 200):
            return True
        return False

    def is_delicious(self):
        return True

class JellyBean(Dessert):
    def __init__(self, name = None, calories = None, flavor = None):
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        if self.flavor == "black licorice":
            return False
        return True

    def is_healthy(self):
        if (isinstance(self._calories, (int, float)) and self._calories < 200):
            return True
        return False


