import pygame

BUTTON_NUMBER_NAMES = { 0 : "X", 
                        1 : "A",
                        2 : "B",
                        3 : "Y",
                        8 : "BACK"}
HAT_NUMBER_NAMES = { 1 : "UP",
                    -1 : "DOWN"}

class Controller:
    """
    Represents a game controller connected to the system.

    Attributes:
    - index (int): The index of the controller.
    - is_connected (bool): Indicates whether the controller is connected or not.
    - joystick (pygame.joystick.Joystick): The joystick object representing the controller.
    - connection_warning (bool): Indicates whether a connection warning has been displayed or not.

    Methods:
    - __init__(self, index: int = 0): Initializes the Controller object.
    - connect_controller(self): Connects the controller to the system.
    - get_joystick_position(self, knob_number: int = 0, value_factor: float = 1): Returns the position of the joystick knob.
    - get_active_button(self): Returns the currently active button on the controller.
    - apply_deadzone(self, value): Applies deadzone to the joystick value.
    - event_checker(self): Checks for events related to the controller.
    - stop(self): Stops the controller and quits pygame.
    - __del__(self): Destructor method to clean up resources.
    """
    def __init__(self, index: int = 0):
        """
        Initializes the Controller object.

        Parameters:
        - index (int): The index of the controller (default: 0).
        """
        pygame.init()
        self.index = index
        self.is_connected = False
        self.joystick = None
        self.connection_warning = False
        self.connect_controller()

    def connect_controller(self):
        """
        Connects the controller to the system.
        """
        pygame.event.pump()
        pygame.joystick.init()

        if not self.is_connected and pygame.joystick.get_count() == 0:
            if not self.connection_warning:
                print("koble til joystick")
                self.connection_warning = True
            self.joystick = None

        elif self.is_connected:
            try:
                self.joystick.init()
            except pygame.error as e:
                if str(e) == 'Invalid joystick device number':
                    self.is_connected = False
                    self.connection_warning = False
                else:
                    raise e

        else:
            try:
                self.joystick = pygame.joystick.Joystick(self.index)
                self.joystick.init()
                print(f"Kontroller [{self.joystick.get_name()}] ble koblet til")
                self.is_connected = True
            except pygame.error as e:
                if str(e) == 'Invalid joystick device number':
                    self.is_connected = False
                    self.connection_warning = False
                else: raise e

    def get_joystick_position(self, knob_number: int = 0, value_factor: float = 1):
        """
        Returns the position of the joystick knob.

        Parameters:
        - knob_number (int): The number of the joystick knob (default: 0).
        - value_factor (float): The factor to scale the joystick values (default: 1).

        Returns:
        - str: The joystick position in the format "xxx,yyy".
        """
        self.event_checker()
        try:
            if self.is_connected:
                x = round(self.apply_deadzone(self.joystick.get_axis((knob_number+1)*2-2)*100)*value_factor)
                y = round(self.apply_deadzone(self.joystick.get_axis((knob_number+1)*2-1)*100)*value_factor)
            else:
                self.connect_controller()
                x = 0
                y = 0
            return f"{x:03d},{y:03d}"
        except AttributeError:
            # Hvis kontrolleren ikke er tilgjengelig, skriver den ut en melding
            print("Kontrolleren er ikke tilgjengelig")
            return None

    def get_active_button(self):
        """
        Returns the currently active button on the controller.

        Returns:
        - str: The name of the active button, or None if no button is active.
        """
        self.event_checker()

        if not self.is_connected:
            self.connect_controller() 
            return None

        try:
            for i in range(self.joystick.get_numbuttons()):
                if (self.joystick.get_button(i) == 1) and i in BUTTON_NUMBER_NAMES:
                    return BUTTON_NUMBER_NAMES[i]

            hat = self.joystick.get_hat(0)[1]
            if hat != 0 and hat in HAT_NUMBER_NAMES:
                return HAT_NUMBER_NAMES[hat]
            
            return None
            
        except AttributeError:
            # Hvis kontrolleren ikke er tilgjengelig, skriver den ut en melding
            print("Kontrolleren er ikke tilgjengelig")
            return None

    def apply_deadzone(self, value):
        """
        Applies deadzone to the joystick value.

        Parameters:
        - value: The joystick value to apply deadzone to.

        Returns:
        - float: The joystick value after applying deadzone.
        """
        if value <= -100:
            return -100
        elif value >= 100:
            return 100
        elif abs(value) <= 10:
            return 0
        elif value < 0:
            return -((abs(value) - 10) / 90) * 100
        else:
            return ((abs(value) - 10) / 90) * 100

    def event_checker(self):
        """
        Checks for events related to the controller.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            elif event.type == pygame.JOYDEVICEREMOVED:
                if self.joystick is not None:
                    self.joystick.quit()
                self.joystick = None
                self.is_connected = False

    def stop(self):
        """
        Stops the controller and quits pygame.
        """
        pygame.quit()

    def __del__(self):
        """
        Destructor method to clean up resources.
        """
        pygame.quit()