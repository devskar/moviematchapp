from enum import Enum


class Genre(Enum):
    """Enum to match the genre name to the specific id of api"""
    Action = 28
    Adventure = 12
    Animation = 16
    Comedy = 35
    Crime = 80
    Documentary = 99
    Drama = 18
    Family = 10751
    Fantasy = 14
    History = 36
    Horror = 27
    Music = 10402
    Mystery = 9648
    Romance = 10749
    Science_Fiction = 878
    TV_Movie = 10770
    Thriller = 53
    War = 10752
    Western = 37


class Language(Enum):
    German = 'de'
    English = 'en-US'
