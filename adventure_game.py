#!/usr/bin/python3


class Player:
    _current_room = None
    _next_room = None
    name = None

    def __init__(self, name='Nameless'):  # create object Player
        self.name = name
        self.has_bottle = False
        self.has_key = False
        self._next_room = DarkRoom()  # create DarkRoom as initial room

    def enter_room(self, room):
        self._current_room = room  # assign prompted room as current
        self._next_room = None  # set next room attribute to None-Type
        if room is None:
            pass  # if current room is None-Type go back to game engine
        else:
            self._current_room.enter(self)  # enter room assigned as current

    def exit_current_room_to(self, next_room):
        self._current_room = None
        self.get_next_room(next_room)

    def get_next_room(self, next_room):
        self._next_room = next_room
        self.enter_next_room(self._next_room)

    def enter_next_room(self, next_room):
        self.enter_room(next_room)


class Room:
    _player: Player

    def __init__(self):
        self._room_name = self.__class__.__name__

    def enter(self, player):
        self._on_entry(player)  # run room's story

    def exit(self, player):
        self._on_exit(player)  # check if anything happen to on exit

    def _on_entry(self, player):
        self.exit(player)

    def _on_exit(self, player):
        pass


class DarkRoom(Room):
    _player: Player

    def __init__(self):
        super().__init__()

    def _on_entry(self, player):
        print('You wake up in a dark room. You don\'t know where you are. Why '
              'are you here?')
        print('"Oh yes. My friend is in danger. I must find her!" you recall.')
        print('Suddenly, you feel chilly. The Darkness around you seems to '
              'leech the air that you breathe.')
        print('"I must get out of here or I\'m gonna be consumed" you think.')
        print('You stand up and look around. There are two doors - the left '
              'and the right one.')
        print('"Which one should I choose?" you wonder.')
        self.choice_room(player)

    @staticmethod
    def choice_room(player):
        choice = int(input('Go left (1) or right (2)?'))
        if choice == 1:
            print('You decide to go left.')
            player.exit_current_room_to(next_room=Stairs())
        elif choice == 2:
            print('You decide to go right.')
            player.exit_current_room_to(next_room=MonsterRoom())
        else:
            print('You could not choose where to go. It\'s getting harder to '
                  'breathe...')
            print('The Darkness consumed you.')
            player.exit_current_room_to(next_room=None)

    def _on_exit(self, player):
        pass


class Stairs(Room):
    _player: Player

    def __init__(self):
        super().__init__()

    def _on_entry(self, player):
        print('When you open the door you see a devastated stone stairs. They '
              'don\'t look very stable. Also, there are some cracked spaces '
              'on the way. However, maybe the stairs might withstand?...')
        self.first_choice(player)

    def first_choice(self, player):
        first_choice_ = str(input('Use stairs (yes/no)?'))
        if first_choice_ == 'yes':
            print('The stairs suddenly collapse under your weight!')
            player.exit_current_room_to(next_room=None)
        elif first_choice_ == 'no':
            print('"There must be another way. Maybe I should look around." '
                  'you think.')
            self.second_choice(player)
        else:
            print('You could not choose what to do. It\'s getting harder to '
                  'breathe...')
            print('The Darkness consumed you.')
            player.exit_current_room_to(next_room=None)

    @staticmethod
    def second_choice(player):
        print('You may try to jump over the cracks. On the other hand, you '
              'notice a line hanging down next to the stairs. It looks quite '
              'old and worn.')
        second_choice_ = int(input('Try to jump (1) or use the rope (2)?'))
        if second_choice_ == 1:
            print('That was a bad decision. You fell into abyss.')
            player.exit_current_room_to(next_room=None)
        elif second_choice_ == 2:
            print('You reach the bottom and find a door. You enter the next '
                  'room.')
            player.exit_current_room_to(next_room=Prison())
        else:
            print('You could not choose what to do. It\'s getting harder to '
                  'breathe...')
            print('The Darkness consumed you.')
            player.exit_current_room_to(next_room=None)

    def _on_exit(self, player):
        pass


class MonsterRoom(Room):
    _player: Player

    def __init__(self):
        super().__init__()

    def _on_entry(self, player):
        print('You enter the room and see a huge monster at the center. It '
              'seems to be asleep.')
        print('"Maybe I should get rid of this monster while it\'s asleep? '
              'It may be problematic later when it wakes up" a though appeared'
              ' in your head.')
        self.choice_monster(player)

    @staticmethod
    def choice_monster(player):
        choice_monster_ = str(input('Attack monster (yes/no)?'))
        if choice_monster_ == 'yes':
            print('You take a chance and attack the monster, inflicting a '
                  'wound. The monster wakes up momentarily and quickly '
                  'throwing off the surprise it charges towards you. It moves'
                  ' so fast that you have no time to guard.')
            print('The monster ripped out your heart.')
            player.exit_current_room_to(next_room=None)
        elif choice_monster_ == 'no':
            print('"Nah, it\'s not worth it." you think. You quietly advance '
                  'through the room. The monster seems to be still asleep as '
                  'you reach the next door.')
            player.exit_current_room_to(next_room=Prison())
        else:
            print('You wondered so long that the monster wakes up. As soon as'
                  ' it notices you, it charges towards you. It moves so fast '
                  'that you have no time to guard.')
            print('The monster ripped out your heart.')
            player.exit_current_room_to(next_room=None)

    def _on_exit(self, player):
        pass


class Prison(Room):
    _player: Player

    def __init__(self):
        super().__init__()

    def _on_entry(self, player):
        print('You enter a room with cells. "It looks like a prison" you '
              'think.')
        print('You wander a while in the corridors. Most of cells are empty, '
              'in some you notice human skeletons.')
        print('"What a horrible place to be in" you presume.')
        self.event_prisoner(player)

    def event_prisoner(self, player):
        print('"Who\'s there?" you suddenly hear a faint voice. You quickly '
              'look around and see that there is a live prisoner in one of the'
              ' cells. He looks miserable and weak now, but guessing from his'
              ' physique it seems that he used to be a muscular man.')
        print('"Hey you. You\'re not a guard, are you? Please, get me out of '
              'here! I\'m innocent! Look, the key to the cell is right there" '
              'he points behind you back. The key is indeed hanging on a spike'
              ' on the wall.')
        event_prisoner_ = str(input('Should you free the prisoner (yes/no)?'))
        if event_prisoner_ == 'yes':
            print('"Nobody should stay here." you think while taking the key '
                  'to the cell. You open the door. The prisoner looks '
                  'surprised and thankful.')
            print('"Thank you, kind sir. I\'m not gonna forget this! It may '
                  'not be much, but please take this bottle. It\'s a potion '
                  'that release you from poison. Maybe you\'ll find it useful.'
                  ' Farewell!" he says while bowing his head slightly.')
            print('The prisoner leaves quickly. You put the bottle into your '
                  'pocket.')
            player.has_bottle = True
            self.event_guard(player)
        elif event_prisoner_ == 'no':
            print('"Why should I free this man? He probably bluffs about his '
                  'innocence. What if he\'s a dangerous inmate who will take '
                  'advantage of my kindness? I can\'t waste time here. My '
                  'friend needs my help!" you think and quickly go further ')
            self.event_guard(player)
        else:
            print('You could not decide what to do. It\'s getting harder to '
                  'breathe...')
            print('The Darkness consumed you.')
            player.exit_current_room_to(next_room=None)

    @staticmethod
    def event_guard(player):
        print('You continue your journey through the prison. Suddenly, you '
              'run into a guard.')
        print('"Who are you?! Surrender!" he shouts.')
        fight_run = int(input('Should you fight (1) or try to escape (2)?'))
        if fight_run == 1:
            print('You notice a metal pipe lying nearby. You take a chance in'
                  ' a fight with the guard!')
            print('The guard does not seem to be very bright. You manage to '
                  'get him down.')
            print('As soon as he is disarmed, the guard shouts: "Have mercy! '
                  'I have a wife and a child to feed. I don\'t want to be '
                  'here either!"')
            spare = str(input('Should you spare the guard (yes/no)?'))
            if spare == 'yes':
                print('You decide to spare the guard. He looks shocked. He '
                      'stands up slowly.')
                print('"I don\'t know what to say... Thank you" he stutters.')
                print('"My friend... She is held captive here" you say.')
                print('The guard quickly looks around and starts to poke in '
                      'his sack. Finally, he pulls out a bronze key.')
                print('"Take it" he whispers and gives you the key. He turns '
                      'his back on you.')
                print('"I haven\'t seen anyone." he says and leaves into the '
                      'labyrinth.')
                print('You put the key into your pocket. It\'s time to move.')
                player.has_key = True
                player.exit_current_room_to(next_room=Basement())
            elif spare == 'no':
                print('You decide to silence the guard permanently. You take '
                      'guard\'s sword lying nearby. The blade quickly slices '
                      'guard\'s throat. The guard tries to gasp some air, but'
                      ' ultimately he succumbs. You move his lifeless body in '
                      'an open empty cell.')
                print('Suddenly, you hear voices approaching. You have no time'
                      ' to search the guard. You move quickly further into '
                      'the labyrinth.')
                player.exit_current_room_to(next_room=Basement())
            else:
                print('You wonder for so long, that the guard takes a chance '
                      'to get his sword. He wails and quickly spikes you with '
                      'the sword.')
                print('You bleed out.')
                player.exit_current_room_to(next_room=None)
        elif fight_run == 2:
            print('You try to escape the guard. He shouts after you and begins'
                  ' to pursue. He\'s quick, you can feel that he\'s right '
                  'behind you. The next turn you take you meet a dead end. You'
                  ' gasp in desperation, but the next moment you feel a sword '
                  'spiking you through your guts.')
            print('You bleed out.')
            player.exit_current_room_to(next_room=None)
        else:
            print('You wondered so long that the guard takes you down. You are'
                  ' thrown into a cell. As soon as he leaves, you feel that '
                  'it\'s getting harder to breathe...')
            print('The Darkness consumed you.')
            player.exit_current_room_to(next_room=None)

    def _on_exit(self, player):
        pass


class Basement(Room):
    _player: Player

    def __init__(self):
        super().__init__()
        self._happy_end = False

    def _on_entry(self, player):
        print('You finally reach a door that is not a cell door. You '
              'cautiously open the door and enter the next room. You see only '
              'one cell here. ')
        print('"' + player.name + '!" somebody calls your name.')
        print('You turn towards the source of voice. It\'s your friend...')
        print('"Ann..." you share a tear when you see her poor condition. Her '
              'golden hair has been cut, her face seems dry, she\'s skinny...')
        self.rescue_friend(player)

    def rescue_friend(self, player):
        approach = int(input('Should you get closer quickly (1) or slowly '
                             '(2)?'))
        if approach == 1:
            print('You rush towards the cell. Unfortunately, you haven\'t '
                  'noticed that a tile on your way looks a little different '
                  'than others. You pressed some mechanism. Suddenly, you hear'
                  ' a swish and your friend\'s cry. When you get to the cell, '
                  'you notice that Ann is quickly getting purple.')
            print('"Poison..." she gasps.')
            if player.has_bottle:
                print('Thoughts run through your mind in the speed of light. '
                      '"The bottle!" it reaches you.')
                print('You give Ann the bottle. "Drink it, quickly!" you '
                      'insist. She barely manages to empty the bottle. She '
                      'breathes deeply for a minute and then the purple color '
                      'goes off her face.')
                print('"Thank you, ' + player.name + '..." she whispers '
                                                     'faintly.')
                print('You feel relieved. Now you can think how to get Ann out'
                      ' of here.')
                if player.has_key:
                    print('You try to unlock the cell using the bronze key. It'
                          ' works!')
                    print('"Ann, come with me. Use my shoulder" you say.')
                    print('Ann smiles weakly and both of you exit the room. '
                          'After some time you manage to reach the exit.')
                    print('You take a deep breath as you get outside. "It\'s '
                          'gonna be ok" you think.')
                    self._happy_end = True
                    self._on_exit(player)
                else:
                    print('"How do I get her out?" you think looking around.')
                    print('You desperately try to find a way to open the cell.'
                          ' You still have the metal pipe from prison, which '
                          'you use in your attempt to open the cell. After '
                          'some struggle you manage to break the lock. '
                          'However, you make a lot of noise and two guards '
                          'appear quickly.')
                    print('"Hold! Don\'t move!" one of guards yells.')
                    print('The metal pipe is useless after breaking the lock. '
                          'You have no means to defend. The guards apprehend '
                          'you and throw you to a dark cell.')
                    print('"Stay here, you scum!" they shout and leave '
                          'laughing.')
                    print('...')
                    print('"Well, well" you hear a sinister thin voice "So you'
                          ' are weak. Well, weak people are also tasty" it '
                          'cackles.')
                    print('It\'s getting harder to breathe...')
                    print('The Darkness consumed you. Behold eternal pain...')
                    self._happy_end = False
                    self._on_exit(player)
            else:
                if player.has_key:
                    print('You quickly get the bronze key out of your pocket. '
                          'You struggle with the lock as your hands are '
                          'shaking. Finally, you open the cell and grasp Ann '
                          'into your arms.')
                    print('"No... Please, Ann... Don\'t go..." you sob as Ann '
                          'foam appears on her mouth.')
                    print('Few minutes later her body shudders and subsides.')
                    print('...')
                    print('The only thing you feel is despair.')
                    print('...')
                    print('"Splendid..." you hear a sinister thin voice "Your '
                          'despair is mine" it cackles.')
                    print('It\'s getting harder to breathe...')
                    print('The Darkness consumed you. Behold eternal pain...')
                    self._happy_end = False
                    self._on_exit(player)
                else:
                    print('You desperately try to break the lock using the '
                          'metal pipe. However, before you manage to do so, '
                          'Ann is lying lifelessly on the ground. Before you '
                          'are able to open the cell doors two guards are '
                          'lured by the noise.')
                    print('"Hold! Don\'t move!" one of guards yells.')
                    print('You ignore the guards and still try to break the '
                          'lock. The guards don\'t wait until you break in. '
                          'They apprehend you and throw you to a dark cell.')
                    print('"Stay here, you scum!" they shout and leave '
                          'laughing.')
                    print('...')
                    print('"Well, well" you hear a sinister thin voice "So you'
                          ' are weak. Well, weak people are also tasty" it '
                          'cackles.')
                    print('It\'s getting harder to breathe...')
                    print('The Darkness consumed you. Behold eternal pain...')
                    self._happy_end = False
                    self._on_exit(player)
        elif approach == 2:
            print('You approach cautiously. Looking around you notice that one'
                  ' of tiles looks different. You skip the slab. You '
                  'cautiously approach Ann\'s cell.')
            print('"Are you all right?" you ask quietly.')
            print('"I\'m good." she replies "I\'m only a little weakened"')
            if player.has_key:
                print('You try to unlock the cell using the bronze key. It '
                      'works!')
                print('"Ann, come with me. Use my shoulder" you say.')
                print('Ann smiles weakly and both of you exit the room. After '
                      'some time you manage to reach the exit.')
                print('You take a deep breath as you get outside. "It\'s gonna'
                      ' be ok" you think.')
                self._happy_end = True
                self._on_exit(player)
            else:
                print('You desperately try to find a way to open the cell. You'
                      ' still have the metal pipe from prison, which you use '
                      'in your attempt to open the cell. After some struggle '
                      'you manage to break the lock. However, you make a lot '
                      'of noise and two guards appear quickly.')
                print('"Hold! Don\'t move!" one of guards yells.')
                print('You open the cell doors and the moment you enter, the '
                      'other guard shoot a bolt from his crossbow. Before you '
                      'can do anything, you find yourself holding Ann. Blood '
                      'is pouring from her chest where the bolt landed.')
                print('"Ann!" you cry.')
                print('She smiles weakly and whispers: "I\'m glad... You\'re '
                      'ok...".')
                print('Suddenly, her body shudders and subsides.')
                print('...')
                print('"...What...?" you stammer in shock. You feel anger '
                      'flowing through you.')
                print('"Get up, you scum!" you hear a guard\'s shout. You '
                      'stand up and everything turns black.')
                print('...')
                print('The next moment you snap out you stand in the pool of '
                      'blood. There are at least ten guards lying at your '
                      'feet. The air is filled with the smell of blood. The '
                      'only thing you feel is despair.')
                print('"Splendid..." you hear a sinister thin voice "Your '
                      'anger is mine" it cackles.')
                print('It\'s getting harder to breathe...')
                print('The Darkness consumed you. Behold eternal pain...')
                self._happy_end = False
                self._on_exit(player)
        else:
            print('You spend too much time on wondering. Suddenly, it\'s '
                  'getting harder to breathe...')
            print('The Darkness consumed you.')
            player.exit_current_room_to(next_room=None)

    def _on_exit(self, player):
        if self._happy_end:
            print('HAPPY END')
        else:
            print('BAD END')
        player.exit_current_room_to(next_room=None)


def game_engine(player):
    while player.get_next_room(player._next_room):  # as long as Player object
        # can access next room...
        player.enter_next_room()  # ...enter that room
    else:
        print('Game over')  # If next room in None-Type when accessed,
        # exit the game


if __name__ == '__main__':
    player_ = Player()  # create object Player and initial room
    game_engine(player_)  # start game engine
