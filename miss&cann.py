boat_side = "Right"
missionary_on_right = 3
cannibals_on_right = 3
missionary_on_left = 0
cannibals_on_left = 0

while True:
    missionary = int(input("Enter number of Missionary in boat on "+ boat_side + ":"))
    cannibals = int(input("Enter number of Cannibals in boat on " + boat_side + ":"))
   
    #Maximum number of people one the boat should be 1 or 2
    if (missionary+cannibals) != 1 and (missionary+cannibals) != 2:
        print("Invalid move")
        continue
   
    #Turn based decisions
    if boat_side == "Right":
        if missionary > missionary_on_right or cannibals > cannibals_on_right:
            print("Invalid move")
            continue
           
        missionary_on_right -= missionary
        cannibals_on_right -= cannibals
        missionary_on_left += missionary
        cannibals_on_left += cannibals
       
        boat_side = "Left"
       
    else:
        if missionary > missionary_on_left or cannibals > cannibals_on_left:
            print("Invalid move")
            continue
           
        missionary_on_right += missionary
        cannibals_on_right += cannibals
        missionary_on_left -= missionary
        cannibals_on_left -= cannibals
       
        boat_side = "Right"
       
     
    #condition for losing
    if (missionary_on_right != 0 and missionary_on_right < cannibals_on_right) or (missionary_on_left != 0 and missionary_on_left < cannibals_on_left):
        print("YOU LOSE")
        break
   
    #condition for winning
    if missionary_on_left == 3 and cannibals_on_left == 3:
        print("YOU WIN")
        break
print("GAME OVER")