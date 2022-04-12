#!/usr/bin/python3

import sys
import time


def slow_print(input_string):
    """A function slowing down printing messages and forcing the user for
    input to continue"""
    for char in input_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    sys.stdout.write('\n ...')
    input()


class Player:
    """A class representing the Player and handling all their mechanics.

    Attributes:
    -------------
    _current_room : Room
        The room in which the Player is currently staying
    _next_room : Room
        The room the Player is moving to after completion of _current_room
    name : str
        The name of the Player
    has_bottle : bool
        Indicates if the Player has obtained a specified item
    has_key : bool
        Indicates if the Player has obtained a specified item

    Methods:
    -------------
    enter_room(room)
    exit_current_room_to(next_room)
    get_next_room(next_room)
    enter_next_room(next_room)
    """

    _current_room = None
    _next_room = None
    name = None

    def __init__(self, initial_room, name):  # create object Player
        self.name = name
        self.has_bottle = False
        self.has_key = False
        self._next_room = initial_room()  # execute initial room's story

    def enter_room(self, room):
        """A method handling entering a room by the Player. Assigns a prompted
        room as _current_room, sets _next_room to None. If _current_room is
        NoneType go back to game engine. Otherwise, enter the room assigned as
        _current_room."""
        self._current_room = room
        self._next_room = None
        if room is None:
            pass
        else:
            self._current_room.enter(self)

    def exit_current_room_to(self, next_room):
        """A method handling the change of _current_room by setting
        _current_room to None and executing get_next_room method."""
        self._current_room = None
        self.get_next_room(next_room)

    def get_next_room(self, next_room):
        """A method handling setting _next_room and executing enter_next_room
        method."""
        self._next_room = next_room
        self.enter_next_room(self._next_room)

    def enter_next_room(self, next_room):
        """A method allowing the Player to enter the next room."""
        self.enter_room(next_room)


class Room:
    """A parent class handling the main mechanics for each Room.

    Attributes:
    -------------
    _room_name : str
        The name of the room

    Methods:
    -------------
    enter(player)
    exit(player)
    _on_entry(player)
    _on_exit(player)

    Subclasses:
    -------------
    DarkRoom
    Stairs
    MonsterRoom
    Prison
    Basement
    """

    def __init__(self):
        self._room_name = self.__class__.__name__

    def enter(self, player):
        """A method handling entering the room."""
        self._on_entry(player)

    def exit(self, player):
        """A method that checks if anything happened to the Player while
        exiting the room."""
        self._on_exit(player)

    def _on_entry(self, player):
        """A method running the room's story."""
        self.exit(player)

    def _on_exit(self, player):
        """A method that executes events that happen to the Player while
        exiting the room."""
        pass

    @staticmethod
    def user_choice(prompt, choices):
        """ A method handling getting input from the Player."""
        while True:
            choice = input(f'{prompt}')
            if choice in choices:
                return choice


class DarkRoom(Room):
    """A child class of Room, handling the story for the Dark Room.

    Attributes:
    -------------
    _room_name : str
        The name of the room

    Methods:
    -------------
    _on_entry(player)
    choice_room(player)
    """

    def __init__(self):
        super().__init__()

    def _on_entry(self, player):
        slow_print('You wake up in a dark room. You don\'t know where you are.'
                   ' Why are you here?')
        slow_print('"Oh yes. My friend is in danger. I must find her!" you '
                   'recall.')
        slow_print('Suddenly, you feel chilly. The Darkness around you seems '
                   'to leech the air that you breathe.')
        slow_print('"I must get out of here or I\'m gonna be consumed" you '
                   'think.')
        slow_print('You stand up and look around. There are two doors - the '
                   'left and the right one.')
        slow_print('"Which one should I choose?" you wonder.')
        self.choice_room(player)

    def choice_room(self, player):
        choice = self.user_choice('Go left (1) or right (2)?', ['1', '2'])
        if choice == '1':
            slow_print('You decide to go left.')
            player.exit_current_room_to(next_room=Stairs())
        elif choice == '2':
            slow_print('You decide to go right.')
            player.exit_current_room_to(next_room=MonsterRoom())


class Stairs(Room):
    """A child class of Room, handling the story for the Stairs.

    Attributes:
    -------------
    _room_name : str
        The name of the room

    Methods:
    -------------
    _on_entry(player)
    first_choice(player)
    second_choice(player)
    """

    def __init__(self):
        super().__init__()

    def _on_entry(self, player):
        slow_print('When you open the door you see a devastated stone stairs. '
                   'They don\'t look very stable. Also, there are some cracked'
                   ' spaces on the way. However, maybe the stairs might '
                   'withstand?...')
        self.first_choice(player)

    def first_choice(self, player):
        choice = self.user_choice('Use stairs (yes/no)?', ['yes', 'no'])
        if choice == 'yes':
            slow_print('The stairs suddenly collapse under your weight!')
            player.exit_current_room_to(next_room=None)
        elif choice == 'no':
            slow_print('"There must be another way. Maybe I should look '
                       'around." you think.')
            self.second_choice(player)

    def second_choice(self, player):
        slow_print('You may try to jump over the cracks. On the other hand, '
                   'you notice a line hanging down next to the stairs. It '
                   'looks quite old and worn.')
        choice = self.user_choice('Try to jump (1) or use the rope (2)?',
                                  ['1', '2'])
        if choice == '1':
            slow_print('That was a bad decision. You fell into abyss.')
            player.exit_current_room_to(next_room=None)
        elif choice == '2':
            slow_print('You reach the bottom and find a door. You enter the '
                       'next room.')
            player.exit_current_room_to(next_room=Prison())


class MonsterRoom(Room):
    """A child class of Room, handling the story for the Monster Room.

    Attributes:
    -------------
    _room_name : str
        The name of the room

    Methods:
    -------------
    _on_entry(player)
    choice_monster(player)
    """

    def __init__(self):
        super().__init__()

    def _on_entry(self, player):
        slow_print('You enter the room and see a huge monster at the center. '
                   'It seems to be asleep.')
        slow_print('"Maybe I should get rid of this monster while it\'s '
                   'asleep? It may be problematic later when it wakes up" a '
                   'though appeared in your head.')
        self.choice_monster(player)

    def choice_monster(self, player):
        choice = self.user_choice('Attack monster (yes/no)?', ['yes', 'no'])
        if choice == 'yes':
            slow_print('You take a chance and attack the monster, inflicting '
                       'a wound. The monster wakes up momentarily and quickly '
                       'throwing off the surprise it charges towards you. It '
                       'moves so fast that you have no time to guard.')
            slow_print('The monster ripped out your heart.')
            player.exit_current_room_to(next_room=None)
        elif choice == 'no':
            slow_print('"Nah, it\'s not worth it." you think. You quietly '
                       'advance through the room. The monster seems to be '
                       'still asleep as you reach the next door.')
            player.exit_current_room_to(next_room=Prison())


class Prison(Room):
    """A child class of Room, handling the story for the Prison.

    Attributes:
    -------------
    _room_name : str
        The name of the room

    Methods:
    -------------
    _on_entry(player)
    event_prisoner(player)
    event_guard(player)
    """

    def __init__(self):
        super().__init__()

    def _on_entry(self, player):
        slow_print('You enter a room with cells. "It looks like a prison" you '
                   'think.')
        slow_print('You wander a while in the corridors. Most of cells are '
                   'empty, in some you notice human skeletons.')
        slow_print('"What a horrible place to be in" you presume.')
        self.event_prisoner(player)

    def event_prisoner(self, player):
        slow_print('"Who\'s there?" you suddenly hear a faint voice. You '
                   'quickly look around and see that there is a live prisoner '
                   'in one of the cells. He looks miserable and weak now, but '
                   'guessing from his physique it seems that he used to be a '
                   'muscular man.')
        slow_print('"Hey you. You\'re not a guard, are you? Please, get me out'
                   ' of here! I\'m innocent! Look, the key to the cell is '
                   'right there" he points behind you back. The key is indeed '
                   'hanging on a spike on the wall.')
        choice = self.user_choice('Should you free the prisoner (yes/no)?',
                                  ['yes', 'no'])
        if choice == 'yes':
            slow_print('"Nobody should stay here." you think while taking the '
                       'key to the cell. You open the door. The prisoner looks'
                       ' surprised and thankful.')
            slow_print('"Thank you, kind sir. I\'m not gonna forget this! It '
                       'may not be much, but please take this bottle. It\'s a '
                       'potion that release you from poison. Maybe you\'ll '
                       'find it useful. Farewell!" he says while bowing his '
                       'head slightly.')
            slow_print('The prisoner leaves quickly. You put the bottle into '
                       'your pocket.')
            player.has_bottle = True
            self.event_guard(player)
        elif choice == 'no':
            slow_print('"Why should I free this man? He probably bluffs about '
                       'his innocence. What if he\'s a dangerous inmate who '
                       'will take advantage of my kindness? I can\'t waste '
                       'time here. My friend needs my help!" you think and '
                       'quickly go further ')
            self.event_guard(player)

    def event_guard(self, player):
        slow_print('You continue your journey through the prison. Suddenly, '
                   'you run into a guard.')
        slow_print('"Who are you?! Surrender!" he shouts.')
        fight_run = self.user_choice('Should you fight (1) or try to escape '
                                     '(2)?', ['1', '2'])
        if fight_run == '1':
            slow_print('You notice a metal pipe lying nearby. You take a '
                       'chance in a fight with the guard!')
            slow_print('The guard does not seem to be very bright. You manage '
                       'to get him down.')
            slow_print('As soon as he is disarmed, the guard shouts: "Have '
                       'mercy! I have a wife and a child to feed. I don\'t '
                       'want to be here either!"')
            spare = self.user_choice('Should you spare the guard (yes/no)?',
                                     ['yes', 'no'])
            if spare == 'yes':
                slow_print('You decide to spare the guard. He looks shocked. '
                           'He stands up slowly.')
                slow_print('"I don\'t know what to say... Thank you" he '
                           'stutters.')
                slow_print('"My friend... She is held captive here" you say.')
                slow_print('The guard quickly looks around and starts to poke '
                           'in his sack. Finally, he pulls out a bronze key.')
                slow_print('"Take it" he whispers and gives you the key. He '
                           'turns his back on you.')
                slow_print('"I haven\'t seen anyone." he says and leaves into '
                           'the labyrinth.')
                slow_print('You put the key into your pocket. It\'s time to '
                           'move.')
                player.has_key = True
                player.exit_current_room_to(next_room=Basement())
            elif spare == 'no':
                slow_print('You decide to silence the guard permanently. You '
                           'take guard\'s sword lying nearby. The blade '
                           'quickly slices guard\'s throat. The guard tries to'
                           ' gasp some air, but ultimately he succumbs. You '
                           'move his lifeless body in an open empty cell.')
                slow_print('Suddenly, you hear voices approaching. You have no'
                           ' time to search the guard. You move quickly '
                           'further into the labyrinth.')
                player.exit_current_room_to(next_room=Basement())
        elif fight_run == '2':
            slow_print('You try to escape the guard. He shouts after you and '
                       'begins to pursue. He\'s quick, you can feel that he\'s'
                       ' right behind you. The next turn you take you meet a '
                       'dead end. You gasp in desperation, but the next moment'
                       ' you feel a sword spiking you through your guts.')
            slow_print('You bleed out.')
            player.exit_current_room_to(next_room=None)


class Basement(Room):
    """A child class of Room, handling the story for the Basement.

    Attributes:
    -------------
    _room_name : str
        The name of the room
    _happy_end : bool
        Indicates if the game ends with a happy end

    Methods:
    -------------
    _on_entry(player)
    rescue_friend(player)
    _on_exit(player)
    """

    def __init__(self):
        super().__init__()
        self._happy_end = False

    def _on_entry(self, player):
        slow_print('You finally reach a door that is not a cell door. You '
                   'cautiously open the door and enter the next room. You '
                   'see only one cell here. ')
        slow_print('"' + player.name + '!" somebody calls your name.')
        slow_print('You turn towards the source of voice. It\'s your '
                   'friend...')
        slow_print('"Ann..." you share a tear when you see her poor condition.'
                   ' Her golden hair has been cut, her face seems dry, she\'s'
                   ' skinny...')
        self.rescue_friend(player)

    def rescue_friend(self, player):
        approach = self.user_choice('Should you get closer quickly (1) or '
                                    'slowly (2)?', ['1', '2'])
        if approach == '1':
            slow_print('You rush towards the cell. Unfortunately, you haven\'t'
                       ' noticed that a tile on your way looks a little '
                       'different than others. You pressed some mechanism. '
                       'Suddenly, you hear a swish and your friend\'s cry. '
                       'When you get to the cell, you notice that Ann is '
                       'quickly getting purple.')
            slow_print('"Poison..." she gasps.')
            if player.has_bottle:
                slow_print('Thoughts run through your mind in the speed of '
                           'light. "The bottle!" it reaches you.')
                slow_print('You give Ann the bottle. "Drink it, quickly!" you '
                           'insist. She barely manages to empty the bottle. '
                           'She breathes deeply for a minute and then the '
                           'purple color goes off her face.')
                slow_print('"Thank you, ' + player.name + '..." she whispers '
                                                          'faintly.')
                slow_print('You feel relieved. Now you can think how to get '
                           'Ann out of here.')
                if player.has_key:
                    slow_print('You try to unlock the cell using the bronze '
                               'key. It works!')
                    slow_print('"Ann, come with me. Use my shoulder" you say.')
                    slow_print('Ann smiles weakly and both of you exit the '
                               'room. After some time you manage to reach the '
                               'exit.')
                    slow_print('You take a deep breath as you get outside. '
                               '"It\'s gonna be ok" you think.')
                    self._happy_end = True
                    self._on_exit(player)
                else:
                    slow_print('"How do I get her out?" you think looking '
                               'around.')
                    slow_print('You desperately try to find a way to open the '
                               'cell. You still have the metal pipe from '
                               'prison, which you use in your attempt to open '
                               'the cell. After some struggle you manage to '
                               'break the lock. However, you make a lot of '
                               'noise and two guards appear quickly.')
                    slow_print('"Hold! Don\'t move!" one of guards yells.')
                    slow_print('The metal pipe is useless after breaking the '
                               'lock. You have no means to defend. The guards '
                               'apprehend you and throw you to a dark cell.')
                    slow_print('"Stay here, you scum!" they shout and leave '
                               'laughing.')
                    slow_print('...')
                    slow_print('"Well, well" you hear a sinister thin voice '
                               '"So you are weak. Well, weak people are also '
                               'tasty" it cackles.')
                    slow_print('It\'s getting harder to breathe...')
                    slow_print('The Darkness consumed you. Behold eternal '
                               'pain...')
                    self._happy_end = False
                    self._on_exit(player)
            else:
                if player.has_key:
                    slow_print('You quickly get the bronze key out of your '
                               'pocket. You struggle with the lock as your '
                               'hands are shaking. Finally, you open the cell '
                               'and grasp Ann into your arms.')
                    slow_print('"No... Please, Ann... Don\'t go..." you sob as'
                               ' Ann foam appears on her mouth.')
                    slow_print('Few minutes later her body shudders and '
                               'subsides.')
                    slow_print('...')
                    slow_print('The only thing you feel is despair.')
                    slow_print('...')
                    slow_print('"Splendid..." you hear a sinister thin voice '
                               '"Your despair is mine" it cackles.')
                    slow_print('It\'s getting harder to breathe...')
                    slow_print('The Darkness consumed you. Behold eternal '
                               'pain...')
                    self._happy_end = False
                    self._on_exit(player)
                else:
                    slow_print('You desperately try to break the lock using '
                               'the metal pipe. However, before you manage to '
                               'do so, Ann is lying lifelessly on the ground. '
                               'Before you are able to open the cell doors two'
                               ' guards are lured by the noise.')
                    slow_print('"Hold! Don\'t move!" one of guards yells.')
                    slow_print('You ignore the guards and still try to break '
                               'the lock. The guards don\'t wait until you '
                               'break in. They apprehend you and throw you to '
                               'a dark cell.')
                    slow_print('"Stay here, you scum!" they shout and leave '
                               'laughing.')
                    slow_print('...')
                    slow_print('"Well, well" you hear a sinister thin voice '
                               '"So you are weak. Well, weak people are also '
                               'tasty" it cackles.')
                    slow_print('It\'s getting harder to breathe...')
                    slow_print('The Darkness consumed you. Behold eternal '
                               'pain...')
                    self._happy_end = False
                    self._on_exit(player)
        elif approach == '2':
            slow_print('You approach cautiously. Looking around you notice '
                       'that one of tiles looks different. You skip the slab. '
                       'You cautiously approach Ann\'s cell.')
            slow_print('"Are you all right?" you ask quietly.')
            slow_print('"I\'m good." she replies "I\'m only a little '
                       'weakened"')
            if player.has_key:
                slow_print('You try to unlock the cell using the bronze key. '
                           'It works!')
                slow_print('"Ann, come with me. Use my shoulder" you say.')
                slow_print('Ann smiles weakly and both of you exit the room. '
                           'After some time you manage to reach the exit.')
                slow_print('You take a deep breath as you get outside. "It\'s '
                           'gonna be ok" you think.')
                self._happy_end = True
                self._on_exit(player)
            else:
                slow_print('You desperately try to find a way to open the '
                           'cell. You still have the metal pipe from prison, '
                           'which you use in your attempt to open the cell. '
                           'After some struggle you manage to break the lock.'
                           ' However, you make a lot of noise and two guards '
                           'appear quickly.')
                slow_print('"Hold! Don\'t move!" one of guards yells.')
                slow_print('You open the cell doors and the moment you enter, '
                           'the other guard shoot a bolt from his crossbow. '
                           'Before you can do anything, you find yourself '
                           'holding Ann. Blood is pouring from her chest where'
                           ' the bolt landed.')
                slow_print('"Ann!" you cry.')
                slow_print('She smiles weakly and whispers: "I\'m glad... '
                           'You\'re ok...".')
                slow_print('Suddenly, her body shudders and subsides.')
                slow_print('...')
                slow_print('"...What...?" you stammer in shock. You feel anger'
                           ' flowing through you.')
                slow_print('"Get up, you scum!" you hear a guard\'s shout. You'
                           ' stand up and everything turns black.')
                slow_print('...')
                slow_print('The next moment you snap out you stand in the pool'
                           ' of blood. There are at least ten guards lying at '
                           'your feet. The air is filled with the smell of '
                           'blood. The only thing you feel is despair.')
                slow_print('"Splendid..." you hear a sinister thin voice "Your'
                           ' anger is mine" it cackles.')
                slow_print('It\'s getting harder to breathe...')
                slow_print('The Darkness consumed you. Behold eternal pain...')
                self._happy_end = False
                self._on_exit(player)

    def _on_exit(self, player):
        if self._happy_end:
            slow_print('HAPPY END')
        else:
            slow_print('BAD END')
        player.exit_current_room_to(next_room=None)


def game_engine(player):
    """Game engine function. As long as the Player object can access the next
    room, enter that room. Otherwise, exit the game."""
    while player.get_next_room(player._next_room):
        player.enter_next_room()
    else:
        slow_print('Game over')


if __name__ == '__main__':
    # Create object Player with a specified initial room and start game engine
    name_ = input('Name yor character: ')
    slow_print('---Press ENTER to continue when you see "..."---')
    player_ = Player(DarkRoom, name_)
    game_engine(player_)
