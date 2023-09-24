class Car:

    def __init__(
            self,
            id: str | None,
            title: str,
            brand: str,
            model: str,
            year: int,
            color: str | None,
            price: float | None,
            description: str,
            created_at: str,
            updated_at: str
    ):
        self.id = id
        self.name = title
        self.brand = brand  # todo: make this an enum
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.name,
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'color': self.color,
            'price': self.price,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
