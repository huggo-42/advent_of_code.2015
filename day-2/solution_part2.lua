local BUFSIZE = 2^13

local file = io.open("input.txt", "r")
io.input(file)
local file_content = io.read(BUFSIZE, "*line")
io.close(file)

local present_ribbon = 0

for a in string.gmatch(file_content, "%S+") do
  local values = {}
  local cnt = 0

  for b in string.gmatch(a, "%x+") do
    values[cnt] = b
    cnt = cnt + 1
  end

  local bow_ribbon = values[0] * values[1] * values[2]

  local xyz = {values[0], values[1], values[2]}
  local higher = values[0]
  local higher_pos = 1

  for c in pairs(xyz) do
    if tonumber(xyz[c]) > tonumber(higher) then
      higher = xyz[c]
      higher_pos = c
    end
  end
  table.remove(xyz, higher_pos)

  present_ribbon = present_ribbon + (2 * xyz[1]) + (2 * xyz[2]) + bow_ribbon

end
print(present_ribbon)
