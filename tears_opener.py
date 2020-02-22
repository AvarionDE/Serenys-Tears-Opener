from pynput import mouse
import time


#registering 3 mouse clicks
def on_click(x,y, button, pressed):
    if pressed:
        mouse_cords.append((x,y))
        if len(mouse_cords) == 3:
            listener.stop()

    
#Start: Entering number of tears
mouse_cords = []
tears = int(input("How many Goddess Tears do you want to open?\n"))


#Listening to 3 mouse clicks
print("Please open one tear")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()    


#Preparing user
input("Press ENTER if you are ready\n")
print("Starting in 5 seconds! Please focus the game!")
time.sleep(5)

      
#Opening the tears with the controller
print("The script will now open your tears automatically!")

for j in range(tears):
    cursor = mouse.Controller()

    print(str(j+1) + "...")
    cursor.position = mouse_cords[0]
    cursor.press(mouse.Button.left)
    time.sleep(0.1)
    cursor.release(mouse.Button.left)

    time.sleep(0.5)
    cursor.position = mouse_cords[1]
    cursor.press(mouse.Button.left)
    time.sleep(0.1)
    cursor.release(mouse.Button.left)

    time.sleep(3.5)
    cursor.position = mouse_cords[2]
    cursor.press(mouse.Button.left)
    time.sleep(0.1)
    cursor.release(mouse.Button.left)

#Exit program
print("Tears successfully opened")


