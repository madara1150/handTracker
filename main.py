import startGame
import Datacollection as collection

print("1. เริ่มเกม \n2. สร้างด่าน")
input = int(input('กรุณาพิมพ์ 1 หรือ 2 เพื่อเลือก : '))

if input == 1:
    startGame.run()
if input == 2:
    collection.create()
  
