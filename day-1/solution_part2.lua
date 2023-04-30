local file = io.open("input.txt", "r")
io.input(file)
local file_content = io.read()
io.close(file)

local floor = 0
local i = 1

while (floor ~= -1)
do
  if file_content:sub(i, i) == "(" then
    floor = floor + 1
  else
    floor = floor - 1
  end
  print(i.." -> "..floor)
  i = i + 1
end

print("The first time santa reaches the basement is at movement " ..( i -1 ).. ".");
