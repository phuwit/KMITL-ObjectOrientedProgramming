import unittest
from main import *


class UnitTests(unittest.TestCase):

    def test_update_records(self):
        record_collection = {
            2548: {
                'albumTitle': 'Slippery When Wet',
                'artist': 'Bon Jovi',
                'tracks': ['Let It Rock', 'You Give Love a Bad Name']
            },
            2468: {
                'albumTitle': '1999',
                'artist': 'Prince',
                'tracks': ['1999', 'Little Red Corvette']
            },
            1245: {
                'artist': 'Robert Palmer',
                'tracks': []
            },
            5439: {
                'albumTitle': 'ABBA Gold'
            }
        }
        # Test case 1 will check the case if the value is empty,
        self.assertEquals(update_records(record_collection, 2548, "artist", ""), {
            2548: {'albumTitle': 'Slippery When Wet', 'tracks': ['Let It Rock', 'You Give Love a Bad Name']},
            2468: {'albumTitle': '1999', 'artist': 'Prince', 'tracks': ['1999', 'Little Red Corvette']},
            1245: {'artist': 'Robert Palmer', 'tracks': []}, 5439: {'albumTitle': 'ABBA Gold'}})

        # test case 2 change artist
        self.assertEquals(update_records(record_collection, 2548, "artist", "Black Pink"), {
            2548: {'albumTitle': 'Slippery When Wet', 'artist': 'Black Pink',
                   'tracks': ['Let It Rock', 'You Give Love a Bad Name']},
            2468: {'albumTitle': '1999', 'artist': 'Prince', 'tracks': ['1999', 'Little Red Corvette']},
            1245: {'artist': 'Robert Palmer', 'tracks': []}, 5439: {'albumTitle': 'ABBA Gold'}})

    # Test case 4 will check if the prop is tracks, and it should add the value to the tracks list of the given id.
    # self.assertEquals(update_records(record_collection,1245,"tracks","Addicted to Love")

    def test_update_record2(self):
        record_collection = {
            2548: {
                'albumTitle': 'Slippery When Wet',
                'artist': 'Bon Jovi',
                'tracks': ['Let It Rock', 'You Give Love a Bad Name']
            },
            2468: {
                'albumTitle': '1999',
                'artist': 'Prince',
                'tracks': ['1999', 'Little Red Corvette']
            },
            1245: {
                'artist': 'Robert Palmer',
                'tracks': []
            },
            5439: {
                'albumTitle': 'ABBA Gold'
            }
        }

        # test case 3 change albumTitle
        self.assertEquals(update_records(record_collection, 2548, "albumTitle", "Have a Nice Day"), {
            2548: {'albumTitle': 'Have a Nice Day', 'artist': 'Bon Jovi',
                   'tracks': ['Let It Rock', 'You Give Love a Bad Name']},
            2468: {'albumTitle': '1999', 'artist': 'Prince', 'tracks': ['1999', 'Little Red Corvette']},
            1245: {'artist': 'Robert Palmer', 'tracks': []}, 5439: {'albumTitle': 'ABBA Gold'}})

    def test_update_record3(self):
        record_collection = {
            2548: {
                'albumTitle': 'Slippery When Wet',
                'artist': 'Bon Jovi',
                'tracks': ['Let It Rock', 'You Give Love a Bad Name']
            },
            2468: {
                'albumTitle': '1999',
                'artist': 'Prince',
                'tracks': ['1999', 'Little Red Corvette']
            },
            1245: {
                'artist': 'Robert Palmer',
                'tracks': []
            },
            5439: {
                'albumTitle': 'ABBA Gold'
            }
        }

        # Test case 4 will check if the prop is tracks, and it should add the value to the tracks list of the given id.
        self.assertEquals(update_records(record_collection, 1245, "tracks", "Addicted to Love"), {
            2548: {'albumTitle': 'Slippery When Wet', 'artist': 'Bon Jovi',
                   'tracks': ['Let It Rock', 'You Give Love a Bad Name']},
            2468: {'albumTitle': '1999', 'artist': 'Prince', 'tracks': ['1999', 'Little Red Corvette']},
            1245: {'artist': 'Robert Palmer', 'tracks': ['Addicted to Love']}, 5439: {'albumTitle': 'ABBA Gold'}})

    def test_update_record4(self):
        record_collection = {
            2548: {
                'albumTitle': 'Slippery When Wet',
                'artist': 'Bon Jovi',
                'tracks': ['Let It Rock', 'You Give Love a Bad Name']
            },
            2468: {
                'albumTitle': '1999',
                'artist': 'Prince',
                'tracks': ['1999', 'Little Red Corvette']
            },
            1245: {
                'artist': 'Robert Palmer',
                'tracks': []
            },
            5439: {
                'albumTitle': 'ABBA Gold'
            }
        }

        self.assertEquals(update_records(record_collection, 2468, "tracks", ""), {
            2548: {'albumTitle': 'Slippery When Wet', 'artist': 'Bon Jovi',
                   'tracks': ['Let It Rock', 'You Give Love a Bad Name']},
            2468: {'albumTitle': '1999', 'artist': 'Prince'}, 1245: {'artist': 'Robert Palmer', 'tracks': []},
            5439: {'albumTitle': 'ABBA Gold'}})

    def test_update_record5(self):
        record_collection = {
            2548: {
                'albumTitle': 'Slippery When Wet',
                'artist': 'Bon Jovi',
                'tracks': ['Let It Rock', 'You Give Love a Bad Name']
            },
            2468: {
                'albumTitle': '1999',
                'artist': 'Prince',
                'tracks': ['1999', 'Little Red Corvette']
            },
            1245: {
                'artist': 'Robert Palmer',
                'tracks': []
            },
            5439: {
                'albumTitle': 'ABBA Gold'
            }
        }

        self.assertEquals(update_records(record_collection, 2468, "tracks", "International Lover"), {
            2548: {'albumTitle': 'Slippery When Wet', 'artist': 'Bon Jovi',
                   'tracks': ['Let It Rock', 'You Give Love a Bad Name']},
            2468: {'albumTitle': '1999', 'artist': 'Prince',
                   'tracks': ['1999', 'Little Red Corvette', 'International Lover']},
            1245: {'artist': 'Robert Palmer', 'tracks': []}, 5439: {'albumTitle': 'ABBA Gold'}})

    def test_update_record6(self):
        record_collection = {
            2548: {
                'albumTitle': 'Slippery When Wet',
                'artist': 'Bon Jovi',
                'tracks': ['Let It Rock', 'You Give Love a Bad Name']
            },
            2468: {
                'albumTitle': '1999',
                'artist': 'Prince',
                'tracks': ['1999', 'Little Red Corvette']
            },
            1245: {
                'artist': 'Robert Palmer',
                'tracks': []
            },
            5439: {
                'albumTitle': 'ABBA Gold'
            }
        }

        self.assertEquals(update_records(record_collection, 5349, "artist", ""), {
            2548: {'albumTitle': 'Slippery When Wet', 'artist': 'Bon Jovi',
                   'tracks': ['Let It Rock', 'You Give Love a Bad Name']},
            2468: {'albumTitle': '1999', 'artist': 'Prince', 'tracks': ['1999', 'Little Red Corvette']},
            1245: {'artist': 'Robert Palmer', 'tracks': []}, 5439: {'albumTitle': 'ABBA Gold'}})
        # Enter code here


