local file = io.open("input.txt", "r")
io.input(file)
local file_content = io.read()
io.close(file)

local floor = 0

for i = 1, #file_content do
  if file_content:sub(i, i) == "(" then
    floor = floor + 1
  else
    floor = floor - 1
  end
end

print("The instructions takes santa to floor number " ..floor.. ".");
