class ProfileCaloriesMixin:
    def body_mass_index(self):
        '''Индекс массы тела'''
        return int(self.weight / (self.height / 100) ** 2)

    def normal_weight(self):
        '''Рекомендуемый вес'''
        min_weight = int(18 * ((self.height / 100) ** 2))
        max_weight = int(25 * ((self.height / 100) ** 2))
        dict_normal_weight = {
            'min_weight': min_weight,
            'max_weight': max_weight
        }
        return dict_normal_weight

    def normal_calories(self):
        '''Норма каллорий'''
        if self.sex == 'man':
            return int((10 * self.weight + 6.25 * self.height - 5 * self.age + 5) * float(self.activity))
        return int((10 * self.weight + 6.25 * self.height - 5 * self.age - 161) * float(self.activity))

    def deficit_calories(self):
        '''Норма дефицита каллорий при похудении'''
        return int(self.normal_calories() - self.normal_calories() * 0.15)

    def normal_protein_fat_carbohydrate(self):
        '''Норма БЖУ'''
        protein = int(1.8 * self.weight)
        fat = int(self.weight)
        carbohydrate = int((self.normal_calories() - 4 * protein - fat * 9) / 4)
        dict_normal_protein_fat_carbohydrate = {
            'protein': protein,
            'fat': fat,
            'carbohydrate': carbohydrate
        }
        return dict_normal_protein_fat_carbohydrate

    def deficit_protein_fat_carbohydrate(self):
        '''Норма БЖУ при похудении'''
        protein = int(2 * self.weight)
        fat = self.weight if self.body_mass_index() <= 25 else 0.9 * self.weight
        carbohydrate = int((self.deficit_calories() - 4 * protein - fat * 9) / 4)
        dict_deficit_protein_fat_carbohydrate = {
            'protein': protein,
            'fat': fat,
            'carbohydrate': carbohydrate
        }
        return dict_deficit_protein_fat_carbohydrate
