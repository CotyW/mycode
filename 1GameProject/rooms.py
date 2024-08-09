from roomdescriptions import descriptions 

rooms = {
    'Hall': {
        'north': 'Great Hall',
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key',
        'description': descriptions['Hall'],
    },
    'Great Hall': {
        'south': 'Hall',
        'item': '',
        'description': descriptions['Great Hall']
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'cupboard',
        'cupboard': 'cupboard',
        'description': descriptions['Kitchen'],
    },
    'cupboard':{
        'item': 'basketball',
        'kitchen': 'Kitchen',
        'description': descriptions['cupboard'],
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'description': descriptions['Dining Room'],
    },
    'Garden': {
        'north': 'Dining Room',
        'east': 'Courtyard',
        'west': 'Stables',
        'description': descriptions['Garden'],
    },
    'Stables': {
        'east': 'Garden',

    },
    'Courtyard': {
        'west': 'Garden',
        'description': descriptions['Courtyard'],
    }
}
