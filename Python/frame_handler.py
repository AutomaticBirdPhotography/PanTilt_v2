import numpy as np
import cv2
KERNEL = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
from screeninfo import get_monitors
STANDARD_FRAME_SIZE = (700,500)
STANDARD_SCREEN_SIZE = (840,680)
screen_size_offset = 200    #+- hvor mange piksler skjærmstørrelsen kan avvike fra standard før den går til standard

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_scale = 1
FONT_thickness = 2

def get_screen_size():
    """
    Returns the size of the screen.

    Returns:
        tuple: A tuple containing the width and height of the screen.
    """
    screen_info = get_monitors()[0]
    width = screen_info.width
    height = screen_info.height

    if width > STANDARD_SCREEN_SIZE[0] + screen_size_offset or width < STANDARD_SCREEN_SIZE[0] - screen_size_offset:
        width = STANDARD_SCREEN_SIZE[0]
    
    if height > STANDARD_SCREEN_SIZE[1] + screen_size_offset or height < STANDARD_SCREEN_SIZE[1] - screen_size_offset:
        height = STANDARD_SCREEN_SIZE[1]
    
    return (width, height)

def get_frame_size(frame):
    """
    Returns the size of the frame.

    Parameters:
        frame (numpy.ndarray): The frame.

    Returns:
        tuple: A tuple containing the width and height of the frame.
    """
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    return (frame_width, frame_height)

def ensure_valid_frame(frame):
    """
    Returns the frame if it is a valid image and does not deviate too much from the standard frame size.

    Parameters:
        frame (numpy.ndarray): The frame.

    Returns:
        numpy.ndarray: The frame if it is valid, otherwise an error window image.
    """
    if type(frame) == np.ndarray:
        if np.any(frame):
            try:
                frame_width, frame_height = get_frame_size(frame)
                if frame_height < 50 or frame_height > 2000 or frame_width < 50 or frame_width > 2000:
                    frame = error_window()
                else:
                    frame = frame
            except:
                frame = error_window()
        else:
            frame = error_window()
    else:
        frame = error_window()
    return frame

def get_text_size(text):
    """
    Returns the size of the text.

    Parameters:
        text (str): The text.

    Returns:
        tuple: A tuple containing the width and height of the text.
    """
    return cv2.getTextSize(text, FONT, FONT_scale, FONT_thickness)[0]

def calculate_center_text(frame_width : int, frame_height : int, text : str = "", text_width : int = 0, text_height : int = 0, text_offset_position : tuple = (0,0)):
    """
    Calculates the position of the center of the text in the frame.

    Parameters:
        frame_width (int): The width of the frame.
        frame_height (int): The height of the frame.
        text (str): The text.
        text_width (int): The width of the text.
        text_height (int): The height of the text.
        text_offset_position (tuple): The position of the upper left corner of the frame.

    Returns:
        tuple: A tuple containing the x and y coordinates of the center of the text.
    """
    if text_width == 0 and text_height == 0:
        (text_width, text_height) = get_text_size(text)
    text_x = (frame_width - text_width) // 2 + text_offset_position[0]
    text_y = (frame_height + text_height) // 2 + text_offset_position[1]
    return text_x, text_y


def error_window(width: int = STANDARD_FRAME_SIZE[0], height: int = STANDARD_FRAME_SIZE[1], text: str = "") -> np.ndarray:
    """
    Creates an image of a non-contact screen effect.

    Parameters:
        width (int): The width of the image.
        height (int): The height of the image.
        text (str): The text on the image.

    Returns:
        numpy.ndarray: A numpy array representing the image of the non-contact screen.
    """
    image = np.zeros((height, width, 3), dtype=np.uint8)
    num_sectors = 5
    sector_width = width // num_sectors
    colors = [(255, 255, 255), (0, 255, 255), (0, 255, 0), (255, 0, 255), (255, 255, 0)]
    for i in range(num_sectors):
        color = colors[i]
        sector_start = i * sector_width
        sector_end = (i + 1) * sector_width
        image[:, sector_start:sector_end] = color
    if text != "":
        try:
            (text_width, text_height) = get_text_size(text)
            text_x, text_y = calculate_center_text(width, height, text_width=text_width, text_height=text_height)
            rect_x = text_x - 20
            rect_y = text_y-text_height - 20
            rect_width = text_width + 40
            rect_height = text_height + 40
            image = cv2.rectangle(image, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (0, 0, 0), -1)
            image = cv2.putText(image, text, (text_x, text_y), FONT, FONT_scale, (255, 255, 255), FONT_thickness, cv2.LINE_AA)
        except:
            pass
    return image
