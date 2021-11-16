import pyautogui, PIL, time, keyboard

# pillow
import win32api

# replace "amongus.png" with the path of the file you want to print
im = PIL.Image.open("amongus.png")
width, hight = im.size
pixel_values = list(im.getdata())

# times of amongus.png picture
# 14:20 - with lines
# 20:01 - without lines

# number of pixels
print(f"number of pixels: {width * hight}")

# variables
temp = 0
startY = 0
startX = 0

selection = input("1 for 30% faster | 2 for higher quality: ")

print("now place your mouse at the starting position and press F to start!")
keyboard.wait('F')
# set these to your location
drawX, drawY = win32api.GetCursorPos()

# delay to select paint / other drawing programs
print("you have 5 second to select your application")
time.sleep(5)

if selection == "1":
    for x in range(0, width):
        for y in range(0, hight):
            if pixel_values[width * y + x][1] > 0:
                pyautogui.click(x + drawX, y + drawY)

elif selection == "2":
    for x in range(0, width):
        y = 0
        while y < hight:

            if pixel_values[width * y + x][1] > 0:
                temp = 1
                startX = x
                startY = y
                if pixel_values[width * y + x][1] == pixel_values[width * y + x + 1][1]:
                    pyautogui.moveTo(startX + drawX, startY + drawY)
                    while pixel_values[width * y + x + temp][1] == pixel_values[width * y + x + 1 + temp][1]:
                        temp += 1
                    y += temp

                    pyautogui.dragTo(startX + drawX, startY + drawY + temp)
                else:
                    pyautogui.click(x + drawX, y + drawY)
            y += 1