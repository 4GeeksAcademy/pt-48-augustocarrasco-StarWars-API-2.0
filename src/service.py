from models import Favourite, User, session as Session
from models import Character, Item, Planet, Starship
from sqlalchemy import select


class BDManagement:
    @staticmethod
    def get_item_list():
        query = Session.query(Item).all()
        response = list(map(lambda item: item.serialize(), query))
        return response

    @staticmethod
    def get_item_by_id(item_id):
        query = Session.query(Item).where(Item.id == int(item_id))
        response = list(map(lambda item: item.serialize(), query))
        return response

    @staticmethod
    def add_new_item(item):
        item_to_add = Item(
            name=item["name"], description=item["description"], img=item["img"]
        )
        Session.add(item_to_add)
        Session.commit()
        query = Session.query(Item).all()
        response = list(map(lambda item: item.serialize(), query))
        return response

    @staticmethod
    def get_character_list():
        params = select(Character, Item).join(Item)
        query = Session.scalars(params).all()
        response = list(map(lambda character: character.serialize(), query))
        return response

    @staticmethod
    def get_character_by_id(character_id):
        query = Session.query(Item).where(Item.id == int(character_id))
        response = list(map(lambda character: character.serialize(), query))
        return response

    @staticmethod
    def get_planet_list():
        query = Session.query(Planet).all()
        response = list(map(lambda planet: planet.serialize(), query))
        return response

    @staticmethod
    def get_planet_by_id(planet_id):
        query = Session.query(Planet).where(Planet.id == str(planet_id))
        response = list(map(lambda planet: planet.serialize(), query))
        return response

    @staticmethod
    def get_starship_list():
        query = Session.query(Starship).all()
        response = list(map(lambda starship: starship.serialize(), query))
        return response

    @staticmethod
    def get_starship_by_id(starship_id):
        query = Session.query(Planet).where(Planet.id == str(starship_id))
        response = list(map(lambda starship: starship.serialize(), query))
        return response

    @staticmethod
    def get_user_list():
        query = Session.query(User)
        response = list(map(lambda user: user.serialize(), query))
        return response

    @staticmethod
    def get_user_by_id(user_id):
        query = Session.query(User).where(User.id == user_id)
        response = list(map(lambda user: user.serialize(), query))
        return response

    @staticmethod
    def get_user_favourites(user_id):
        query = Session.query(Favourite).where(Favourite.user_id == user_id)
        response = list(map(lambda user: user.serialize(), query))
        return response

    @staticmethod
    def add_user_favourite(favourite_info):
        favourite_to_be_added = Favourite(
            user_id=favourite_info["user_id"], item_id=favourite_info["item_id"]
        )
        Session.add(favourite_to_be_added)
        Session.commit()
        query = Session.query(Favourite).where(
            Favourite.user_id == favourite_info["user_id"]
        )
        response = list(map(lambda item: item.serialize(), query))
        return response