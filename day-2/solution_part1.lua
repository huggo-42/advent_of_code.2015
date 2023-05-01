local BUFSIZE = 2^13

local file = io.open("input.txt", "r")
io.input(file)
local file_content = io.read(BUFSIZE, "*line")
io.close(file)

local paper_tobuy = 0

for i in string.gmatch(file_content, "%S+") do
  local values = {}
  local cnt = 0

  for m in string.gmatch(i, "%x+") do
    values[cnt] = m
    cnt = cnt + 1
  end

  local x = values[0] * values[1]
  local y = values[1] * values[2]
  local z = values[0] * values[2]

  local smallest_side = x
  if y < smallest_side then smallest_side = y end
  if z < smallest_side then smallest_side = z end
  paper_tobuy = paper_tobuy + (2 * x) + (2 * y) + (2 * z) + smallest_side
end
print("Paper to buy: " .. paper_tobuy .. " feet.")
